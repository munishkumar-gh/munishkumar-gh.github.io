# /***********************************************/
#  * File dynamically created from IP: 08/24/2022 15:30:44
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

	def get_Array_VSH_MaxX(self):
		return self._inArrayX[0]

	Array_VSH_MaxX = property(fget=get_Array_VSH_MaxX)

	def get_Array_VSH_MaxY(self):
		return self._inArrayY[0]

	Array_VSH_MaxY = property(fget=get_Array_VSH_MaxY)

	def VCL(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[1],1, index, True)

	def Array_VCL(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[1],1, index, xVal, yVal, True)

	def VCL_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[1], index)

	def Array_VCL_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[1], index, xVal, yVal)

	def get_VCL_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 1)

	VCL_Name = property(fget=get_VCL_Name)

	def get_VCL_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 2)

	VCL_Units = property(fget=get_VCL_Units)

	def get_VCL_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 3)

	VCL_Comments = property(fget=get_VCL_Comments)

	def Save_VCL_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[1], 3, str(newValue))

	def Get_VCL_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[1], attributeName)

	def Set_VCL_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[1], attributeName, str(newValue))

	def get_Array_VCL_MaxX(self):
		return self._inArrayX[1]

	Array_VCL_MaxX = property(fget=get_Array_VCL_MaxX)

	def get_Array_VCL_MaxY(self):
		return self._inArrayY[1]

	Array_VCL_MaxY = property(fget=get_Array_VCL_MaxY)

	def PHIT(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[2],2, index, True)

	def Array_PHIT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[2],2, index, xVal, yVal, True)

	def PHIT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[2], index)

	def Array_PHIT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[2], index, xVal, yVal)

	def get_PHIT_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 1)

	PHIT_Name = property(fget=get_PHIT_Name)

	def get_PHIT_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 2)

	PHIT_Units = property(fget=get_PHIT_Units)

	def get_PHIT_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 3)

	PHIT_Comments = property(fget=get_PHIT_Comments)

	def Save_PHIT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[2], 3, str(newValue))

	def Get_PHIT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[2], attributeName)

	def Set_PHIT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[2], attributeName, str(newValue))

	def get_Array_PHIT_MaxX(self):
		return self._inArrayX[2]

	Array_PHIT_MaxX = property(fget=get_Array_PHIT_MaxX)

	def get_Array_PHIT_MaxY(self):
		return self._inArrayY[2]

	Array_PHIT_MaxY = property(fget=get_Array_PHIT_MaxY)

	def PHIE(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[3],3, index, True)

	def Array_PHIE(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[3],3, index, xVal, yVal, True)

	def PHIE_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[3], index)

	def Array_PHIE_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[3], index, xVal, yVal)

	def get_PHIE_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 1)

	PHIE_Name = property(fget=get_PHIE_Name)

	def get_PHIE_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 2)

	PHIE_Units = property(fget=get_PHIE_Units)

	def get_PHIE_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 3)

	PHIE_Comments = property(fget=get_PHIE_Comments)

	def Save_PHIE_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[3], 3, str(newValue))

	def Get_PHIE_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[3], attributeName)

	def Set_PHIE_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[3], attributeName, str(newValue))

	def get_Array_PHIE_MaxX(self):
		return self._inArrayX[3]

	Array_PHIE_MaxX = property(fget=get_Array_PHIE_MaxX)

	def get_Array_PHIE_MaxY(self):
		return self._inArrayY[3]

	Array_PHIE_MaxY = property(fget=get_Array_PHIE_MaxY)

	def SWT(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[4],4, index, True)

	def Array_SWT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[4],4, index, xVal, yVal, True)

	def SWT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[4], index)

	def Array_SWT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[4], index, xVal, yVal)

	def get_SWT_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 1)

	SWT_Name = property(fget=get_SWT_Name)

	def get_SWT_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 2)

	SWT_Units = property(fget=get_SWT_Units)

	def get_SWT_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 3)

	SWT_Comments = property(fget=get_SWT_Comments)

	def Save_SWT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[4], 3, str(newValue))

	def Get_SWT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[4], attributeName)

	def Set_SWT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[4], attributeName, str(newValue))

	def get_Array_SWT_MaxX(self):
		return self._inArrayX[4]

	Array_SWT_MaxX = property(fget=get_Array_SWT_MaxX)

	def get_Array_SWT_MaxY(self):
		return self._inArrayY[4]

	Array_SWT_MaxY = property(fget=get_Array_SWT_MaxY)

	def SWE(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[5],5, index, True)

	def Array_SWE(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[5],5, index, xVal, yVal, True)

	def SWE_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[5], index)

	def Array_SWE_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[5], index, xVal, yVal)

	def get_SWE_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 1)

	SWE_Name = property(fget=get_SWE_Name)

	def get_SWE_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 2)

	SWE_Units = property(fget=get_SWE_Units)

	def get_SWE_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 3)

	SWE_Comments = property(fget=get_SWE_Comments)

	def Save_SWE_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[5], 3, str(newValue))

	def Get_SWE_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[5], attributeName)

	def Set_SWE_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[5], attributeName, str(newValue))

	def get_Array_SWE_MaxX(self):
		return self._inArrayX[5]

	Array_SWE_MaxX = property(fget=get_Array_SWE_MaxX)

	def get_Array_SWE_MaxY(self):
		return self._inArrayY[5]

	Array_SWE_MaxY = property(fget=get_Array_SWE_MaxY)

	def Save_VSH(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, float(value))

	def Save_Array_VSH(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, float(value), xVal, yVal)

	def Save_VSH_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, str(value))

	def Save_Array_VSH_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, str(value), xVal, yVal)

	def Save_VCL(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value))

	def Save_Array_VCL(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value), xVal, yVal)

	def Save_VCL_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value))

	def Save_Array_VCL_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value), xVal, yVal)

	def Save_PHIT(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, float(value))

	def Save_Array_PHIT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, float(value), xVal, yVal)

	def Save_PHIT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, str(value))

	def Save_Array_PHIT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, str(value), xVal, yVal)

	def Save_PHIE(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, float(value))

	def Save_Array_PHIE(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, float(value), xVal, yVal)

	def Save_PHIE_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, str(value))

	def Save_Array_PHIE_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, str(value), xVal, yVal)

	def Save_SWT(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, float(value))

	def Save_Array_SWT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, float(value), xVal, yVal)

	def Save_SWT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, str(value))

	def Save_Array_SWT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, str(value), xVal, yVal)

	def Save_SWE(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[5], index, float(value))

	def Save_Array_SWE(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[5], index, float(value), xVal, yVal)

	def Save_SWE_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[5], index, str(value))

	def Save_Array_SWE_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[5], index, str(value), xVal, yVal)

	def PHI_MAX(self, index):
		if self._parCnIn[0] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[0], index)
		else:
			return self._inputParameters[0]

	def Save_PHI_MAX(self, index, value):
		if self._parCnIn[0] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[0], index, float(value))
		else:
			self._IPProxy.SetNumericParam(1, float(value))
			self._inputParameters[0] = float(value)

	def get_PHI_MAX_Name(self):
		if self._parCnIn[0] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[0], 1)
		else:
			return str(self._inputParameters[0])

	PHI_MAX_Name = property(fget=get_PHI_MAX_Name)

