
#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include "Functions.h"
#include <math.h>



extern __declspec (dllexport)  void usercode_()
{
	
   int index;

   char *aString;
   char *aUnits;
   char aName[150];
   FILE *Outfile;

   for ( index = TopDepth() ; index < BottomDepth()-5 ; index++ ) {
     //ENTER USER CODE HERE
	
     //check for curve equal to zero
     if ( numCrv(index)-numCrv(index-1) == 0 )  {
         Save_DiffCrv(index,-999); }
	 else if ( denCrv(index)-denCrv(index-1) == 0 )  {
         Save_DiffCrv(index,-999); }
      else {
      //Calculate the first derivative
         Save_DiffCrv(index,(numCrv(index)-numCrv(index-1))/(denCrv(index)-denCrv(index-1)));  }

     //END OF USER CODE
      }


    //Write to database who created these curves
    aString = InitString( MAX_STRING_1 );
    sprintf(aString, "Curve written by User Program");
    Save_numCrv_Comments( aString );
    Save_DiffCrv_Comments( aString );
    free( aString );	
 }
