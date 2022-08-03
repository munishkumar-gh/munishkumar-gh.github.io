c
c User Code for Fortran 77
c 
      SUBROUTINE  UserCode()
      IMPLICIT INTEGER (I-N)
      INCLUDE 'InOutDef.INC' 
      CHARACTER*(40) RwString
c
c     All user defined input parameters and logic flags are treated as functions.
c     As such they must be used with a () at the end of their name.
c     For example: Input parameter RW is used in an equation as RW(); AA = RW() + 2.
c     To use trend curves as input parameters the depth INDEX must also be passed into the function.
c       RW(INDEX), AA = RW(INDEX) + 2. 
c
c     Input curves are used in equations as functions.
c     Vclay = (GR(INDEX) - GRclean(INDEX)) / (GRclay(INDEX) - GRclean(INDEX))
c     INDEX is the integer index into the curve array. GRclay and GRclean are defined
c     as input parameters. GR is the input curve. If GRclean is enterd by the use as a fixed value
c     then the INDEX parameter in GRclean(INDEX) is ignored.
c     Input curve DEPTH is always available and does not have to be defined as an input curve.
c
c     Data is saved by using the SAVE_***(INDEX, VALUE) procedure. Where *** is the 
c     output curve name. VALUE is the value to store at INDEX.
c     CALL SAVE_VCL(INDEX, 0.5)   saves value 0.5 into the output curve VCL.
c
c
c     calculate the Pickett plot end point parameters
      Call CalculatePickett
c
c     Intitalize zonal averages
      PayNet = 0.0
      ResNet = 0.0
      PhiPay = 0.0
      PhiRes = 0.0
      SwPay = 0.0
      SwRes = 0.0
      VclPay = 0.0
      VclRes = 0.0
      BVWPay = 0.0
      BVWRes = 0.0
      PayCount = 0.0
      ResCount = 0.0
c
c Loop through the data one level at a time
c Index_Topdepth and Index_BottomDepth are the index equivalent depths entered on the run window. 
C 
      DO 100 INDEX = Index_Topdepth() , Index_BottomDepth()
c
c
c       Calculate porosity depending om method 
        IF (PorEq() .EQ. 'Sonic') THEN
           S = Son(INDEX)
           IF (S .GT. 0.0) THEN
             Por = (S - SonMat(INDEX)) * SonCp(INDEX) / 
     >             (SonFluid(INDEX) - SonMat(INDEX))  
           ELSE
              Por = -999.0
           endif   
c        Calculate clay porosity              
           PorClay = (SonClay(INDEX) - SonMat(INDEX)) * SonCp(INDEX) / 
     >               (SonFluid(INDEX) - SonMat(INDEX))  
           
        ELSE 
           D = Den(INDEX)
           IF (D .GT. 0.0) THEN
             Por = (D - DenMat(INDEX)) / 
     >             (DenFluid(INDEX) - DenMat(INDEX))  
           ELSE
              Por = -999.0
           ENDIF
c        Calculate clay porosity              
           PorClay = (DenClay(INDEX) - DenMat(INDEX)) / 
     >               (DenFluid(INDEX) - DenMat(INDEX))  
        ENDIF   
        
c       Calculate Clay volume 
        G = GR(INDEX)
        IF (G .NE. -999.0) THEN 
           VClay = (G - GRCLEAN(INDEX)) / 
     >           (GRCLAY(INDEX) - GRCLEAN(INDEX))
     
           IF (Vclay .GT. 1.0) THEN
              Vclay = 1.0
           ELSEIF (Vclay .LT. 0.0) THEN
              Vclay = 0.0
           ENDIF   
c       Correct Porosity for clay 
           Por = Por - Vclay * PorClay
           IF (Por .LT. 0.0001) THEN 
              Por = 0.0001 
           ENDIF      
        ELSE
           VClay = -999.0
           Por = -999.0
        ENDIF    
        
c       Calculate Water Saturation
        Res = Rt(Index)
        IF ((Por .LE. 0.0) .OR. (Res .LE. 0.0)) THEN
           WatSat = -999.0
           Rwa = -999.0
           BVW = -999.0
        ELSE
c       Check for Shell m
           IF (Shellm()) THEN
              XX = 1.87 + 0.019 / Por
           ELSE
c       set m to input parameter 
              XX = XM(INDEX)
           ENDIF
c       Check for Archie equation  
           IF (SwEq() .EQ. 'Archie') THEN
c          calculate F
              F = XA(INDEX) / Por**XX
c          calculate Sw
              WatSat = (F * Rw(INDEX) / Res)**(1.0/XN(INDEX))
           ELSE
c          calculate Sw Indonesian 
              WatSat = (Res**0.5 *
     >                 ( VClay**(1.0-VClay/2.0) / Rclay(INDEX)**0.5 +
     >                    Por**(XX/2.0) / (XA(INDEX)*Rw(INDEX))**0.5 )
     >                     ) ** (-2.0/XN(INDEX))
           ENDIF   
