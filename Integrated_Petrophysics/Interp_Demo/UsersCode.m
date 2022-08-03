function UsersCode(up)

	Methods
    
	CalculatePicket(up);

	try
		%
		%   Intitalize zonal averages
        PhiPay = 0.0;
		PhiRes = 0.0;
        
		VclPay = 0.0;
		VclRes = 0.0;
		BVWPay = 0.0;
		BVWRes = 0.0;
		PayCount = 0.0;
		ResCount = 0.0;
       
		%
		% Loop through the data one level at a time
		% TopDepth and BottomDepth are the index equivalent depths entered on the run window.
		%
		for index = TopDepth():BottomDepth()
			%
			%     Calculate porosity depending om method
			if strcmp(PorEq(), 'Sonic')

				S = Son(index);
				if (S > 0.0)

					Por = (S - SonMat(index)) * SonCp(index) / (SonFluid(index) - SonMat(index));
				else

					Por = -999.0;
				end
				%      Calculate clay porosity
				PorClay = (SonClay(index) - SonMat(index)) * SonCp(index) / (SonFluid(index) - SonMat(index));

			else

				D = Den(index);
				if (D > 0.0)

					Por = (D - DenMat(index)) / (DenFluid(index) - DenMat(index));
				else

					Por = -999.0;
				end
				%      Calculate clay porosity
				PorClay = (DenClay(index) - DenMat(index)) / (DenFluid(index) - DenMat(index));
			end

			%     Calculate Clay volume
			G = Gr(index);
			if (G ~= -999.0)

				VClay = (G - GrClean(index)) / (GrClay(index) - GrClean(index));
				if (VClay > 1.0)

					VClay = 1.0;

				elseif (VClay < 0.0)

					VClay = 0.0;

				end
				%     Correct Porosity for clay
				Por = Por - VClay * PorClay;
				if Por < 0.0001

					Por = 0.0001;
				end
			else

				VClay = -999.0;
				Por = -999.0;
			end
			%     Calculate Water Saturation
			Res = Rt(index);
			if (Por < 0.0) || (Res <= 0.0)

				WatSat = -999.0;
				Rwa = -999.0;
				BVW = -999.0;

			else

				%     Check for Shell m
				if (Shellm())

					XX = 1.87 + 0.019 / Por;

				else

					%     set m to input parameter
					XX = xm(index);
				end
				%     Check for Archie equation
				if strcmp(SwEq(), 'Archie')

					%        calculate F
					F = xa(index) / power(Por,XX);
					%        calculate Sw
					WatSat = (F * Rw(index) / Res)^ (1.0/xn(index));

				else

					%        calculate Sw Indonesian
					WatSat =  (Res^0.5 * (VClay^(1.0-VClay/2.0)) / Rclay(index)^0.5 + (Por^(XX/2.0)) /(xa(index)*Rw(index)^0.5))^(-2.0/xn(index));
				end
				% Limit Sw
				if (WatSat > 1.2)
					WatSat = 1.2;
				end
				% calculate Rw apparent
				Rwa = Res * (Por^XX) / xa(index);
				% calculate BVW
				if (WatSat < 1.0)
					BVW = WatSat * Por;
				else
					BVW = Por;
				end
			end

			%  calculate the Net pay and net reservoir
			%     Limit Sw to 1.0
			if (WatSat > 1.0)
				WS = 1.0;
			else
				WS = WatSat;
			end
			if ((Por >= PhiCut(index)) && (VClay <= VclCut(index)))

				ResFlg = 1.0;
				if (WS <= SwCut(index))
					PayFlg = 1.0;
				else
					PayFlg = 0.0;
				end

			else
				ResFlg = 0.0;
				PayFlg = 0.0;
			end

			%  add results to zone averages
			if ResFlg == 1.0
				ResCount = ResCount + 1.0;
				PhiRes = PhiRes + Por;
				BVWRes = BVWRes + Por * WS;
				VclRes = VclRes + VClay;
			end
			if PayFlg == 1.0
				PayCount = PayCount + 1.0;
				PhiPay = PhiPay + Por;
				BVWPay = BVWPay + Por * WS;
				VclPay = VclPay + VClay;
			end

			% output the curve results
			Save_Phi(index,Por);
			Save_Vcl(index,VClay);
			Save_Sw(index,WatSat);
			Save_Rwapp(index,Rwa);
			Save_BVW(index,BVW);
			Save_NetResFlg(index,ResFlg);
			Save_NetPayFlg(index,PayFlg);

		end
		%
		%
		%  Calculate Well Step from first 2 depths
		Step = Depth(TopDepth()+1) - Depth(TopDepth());
		%  Calculate the zonal averages
		ResNet = ResCount * Step;
		if ResCount == 0.0
			PhiRes = 0.0;
			VclRes = 0.0;
			SwRes  = 0.0;
		else
			PhiRes = PhiRes / ResCount;
			VclRes = VclRes / ResCount;
			BVWRes = BVWRes / ResCount;
			SwRes  = BVWRes / PhiRes;
		end

		PayNet = PayCount * Step;
		if PayCount == 0.0
			PhiPay = 0.0;
			VclPay = 0.0;
			SwPay  = 0.0;
		else
			PhiPay = PhiPay / PayCount;
			VclPay = VclPay / PayCount;
			BVWPay = BVWPay / PayCount;
			SwPay  = BVWPay / PhiRes;
		end
		%
		%  Output results back to parameters
		%  We loop through all the data because it is possible that the result parameters are set as curves !
		for index = TopDepth():BottomDepth()
			Save_NetRes(index,ResNet);
			Save_AvPhiRes(index,PhiRes);
			Save_AvVclRes(index,VclRes);
			Save_AvSwRes(index,SwRes);

			Save_NetPay(index,PayNet);
			Save_AvPhiPay(index,PhiPay);
			Save_AvVclPay(index,VclPay);
			Save_AvSwPay(index,SwPay);
		end
		%
		%
		% Create a report to a file if this is the last zone
		if ZoneNumber() == TotalZones()
			outFile = fopen('Interp Demo MatLab Report.TXT', 'w+');
			fprintf(outFile,' USER PROGRAM INTERP MATLAB DEMO PARAMETERS');
			fprintf(outFile, '\r\n');
			fprintf(outFile, [' Well    : ' Well_Name()]);
			% Write well attributes using attribute name
			fprintf(outFile, [' Company : ' Read_Well_Attribute('Company') '\r\n']);
			fprintf(outFile, [' Field   : ' Read_Well_Attribute('Field') '\r\n']);
			fprintf(outFile, [' KB Elev : ' Read_Well_Attribute('KBElev') '\r\n']);
			fprintf(outFile, [' Input Curves ' '\r\n']);
			fprintf(outFile, ['    Rt     = ' Rt_Name() '(' Rt_Units() ')' '\r\n']);
			fprintf(outFile, ['    Gr     = ' Gr_Name() '(' Gr_Units() ')' '\r\n']);
			fprintf(outFile, ['    Den    = ' Den_Name() '(' Den_Units() ')' '\r\n']);
			fprintf(outFile, ['    Son    = ' Son_Name() '(' Son_Units() ')' '\r\n']);
			fprintf(outFile, [' Output Curve '  '\r\n']);
			fprintf(outFile, ['    Phi    = ' Phi_Name() '(' Phi_Units() ')' '\r\n']);
			fprintf(outFile, ['    Vcl    = ' Vcl_Name() '(' Vcl_Units() ')' '\r\n']);
			fprintf(outFile, ['    Sw     = ' Sw_Name() '(' Sw_Units() ')' '\r\n']);
			fprintf(outFile, ['    Rwapp  = ' Rwapp_Name() '(' Rwapp_Units() ')' '\r\n']);
			fprintf(outFile, ['    BVW    = ' BVW_Name() '(' BVW_Units() ')' '\r\n']);
			fprintf(outFile, ['    NetPay = ' NetPayFlg_Name() '\r\n']);
			fprintf(outFile, ['    NetRes = ' NetResFlg_Name() '\r\n']);

			% Write the parameters by zone
			for i = 1:TotalZones()
				% Set the zone number so we can get the parameters for each zone
				SetZone(i);
				fprintf(outFile, '\r\n');
				fprintf(outFile, [' Zone ' num2str(i) ' Input Parameters' '\r\n']);
				fprintf(outFile, ['    a          = ' num2str(xa(1)) '\r\n']);
				fprintf(outFile, ['    m          = ' num2str(xm(1)) '\r\n']);
				fprintf(outFile, ['    n          = ' num2str(xn(1)) '\r\n']);
				fprintf(outFile, ['    Rw         = ' num2str(Rw(1)) '\r\n']);
				fprintf(outFile, ['    Sw Eq      = ' SwEq() '\r\n']);
				fprintf(outFile, ['    Son Matrix = ' num2str(SonMat(1)) '\r\n']);
				fprintf(outFile, ['    Son Fluid  = ' num2str(SonFluid(1)) '\r\n']);
				fprintf(outFile, ['    Son CP     = ' num2str(SonCp(1)) '\r\n']);
				fprintf(outFile, ['    Son Clay   = ' num2str(SonClay(1)) '\r\n']);
				fprintf(outFile, ['    Den Matrix = ' num2str(DenMat(1)) '\r\n']);
				fprintf(outFile, ['    Den Fluid  = ' num2str(DenFluid(1)) '\r\n']);
				fprintf(outFile, ['    Por Eq     = ' PorEq() '\r\n']);
				fprintf(outFile, ['    Den Clay   = ' num2str(DenClay(1)) '\r\n']);
				fprintf(outFile, ['    Gr Clean   = ' num2str(GrClean(1)) '\r\n']);
				fprintf(outFile, ['    Gr Clay    = ' num2str(GrClay(1)) '\r\n']);
				fprintf(outFile, ['    Depth Interval' '\r\n']);
				fprintf(outFile, ['    Top = ' num2str(Depth(TopDepth())) '     Bottom = ' num2str(Depth(BottomDepth())) '\r\n']);
			end;
			fclose(outFile);
		end;
		%
		%  Write to database who created these curves
		Save_Sw_Comments('Curve written by Interp Demo user program');
		Save_Rwapp_Comments('Curve written by Interp Demo user program');
		Save_Phi_Comments('Curve written by Interp Demo user program');
		Save_Vcl_Comments('Curve written by Interp Demo user program');
		Save_BVW_Comments('Curve written by Interp Demo user program');
		Save_NetResFlg_Comments('Curve written by Interp Demo user program');
		Save_NetPayFlg_Comments('Curve written by Interp Demo user program');


		% show any errors
	catch exception
	
		errordlg(strcat('Error occurred: ', exception.getReport()));
        
		% close the report file
		fclose(outFile);
	end
    
