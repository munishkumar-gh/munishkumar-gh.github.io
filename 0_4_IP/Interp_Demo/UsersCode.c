
#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include "Functions.h"
#include <math.h>
#include <string.h>


void  CalculatePickett() ;


extern __declspec (dllexport)  void usercode_()
{
	
   int index, i;
   char *aString; 
   char *attribute; 
   char *aUnits;
   FILE *Outfile;
   float PayNet, ResNet, PhiPay, PhiRes, SwPay, SwRes, VclPay, VclRes, BVWPay, BVWRes, PayCount, ResCount;
   float D, S, G, Por, VClay, PorClay, Res, XX, WatSat, BVW, WS, Step, Rwa, F, ResFlg, PayFlg; 

   aString = InitString( MAX_STRING_1 );
   attribute = InitString( MAX_STRING_1 );
   aUnits  = InitString( MAX_STRING_1 );

//   calculate the Pickett plot end point parameters
   CalculatePickett();
//
//   Intitalize zonal averages
   PayNet = 0.0;
   ResNet = 0.0;
   PhiPay = 0.0;
   PhiRes = 0.0;
   SwPay = 0.0;
   SwRes = 0.0;
   VclPay = 0.0;
   VclRes = 0.0;
   BVWPay = 0.0;
   BVWRes = 0.0;
   PayCount = 0.0;
   ResCount = 0.0;
//
// Loop through the data one level at a time
// TopDepth and BottomDepth are the index equivalent depths entered on the run window. 
// 
   for ( index = TopDepth() ; index <= BottomDepth() ; index++ ) {
//
//
//     Calculate porosity depending om method 
	   if (strcmp(PorEq(), "Sonic") == 0) {
           S = Son(index);
		   if (S > 0.0) {
             Por = (S - SonMat(index)) * SonCp(index) / (SonFluid(index) - SonMat(index));  
		   }
		   else {
              Por = -999.0;
		   }
//      Calculate clay porosity              
          PorClay = (SonClay(index) - SonMat(index)) * SonCp(index) / (SonFluid(index) - SonMat(index));  
	   }
	   else { 
           D = Den(index);
		   if (D > 0.0) {
             Por = (D - DenMat(index)) / (DenFluid(index) - DenMat(index)); 
		   }
		   else {
              Por = -999.0;
		   }
//      Calculate clay porosity              
           PorClay = (DenClay(index) - DenMat(index)) / (DenFluid(index) - DenMat(index));  
	   }   
        
//     Calculate Clay volume 
        G = Gr(index);
		if (G != -999.0) { 
           VClay = (G - GrClean(index)) / (GrClay(index) - GrClean(index));
		   if (VClay > 1.0) {
              VClay = 1.0;
		   }
		   else if (VClay < 0.0) {
              VClay = 0.0;
		   }
//     Correct Porosity for clay 
           Por = Por - VClay * PorClay;
		   if (Por < 0.0001) { 
              Por = 0.0001 ;
		   }     
		}
		else {
           VClay = -999.0;
           Por = -999.0;
		}   

//     Calculate Water Saturation
        Res = Rt(index);
		if ((Por < 0.0) | (Res <= 0.0)) {
           WatSat = -999.0;
           Rwa = -999.0;
           BVW = -999.0;
		}
		else {
//     Check for Shell m
		   if (Shellm()) {
              XX = 1.87 + 0.019 / Por;
		   }
		   else {
//     set m to input parameter 
              XX = xm(index);
		   }

//     Check for Archie equation  
       if (strcmp(SwEq(), "Archie") == 0) {
//        calculate F
              F = xa(index) / pow(Por,XX);
//        calculate Sw
              WatSat = pow(F * Rw(index) / Res, 1.0/xn(index));
		   }
		   else {
//        calculate Sw Indonesian 
              WatSat = pow( pow(Res,0.5) * ( pow(VClay, (1.0-VClay/2.0)) / pow(Rclay(index),0.5) +
                         pow(Por, (XX/2.0)) / pow(xa(index)*Rw(index),0.5) ), -2.0/xn(index));
		   }
// Limit Sw            
		   if (WatSat > 1.2) {
              WatSat = 1.2;
		   }
// calculate Rw apparent
           Rwa = Res * pow(Por,XX) / xa(index);
// calculate BVW
		   if (WatSat < 1.0) {
              BVW = WatSat * Por;
		   }
		   else {
              BVW = Por;
		   }                 
		}
        
//  calculate the Net pay and net reservoir
//     Limit Sw to 1.0
		if (WatSat > 1.0) {
           WS = 1.0;
		}
		else {
           WS = WatSat;      
		}    
        if ((Por >= PhiCut(index)) && (VClay <= VclCut(index))) {
           ResFlg = 1.0;
		   if (WS <= SwCut(index)) {
              PayFlg = 1.0;
		   }
		   else {   
              PayFlg = 0.0;
		   }
		} 
		else {
           ResFlg = 0.0;
           PayFlg = 0.0;
		}
        
//  add results to zone averages 
		if (ResFlg == 1.0) {  
            ResCount = ResCount + 1.0;
            PhiRes = PhiRes + Por;
            BVWRes = BVWRes + Por * WS;
            VclRes = VclRes + VClay;
		}    
		if (PayFlg == 1.0) {  
            PayCount = PayCount + 1.0;
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
      Step = Depth(TopDepth()+1) - Depth(TopDepth()); 
//  Calculate the zonal averages
      ResNet = ResCount * Step;
	  if (ResCount == 0.0) {
         PhiRes = 0.0;  
         VclRes = 0.0; 
         BVWRes = 0.0;
         SwRes  = 0.0;
	  }
	  else {
         PhiRes = PhiRes / ResCount;  
         VclRes = VclRes / ResCount;  
         BVWRes = BVWRes / ResCount;
         SwRes  = BVWRes / PhiRes; 
	  }
      
      PayNet = PayCount * Step; 
	  if (PayCount == 0.0) {
         PhiPay = 0.0; 
         VclPay = 0.0;  
         BVWPay = 0.0;
         SwPay  = 0.0;
	  }
	  else {
         PhiPay = PhiPay / PayCount;  
         VclPay = VclPay / PayCount;  
         BVWPay = BVWPay / PayCount;
         SwPay  = BVWPay / PhiRes; 
	  }    
//
//  Output results back to parameters
//  We loop through all the data because it is possible that the result parameters are set as curves !
   for ( index = TopDepth() ; index < BottomDepth() ; index++ ) {
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
   if ( ZoneNumber() == TotalZones() ) {
 	    Outfile = fopen("Interp Demo C Report.txt", "w+"); 
  	    if(Outfile==NULL) {
  	    }
	    else {  
	        fprintf(Outfile, " USER PROGRAM INTERP PARAMETERS \n");
            fprintf(Outfile, "\n");
            Well_Name( aString );
            fprintf(Outfile, " Well    : %s\n" , aString );
            // Write well attributes using attribute name         
     	    sprintf(attribute, "Company");
            Read_Well_Attribute(attribute, aString);
	        fprintf(Outfile, " Company : %s\n", aString );

     	    sprintf(attribute, "Field");
            Read_Well_Attribute(attribute, aString);
	        fprintf(Outfile, " Field   : %s\n", aString );

     	    sprintf(attribute, "KBElev");
            Read_Well_Attribute(attribute, aString);
	        fprintf(Outfile, " KB Elev : %s\n", aString );

	        fprintf(Outfile, "\n Input Curves\n" );

            Rt_Name( aString );
            Rt_Units( aUnits);
            fprintf(Outfile, "\n    Rt     = %s (%s)", aString, aUnits );
            Gr_Name( aString );
            Gr_Units( aUnits);
            fprintf(Outfile, "\n    Gr     = %s (%s)", aString, aUnits );
            Den_Name( aString );
            Den_Units( aUnits);
            fprintf(Outfile, "\n    Den    = %s (%s)", aString, aUnits );
            Son_Name( aString );
            Son_Units( aUnits);
            fprintf(Outfile, "\n    Son    = %s (%s)", aString, aUnits );

	        fprintf(Outfile, "\n Output Curves\n" );

            Phi_Name( aString );
            Phi_Units( aUnits);
            fprintf(Outfile, "\n    Phi    = %s (%s)", aString, aUnits );
            Vcl_Name( aString );
            Vcl_Units( aUnits);
            fprintf(Outfile, "\n    Vcl    = %s (%s)", aString, aUnits );
            Sw_Name( aString );
            Sw_Units( aUnits);
            fprintf(Outfile, "\n    Sw     = %s (%s)", aString, aUnits );
            Rwapp_Name( aString );
            Rwapp_Units( aUnits);
            fprintf(Outfile, "\n    Rwapp  = %s (%s)", aString, aUnits );
            BVW_Name( aString );
            BVW_Units( aUnits);
            fprintf(Outfile, "\n    BVW    = %s (%s)", aString, aUnits );
            Phi_Name( aString );
            fprintf(Outfile, "\n    NetPay = %s ", aString );
            Phi_Name( aString );
            fprintf(Outfile, "\n    NetRes = %s ", aString );


            // Write the parameters by zone   
           for ( i = 1 ; i <= TotalZones() ; i++ ) {
                // Set the zone number so we can get the parameters for each zone        
                SetZone(i);
                fprintf(Outfile, "\n");
	            fprintf(Outfile, "\n Zone %i Input Parameters\n", i );

    	        fprintf(Outfile,   "    a          = %f \n", xa(1));
    	        fprintf(Outfile,   "    m          = %f \n", xm(1));
    	        fprintf(Outfile,   "    n          = %f \n", xn(1));
    	        fprintf(Outfile,   "    Rw         = %f \n", Rw(1));
    	        fprintf(Outfile,   "    Sw Eq      = %s \n", SwEq());
    	        fprintf(Outfile,   "    Son Matrix = %f \n", SonMat(1));
    	        fprintf(Outfile,   "    Son Fluid  = %f \n", SonFluid(1));
    	        fprintf(Outfile,   "    Son CP     = %f \n", SonCp(1));
    	        fprintf(Outfile,   "    Son Clay   = %f \n", SonClay(1));
    	        fprintf(Outfile,   "    Den Matrix = %f \n", DenMat(1));
    	        fprintf(Outfile,   "    Den Fluid  = %f \n", DenFluid(1));
    	        fprintf(Outfile,   "    Por Eq     = %s \n", PorEq());
    	        fprintf(Outfile,   "    Den Clay   = %f \n", DenClay(1));
    	        fprintf(Outfile,   "    Gr Clean   = %f \n", GrClean(1));
    	        fprintf(Outfile,   "    Gr Clay    = %f \n", GrClay(1));

                //Show Depth Interval
    	        fprintf(Outfile, "    Depth Interval\n");
                fprintf(Outfile, "    Top = %f     Bottom = %f\n", Depth(TopDepth()), Depth(BottomDepth()));
           }
        fclose(Outfile);
        }
	}
//
//  Write to database who created these curves
   	sprintf(aString, "Curve written by Archie user program1");

    Save_Sw_Comments(aString);
    Save_Rwapp_Comments(aString);
    Save_Phi_Comments(aString);
    Save_Vcl_Comments(aString);
    Save_BVW_Comments(aString);
    Save_NetResFlg_Comments(aString);
    Save_NetPayFlg_Comments(aString);
//
    //Write_Well_Attribute("Location", "IP Test Location");
    //Read_Log_Attribute("Rw", aString, 1);
    //Write_Log_Attribute("Rw", aString, 2);


	free( aString );
	free( attribute );
	free( aUnits );

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
	  if (Phi1 != Phi2) {
         xmc = ( log10(max(Ro1,0.01)) - log10(max(Ro2,0.01)) ) / 
               ( log10(max(Phi2,0.001)) - log10(max(Phi1,0.001)) );
	  }
	  else {
         xmc = xm(-1);
	  }
      Rwc = Ro1 * pow(Phi1,xmc) / xa(-1);
      Rwc = max(0.0001,min(Rwc,100.0));
//    
//  Check to see if the values calculated are the default values
//  If they are then assume that the pickett plot is not open and in use
//  and therefore assume that the values to use for m and Rw are the input normal parameters
//
	  if ( ( fabs(Rwc-Rwpick(-1)) < 0.001) && ( fabs(xmc-Mpick(-1)) < 0.01) ) {
         Rwc = Rw(-1);
         Save_Rwpick(-1,Rwc);
         xmc = xm(-1);
         Save_Mpick(-1,xmc);
//   Recalculate the line using the parameter values of m and Rw and save
         Ro1 = xa(-1) * Rwc * pow(Phi1,-xmc);
         Ro2 = xa(-1) * Rwc * pow(Phi2,-xmc);
         Save_PPres1(-1,Ro1);
         Save_PPres2(-1,Ro2);
	  }
	  else {  
//   New values of m and Rw save these and also the pickett defaults
         Save_Rw(-1,Rwc);
         Save_xm(-1,xmc);
         Save_Rwpick(-1,Rwc);
         Save_Mpick(-1,xmc);
	  }  
//    
}
