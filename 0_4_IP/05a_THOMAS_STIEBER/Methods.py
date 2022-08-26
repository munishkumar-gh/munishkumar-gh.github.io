# /***********************************************/
#  * File dynamically created from IP: 08/24/2022 15:16:24
#  * DO NOT MANUALLY EDIT
# /***********************************************/

class Methods:
	def __init__(self):
		self._FIRST_AVAILABLE_LOG_RUN = -1
		self._LAST_AVAILABLE_LOG_RUN = -2

	def Depth(self, index):
		return self._IPProxy.GetCurveData(1, index)

	def VSH(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[0],0, index, True)

	def Array_VSH(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[0],0, index, xVal, yVal, True)

	def VSH_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[0], index)

	def Array_VSH_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[0], index, xVal, yVal)

	def get_VSH_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 1)

	VSH_Name = property(fget=get_VSH_Name)

	def get_VSH_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 2)

	VSH_Units = property(fget=get_VSH_Units)

	def get_VSH_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 3)

	VSH_Comments = property(fget=get_VSH_Comments)

	def Save_VSH_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[0], 3, str(newValue))

	def Get_VSH_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[0], attributeName)

	def Set_VSH_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[0], attributeName, str(newValue))

	def Save_VSH(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[0], index, float(value))

	def Save_Array_VSH(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[0], index, float(value), xVal, yVal)

	def Save_VSH_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[0], index, str(value))

	def Save_Array_VSH_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[0], index, str(value), xVal, yVal)

	def get_Array_VSH_MaxX(self):
		return self._inArrayX[0]

	Array_VSH_MaxX = property(fget=get_Array_VSH_MaxX)

	def get_Array_VSH_MaxY(self):
		return self._inArrayY[0]

	Array_VSH_MaxY = property(fget=get_Array_VSH_MaxY)

	def PHIT(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[1],1, index, True)

	def Array_PHIT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[1],1, index, xVal, yVal, True)

	def PHIT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[1], index)

	def Array_PHIT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[1], index, xVal, yVal)

	def get_PHIT_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 1)

	PHIT_Name = property(fget=get_PHIT_Name)

	def get_PHIT_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 2)

	PHIT_Units = property(fget=get_PHIT_Units)

	def get_PHIT_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 3)

	PHIT_Comments = property(fget=get_PHIT_Comments)

	def Save_PHIT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[1], 3, str(newValue))

	def Get_PHIT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[1], attributeName)

	def Set_PHIT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[1], attributeName, str(newValue))

	def Save_PHIT(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[1], index, float(value))

	def Save_Array_PHIT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[1], index, float(value), xVal, yVal)

	def Save_PHIT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[1], index, str(value))

	def Save_Array_PHIT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[1], index, str(value), xVal, yVal)

	def get_Array_PHIT_MaxX(self):
		return self._inArrayX[1]

	Array_PHIT_MaxX = property(fget=get_Array_PHIT_MaxX)

	def get_Array_PHIT_MaxY(self):
		return self._inArrayY[1]

	Array_PHIT_MaxY = property(fget=get_Array_PHIT_MaxY)

	def SWT(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[2],2, index, True)

	def Array_SWT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[2],2, index, xVal, yVal, True)

	def SWT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[2], index)

	def Array_SWT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[2], index, xVal, yVal)

	def get_SWT_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 1)

	SWT_Name = property(fget=get_SWT_Name)

	def get_SWT_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 2)

	SWT_Units = property(fget=get_SWT_Units)

	def get_SWT_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 3)

	SWT_Comments = property(fget=get_SWT_Comments)

	def Save_SWT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[2], 3, str(newValue))

	def Get_SWT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[2], attributeName)

	def Set_SWT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[2], attributeName, str(newValue))

	def Save_SWT(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[2], index, float(value))

	def Save_Array_SWT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[2], index, float(value), xVal, yVal)

	def Save_SWT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[2], index, str(value))

	def Save_Array_SWT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[2], index, str(value), xVal, yVal)

	def get_Array_SWT_MaxX(self):
		return self._inArrayX[2]

	Array_SWT_MaxX = property(fget=get_Array_SWT_MaxX)

	def get_Array_SWT_MaxY(self):
		return self._inArrayY[2]

	Array_SWT_MaxY = property(fget=get_Array_SWT_MaxY)

	def FT(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[3],3, index, True)

	def Array_FT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[3],3, index, xVal, yVal, True)

	def FT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[3], index)

	def Array_FT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[3], index, xVal, yVal)

	def get_FT_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 1)

	FT_Name = property(fget=get_FT_Name)

	def get_FT_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 2)

	FT_Units = property(fget=get_FT_Units)

	def get_FT_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 3)

	FT_Comments = property(fget=get_FT_Comments)

	def Save_FT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[3], 3, str(newValue))

	def Get_FT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[3], attributeName)

	def Set_FT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[3], attributeName, str(newValue))

	def Save_FT(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[3], index, float(value))

	def Save_Array_FT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[3], index, float(value), xVal, yVal)

	def Save_FT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[3], index, str(value))

	def Save_Array_FT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[3], index, str(value), xVal, yVal)

	def get_Array_FT_MaxX(self):
		return self._inArrayX[3]

	Array_FT_MaxX = property(fget=get_Array_FT_MaxX)

	def get_Array_FT_MaxY(self):
		return self._inArrayY[3]

	Array_FT_MaxY = property(fget=get_Array_FT_MaxY)

	def RESDEEP(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[4],4, index, True)

	def Array_RESDEEP(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[4],4, index, xVal, yVal, True)

	def RESDEEP_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[4], index)

	def Array_RESDEEP_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[4], index, xVal, yVal)

	def get_RESDEEP_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 1)

	RESDEEP_Name = property(fget=get_RESDEEP_Name)

	def get_RESDEEP_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 2)

	RESDEEP_Units = property(fget=get_RESDEEP_Units)

	def get_RESDEEP_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 3)

	RESDEEP_Comments = property(fget=get_RESDEEP_Comments)

	def Save_RESDEEP_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[4], 3, str(newValue))

	def Get_RESDEEP_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[4], attributeName)

	def Set_RESDEEP_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[4], attributeName, str(newValue))

	def Save_RESDEEP(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[4], index, float(value))

	def Save_Array_RESDEEP(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[4], index, float(value), xVal, yVal)

	def Save_RESDEEP_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[4], index, str(value))

	def Save_Array_RESDEEP_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[4], index, str(value), xVal, yVal)

	def get_Array_RESDEEP_MaxX(self):
		return self._inArrayX[4]

	Array_RESDEEP_MaxX = property(fget=get_Array_RESDEEP_MaxX)

	def get_Array_RESDEEP_MaxY(self):
		return self._inArrayY[4]

	Array_RESDEEP_MaxY = property(fget=get_Array_RESDEEP_MaxY)

	def Save_VSH_SH(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, float(value))

	def Save_Array_VSH_SH(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, float(value), xVal, yVal)

	def Save_VSH_SH_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, str(value))

	def Save_Array_VSH_SH_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, str(value), xVal, yVal)

	def VSH_SH(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[0], index)

	def Array_VSH_SH(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[0], index, xVal, yVal)

	def VSH_SH_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[0], index)

	def Array_VSH_SH_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[0], index, xVal, yVal)

	def get_VSH_SH_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 1)

	VSH_SH_Name = property(fget=get_VSH_SH_Name)

	def get_VSH_SH_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 2)

	VSH_SH_Units = property(fget=get_VSH_SH_Units)

	def get_VSH_SH_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 3)

	VSH_SH_Comments = property(fget=get_VSH_SH_Comments)

	def Save_VSH_SH_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[0], 3, str(newValue))

	def get_Array_VSH_SH_MaxX(self):
		return self._outArrayX[0]

	Array_VSH_SH_MaxX = property(fget=get_Array_VSH_SH_MaxX)

	def get_Array_VSH_SH_MaxY(self):
		return self._outArrayY[0]

	Array_VSH_SH_MaxY = property(fget=get_Array_VSH_SH_MaxY)

	def Get_VSH_SH_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[0], attributeName)

	def Set_VSH_SH_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[0], attributeName, str(newValue))

	def Save_PHIT_SH(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value))

	def Save_Array_PHIT_SH(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value), xVal, yVal)

	def Save_PHIT_SH_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value))

	def Save_Array_PHIT_SH_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value), xVal, yVal)

	def PHIT_SH(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[1], index)

	def Array_PHIT_SH(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[1], index, xVal, yVal)

	def PHIT_SH_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[1], index)

	def Array_PHIT_SH_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[1], index, xVal, yVal)

	def get_PHIT_SH_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 1)

	PHIT_SH_Name = property(fget=get_PHIT_SH_Name)

	def get_PHIT_SH_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 2)

	PHIT_SH_Units = property(fget=get_PHIT_SH_Units)

	def get_PHIT_SH_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 3)

	PHIT_SH_Comments = property(fget=get_PHIT_SH_Comments)

	def Save_PHIT_SH_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[1], 3, str(newValue))

	def get_Array_PHIT_SH_MaxX(self):
		return self._outArrayX[1]

	Array_PHIT_SH_MaxX = property(fget=get_Array_PHIT_SH_MaxX)

	def get_Array_PHIT_SH_MaxY(self):
		return self._outArrayY[1]

	Array_PHIT_SH_MaxY = property(fget=get_Array_PHIT_SH_MaxY)

	def Get_PHIT_SH_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[1], attributeName)

	def Set_PHIT_SH_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[1], attributeName, str(newValue))

	def Save_VSH_SST(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, float(value))

	def Save_Array_VSH_SST(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, float(value), xVal, yVal)

	def Save_VSH_SST_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, str(value))

	def Save_Array_VSH_SST_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, str(value), xVal, yVal)

	def VSH_SST(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[2], index)

	def Array_VSH_SST(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[2], index, xVal, yVal)

	def VSH_SST_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[2], index)

	def Array_VSH_SST_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[2], index, xVal, yVal)

	def get_VSH_SST_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 1)

	VSH_SST_Name = property(fget=get_VSH_SST_Name)

	def get_VSH_SST_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 2)

	VSH_SST_Units = property(fget=get_VSH_SST_Units)

	def get_VSH_SST_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 3)

	VSH_SST_Comments = property(fget=get_VSH_SST_Comments)

	def Save_VSH_SST_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[2], 3, str(newValue))

	def get_Array_VSH_SST_MaxX(self):
		return self._outArrayX[2]

	Array_VSH_SST_MaxX = property(fget=get_Array_VSH_SST_MaxX)

	def get_Array_VSH_SST_MaxY(self):
		return self._outArrayY[2]

	Array_VSH_SST_MaxY = property(fget=get_Array_VSH_SST_MaxY)

	def Get_VSH_SST_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[2], attributeName)

	def Set_VSH_SST_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[2], attributeName, str(newValue))

	def Save_PHIT_SST(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, float(value))

	def Save_Array_PHIT_SST(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, float(value), xVal, yVal)

	def Save_PHIT_SST_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, str(value))

	def Save_Array_PHIT_SST_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, str(value), xVal, yVal)

	def PHIT_SST(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[3], index)

	def Array_PHIT_SST(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[3], index, xVal, yVal)

	def PHIT_SST_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[3], index)

	def Array_PHIT_SST_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[3], index, xVal, yVal)

	def get_PHIT_SST_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 1)

	PHIT_SST_Name = property(fget=get_PHIT_SST_Name)

	def get_PHIT_SST_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 2)

	PHIT_SST_Units = property(fget=get_PHIT_SST_Units)

	def get_PHIT_SST_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 3)

	PHIT_SST_Comments = property(fget=get_PHIT_SST_Comments)

	def Save_PHIT_SST_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[3], 3, str(newValue))

	def get_Array_PHIT_SST_MaxX(self):
		return self._outArrayX[3]

	Array_PHIT_SST_MaxX = property(fget=get_Array_PHIT_SST_MaxX)

	def get_Array_PHIT_SST_MaxY(self):
		return self._outArrayY[3]

	Array_PHIT_SST_MaxY = property(fget=get_Array_PHIT_SST_MaxY)

	def Get_PHIT_SST_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[3], attributeName)

	def Set_PHIT_SST_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[3], attributeName, str(newValue))

	def Save_SWT_SST(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, float(value))

	def Save_Array_SWT_SST(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, float(value), xVal, yVal)

	def Save_SWT_SST_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, str(value))

	def Save_Array_SWT_SST_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, str(value), xVal, yVal)

	def SWT_SST(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[4], index)

	def Array_SWT_SST(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[4], index, xVal, yVal)

	def SWT_SST_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[4], index)

	def Array_SWT_SST_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[4], index, xVal, yVal)

	def get_SWT_SST_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 1)

	SWT_SST_Name = property(fget=get_SWT_SST_Name)

	def get_SWT_SST_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 2)

	SWT_SST_Units = property(fget=get_SWT_SST_Units)

	def get_SWT_SST_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 3)

	SWT_SST_Comments = property(fget=get_SWT_SST_Comments)

	def Save_SWT_SST_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[4], 3, str(newValue))

	def get_Array_SWT_SST_MaxX(self):
		return self._outArrayX[4]

	Array_SWT_SST_MaxX = property(fget=get_Array_SWT_SST_MaxX)

	def get_Array_SWT_SST_MaxY(self):
		return self._outArrayY[4]

	Array_SWT_SST_MaxY = property(fget=get_Array_SWT_SST_MaxY)

	def Get_SWT_SST_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[4], attributeName)

	def Set_SWT_SST_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[4], attributeName, str(newValue))

	def Save_SWT_ARCH(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[5], index, float(value))

	def Save_Array_SWT_ARCH(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[5], index, float(value), xVal, yVal)

	def Save_SWT_ARCH_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[5], index, str(value))

	def Save_Array_SWT_ARCH_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[5], index, str(value), xVal, yVal)

	def SWT_ARCH(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[5], index)

	def Array_SWT_ARCH(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[5], index, xVal, yVal)

	def SWT_ARCH_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[5], index)

	def Array_SWT_ARCH_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[5], index, xVal, yVal)

	def get_SWT_ARCH_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 1)

	SWT_ARCH_Name = property(fget=get_SWT_ARCH_Name)

	def get_SWT_ARCH_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 2)

	SWT_ARCH_Units = property(fget=get_SWT_ARCH_Units)

	def get_SWT_ARCH_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 3)

	SWT_ARCH_Comments = property(fget=get_SWT_ARCH_Comments)

	def Save_SWT_ARCH_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[5], 3, str(newValue))

	def get_Array_SWT_ARCH_MaxX(self):
		return self._outArrayX[5]

	Array_SWT_ARCH_MaxX = property(fget=get_Array_SWT_ARCH_MaxX)

	def get_Array_SWT_ARCH_MaxY(self):
		return self._outArrayY[5]

	Array_SWT_ARCH_MaxY = property(fget=get_Array_SWT_ARCH_MaxY)

	def Get_SWT_ARCH_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[5], attributeName)

	def Set_SWT_ARCH_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[5], attributeName, str(newValue))

	def Save_VSST(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[6], index, float(value))

	def Save_Array_VSST(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[6], index, float(value), xVal, yVal)

	def Save_VSST_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[6], index, str(value))

	def Save_Array_VSST_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[6], index, str(value), xVal, yVal)

	def VSST(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[6], index)

	def Array_VSST(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[6], index, xVal, yVal)

	def VSST_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[6], index)

	def Array_VSST_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[6], index, xVal, yVal)

	def get_VSST_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 1)

	VSST_Name = property(fget=get_VSST_Name)

	def get_VSST_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 2)

	VSST_Units = property(fget=get_VSST_Units)

	def get_VSST_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 3)

	VSST_Comments = property(fget=get_VSST_Comments)

	def Save_VSST_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[6], 3, str(newValue))

	def get_Array_VSST_MaxX(self):
		return self._outArrayX[6]

	Array_VSST_MaxX = property(fget=get_Array_VSST_MaxX)

	def get_Array_VSST_MaxY(self):
		return self._outArrayY[6]

	Array_VSST_MaxY = property(fget=get_Array_VSST_MaxY)

	def Get_VSST_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[6], attributeName)

	def Set_VSST_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[6], attributeName, str(newValue))

	def Save_PHIT_SST_MOD(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[7], index, float(value))

	def Save_Array_PHIT_SST_MOD(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[7], index, float(value), xVal, yVal)

	def Save_PHIT_SST_MOD_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[7], index, str(value))

	def Save_Array_PHIT_SST_MOD_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[7], index, str(value), xVal, yVal)

	def PHIT_SST_MOD(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[7], index)

	def Array_PHIT_SST_MOD(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[7], index, xVal, yVal)

	def PHIT_SST_MOD_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[7], index)

	def Array_PHIT_SST_MOD_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[7], index, xVal, yVal)

	def get_PHIT_SST_MOD_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 1)

	PHIT_SST_MOD_Name = property(fget=get_PHIT_SST_MOD_Name)

	def get_PHIT_SST_MOD_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 2)

	PHIT_SST_MOD_Units = property(fget=get_PHIT_SST_MOD_Units)

	def get_PHIT_SST_MOD_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 3)

	PHIT_SST_MOD_Comments = property(fget=get_PHIT_SST_MOD_Comments)

	def Save_PHIT_SST_MOD_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[7], 3, str(newValue))

	def get_Array_PHIT_SST_MOD_MaxX(self):
		return self._outArrayX[7]

	Array_PHIT_SST_MOD_MaxX = property(fget=get_Array_PHIT_SST_MOD_MaxX)

	def get_Array_PHIT_SST_MOD_MaxY(self):
		return self._outArrayY[7]

	Array_PHIT_SST_MOD_MaxY = property(fget=get_Array_PHIT_SST_MOD_MaxY)

	def Get_PHIT_SST_MOD_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[7], attributeName)

	def Set_PHIT_SST_MOD_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[7], attributeName, str(newValue))

	def Save_SWT_BULK(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[8], index, float(value))

	def Save_Array_SWT_BULK(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[8], index, float(value), xVal, yVal)

	def Save_SWT_BULK_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[8], index, str(value))

	def Save_Array_SWT_BULK_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[8], index, str(value), xVal, yVal)

	def SWT_BULK(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[8], index)

	def Array_SWT_BULK(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[8], index, xVal, yVal)

	def SWT_BULK_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[8], index)

	def Array_SWT_BULK_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[8], index, xVal, yVal)

	def get_SWT_BULK_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 1)

	SWT_BULK_Name = property(fget=get_SWT_BULK_Name)

	def get_SWT_BULK_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 2)

	SWT_BULK_Units = property(fget=get_SWT_BULK_Units)

	def get_SWT_BULK_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 3)

	SWT_BULK_Comments = property(fget=get_SWT_BULK_Comments)

	def Save_SWT_BULK_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[8], 3, str(newValue))

	def get_Array_SWT_BULK_MaxX(self):
		return self._outArrayX[8]

	Array_SWT_BULK_MaxX = property(fget=get_Array_SWT_BULK_MaxX)

	def get_Array_SWT_BULK_MaxY(self):
		return self._outArrayY[8]

	Array_SWT_BULK_MaxY = property(fget=get_Array_SWT_BULK_MaxY)

	def Get_SWT_BULK_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[8], attributeName)

	def Set_SWT_BULK_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[8], attributeName, str(newValue))

	def Save_PHIT_SST_BULK(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[9], index, float(value))

	def Save_Array_PHIT_SST_BULK(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[9], index, float(value), xVal, yVal)

	def Save_PHIT_SST_BULK_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[9], index, str(value))

	def Save_Array_PHIT_SST_BULK_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[9], index, str(value), xVal, yVal)

	def PHIT_SST_BULK(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[9], index)

	def Array_PHIT_SST_BULK(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[9], index, xVal, yVal)

	def PHIT_SST_BULK_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[9], index)

	def Array_PHIT_SST_BULK_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[9], index, xVal, yVal)

	def get_PHIT_SST_BULK_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[9], 1)

	PHIT_SST_BULK_Name = property(fget=get_PHIT_SST_BULK_Name)

	def get_PHIT_SST_BULK_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[9], 2)

	PHIT_SST_BULK_Units = property(fget=get_PHIT_SST_BULK_Units)

	def get_PHIT_SST_BULK_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[9], 3)

	PHIT_SST_BULK_Comments = property(fget=get_PHIT_SST_BULK_Comments)

	def Save_PHIT_SST_BULK_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[9], 3, str(newValue))

	def get_Array_PHIT_SST_BULK_MaxX(self):
		return self._outArrayX[9]

	Array_PHIT_SST_BULK_MaxX = property(fget=get_Array_PHIT_SST_BULK_MaxX)

	def get_Array_PHIT_SST_BULK_MaxY(self):
		return self._outArrayY[9]

	Array_PHIT_SST_BULK_MaxY = property(fget=get_Array_PHIT_SST_BULK_MaxY)

	def Get_PHIT_SST_BULK_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[9], attributeName)

	def Set_PHIT_SST_BULK_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[9], attributeName, str(newValue))

	def Save_PHIT_SH_BULK(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[10], index, float(value))

	def Save_Array_PHIT_SH_BULK(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[10], index, float(value), xVal, yVal)

	def Save_PHIT_SH_BULK_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[10], index, str(value))

	def Save_Array_PHIT_SH_BULK_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[10], index, str(value), xVal, yVal)

	def PHIT_SH_BULK(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[10], index)

	def Array_PHIT_SH_BULK(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[10], index, xVal, yVal)

	def PHIT_SH_BULK_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[10], index)

	def Array_PHIT_SH_BULK_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[10], index, xVal, yVal)

	def get_PHIT_SH_BULK_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[10], 1)

	PHIT_SH_BULK_Name = property(fget=get_PHIT_SH_BULK_Name)

	def get_PHIT_SH_BULK_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[10], 2)

	PHIT_SH_BULK_Units = property(fget=get_PHIT_SH_BULK_Units)

	def get_PHIT_SH_BULK_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[10], 3)

	PHIT_SH_BULK_Comments = property(fget=get_PHIT_SH_BULK_Comments)

	def Save_PHIT_SH_BULK_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[10], 3, str(newValue))

	def get_Array_PHIT_SH_BULK_MaxX(self):
		return self._outArrayX[10]

	Array_PHIT_SH_BULK_MaxX = property(fget=get_Array_PHIT_SH_BULK_MaxX)

	def get_Array_PHIT_SH_BULK_MaxY(self):
		return self._outArrayY[10]

	Array_PHIT_SH_BULK_MaxY = property(fget=get_Array_PHIT_SH_BULK_MaxY)

	def Get_PHIT_SH_BULK_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[10], attributeName)

	def Set_PHIT_SH_BULK_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[10], attributeName, str(newValue))

	def Save_VOLHC_SST_BULK(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[11], index, float(value))

	def Save_Array_VOLHC_SST_BULK(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[11], index, float(value), xVal, yVal)

	def Save_VOLHC_SST_BULK_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[11], index, str(value))

	def Save_Array_VOLHC_SST_BULK_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[11], index, str(value), xVal, yVal)

	def VOLHC_SST_BULK(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[11], index)

	def Array_VOLHC_SST_BULK(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[11], index, xVal, yVal)

	def VOLHC_SST_BULK_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[11], index)

	def Array_VOLHC_SST_BULK_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[11], index, xVal, yVal)

	def get_VOLHC_SST_BULK_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[11], 1)

	VOLHC_SST_BULK_Name = property(fget=get_VOLHC_SST_BULK_Name)

	def get_VOLHC_SST_BULK_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[11], 2)

	VOLHC_SST_BULK_Units = property(fget=get_VOLHC_SST_BULK_Units)

	def get_VOLHC_SST_BULK_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[11], 3)

	VOLHC_SST_BULK_Comments = property(fget=get_VOLHC_SST_BULK_Comments)

	def Save_VOLHC_SST_BULK_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[11], 3, str(newValue))

	def get_Array_VOLHC_SST_BULK_MaxX(self):
		return self._outArrayX[11]

	Array_VOLHC_SST_BULK_MaxX = property(fget=get_Array_VOLHC_SST_BULK_MaxX)

	def get_Array_VOLHC_SST_BULK_MaxY(self):
		return self._outArrayY[11]

	Array_VOLHC_SST_BULK_MaxY = property(fget=get_Array_VOLHC_SST_BULK_MaxY)

	def Get_VOLHC_SST_BULK_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[11], attributeName)

	def Set_VOLHC_SST_BULK_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[11], attributeName, str(newValue))

	def Save_VOLWAT_SST_BULK(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[12], index, float(value))

	def Save_Array_VOLWAT_SST_BULK(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[12], index, float(value), xVal, yVal)

	def Save_VOLWAT_SST_BULK_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[12], index, str(value))

	def Save_Array_VOLWAT_SST_BULK_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[12], index, str(value), xVal, yVal)

	def VOLWAT_SST_BULK(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[12], index)

	def Array_VOLWAT_SST_BULK(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[12], index, xVal, yVal)

	def VOLWAT_SST_BULK_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[12], index)

	def Array_VOLWAT_SST_BULK_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[12], index, xVal, yVal)

	def get_VOLWAT_SST_BULK_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[12], 1)

	VOLWAT_SST_BULK_Name = property(fget=get_VOLWAT_SST_BULK_Name)

	def get_VOLWAT_SST_BULK_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[12], 2)

	VOLWAT_SST_BULK_Units = property(fget=get_VOLWAT_SST_BULK_Units)

	def get_VOLWAT_SST_BULK_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[12], 3)

	VOLWAT_SST_BULK_Comments = property(fget=get_VOLWAT_SST_BULK_Comments)

	def Save_VOLWAT_SST_BULK_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[12], 3, str(newValue))

	def get_Array_VOLWAT_SST_BULK_MaxX(self):
		return self._outArrayX[12]

	Array_VOLWAT_SST_BULK_MaxX = property(fget=get_Array_VOLWAT_SST_BULK_MaxX)

	def get_Array_VOLWAT_SST_BULK_MaxY(self):
		return self._outArrayY[12]

	Array_VOLWAT_SST_BULK_MaxY = property(fget=get_Array_VOLWAT_SST_BULK_MaxY)

	def Get_VOLWAT_SST_BULK_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[12], attributeName)

	def Set_VOLWAT_SST_BULK_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[12], attributeName, str(newValue))

	def Save_FACIES_TBA(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[13], index, float(value))

	def Save_Array_FACIES_TBA(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[13], index, float(value), xVal, yVal)

	def Save_FACIES_TBA_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[13], index, str(value))

	def Save_Array_FACIES_TBA_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[13], index, str(value), xVal, yVal)

	def FACIES_TBA(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[13], index)

	def Array_FACIES_TBA(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[13], index, xVal, yVal)

	def FACIES_TBA_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[13], index)

	def Array_FACIES_TBA_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[13], index, xVal, yVal)

	def get_FACIES_TBA_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[13], 1)

	FACIES_TBA_Name = property(fget=get_FACIES_TBA_Name)

	def get_FACIES_TBA_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[13], 2)

	FACIES_TBA_Units = property(fget=get_FACIES_TBA_Units)

	def get_FACIES_TBA_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[13], 3)

	FACIES_TBA_Comments = property(fget=get_FACIES_TBA_Comments)

	def Save_FACIES_TBA_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[13], 3, str(newValue))

	def get_Array_FACIES_TBA_MaxX(self):
		return self._outArrayX[13]

	Array_FACIES_TBA_MaxX = property(fget=get_Array_FACIES_TBA_MaxX)

	def get_Array_FACIES_TBA_MaxY(self):
		return self._outArrayY[13]

	Array_FACIES_TBA_MaxY = property(fget=get_Array_FACIES_TBA_MaxY)

	def Get_FACIES_TBA_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[13], attributeName)

	def Set_FACIES_TBA_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[13], attributeName, str(newValue))

	def PHIT_SST_REF(self, index):
		if self._parCnIn[0] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[0], index)
		else:
			return self._inputParameters[0]

	def Save_PHIT_SST_REF(self, index, value):
		if self._parCnIn[0] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[0], index, float(value))
		else:
			self._IPProxy.SetNumericParam(1, float(value))
			self._inputParameters[0] = float(value)

	def get_PHIT_SST_REF_Name(self):
		if self._parCnIn[0] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[0], 1)
		else:
			return str(self._inputParameters[0])

	PHIT_SST_REF_Name = property(fget=get_PHIT_SST_REF_Name)

	def VSH_SST_REF(self, index):
		if self._parCnIn[1] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[1], index)
		else:
			return self._inputParameters[1]

	def Save_VSH_SST_REF(self, index, value):
		if self._parCnIn[1] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[1], index, float(value))
		else:
			self._IPProxy.SetNumericParam(2, float(value))
			self._inputParameters[1] = float(value)

	def get_VSH_SST_REF_Name(self):
		if self._parCnIn[1] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[1], 1)
		else:
			return str(self._inputParameters[1])

	VSH_SST_REF_Name = property(fget=get_VSH_SST_REF_Name)

	def PHIT_SH_REF(self, index):
		if self._parCnIn[2] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[2], index)
		else:
			return self._inputParameters[2]

	def Save_PHIT_SH_REF(self, index, value):
		if self._parCnIn[2] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[2], index, float(value))
		else:
			self._IPProxy.SetNumericParam(3, float(value))
			self._inputParameters[2] = float(value)

	def get_PHIT_SH_REF_Name(self):
		if self._parCnIn[2] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[2], 1)
		else:
			return str(self._inputParameters[2])

	PHIT_SH_REF_Name = property(fget=get_PHIT_SH_REF_Name)

	def VSH_SH_REF(self, index):
		if self._parCnIn[3] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[3], index)
		else:
			return self._inputParameters[3]

	def Save_VSH_SH_REF(self, index, value):
		if self._parCnIn[3] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[3], index, float(value))
		else:
			self._IPProxy.SetNumericParam(4, float(value))
			self._inputParameters[3] = float(value)

	def get_VSH_SH_REF_Name(self):
		if self._parCnIn[3] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[3], 1)
		else:
			return str(self._inputParameters[3])

	VSH_SH_REF_Name = property(fget=get_VSH_SH_REF_Name)

	def SHALE_CUTOFF(self, index):
		if self._parCnIn[4] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[4], index)
		else:
			return self._inputParameters[4]

	def Save_SHALE_CUTOFF(self, index, value):
		if self._parCnIn[4] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[4], index, float(value))
		else:
			self._IPProxy.SetNumericParam(5, float(value))
			self._inputParameters[4] = float(value)

	def get_SHALE_CUTOFF_Name(self):
		if self._parCnIn[4] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[4], 1)
		else:
			return str(self._inputParameters[4])

	SHALE_CUTOFF_Name = property(fget=get_SHALE_CUTOFF_Name)

	def SHALY_LAM(self, index):
		if self._parCnIn[5] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[5], index)
		else:
			return self._inputParameters[5]

	def Save_SHALY_LAM(self, index, value):
		if self._parCnIn[5] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[5], index, float(value))
		else:
			self._IPProxy.SetNumericParam(6, float(value))
			self._inputParameters[5] = float(value)

	def get_SHALY_LAM_Name(self):
		if self._parCnIn[5] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[5], 1)
		else:
			return str(self._inputParameters[5])

	SHALY_LAM_Name = property(fget=get_SHALY_LAM_Name)

	def SANDY_LAM(self, index):
		if self._parCnIn[6] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[6], index)
		else:
			return self._inputParameters[6]

	def Save_SANDY_LAM(self, index, value):
		if self._parCnIn[6] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[6], index, float(value))
		else:
			self._IPProxy.SetNumericParam(7, float(value))
			self._inputParameters[6] = float(value)

	def get_SANDY_LAM_Name(self):
		if self._parCnIn[6] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[6], 1)
		else:
			return str(self._inputParameters[6])

	SANDY_LAM_Name = property(fget=get_SANDY_LAM_Name)

	def SALINITY(self, index):
		if self._parCnIn[7] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[7], index)
		else:
			return self._inputParameters[7]

	def Save_SALINITY(self, index, value):
		if self._parCnIn[7] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[7], index, float(value))
		else:
			self._IPProxy.SetNumericParam(8, float(value))
			self._inputParameters[7] = float(value)

	def get_SALINITY_Name(self):
		if self._parCnIn[7] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[7], 1)
		else:
			return str(self._inputParameters[7])

	SALINITY_Name = property(fget=get_SALINITY_Name)

	def M(self, index):
		if self._parCnIn[8] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[8], index)
		else:
			return self._inputParameters[8]

	def Save_M(self, index, value):
		if self._parCnIn[8] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[8], index, float(value))
		else:
			self._IPProxy.SetNumericParam(9, float(value))
			self._inputParameters[8] = float(value)

	def get_M_Name(self):
		if self._parCnIn[8] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[8], 1)
		else:
			return str(self._inputParameters[8])

	M_Name = property(fget=get_M_Name)

	def N(self, index):
		if self._parCnIn[9] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[9], index)
		else:
			return self._inputParameters[9]

	def Save_N(self, index, value):
		if self._parCnIn[9] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[9], index, float(value))
		else:
			self._IPProxy.SetNumericParam(10, float(value))
			self._inputParameters[9] = float(value)

	def get_N_Name(self):
		if self._parCnIn[9] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[9], 1)
		else:
			return str(self._inputParameters[9])

	N_Name = property(fget=get_N_Name)

	def A(self, index):
		if self._parCnIn[10] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[10], index)
		else:
			return self._inputParameters[10]

	def Save_A(self, index, value):
		if self._parCnIn[10] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[10], index, float(value))
		else:
			self._IPProxy.SetNumericParam(11, float(value))
			self._inputParameters[10] = float(value)

	def get_A_Name(self):
		if self._parCnIn[10] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[10], 1)
		else:
			return str(self._inputParameters[10])

	A_Name = property(fget=get_A_Name)

	def get_OPT_TEMP_UNITS(self):
		return self._textInputParameters[0]

	OPT_TEMP_UNITS = property(fget=get_OPT_TEMP_UNITS)

