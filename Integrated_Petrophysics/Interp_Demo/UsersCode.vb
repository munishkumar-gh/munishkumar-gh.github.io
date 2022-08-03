Imports System.IO
Imports System.Windows.Forms

Partial Public Class IPLink

    Public Sub UserCode()

        Dim index, i as Integer
        Dim writer As TextWriter = Nothing
        Dim PayNet, ResNet, PhiPay, PhiRes, SwPay, SwRes, VclPay, VclRes, BVWPay, BVWRes, PayCount, ResCount as Single
        Dim D, S, G, Por, VClay, PorClay, Res, XX, WatSat, BVW, WS, IStep, Rwa, F, ResFlg, PayFlg as Single 

        Try
    '   calculate the Pickett plot end point parameters
        CalculatePickett()
    '
    '   Intitalize zonal averages
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
    '
    '   Loop through the data one level at a time
    '   TopDepth and BottomDepth are the index equivalent depths entered on the run window. 
    ' 
        For index = TopDepth To BottomDepth
    '
    '
    '       Calculate porosity depending om method 
            If (PorEq = "Sonic") Then
               S = Son(index)
               IF (S > 0.0) Then
                 Por = (S - SonMat(index)) * SonCp(index) / _
                       (SonFluid(index) - SonMat(index))  
               Else
                  Por = -999.0
               End If   
    '          Calculate clay porosity              
               PorClay = (SonClay(index) - SonMat(index)) * SonCp(index) / _
                          (SonFluid(index) - SonMat(index))  
            Else 
               D = Den(index)
               IF (D > 0.0) Then
                  Por = (D - DenMat(index)) / (DenFluid(index) - DenMat(index))  
               Else
                  Por = -999.0
               End If
    '          Calculate clay porosity              
               PorClay = (DenClay(index) - DenMat(index)) / (DenFluid(index) - DenMat(index))  
            End If   
            
    '       Calculate Clay volume 
            G = GR(index)
            If (G <> -999.0) Then 
               VClay = (G - GrClean(index)) / (GrClay(index) - GrClean(index))
               If (Vclay > 1.0) Then
                  Vclay = 1.0
               Else IF (Vclay < 0.0) Then
                  Vclay = 0.0
               End If
    '       Correct Porosity for clay 
               Por = Por - Vclay * PorClay
               IF (Por < 0.0001) Then 
                  Por = 0.0001 
               End If
            Else
               VClay = -999.0
               Por = -999.0
            End If    
            
    '       Calculate Water Saturation
            Res = Rt(Index)
            If ((Por <= 0.0) OrElse (Res <= 0.0)) Then
               WatSat = -999.0
               Rwa = -999.0
               BVW = -999.0
            Else
    '          Check for Shell m
               If (Shellm) Then
                   XX = 1.87 + 0.019 / Por
               Else
    '          set m to input parameter 
                   XX = XM(index)
               End If
    '          Check for Archie equation  
               If (SwEq = "Archie") Then
    '             calculate F
                   F = XA(index) / Math.Pow(Por,XX)
    '             calculate Sw
                   WatSat = Math.Pow(F * Rw(index) / Res,(1.0/XN(index)))
               Else
    '             calculate Sw Indonesian 
                   WatSat = Math.Pow( Math.Pow(Res,0.5) * ( Math.Pow(VClay, (1.0-VClay/2.0)) / Math.Pow(Rclay(index),0.5) + _
                            Math.Pow(Por, (XX/2.0)) / Math.Pow(xa(index)*Rw(index),0.5) ), -2.0/xn(index))
               End If   
    '          Limit Sw            
               If (WatSat > 1.2) Then
                   WatSat = 1.2
               End If    
    '          calculate Rw apparent
               Rwa = Res * Math.Pow(Por,XX) / XA(index)
    '          calculate BVW
               If (WatSat < 1.0) Then
                   BVW = WatSat * Por 
               Else
                   BVW = Por
               End If                 
            End If
            
    '    calculate the Net pay and net reservoir
    '       Limit Sw to 1.0
            If (WatSat > 1.0) Then
               WS = 1.0
            Else
               WS = WatSat      
            End If   
 
            If ((Por >= PhiCut(index)) and (VClay <= VclCut(index))) Then
               ResFlg = 1.0
               If (WS <= SwCut(index)) Then
                  PayFlg = 1.0
               Else   
                  PayFlg = 0.0
               End If 
            Else
               ResFlg = 0.0
               PayFlg = 0.0
            End If
            
    '    add results to zone averages 
            IF (ResFlg = 1.0) Then  
               ResCount = ResCount + 1.0
               PhiRes = PhiRes + Por
               BVWRes = BVWRes + Por * WS
               VclRes = VclRes + VClay
            End If    
            If (PayFlg = 1.0) Then  
               PayCount = PayCount + 1.0
               PhiPay = PhiPay + Por
               BVWPay = BVWPay + Por * WS
               VclPay = VclPay + VClay
            End If    
            
    '   output the curve results
            SAVE_Phi(index,Por)
            SAVE_Vcl(index,VClay)
            SAVE_Sw(index,WatSat)
            SAVE_Rwapp(index,Rwa)
            SAVE_BVW(index,BVW)
            SAVE_NetResFlg(index,ResFlg)
            SAVE_NetPayFlg(index,PayFlg)
                                
       Next
    '
    '
    '    Calculate Well Step from first 2 depths
        IStep = Depth(TopDepth()+1) - Depth(TopDepth()) 
    '    Calculate the zonal averages
        ResNet = ResCount * IStep
        If (ResCount = 0.0) Then
            PhiRes = 0.0  
            VclRes = 0.0 
            BVWRes = 0.0
            SwRes  = 0.0
        Else
            PhiRes = PhiRes / ResCount  
            VclRes = VclRes / ResCount  
            BVWRes = BVWRes / ResCount
            SwRes  = BVWRes / PhiRes 
        End If
          
        PayNet = PayCount * IStep 
        If (PayCount = 0.0) Then
            PhiPay = 0.0 
            VclPay = 0.0  
            BVWPay = 0.0
            SwPay  = 0.0
        Else
            PhiPay = PhiPay / PayCount  
            VclPay = VclPay / PayCount  
            BVWPay = BVWPay / PayCount
            SwPay  = BVWPay / PhiRes 
        End If    
    '
    '    Output results back to parameters
    '    We loop through all the data because it is possible that the result parameters are set as curves !
        For index = TopDepth To BottomDepth
            SAVE_NetRes(index,ResNet)
            SAVE_AvPhiRes(index,PhiRes)
            SAVE_AvVclRes(index,VclRes)
            SAVE_AvSwRes(index,SwRes)
          
            SAVE_NetPay(index,PayNet)
            SAVE_AvPhiPay(index,PhiPay)
            SAVE_AvVclPay(index,VclPay)
            SAVE_AvSwPay(index,SwPay)
        Next
    '      
    ' 
    '   Create a report to a file if this is the last zone
        If (ZoneNumber = TotalZones) Then
            writer = New StreamWriter("Interp Demo VB Report.TXT")
            writer.WriteLine(" USER PROGRAM INTERP PARAMETERS")
            writer.WriteLine()
            writer.WriteLine(" Well    : " & Well_Name)
        '   Write well attributes using attribute name  
            writer.WriteLine(" Company : " & Read_Well_Attribute("Company"))
            writer.WriteLine(" Field   : " & Read_Well_Attribute("Field"))
            writer.WriteLine(" KB Elev : " & Read_Well_Attribute("KBElev"))
            writer.WriteLine()
            writer.WriteLine(" Input Curves ")
            writer.WriteLine(String.Concat("    Rt         = ", Rt_Name, " (", Rt_Units, ")"))
            writer.WriteLine(String.Concat("    Gr         = ", Gr_Name, " (", Gr_Units, ")"))
            writer.WriteLine(String.Concat("    Den        = ", Den_Name, " (", Den_Units, ")"))
            writer.WriteLine(String.Concat("    Son        = ", Son_Name, " (", Son_Units, ")"))
            writer.WriteLine(" Output Curves ")
            writer.WriteLine(String.Concat("    Phi        = ", Phi_Name, " (", Phi_Units, ")"))
            writer.WriteLine(String.Concat("    Vcl        = ", Vcl_Name, " (", Vcl_Units, ")"))
            writer.WriteLine(String.Concat("    Sw         = ", Sw_Name, " (", Sw_Units, ")"))
            writer.WriteLine(String.Concat("    BVW        = ", BVW_Name, " (", BVW_Units, ")"))
            writer.WriteLine(String.Concat("    Rwapp      = ", Rwapp_Name, " (", Rwapp_Units, ")"))
            writer.WriteLine(String.Concat("    NetPay Flg = ", NetPayFlg_Name))
            writer.WriteLine(String.Concat("    NetRes Flg = ", NetResFlg_Name))
            For i = 1 To TotalZones
                ' Set the zone number so we can get the parameters for each zone        
                SetZone(i)
                writer.WriteLine()
                writer.WriteLine(String.Concat(" Zone ", i, " Input Parameters "))
                writer.WriteLine(String.Format("    a          = {0:00.0000}", XA(1)))
                writer.WriteLine(String.Format("    m          = {0:00.0000}", XM(1)))
                writer.WriteLine(String.Format("    n          = {0:00.0000}", XN(1)))
                writer.WriteLine(String.Format("    Rw         = {0:00.0000}", Rw(1)))
                writer.WriteLine(String.Format("    Sw Eq      = {0:00.0000}", SwEq))
                writer.WriteLine(String.Format("    Son Matrix = {0:00.0000}", SonMat(1)))
                writer.WriteLine(String.Format("    Son Fluid  = {0:00.0000}", SonFluid(1)))
                writer.WriteLine(String.Format("    Son CP     = {0:00.0000}", SonCp(1)))
                writer.WriteLine(String.Format("    Son Clay   = {0:00.0000}", SonClay(1)))
                writer.WriteLine(String.Format("    Den Matrix = {0:00.0000}", DenMat(1)))
                writer.WriteLine(String.Format("    Den Fluid  = {0:00.0000}", DenFluid(1)))
                writer.WriteLine(String.Format("    Por Eq     = {0:00.0000}", PorEq))
                writer.WriteLine(String.Format("    Den Clay   = {0:00.0000}", DenClay(1)))
                writer.WriteLine(String.Format("    Gr Clean   = {0:00.0000}", GrClean(1)))
                writer.WriteLine(String.Format("    Gr Clay    = {0:00.0000}", GrClay(1)))
                writer.WriteLine("    Depth Interval")
                writer.WriteLine(String.Format("    Top = {0:00.0000}", Depth(TopDepth)))
                writer.WriteLine(String.Format("    Bottom = {0:00.0000}", Depth(BottomDepth)))
            Next
        End If
    '
    '    Write to database who created these curves
        Save_Sw_Comments("Curve written by Interp Demo user program")
        Save_Rwapp_Comments("Curve written by Interp Demo user program")
        Save_Phi_Comments("Curve written by Interp Demo user program")
        Save_Vcl_Comments("Curve written by Interp Demo user program")
        Save_BVW_Comments("Curve written by Interp Demo user program")
        Save_NetResFlg_Comments("Curve written by Interp Demo user program")
        Save_NetPayFlg_Comments("Curve written by Interp Demo user program")

    
        Catch exception As Exception
           MessageBox.Show(("Error occurred: " & exception.ToString))
        Finally
           If (Not writer Is Nothing) Then
              writer.Flush()
              writer.Close()
           End If
        End Try

      End Sub
