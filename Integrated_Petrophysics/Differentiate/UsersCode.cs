using System;


public partial class IPLink
{

    public void UserCode()
    {

        for (int index = TopDepth + 1; index <= BottomDepth; index++)
        {
            // Enter user code here
            // Check for curve equal to zero
            if (numCrv(index)-numCrv(index-1) == 0.0)
            {
                Save_DiffCrv(index, -999);
			}
			else if (denCrv(index)-denCrv(index-1) == 0.0)
            {
                Save_DiffCrv(index, -999);
            }
            else
            {
                // Calculate the first derivative
                Save_DiffCrv(index, (numCrv(index)-numCrv(index-1)) / (denCrv(index)-denCrv(index-1)));
            }
        }

        Save_DiffCrv_Comments("Curve Written by User Program");
    }

}

