c
c User Code for Fortran 77
c 
      SUBROUTINE  UserCode()
      IMPLICIT INTEGER (I-N)
      INCLUDE 'InOutDef.INC' 
      REAL*4 :: Der, num1, num2, den1, den2
c
c     All user defined input parameters and logic flags are treated as functions.
c     As such they must be used with a () at the end of their name.
c     For example: Input parameter RW is used in an equation as RW(); AA = RW() + 2.
c
c     Input curves are used in equations as functions.
c     Vclay = (GR(INDEX) - GRclean()) / (GRclay() - GRclean())
c     INDEX is the integer index into the curve array. GRclay and GRclean are defined
c     as input parameters. GR is the input curve.
c     Input curve DEPTH is always available and does not have to be defined as an input curve.
c
c     Data is saved by using the SAVE_***(INDEX, VALUE) procedure. Where *** is the 
c     output curve name. VALUE is the value to store at INDEX.
c     CALL SAVE_VCL(INDEX, 0.5)   saves value 0.5 into the outout curve VCL.
c
c Loop through the data one level at a time
c Index_Topdepth and Index_BottomDepth are the index equivalent depths entered on the run window. 
C 
      DO 100 INDEX = Index_Topdepth()+1 , Index_BottomDepth()
c
c write user code here 
c
c	Assign curve values to variable
		    num1 = numCrv(index)
		    num2 = numCrv(index-1)
		    den1 = denCrv(index)
		    den2 = denCrv(index-1)
c  Check for numerator and denominator equal to zero
         if (num1 - num2 .eq. 0.0) then 
          Call Save_DiffCrv(index,0.0)
         else if (den1 - den2 .eq. 0.0) then
          Call Save_DiffCrv(index,-999.0)
         else
c  Calculate the first derivative

          Der = (num1 - num2) / (den1 - den2)
          Call Save_DiffCrv(index, Der);
         endif;
  
  100 CONTINUE
  110 Call Save_diffcrv_Comments('Updated by Fortran User Program');
c 
     
      RETURN
c
      END
