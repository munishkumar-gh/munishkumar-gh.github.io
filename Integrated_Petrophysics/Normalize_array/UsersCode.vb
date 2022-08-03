Partial Public Class IPLink

    Public Sub UserCode()

        Dim index, Ix, IY As Integer
        Dim gain, shift, R, valMin, valMax As Single

        ' Enter user code here
        ' Find max and min values in array data
        valMax = -0.0000001
        valMin = 9999999999999.9
        For index = Topdepth To BottomDepth
            For IX = 1 To Array_InCrv_MaxX
                For IY = 1 To Array_InCrv_MaxY
                    R = Array_InCrv(Index, Ix, Iy)
                    If (R < ValMin) And (R <> -999.0) Then
                        ValMin = R
                    End If

                    If (R > ValMax) And (R <> -999.0) Then
                        ValMax = R
                    End If

                Next
            Next
        Next

        ' Calculate the gain and shift to normalize
        gain = 1.0 / (Valmax - Valmin)
        shift = -gain * Valmin

        ' Output new array with normalized values
        For index = Topdepth To BottomDepth
            For IX = 1 To Array_InCrv_MaxX
                For IY = 1 To Array_InCrv_MaxY
                    R = Array_InCrv(Index, Ix, Iy) * Gain + shift
                    Save_array_OutCrv(Index, Ix, Iy, R)
                Next
            Next
        Next

        Save_OutCrv_Comments("Updated by Normalize Array User Prog")

    End Sub

End Class