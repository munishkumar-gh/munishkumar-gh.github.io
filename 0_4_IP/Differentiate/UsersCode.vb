Partial Public Class IPLink

			'Differentiate code
		Function Differentiate (numerator1 as single, numerator2 as single, denominator1 as single, denominator2 as single) as single
			Dim differential as single
			differential=(numerator1-numerator2)/(denominator1-denominator2)
			return differential
		End Function
		
    Public Sub UserCode()
        Dim index As Integer
		Dim num1,num2,den1,den2 as single

        For index = Topdepth + 1 To BottomDepth
            
           
                ' Assign curve values to variables
                                num1=numCrv(index)
				num2=numCrv(index-1)
				den1=denCrv(index)
				den2=denCrv(index-1)
				
				' Check that the values wont equal 0 
			If num1-num2=0 then
				save_diffCrv(index, -999)
			elseif den1-den2=0 then
				save_diffCrv(index, -999)
			else	
				Dim diff as single =Differentiate(num1,num2,den1,den2)
				save_diffCrv(index, diff)
            End If
        Next

    End Sub

End Class