'
' 
'   Calculate the Pickett plot line end points
'
      Public Sub  CalculatePickett()
'
      Dim Phi1, Phi2, Ro1, Ro2, xmc, Rwc as Single
'      
'     
'   Calculate m amd Rw from end point lines
      Phi1 = PPphi1(-1)
      Phi2 = PPphi2(-1)
      Ro1 = PPres1(-1)
      Ro2 = PPres2(-1)
      If (Phi1 <> Phi2) Then
         xmc = ( Math.Log10(Math.Max(Ro1,0.01)) - Math.Log10(Math.Max(Ro2,0.01)) ) / _
				( Math.Log10(Math.Max(Phi2,0.001)) - Math.Log10(Math.Max(Phi1,0.001)) )
      Else
         xmc = xm(-1)
      End If
      Rwc = Ro1 * Math.Pow(Phi1, xmc) / XA(-1)
      Rwc = Math.Max(0.0001,Math.Min(Rwc,100.0))
'      
'    Check to see if the values calculated are the default values
'    If they are then assume that the pickett plot is not open and in use
'    and therefore assume that the values to use for m and Rw are the input normal parameters
'
      If ( ( Math.Abs(Rwc-RwPick(-1)) < 0.001) and ( Math.Abs(xmc-MPick(-1)) < 0.01) ) Then
         Rwc = Rw(-1)
         SAVE_RwPick(-1,Rwc)
         xmc = xm(-1)
         SAVE_MPick(-1,xmc)
'        Recalculate the line using the parameter values of m and Rw and save
         Ro1 = XA(-1) * Rwc * Math.Pow(Phi1, -xmc)
         Ro2 = XA(-1) * Rwc * Math.Pow(Phi2, -xmc)
         SAVE_PPres1(-1,Ro1)
         SAVE_PPres2(-1,Ro2)
      Else  
'        New values of m and Rw save these and also the pickett defaults
         SAVE_Rw(-1,Rwc)
         SAVE_XM(-1,xmc)
         SAVE_RwPick(-1,Rwc)
         SAVE_MPick(-1,xmc)
      End If  
'      
    End Sub

End Class