c   Limit Sw            
           IF (WatSat .GT. 1.2) THEN
              WatSat = 1.2
           ENDIF    
C   calculate Rw apparent
           Rwa = Res * Por**XX / XA(INDEX)
c   calculate BVW
           IF (WatSat .LT. 1.0) THEN
              BVW = WatSat * Por 
           ELSE
              BVW = Por
           ENDIF                 
        ENDIF
        
c    calculate the Net pay and net reservoir
c       Limit Sw to 1.0
        IF (WatSat .GT. 1.0) THEN
           WS = 1.0
        ELSE
           WS = WatSat      
        ENDIF    
        IF ((Por .GE. PhiCut(INDEX)) .AND. 
     >      (VClay .LE. VclCut(INDEX))) THEN
           ResFlg = 1.0
           IF (WS .LE. SwCut(INDEX)) THEN
              PayFlg = 1.0
           ELSE   
              PayFlg = 0.0
           ENDIF 
        ELSE
           ResFlg = 0.0
           PayFlg = 0.0
        ENDIF
        
c    add results to zone averages 
        IF (ResFlg .EQ. 1.0) THEN  
            ResCount = ResCount + 1.0
            PhiRes = PhiRes + Por
            BVWRes = BVWRes + Por * WS
            VclRes = VclRes + VClay
        ENDIF    
        IF (PayFlg .EQ. 1.0) THEN  
            PayCount = PayCount + 1.0
            PhiPay = PhiPay + Por
            BVWPay = BVWPay + Por * WS
            VclPay = VclPay + VClay
        ENDIF    
        
c   output the curve results
        Call SAVE_Phi(INDEX,Por)
        Call SAVE_Vcl(INDEX,VClay)
        Call SAVE_Sw(INDEX,WatSat)
        Call SAVE_Rwapp(INDEX,Rwa)
        Call SAVE_BVW(INDEX,BVW)
        Call SAVE_NetResFlg(INDEX,ResFlg)
        Call SAVE_NetPayFlg(INDEX,PayFlg)
                            
  100 CONTINUE
c
c
c    Calculate Well Step from first 2 depths
      Step = Depth(Index_Topdepth()+1) - Depth(Index_Topdepth()) 
c    Calculate the zonal averages
      ResNet = ResCount * Step
      IF (ResCount .EQ. 0.0) THEN
         PhiRes = 0.0  
         VclRes = 0.0 
         BVWRes = 0.0
         SwRes  = 0.0
      ELSE
         PhiRes = PhiRes / ResCount  
         VclRes = VclRes / ResCount  
         BVWRes = BVWRes / ResCount
         SwRes  = BVWRes / PhiRes 
      ENDIF
      
      PayNet = PayCount * Step 
      IF (PayCount .EQ. 0.0) THEN
         PhiPay = 0.0 
         VclPay = 0.0  
         BVWPay = 0.0
         SwPay  = 0.0
      ELSE
         PhiPay = PhiPay / PayCount  
         VclPay = VclPay / PayCount  
         BVWPay = BVWPay / PayCount
         SwPay  = BVWPay / PhiRes 
      ENDIF    
c
c    Output results back to parameters
c    We loop through all the data because it is possible that the result parameters are set as curves !
      DO INDEX = Index_Topdepth() , Index_BottomDepth()
         Call SAVE_NetRes(INDEX,ResNet)
         Call SAVE_AvPhiRes(INDEX,PhiRes)
         Call SAVE_AvVclRes(INDEX,VclRes)
         Call SAVE_AvSwRes(INDEX,SwRes)
      
         Call SAVE_NetPay(INDEX,PayNet)
         Call SAVE_AvPhiPay(INDEX,PhiPay)
         Call SAVE_AvVclPay(INDEX,VclPay)
         Call SAVE_AvSwPay(INDEX,SwPay)
      ENDDO
c      
c 
C   Create a report to a file if this zone is the last zone
      IF (ZoneNumber() .EQ. TotalZones()) THEN
        OPEN (UNIT=55,FILE='Interp Demo FORTRAN Report.TXT',
     >        STATUS='UNKNOWN')
        write(55,*) ' USER PROGRAM INTERP PARAMETERS'
        write(55,*) ''
        write(55,*) ' Well    : ', Well_Name()
c   Write well attributes using attribute name         
        write(55,*) ' Company : ', Read_Well_Attribute('Company') 
        write(55,*) ' Field   : ', Read_Well_Attribute('Field')
        write(55,*) ' KB Elev : ', Read_Well_Attribute('KBElev')
        write(55,*) ' Input Curves '
        write(55,*) '    Rt     = ', Rt_Name(), '(', Rt_Units(), ')'
        write(55,*) '    Gr     = ', Gr_Name(), '(', Gr_Units(), ')'
        write(55,*) '    Den    = ', Den_Name(), '(', Den_Units(), ')'
        write(55,*) '    Son    = ', Son_Name(), '(', Son_Units(), ')'
        write(55,*) ' Output Curve '
        write(55,*) '    Phi    = ', Phi_Name(), '(', Phi_Units(), ')'
        write(55,*) '    Vcl    = ', Vcl_Name(), '(', Vcl_Units(),')'
        write(55,*) '    Sw     = ', Sw_Name(), '(', Sw_Units(),')'
        write(55,*) '    Rwapp  = ', RwApp_Name(), '(', RwApp_Units(),
     >       ')'
        write(55,*) '    BVW    = ', BVW_Name(), '(', BVW_Units(),')'
        write(55,*) '    NetPay = ', NetPayFlg_Name()
        write(55,*) '    NetRes = ', NetResFlg_Name()
