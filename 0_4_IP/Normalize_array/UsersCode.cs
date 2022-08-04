using System;


public partial class IPLink
{

    public void UserCode()
    {
        int index, ix, iy;
        Single gain, shift, R, valMin, valMax;

        // Enter user code here
        // Find max and min values in array data
        valMax = -0.0000001f;
        valMin = 9999999999999.9f;

        for (index = TopDepth; index <= BottomDepth; index++)
        {
            for (ix = 1; ix <= Array_InCrv_MaxX; ix++)
            {
                for (iy = 1; iy <= Array_InCrv_MaxY; iy++)
                {
                    R = Array_InCrv(index, ix, iy);
                    if ((R < valMin) && (R != -999.0))
                    {
                        valMin = R;
                    }

                    if ((R > valMax) && (R != -999.0))
                    {
                        valMax = R;
                    }

                }
            }
        }

        // Calculate the gain and shift to normalize
        gain = (Single)1.0 / (valMax - valMin);
        shift = -gain * valMin;

        // Output new array with normalized values
        for (index = TopDepth; index <= BottomDepth; index++)
        {
            for (ix = 1; ix <= Array_InCrv_MaxX; ix++)
            {
                for (iy = 1; iy <= Array_InCrv_MaxY; iy++)
                {
                    R = Array_InCrv(index, ix, iy) * gain + shift;
                    Save_Array_OutCrv(index, ix, iy, R);
                }
            }
        }

        Save_OutCrv_Comments("Updated by Normalize Array User Prog");
    }

}

