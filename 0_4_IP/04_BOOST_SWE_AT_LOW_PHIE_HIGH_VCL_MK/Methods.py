# /***********************************************/
#  * File dynamically created from IP: 08/24/2022 15:14:40
#  * DO NOT MANUALLY EDIT
# /***********************************************/

class Methods:
	def __init__(self):
		self._FIRST_AVAILABLE_LOG_RUN = -1
		self._LAST_AVAILABLE_LOG_RUN = -2

	def Depth(self, index):
		return self._IPProxy.GetCurveData(1, index)

	def VCL_OLD(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[0],0, index, True)

	def Array_VCL_OLD(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[0],0, index, xVal, yVal, True)

	def VCL_OLD_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[0], index)

	def Array_VCL_OLD_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[0], index, xVal, yVal)

	def get_VCL_OLD_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 1)

	VCL_OLD_Name = property(fget=get_VCL_OLD_Name)

	def get_VCL_OLD_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 2)

	VCL_OLD_Units = property(fget=get_VCL_OLD_Units)

	def get_VCL_OLD_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 3)

	VCL_OLD_Comments = property(fget=get_VCL_OLD_Comments)

	def Save_VCL_OLD_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[0], 3, str(newValue))

	def Get_VCL_OLD_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[0], attributeName)

	def Set_VCL_OLD_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[0], attributeName, str(newValue))

	def Save_VCL_OLD(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[0], index, float(value))

	def Save_Array_VCL_OLD(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[0], index, float(value), xVal, yVal)

	def Save_VCL_OLD_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[0], index, str(value))

	def Save_Array_VCL_OLD_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[0], index, str(value), xVal, yVal)

	def get_Array_VCL_OLD_MaxX(self):
		return self._inArrayX[0]

	Array_VCL_OLD_MaxX = property(fget=get_Array_VCL_OLD_MaxX)

	def get_Array_VCL_OLD_MaxY(self):
		return self._inArrayY[0]

	Array_VCL_OLD_MaxY = property(fget=get_Array_VCL_OLD_MaxY)

	def PHIE_OLD(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[1],1, index, True)

	def Array_PHIE_OLD(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[1],1, index, xVal, yVal, True)

	def PHIE_OLD_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[1], index)

	def Array_PHIE_OLD_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[1], index, xVal, yVal)

	def get_PHIE_OLD_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 1)

	PHIE_OLD_Name = property(fget=get_PHIE_OLD_Name)

	def get_PHIE_OLD_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 2)

	PHIE_OLD_Units = property(fget=get_PHIE_OLD_Units)

	def get_PHIE_OLD_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 3)

	PHIE_OLD_Comments = property(fget=get_PHIE_OLD_Comments)

	def Save_PHIE_OLD_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[1], 3, str(newValue))

	def Get_PHIE_OLD_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[1], attributeName)

	def Set_PHIE_OLD_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[1], attributeName, str(newValue))

	def Save_PHIE_OLD(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[1], index, float(value))

	def Save_Array_PHIE_OLD(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[1], index, float(value), xVal, yVal)

	def Save_PHIE_OLD_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[1], index, str(value))

	def Save_Array_PHIE_OLD_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[1], index, str(value), xVal, yVal)

	def get_Array_PHIE_OLD_MaxX(self):
		return self._inArrayX[1]

	Array_PHIE_OLD_MaxX = property(fget=get_Array_PHIE_OLD_MaxX)

	def get_Array_PHIE_OLD_MaxY(self):
		return self._inArrayY[1]

	Array_PHIE_OLD_MaxY = property(fget=get_Array_PHIE_OLD_MaxY)

	def SWE_OLD(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[2],2, index, True)

	def Array_SWE_OLD(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[2],2, index, xVal, yVal, True)

	def SWE_OLD_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[2], index)

	def Array_SWE_OLD_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[2], index, xVal, yVal)

	def get_SWE_OLD_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 1)

	SWE_OLD_Name = property(fget=get_SWE_OLD_Name)

	def get_SWE_OLD_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 2)

	SWE_OLD_Units = property(fget=get_SWE_OLD_Units)

	def get_SWE_OLD_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 3)

	SWE_OLD_Comments = property(fget=get_SWE_OLD_Comments)

	def Save_SWE_OLD_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[2], 3, str(newValue))

	def Get_SWE_OLD_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[2], attributeName)

	def Set_SWE_OLD_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[2], attributeName, str(newValue))

	def Save_SWE_OLD(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[2], index, float(value))

	def Save_Array_SWE_OLD(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[2], index, float(value), xVal, yVal)

	def Save_SWE_OLD_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[2], index, str(value))

	def Save_Array_SWE_OLD_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[2], index, str(value), xVal, yVal)

	def get_Array_SWE_OLD_MaxX(self):
		return self._inArrayX[2]

	Array_SWE_OLD_MaxX = property(fget=get_Array_SWE_OLD_MaxX)

	def get_Array_SWE_OLD_MaxY(self):
		return self._inArrayY[2]

	Array_SWE_OLD_MaxY = property(fget=get_Array_SWE_OLD_MaxY)

	def BVHC_OLD(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[3],3, index, True)

	def Array_BVHC_OLD(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[3],3, index, xVal, yVal, True)

	def BVHC_OLD_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[3], index)

	def Array_BVHC_OLD_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[3], index, xVal, yVal)

	def get_BVHC_OLD_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 1)

	BVHC_OLD_Name = property(fget=get_BVHC_OLD_Name)

	def get_BVHC_OLD_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 2)

	BVHC_OLD_Units = property(fget=get_BVHC_OLD_Units)

	def get_BVHC_OLD_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 3)

	BVHC_OLD_Comments = property(fget=get_BVHC_OLD_Comments)

	def Save_BVHC_OLD_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[3], 3, str(newValue))

	def Get_BVHC_OLD_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[3], attributeName)

	def Set_BVHC_OLD_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[3], attributeName, str(newValue))

	def Save_BVHC_OLD(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[3], index, float(value))

	def Save_Array_BVHC_OLD(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[3], index, float(value), xVal, yVal)

	def Save_BVHC_OLD_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[3], index, str(value))

	def Save_Array_BVHC_OLD_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[3], index, str(value), xVal, yVal)

	def get_Array_BVHC_OLD_MaxX(self):
		return self._inArrayX[3]

	Array_BVHC_OLD_MaxX = property(fget=get_Array_BVHC_OLD_MaxX)

	def get_Array_BVHC_OLD_MaxY(self):
		return self._inArrayY[3]

	Array_BVHC_OLD_MaxY = property(fget=get_Array_BVHC_OLD_MaxY)

	def FLAG_LOW_SWE_PHIE(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[4],4, index, True)

	def Array_FLAG_LOW_SWE_PHIE(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[4],4, index, xVal, yVal, True)

	def FLAG_LOW_SWE_PHIE_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[4], index)

	def Array_FLAG_LOW_SWE_PHIE_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[4], index, xVal, yVal)

	def get_FLAG_LOW_SWE_PHIE_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 1)

	FLAG_LOW_SWE_PHIE_Name = property(fget=get_FLAG_LOW_SWE_PHIE_Name)

	def get_FLAG_LOW_SWE_PHIE_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 2)

	FLAG_LOW_SWE_PHIE_Units = property(fget=get_FLAG_LOW_SWE_PHIE_Units)

	def get_FLAG_LOW_SWE_PHIE_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 3)

	FLAG_LOW_SWE_PHIE_Comments = property(fget=get_FLAG_LOW_SWE_PHIE_Comments)

	def Save_FLAG_LOW_SWE_PHIE_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[4], 3, str(newValue))

	def Get_FLAG_LOW_SWE_PHIE_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[4], attributeName)

	def Set_FLAG_LOW_SWE_PHIE_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[4], attributeName, str(newValue))

	def Save_FLAG_LOW_SWE_PHIE(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[4], index, float(value))

	def Save_Array_FLAG_LOW_SWE_PHIE(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[4], index, float(value), xVal, yVal)

	def Save_FLAG_LOW_SWE_PHIE_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[4], index, str(value))

	def Save_Array_FLAG_LOW_SWE_PHIE_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[4], index, str(value), xVal, yVal)

	def get_Array_FLAG_LOW_SWE_PHIE_MaxX(self):
		return self._inArrayX[4]

	Array_FLAG_LOW_SWE_PHIE_MaxX = property(fget=get_Array_FLAG_LOW_SWE_PHIE_MaxX)

	def get_Array_FLAG_LOW_SWE_PHIE_MaxY(self):
		return self._inArrayY[4]

	Array_FLAG_LOW_SWE_PHIE_MaxY = property(fget=get_Array_FLAG_LOW_SWE_PHIE_MaxY)

	def Save_SWE_NEW(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, float(value))

	def Save_Array_SWE_NEW(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, float(value), xVal, yVal)

	def Save_SWE_NEW_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, str(value))

	def Save_Array_SWE_NEW_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, str(value), xVal, yVal)

	def SWE_NEW(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[0], index)

	def Array_SWE_NEW(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[0], index, xVal, yVal)

	def SWE_NEW_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[0], index)

	def Array_SWE_NEW_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[0], index, xVal, yVal)

	def get_SWE_NEW_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 1)

	SWE_NEW_Name = property(fget=get_SWE_NEW_Name)

	def get_SWE_NEW_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 2)

	SWE_NEW_Units = property(fget=get_SWE_NEW_Units)

	def get_SWE_NEW_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 3)

	SWE_NEW_Comments = property(fget=get_SWE_NEW_Comments)

	def Save_SWE_NEW_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[0], 3, str(newValue))

	def get_Array_SWE_NEW_MaxX(self):
		return self._outArrayX[0]

	Array_SWE_NEW_MaxX = property(fget=get_Array_SWE_NEW_MaxX)

	def get_Array_SWE_NEW_MaxY(self):
		return self._outArrayY[0]

	Array_SWE_NEW_MaxY = property(fget=get_Array_SWE_NEW_MaxY)

	def Get_SWE_NEW_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[0], attributeName)

	def Set_SWE_NEW_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[0], attributeName, str(newValue))

	def Save_BVHC_NEW(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value))

	def Save_Array_BVHC_NEW(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value), xVal, yVal)

	def Save_BVHC_NEW_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value))

	def Save_Array_BVHC_NEW_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value), xVal, yVal)

	def BVHC_NEW(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[1], index)

	def Array_BVHC_NEW(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[1], index, xVal, yVal)

	def BVHC_NEW_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[1], index)

	def Array_BVHC_NEW_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[1], index, xVal, yVal)

	def get_BVHC_NEW_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 1)

	BVHC_NEW_Name = property(fget=get_BVHC_NEW_Name)

	def get_BVHC_NEW_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 2)

	BVHC_NEW_Units = property(fget=get_BVHC_NEW_Units)

	def get_BVHC_NEW_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 3)

	BVHC_NEW_Comments = property(fget=get_BVHC_NEW_Comments)

	def Save_BVHC_NEW_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[1], 3, str(newValue))

	def get_Array_BVHC_NEW_MaxX(self):
		return self._outArrayX[1]

	Array_BVHC_NEW_MaxX = property(fget=get_Array_BVHC_NEW_MaxX)

	def get_Array_BVHC_NEW_MaxY(self):
		return self._outArrayY[1]

	Array_BVHC_NEW_MaxY = property(fget=get_Array_BVHC_NEW_MaxY)

	def Get_BVHC_NEW_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[1], attributeName)

	def Set_BVHC_NEW_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[1], attributeName, str(newValue))

	def Save_BVW_NEW(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, float(value))

	def Save_Array_BVW_NEW(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, float(value), xVal, yVal)

	def Save_BVW_NEW_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, str(value))

	def Save_Array_BVW_NEW_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, str(value), xVal, yVal)

	def BVW_NEW(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[2], index)

	def Array_BVW_NEW(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[2], index, xVal, yVal)

	def BVW_NEW_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[2], index)

	def Array_BVW_NEW_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[2], index, xVal, yVal)

	def get_BVW_NEW_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 1)

	BVW_NEW_Name = property(fget=get_BVW_NEW_Name)

	def get_BVW_NEW_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 2)

	BVW_NEW_Units = property(fget=get_BVW_NEW_Units)

	def get_BVW_NEW_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 3)

	BVW_NEW_Comments = property(fget=get_BVW_NEW_Comments)

	def Save_BVW_NEW_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[2], 3, str(newValue))

	def get_Array_BVW_NEW_MaxX(self):
		return self._outArrayX[2]

	Array_BVW_NEW_MaxX = property(fget=get_Array_BVW_NEW_MaxX)

	def get_Array_BVW_NEW_MaxY(self):
		return self._outArrayY[2]

	Array_BVW_NEW_MaxY = property(fget=get_Array_BVW_NEW_MaxY)

	def Get_BVW_NEW_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[2], attributeName)

	def Set_BVW_NEW_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[2], attributeName, str(newValue))

	def VCL_EDIT(self, index):
		if self._parCnIn[0] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[0], index)
		else:
			return self._inputParameters[0]

	def Save_VCL_EDIT(self, index, value):
		if self._parCnIn[0] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[0], index, float(value))
		else:
			self._IPProxy.SetNumericParam(1, float(value))
			self._inputParameters[0] = float(value)

	def get_VCL_EDIT_Name(self):
		if self._parCnIn[0] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[0], 1)
		else:
			return str(self._inputParameters[0])

	VCL_EDIT_Name = property(fget=get_VCL_EDIT_Name)

	def PHIE_EDIT(self, index):
		if self._parCnIn[1] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[1], index)
		else:
			return self._inputParameters[1]

	def Save_PHIE_EDIT(self, index, value):
		if self._parCnIn[1] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[1], index, float(value))
		else:
			self._IPProxy.SetNumericParam(2, float(value))
			self._inputParameters[1] = float(value)

	def get_PHIE_EDIT_Name(self):
		if self._parCnIn[1] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[1], 1)
		else:
			return str(self._inputParameters[1])

	PHIE_EDIT_Name = property(fget=get_PHIE_EDIT_Name)

	def MOD_EXPONENT(self, index):
		if self._parCnIn[2] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[2], index)
		else:
			return self._inputParameters[2]

	def Save_MOD_EXPONENT(self, index, value):
		if self._parCnIn[2] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[2], index, float(value))
		else:
			self._IPProxy.SetNumericParam(3, float(value))
			self._inputParameters[2] = float(value)

	def get_MOD_EXPONENT_Name(self):
		if self._parCnIn[2] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[2], 1)
		else:
			return str(self._inputParameters[2])

	MOD_EXPONENT_Name = property(fget=get_MOD_EXPONENT_Name)

