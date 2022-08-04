c
c User Code for Fortran 77
c 
      SUBROUTINE  UserCode()
      IMPLICIT INTEGER (I-N)
      INCLUDE 'InOutDef.INC' 
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
c     CALL SAVE_VCL(INDEX, 0.5)   saves value 0.5 into the output curve VCL.
c
c Loop through the data one level at a time
c Index_Topdepth and Index_BottomDepth are the index equivalent depths entered on the run window. 
C 
c
c write user code here
c     find max and min values in array data
      ValMax = -0.0000001
      ValMin = 9999999999999.9        
      DO INDEX = Index_Topdepth() , Index_BottomDepth()
         Do IX = 1, Array_InCrv_MaxX()
            Do IY = 1, Array_InCrv_MaxY()
               R = Array_InCrv(Index,Ix,Iy)
               if (R .lt. ValMin .and. R .ne. -999.0)
     c            ValMin = R
               if (R .gt. ValMax .and. R .ne. -999.0)
     c            ValMax = R
            enddo
         enddo
      enddo
c     calculate the gain and shift to normalize
      gain = 1.0 / (Valmax - Valmin)
      shift = - gain * Valmin 
c     output new array with normalized values
      DO INDEX = Index_Topdepth() , Index_BottomDepth()
         Do IX = 1, Array_InCrv_MaxX()
            Do IY = 1, Array_InCrv_MaxY()
               R = Array_InCrv(Index,Ix,Iy) * Gain + shift
               call Save_array_OutCrv(Index,Ix,Iy,R)
            enddo
         enddo
      enddo
c 
      Call Save_OutCrv_Comments('Updated by Fortran User Program Array');
      RETURN
c
   
      END