end

function CalculatePicket(up)
        
    Methods

    % Calculate the Pickett plot line end points
    %
    % Calculate m amd Rw from end point lines
    Phi1 = PPphi1(-1);
    Phi2 = PPphi2(-1);
    Ro1 = PPres1(-1);
    Ro2 = PPres2(-1);
    if (Phi1 ~= Phi2)

        xmc = ( log10(max(Ro1,0.01)) - log10(max(Ro2,0.01)) ) / ( log10(max(Phi2,0.001)) - log10(max(Phi1,0.001)) );

    else

        xmc = xm(-1);
    end;
    Rwc = (Ro1 * power(Phi1,xmc)) / xa(-1);
    Rwc = max(0.0001, min(Rwc,100.0));
    %
    %  Check to see if the values calculated are the default values
    %  If they are then assume that the pickett plot is not open and in use
    %  and therefore assume that the values to use for m and Rw are the input normal parameters
    %
    if ( ( abs(Rwc-Rwpick(-1)) < 0.001) && ( abs(xmc-Mpick(-1)) < 0.01) )

        Rwc = Rw(-1);
        Save_Rwpick(-1,Rwc);
        xmc = xm(-1);
        Save_Mpick(-1,xmc);
        %   Recalculate the line using the parameter values of m and Rw and save
        Ro1 = xa(-1) * Rwc * power(Phi1,-xmc);
        Ro2 = xa(-1) * Rwc * power(Phi2,-xmc);
        Save_PPres1(-1,Ro1);
        Save_PPres2(-1,Ro2);

    else

        %   New values of m and Rw save these and also the pickett defaults
        Save_Rw(-1,Rwc);
        Save_xm(-1,xmc);
        Save_Rwpick(-1,Rwc);
        Save_Mpick(-1,xmc);
    end;
end
