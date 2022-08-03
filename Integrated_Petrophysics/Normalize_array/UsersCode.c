
#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include "Functions.h"
#include <math.h>



extern __declspec (dllexport)  void usercode_()
{
	
   int index, IX, IY;
   float gain, shift, R, ValMin, ValMax;
   char *aString;
   char *aUnits;

   //ENTER USER CODE HERE
     
   //find max and min values in array data
   ValMax = -0.0000001;
   ValMin = 9999999999999.9;        
      for (index = TopDepth(); index < BottomDepth(); index++) {
         for (IX = 1; IX <= Array_InCrv_MaxX(); IX++) {
            for (IY = 1; IY <= Array_InCrv_MaxY(); IY++) {
               R = Array_InCrv(index,IX,IY);
               if ((R < ValMin) && (R != -999.0)) 
                  ValMin = R;
               if ((R > ValMax) && (R != -999.0)) 
				  ValMax = R;
            }
         } 
      }

	 //Calculate the gain and shift to normalize
     gain = 1.0 / (ValMax - ValMin);
     shift = - gain * ValMin; 
     //output new array with normalized values
      for (index = TopDepth(); index < BottomDepth(); index++) {
		  for (IX = 1; IX <= Array_InCrv_MaxX(); IX++) {
			  for (IY = 1; IY <= Array_InCrv_MaxY(); IY++) {
               R = Array_InCrv(index,IX,IY) * gain + shift;
               Save_Array_OutCrv(index,IX,IY,R);
			  }
		  }
      }

     //END OF USER CODE
      
    //Write to database who created these curves
    aString = InitString( MAX_STRING_1 );
    sprintf(aString, "Updated by Normalize Array User Prog C++");
    Save_OutCrv_Comments( aString );
    free( aString );	
 }
