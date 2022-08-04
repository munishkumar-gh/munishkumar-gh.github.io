using System;
using System.IO;
using System.Windows.Forms;


public partial class IPLink 
{
	public void UserCode()
	{
        int index, i;
		Single PayNet, ResNet, PhiPay, PhiRes, SwPay, SwRes, VclPay, VclRes, BVWPay, BVWRes, PayCount, ResCount;
		Single D, S, G, Por, VClay, PorClay, Res, XX, WatSat, BVW, WS, Step, Rwa, F, ResFlg, PayFlg; 
		TextWriter writer = null;

        try 
		{
			//   calculate the Pickett plot end point parameters
			CalculatePickett();
			//
			//   Intitalize zonal averages
			PayNet = 0.0f;
			ResNet = 0.0f;
			PhiPay = 0.0f;
			PhiRes = 0.0f;
			SwPay = 0.0f;
			SwRes = 0.0f;
			VclPay = 0.0f;
			VclRes = 0.0f;
			BVWPay = 0.0f;
			BVWRes = 0.0f;
			PayCount = 0.0f;
			ResCount = 0.0f;
			//
			// Loop through the data one level at a time
			// TopDepth and BottomDepth are the index equivalent depths entered on the run window. 
			// 
			for (index = TopDepth; index <= BottomDepth; index++)
			{
				//
				//
				//     Calculate porosity depending om method 
				if (PorEq == "Sonic") 
				{
					S = Son(index);
					if (S > 0.0f) 
					{
						Por = (S - SonMat(index)) * SonCp(index) / (SonFluid(index) - SonMat(index));  
					}
					else 
					{
						Por = -999.0f;
					}
					//      Calculate clay porosity              
					PorClay = (SonClay(index) - SonMat(index)) * SonCp(index) / (SonFluid(index) - SonMat(index));  
				}
				else 
				{ 
					D = Den(index);
					if (D > 0.0f) 
					{
						Por = (D - DenMat(index)) / (DenFluid(index) - DenMat(index)); 
					}
					else 
					{
						Por = -999.0f;
					}
					//      Calculate clay porosity              
					PorClay = (DenClay(index) - DenMat(index)) / (DenFluid(index) - DenMat(index));  
				}   
	        
				//     Calculate Clay volume 
				G = Gr(index);
				if (G != -999.0f) 
				{ 
					VClay = (G - GrClean(index)) / (GrClay(index) - GrClean(index));
					if (VClay > 1.0f) 
					{
						VClay = 1.0f;
					}
					else if (VClay < 0.0f) 
					{
						VClay = 0.0f;
					}
					//     Correct Porosity for clay 
					Por = Por - VClay * PorClay;
					if (Por < 0.0001f) 
					{ 
						Por = 0.0001f ;
					}     
				}
				else 
				{
					VClay = -999.0f;
					Por = -999.0f;
				}    
				//     Calculate Water Saturation
				Res = Rt(index);
				if ((Por < 0.0) | (Res <= 0.0)) 
				{
					WatSat = -999.0f;
					Rwa = -999.0f;
					BVW = -999.0f;
				}
				else 
				{
					//     Check for Shell m
					if (Shellm) 
					{
						XX = 1.87f + 0.019f / Por;
					}
					else 
					{
						//     set m to input parameter 
						XX = xm(index);
					}
					//     Check for Archie equation  
					if (SwEq == "Archie")  
					{
						//        calculate F
						F = xa(index) / (Single)Math.Pow(Por,XX);
						//        calculate Sw
						WatSat = (Single)Math.Pow(F * Rw(index) / Res, 1.0f/xn(index));
					}
					else 
					{
						//        calculate Sw Indonesian 
						WatSat = (Single)Math.Pow( (Single)Math.Pow(Res,0.5f) * ( (Single)Math.Pow(VClay, (1.0f-VClay/2.0f)) / (Single)Math.Pow(Rclay(index),0.5f) +
							     (Single)Math.Pow(Por, (XX/2.0f)) / (Single)Math.Pow(xa(index)*Rw(index),0.5) ), -2.0f/xn(index));
					}
					// Limit Sw            
					if (WatSat > 1.2f) 
					{
						WatSat = 1.2f;
					}
					// calculate Rw apparent
					Rwa = Res * (Single)Math.Pow(Por,XX) / xa(index);
					// calculate BVW
					if (WatSat < 1.0f) 
					{
						BVW = WatSat * Por;
					}
					else 
					{
						BVW = Por;
					}                 
				}
	        
				//  calculate the Net pay and net reservoir
				//     Limit Sw to 1.0
				if (WatSat > 1.0f) 
				{
					WS = 1.0f;
				}
				else 
				{
					WS = WatSat;      
				}    
				if ((Por >= PhiCut(index)) && (VClay <= VclCut(index))) 
				{
					ResFlg = 1.0f;
					if (WS <= SwCut(index)) 
					{
						PayFlg = 1.0f;
					}
					else 
					{   
						PayFlg = 0.0f;
					}
				} 
				else 
				{
					ResFlg = 0.0f;
					PayFlg = 0.0f;
				}
	        
				//  add results to zone averages 
				if (ResFlg == 1.0f) 
				{  
					ResCount = ResCount + 1.0f;
					PhiRes = PhiRes + Por;
					BVWRes = BVWRes + Por * WS;
					VclRes = VclRes + VClay;
				}    
				if (PayFlg == 1.0) 
				{  
					PayCount = PayCount + 1.0f;
					PhiPay = PhiPay + Por;
					BVWPay = BVWPay + Por * WS;
					VclPay = VclPay + VClay;
				}    
	        
				// output the curve results
				Save_Phi(index,Por);
				Save_Vcl(index,VClay);
				Save_Sw(index,WatSat);
				Save_Rwapp(index,Rwa);
				Save_BVW(index,BVW);
				Save_NetResFlg(index,ResFlg);
				Save_NetPayFlg(index,PayFlg);
	                            
			}
			//
			//
			//  Calculate Well Step from first 2 depths
			Step = Depth(TopDepth+1) - Depth(TopDepth); 
			//  Calculate the zonal averages
			ResNet = ResCount * Step;
			if (ResCount == 0.0f) 
			{
				PhiRes = 0.0f;  
				VclRes = 0.0f; 
				BVWRes = 0.0f;
				SwRes  = 0.0f;
			}
			else 
			{
				PhiRes = PhiRes / ResCount;  
				VclRes = VclRes / ResCount;  
				BVWRes = BVWRes / ResCount;
				SwRes  = BVWRes / PhiRes; 
			}
	      
			PayNet = PayCount * Step; 
			if (PayCount == 0.0f) 
			{
				PhiPay = 0.0f; 
				VclPay = 0.0f;  
				BVWPay = 0.0f;
				SwPay  = 0.0f;
			}
			else 
			{
				PhiPay = PhiPay / PayCount;  
				VclPay = VclPay / PayCount;  
				BVWPay = BVWPay / PayCount;
				SwPay  = BVWPay / PhiRes; 
			}    
			//
			//  Output results back to parameters
			//  We loop through all the data because it is possible that the result parameters are set as curves !
			for ( index = TopDepth ; index < BottomDepth ; index++ ) 
			{
				Save_NetRes(index,ResNet);
				Save_AvPhiRes(index,PhiRes);
				Save_AvVclRes(index,VclRes);
				Save_AvSwRes(index,SwRes);
			   
				Save_NetPay(index,PayNet);
				Save_AvPhiPay(index,PhiPay);
				Save_AvVclPay(index,VclPay);
				Save_AvSwPay(index,SwPay);
			}
			//    
			//
            // Create a report to a file if this is the last zone
            if (ZoneNumber == TotalZones) 
            {
                writer = new StreamWriter("Interp Demo c# Report.TXT");
                writer.WriteLine(" USER PROGRAM INTERP PARAMETERS");
                writer.WriteLine();
                writer.WriteLine(" Well    : " + Well_Name);
                // Write well attributes using attribute name         
                writer.WriteLine(" Company : " + Read_Well_Attribute("Company")); 
                writer.WriteLine(" Field   : " + Read_Well_Attribute("Field"));
                writer.WriteLine(" KB Elev : " + Read_Well_Attribute("KBElev"));
                writer.WriteLine();
                writer.WriteLine(" Input Curves ");
                writer.WriteLine("    Rt     = " + Rt_Name +  " (" + Rt_Units + ")");
                writer.WriteLine("    Gr     = " + Gr_Name +  " (" + Gr_Units + ")");
                writer.WriteLine("    Den    = " + Den_Name +  " (" + Den_Units + ")");
                writer.WriteLine("    Son    = " + Son_Name +  " (" + Son_Units + ")");
                writer.WriteLine(" Output Curve ");
                writer.WriteLine("    Phi    = " + Phi_Name +  " (" + Phi_Units + ")");
                writer.WriteLine("    Vcl    = " + Vcl_Name +  " (" + Vcl_Units + ")");
                writer.WriteLine("    Sw     = " + Sw_Name +  " (" + Sw_Units + ")");
                writer.WriteLine("    Rwapp  = " + Rwapp_Name +  " (" + Rwapp_Units + ")");
                writer.WriteLine("    BVW    = " + BVW_Name +  " (" + BVW_Units + ")");
                writer.WriteLine("    NetPay = " + NetPayFlg_Name);
                writer.WriteLine("    NetRes = " + NetResFlg_Name);
                for ( i = 1 ; i <= TotalZones ; i++ ) 
                {  
                    // Set the zone number so we can get the parameters for each zone        
                    SetZone(i);
                    writer.WriteLine();
                    writer.WriteLine(" Input Parameters ");
                    writer.WriteLine("    a          = " + xa(1));
                    writer.WriteLine("    m          = " + xm(1));
                    writer.WriteLine("    n          = " + xn(1));
                    writer.WriteLine("    Rw         = " + Rw(1));
                    writer.WriteLine("    Sw Eq      = " + SwEq);
                    writer.WriteLine("    Son Matrix = " + SonMat(1));
                    writer.WriteLine("    Son Fluid  = " + SonFluid(1));
                    writer.WriteLine("    Son CP     = " + SonCp(1));
                    writer.WriteLine("    Son Clay   = " + SonClay(1));
                    writer.WriteLine("    Den Matrix = " + DenMat(1));
                    writer.WriteLine("    Den Fluid  = " + DenFluid(1));
                    writer.WriteLine("    Por Eq     = " + PorEq);
                    writer.WriteLine("    Den Clay   = " + DenClay(1));
                    writer.WriteLine("    Gr Clean   = " + GrClean(1));
                    writer.WriteLine("    Gr Clay    = " + GrClay(1));
                    writer.WriteLine("    Depth Interval");
                    writer.WriteLine("    Top = " + Depth(TopDepth) + "    Bottom = " + Depth(BottomDepth)); 
                }
            }
			//
			//  Write to database who created these curves
			Save_Sw_Comments("Curve written by Interp Demo user program");
			Save_Rwapp_Comments("Curve written by Interp Demo user program");
			Save_Phi_Comments("Curve written by Interp Demo user program");
			Save_Vcl_Comments("Curve written by Interp Demo user program");
			Save_BVW_Comments("Curve written by Interp Demo user program");
			Save_NetResFlg_Comments("Curve written by Interp Demo user program");
			Save_NetPayFlg_Comments("Curve written by Interp Demo user program");

			//Write_Well_Attribute("Location", "IP Test Location");
			//string RwString = Read_Log_Attribute("Rw", 1);
			//Write_Log_Attribute("Rw", RwString, 2);

		
		}
        // show any errors
		catch (Exception e)
		{
			MessageBox.Show("Error occurred: " + e.ToString());
		}
		finally
		{
			// close the report file 
			if (writer != null)
			{
				writer.Flush();
				writer.Close();
			}
		}
    }
	//
	// 
	// Calculate the Pickett plot line end points
	//
	void  CalculatePickett() 
	{
		//    
		float Phi1, Phi2, Ro1, Ro2, xmc, Rwc;
		//    
		// Calculate m amd Rw from end point lines
		Phi1 = PPphi1(-1);
		Phi2 = PPphi2(-1);
		Ro1 = PPres1(-1);
		Ro2 = PPres2(-1);
		if (Phi1 != Phi2) 
		{
			xmc = ( (Single)Math.Log10(Math.Max(Ro1,0.01f)) - (Single)Math.Log10(Math.Max(Ro2,0.01f)) ) / 
				( (Single)Math.Log10(Math.Max(Phi2,0.001f)) - (Single)Math.Log10(Math.Max(Phi1,0.001f)) );
		}
		else 
		{
			xmc = xm(-1);
		}
		Rwc = Ro1 * (Single)Math.Pow(Phi1,xmc) / xa(-1);
		Rwc = Math.Max(0.0001f,Math.Min(Rwc,100.0f));
		//    
		//  Check to see if the values calculated are the default values
		//  If they are then assume that the pickett plot is not open and in use
		//  and therefore assume that the values to use for m and Rw are the input normal parameters
		//
		if ( ( Math.Abs(Rwc-Rwpick(-1)) < 0.001f) && ( Math.Abs(xmc-Mpick(-1)) < 0.01f) ) 
		{
			Rwc = Rw(-1);
			Save_Rwpick(-1,Rwc);
			xmc = xm(-1);
			Save_Mpick(-1,xmc);
			//   Recalculate the line using the parameter values of m and Rw and save
			Ro1 = xa(-1) * Rwc * (Single)Math.Pow(Phi1,-xmc);
			Ro2 = xa(-1) * Rwc * (Single)Math.Pow(Phi2,-xmc);
			Save_PPres1(-1,Ro1);
			Save_PPres2(-1,Ro2);
		}
		else 
		{  
			//   New values of m and Rw save these and also the pickett defaults
			Save_Rw(-1,Rwc);
			Save_xm(-1,xmc);
			Save_Rwpick(-1,Rwc);
			Save_Mpick(-1,xmc);
		}  
		//    
	}
//   
//
}

