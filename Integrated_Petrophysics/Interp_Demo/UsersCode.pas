unit UsersCode;

interface

uses Functions, Math;

Procedure UserCode; stdcall;
// declare other procedures and function in this Unit
Procedure  CalculatePickett;

implementation

{User Code}
Procedure UserCode; stdcall;
// declare all variables
Var
   index, I : Integer;
   PayNet, ResNet, PhiPay, PhiRes, SwPay, SwRes, VclPay, VclRes, BVWPay, BVWRes, PayCount, ResCount : Single;
   D, S, G, Por, VClay, PorClay, Res, XX, WatSat, BVW, WS, Step, Rwa, F, ResFlg, PayFlg : Single;
   OutFile : TextFile;
   RwString : String;
begin
// calculate the Pickett plot end point parameters
   CalculatePickett;
// Intitalize zonal averages
   PayNet := 0.0;
   ResNet := 0.0;
   PhiPay := 0.0;
   PhiRes := 0.0;
   SwPay := 0.0;
   SwRes := 0.0;
   VclPay := 0.0;
   VclRes := 0.0;
   BVWPay := 0.0;
   BVWRes := 0.0;
   PayCount := 0.0;
   ResCount := 0.0;
//
// Loop through the data one level at a time
// Topdepth and BottomDepth are the index equivalent depths entered on the run window.
//
   FOR index := Topdepth TO BottomDepth DO BEGIN
//
//
//     Calculate porosity depending om method
        IF PorEq() = 'Sonic' THEN BEGIN
           S := Son(INDEX);
           IF (S > 0.0) THEN
             Por := (S - SonMat(INDEX)) * SonCp(INDEX) / (SonFluid(INDEX) - SonMat(INDEX))
           ELSE
              Por := -999.0;
//      Calculate clay porosity
           PorClay := (SonClay(INDEX) - SonMat(INDEX)) * SonCp(INDEX) / (SonFluid(INDEX) - SonMat(INDEX));
        END
        ELSE BEGIN
           D := Den(INDEX);
           IF (D > 0.0) THEN
             Por := (D - DenMat(INDEX)) / (DenFluid(INDEX) - DenMat(INDEX))
           ELSE
              Por := -999.0;
//      Calculate clay porosity
           PorClay := (DenClay(INDEX) - DenMat(INDEX)) / (DenFluid(INDEX) - DenMat(INDEX));
        END;

//     Calculate Clay volume 
        G := GR(INDEX);
        IF G <> -999.0 THEN BEGIN
           VClay := (G - GRCLEAN(INDEX)) / (GRCLAY(INDEX) - GRCLEAN(INDEX));
           IF (Vclay > 1.0) THEN
              Vclay := 1.0
           ELSE IF (Vclay < 0.0) THEN
              Vclay := 0.0;
//     Correct Porosity for clay
           Por := Por - Vclay * PorClay;
           IF Por < 0.0001 THEN
              Por := 0.0001;
        END
        ELSE BEGIN
           VClay := -999.0;
           Por := -999.0;
        END;

//     Calculate Water Saturation
        Res := Rt(Index);
        IF (Por <= 0.0) OR (Res <= 0.0) THEN BEGIN
           WatSat := -999.0;
           Rwa := -999.0;
           BVW := -999.0;
        END
        ELSE BEGIN
//         Check for Shell m
           IF Shellm() THEN
              XX := 1.87 + 0.019 / Por
           ELSE
//            set m to input parameter
              XX := XM(INDEX);
//         Check for Archie equation
           IF SwEq() = 'Archie' THEN BEGIN
//            calculate F
              F := XA(INDEX) / Power(Por,XX);
//        calculate Sw
              WatSat := Power(F * Rw(INDEX) / Res, 1.0/XN(INDEX));
           END
           ELSE
//        calculate Sw Indonesian
              WatSat := Power( Sqrt(Res) * ( Power(VClay, (1.0-VClay/2.0)) / Sqrt(Rclay(INDEX)) +
                         Power(Por, (XX/2.0)) / Sqrt(XA(INDEX)*Rw(INDEX)) ), -2.0/XN(INDEX));
//         Limit Sw
           IF WatSat > 1.2 THEN
              WatSat := 1.2;
//         calculate Rw apparent
           Rwa := Res * Power(Por, XX) / XA(INDEX);
//         calculate BVW
           IF WatSat < 1.0 THEN
              BVW := WatSat * Por
           ELSE
              BVW := Por;
        END;
        