c   Write the parameters by zone   
        DO I = 1, TotalZones()  
c       Set the zone number so we can get the parameters for each zone        
           Call SetZone(I)
           write(55,*) ''
           write(55,*) ' Zone ', I, ' Input Parameters '
           write(55,*) '    a          = ', Xa(1)
           write(55,*) '    m          = ', XM(1)
           write(55,*) '    n          = ', XN(1)
           write(55,*) '    Rw         = ', Rw(1)
           write(55,*) '    Sw Eq      = ', SwEq()
           write(55,*) '    Son Matrix = ', SonMat(1)
           write(55,*) '    Son Fluid  = ', SonFluid(1)
           write(55,*) '    Son CP     = ', SonCp(1)
           write(55,*) '    Son Clay   = ', SonClay(1)
           write(55,*) '    Den Matrix = ', DenMat(1)
           write(55,*) '    Den Fluid  = ', DenFluid(1)
           write(55,*) '    Por Eq     = ', PorEq()
           write(55,*) '    Den Clay   = ', DenClay(1)
           write(55,*) '    Gr Clean   = ', GrClean(1)
           write(55,*) '    Gr Clay    = ', GrClay(1)
           write(55,*) '    Depth Interval'
           write(55,*) '    Top = ',Depth(Index_Topdepth()), 
     >                 '  Bottom = ',Depth(Index_Bottomdepth()) 
        ENDDO
        CLOSE (UNIT=55,STATUS='KEEP') 
      ENDIF  
c
c    Write to database who created these curves
      call Save_Sw_Comments(
     >      'Curve written by Interp Demo user program')
      call Save_Rwapp_Comments(
     >      'Curve written by Interp Demo user program')
      call Save_Phi_Comments(
     >      'Curve written by Interp Demo user program')
      call Save_Vcl_Comments(
     >      'Curve written by Interp Demo user program')
      call Save_BVW_Comments(
     >      'Curve written by Interp Demo user program')
      call Save_NetResFlg_Comments(
     >      'Curve written by Interp Demo user program')
      call Save_NetPayFlg_Comments(
     >      'Curve written by Interp Demo user program')
c    
c    
c   
      RETURN
c
      END
c
c 
c   Calculate the Pickett plot line end points
c
      SUBROUTINE  CalculatePickett()
      IMPLICIT INTEGER (I-N)
      INCLUDE 'InOutDef.INC' 
c      
c      
c   Calculate m amd Rw from end point lines
      Phi1 = PPphi1(-1)
      Phi2 = PPphi2(-1)
      Ro1 = PPres1(-1)
      Ro2 = PPres2(-1)
      IF (Phi1 .NE. Phi2) THEN
         xmc = ( Log10(Max(Ro1,0.01)) - Log10(Max(Ro2,0.01)) ) / 
     >         ( Log10(Max(Phi2,0.001)) - Log10(Max(Phi1,0.001)) )
      ELSE
         xmc = xm(-1)
      ENDIF
      Rwc = Ro1 * Phi1**xmc / XA(-1)
      Rwc = Max(0.0001,Min(Rwc,100.0))
c      
c    Check to see if the values calculated are the default values
c    If they are then assume that the pickett plot is not open and in use
c    and therefore assume that the values to use for m and Rw are the input normal parameters
c
      IF ( ( ABS(Rwc-RwPick(-1)) .LT. 0.001) .AND. 
     >     ( ABS(xmc-MPick(-1)) .LT. 0.01) ) THEN
         Rwc = Rw(-1)
         Call SAVE_RwPick(-1,Rwc)
         xmc = xm(-1)
         Call SAVE_MPick(-1,xmc)
c     Recalculate the line using the parameter values of m and Rw and save
         Ro1 = XA(-1) * Rwc * Phi1**(-xmc)
         Ro2 = XA(-1) * Rwc * Phi2**(-xmc)
         Call SAVE_PPres1(-1,Ro1)
         Call SAVE_PPres2(-1,Ro2)
      ELSE  
c     New values of m and Rw save these and also the pickett defaults
         Call SAVE_Rw(-1,Rwc)
         Call SAVE_XM(-1,xmc)
         Call SAVE_RwPick(-1,Rwc)
         Call SAVE_MPick(-1,xmc)
      ENDIF  
c      
      END