//  calculate the Net pay and net reservoir
//      Limit Sw to 1.0
        IF WatSat > 1.0 THEN
           WS := 1.0
        ELSE
           WS := WatSat;
        IF (Por >= PhiCut(INDEX)) AND (VClay <= VclCut(INDEX)) THEN BEGIN
           ResFlg := 1.0;
           IF WS <= SwCut(INDEX) THEN
              PayFlg := 1.0
           ELSE
              PayFlg := 0.0;
        END
        ELSE BEGIN
           ResFlg := 0.0;
           PayFlg := 0.0;
        END;
        
//  add results to zone averages
        IF ResFlg = 1.0 THEN BEGIN
            ResCount := ResCount + 1.0;
            PhiRes := PhiRes + Por;
            BVWRes := BVWRes + Por * WS;
            VclRes := VclRes + VClay;
        END;
        IF PayFlg = 1.0 THEN BEGIN
            PayCount := PayCount + 1.0;
            PhiPay := PhiPay + Por;
            BVWPay := BVWPay + Por * WS;
            VclPay := VclPay + VClay;
        END;

//   output the curve results
        SAVE_Phi(INDEX,Por);
        SAVE_Vcl(INDEX,VClay);
        SAVE_Sw(INDEX,WatSat);
        SAVE_Rwapp(INDEX,Rwa);
        SAVE_BVW(INDEX,BVW);
        SAVE_NetResFlg(INDEX,ResFlg);
        SAVE_NetPayFlg(INDEX,PayFlg);
                            
  END;  // for index := Topdepth .....
//
//
//    Calculate Well Step from first 2 depths
      Step := Depth(Topdepth+1) - Depth(Topdepth);
//    Calculate the zonal averages
      ResNet := ResCount * Step;
      IF ResCount = 0.0 THEN BEGIN
         PhiRes := 0.0;
         VclRes := 0.0;
         BVWRes := 0.0;
         SwRes  := 0.0;
      END
      ELSE BEGIN
         PhiRes := PhiRes / ResCount;
         VclRes := VclRes / ResCount;
         BVWRes := BVWRes / ResCount;
         SwRes  := BVWRes / PhiRes;
      END;
      
      PayNet := PayCount * Step; 
      IF PayCount = 0.0 THEN BEGIN
         PhiPay := 0.0;
         VclPay := 0.0;
         BVWPay := 0.0;
         SwPay  := 0.0;
      END
      ELSE BEGIN
         PhiPay := PhiPay / PayCount;
         VclPay := VclPay / PayCount;
         BVWPay := BVWPay / PayCount;
         SwPay  := BVWPay / PhiRes;
      END;
//
//    Output results back to parameters
//    We loop through all the data because it is possible that the result parameters are set as curves !
      FOR INDEX := Topdepth to BottomDepth do BEGIN
         SAVE_NetRes(INDEX,ResNet);
         SAVE_AvPhiRes(INDEX,PhiRes);
         SAVE_AvVclRes(INDEX,VclRes);
         SAVE_AvSwRes(INDEX,SwRes);
      
         SAVE_NetPay(INDEX,PayNet);
         SAVE_AvPhiPay(INDEX,PhiPay);
         SAVE_AvVclPay(INDEX,VclPay);
         SAVE_AvSwPay(INDEX,SwPay);
      END;
//    
//
// Create a report to a file if this is the last zone
   IF ZoneNumber = TotalZones THEN BEGIN
		AssignFile(OutFile,'Interp Demo Pascal Report.TXT');
    try
      Rewrite(OutFile);
      WriteLn(OutFile,' USER PROGRAM INTERP DEMO PARAMETERS');
      WriteLn(OutFile);
      WriteLn(OutFile,' Well    : ', Well_Name);
      // Write well attributes using attribute name
      WriteLn(OutFile, ' Company : ', Read_Well_Attribute('Company'));
      WriteLn(OutFile, ' Field   : ', Read_Well_Attribute('Field'));
      WriteLn(OutFile, ' KB Elev : ', Read_Well_Attribute('KBElev'));
      WriteLn(OutFile, ' Input Curves ');
      WriteLn(OutFile, '    Rt     = ', Rt_Name(), '(', Rt_Units(), ')');
      WriteLn(OutFile, '    Gr     = ', Gr_Name(), '(', Gr_Units(), ')');
      WriteLn(OutFile, '    Den    = ', Den_Name(), '(', Den_Units(), ')');
      WriteLn(OutFile, '    Son    = ', Son_Name(), '(', Son_Units(), ')');
      WriteLn(OutFile, ' Output Curve ');
      WriteLn(OutFile, '    Phi    = ', Phi_Name(), '(', Phi_Units(), ')');
      WriteLn(OutFile, '    Vcl    = ', Vcl_Name(), '(', Vcl_Units(),')');
      WriteLn(OutFile, '    Sw     = ', Sw_Name(), '(', Sw_Units(),')');
      WriteLn(OutFile, '    Rwapp  = ', RwApp_Name(), '(', RwApp_Units(),')');
      WriteLn(OutFile, '    BVW    = ', BVW_Name(), '(', BVW_Units(),')');
      WriteLn(OutFile, '    NetPay = ', NetPayFlg_Name() );
      WriteLn(OutFile, '    NetRes = ', NetResFlg_Name() );
      
  //      Write the parameters by zone   
      FOR I := 1 TO TotalZones DO BEGIN  
  //         Set the zone number so we can get the parameters for each zone        
              SetZone(I);
        WriteLn(OutFile);
        WriteLn(OutFile, ' Zone ', I, ' Input Parameters ');
        WriteLn(OutFile, '    a          = ', Xa(1):8:3);
        WriteLn(OutFile, '    m          = ', XM(1):8:3);
        WriteLn(OutFile, '    n          = ', XN(1):8:3);
        WriteLn(OutFile, '    Rw         = ', Rw(1):8:3);
        WriteLn(OutFile, '    Sw Eq      = ', SwEq());
        WriteLn(OutFile, '    Son Matrix = ', SonMat(1):8:3);
        WriteLn(OutFile, '    Son Fluid  = ', SonFluid(1):8:3);
        WriteLn(OutFile, '    Son CP     = ', SonCp(1):8:3);
        WriteLn(OutFile, '    Son Clay   = ', SonClay(1):8:3);
        WriteLn(OutFile, '    Den Matrix = ', DenMat(1):8:3 );
        WriteLn(OutFile, '    Den Fluid  = ', DenFluid(1):8:3);
        WriteLn(OutFile, '    Por Eq     = ', PorEq() );
        WriteLn(OutFile, '    Den Clay   = ', DenClay(1):8:3);
        WriteLn(OutFile, '    Gr Clean   = ', GrClean(1):8:3);
        WriteLn(OutFile, '    Gr Clay    = ', GrClay(1):8:3);
        WriteLn(OutFile, '    Depth Interval');
        WriteLn(OutFile, '    Top = ',Depth(Topdepth):8:3,'     Bottom = ',Depth(Bottomdepth):8:3);
      END;	
    finally
      CloseFile(OutFile);
    end;
   END;		
//
//  Write to database who created these curves
   Save_Sw_Comments('Curve written by Interp Demo user program');
   Save_Rwapp_Comments('Curve written by Interp Demo user program');
   Save_Phi_Comments('Curve written by Interp Demo user program');
   Save_Vcl_Comments('Curve written by Interp Demo user program');
   Save_BVW_Comments('Curve written by Interp Demo user program');
   Save_NetResFlg_Comments('Curve written by Interp Demo user program');
   Save_NetPayFlg_Comments('Curve written by Interp Demo user program');
   
   EXIT;
//
END;
//
//
//
//   Calculate the Pickett plot line end points
//
Procedure  CalculatePickett;
Var
   Phi1, Phi2, Ro1, Ro2, xmc, Rwc : Single;
BEGIN
//
//
//   Calculate m amd Rw from end point lines
   Phi1 := PPphi1(-1);
   Phi2 := PPphi2(-1);
   Ro1 := PPres1(-1);
   Ro2 := PPres2(-1);
   IF Phi1 <> Phi2 THEN
      xmc := ( Log10(Max(Ro1,0.01)) - Log10(Max(Ro2,0.01)) ) /
             ( Log10(Max(Phi2,0.001)) - Log10(Max(Phi1,0.001)) )
   ELSE
      xmc := xm(-1);
   Rwc := Ro1 * Power(Phi1, xmc) / XA(-1);
   Rwc := Max(0.0001,Min(Rwc,100.0));
//
//  Check to see if the values calculated are the default values
//  If they are then assume that the pickett plot is not open and in use
//  and therefore assume that the values to use for m and Rw are the input normal parameters
//
   IF ( ABS(Rwc-RwPick(-1)) < 0.001) AND ( ABS(xmc-MPick(-1)) < 0.01) THEN BEGIN
      Rwc := Rw(-1);
      SAVE_RwPick(-1,Rwc);
      xmc := xm(-1);
      SAVE_MPick(-1,xmc);
//   Recalculate the line using the parameter values of m and Rw and save
      Ro1 := xa(-1) * Rwc * Power(Phi1, -xmc);
      Ro2 := xa(-1) * Rwc * Power(Phi2, -xmc);
      SAVE_PPres1(-1,Ro1);
      SAVE_PPres2(-1,Ro2);
   END
   ELSE BEGIN
//   New values of m and Rw save these and also the pickett defaults
      SAVE_Rw(-1,Rwc);
      SAVE_xm(-1,xmc);
      SAVE_Rwpick(-1,Rwc);
      SAVE_Mpick(-1,xmc);
   END;
//
END;

end.
