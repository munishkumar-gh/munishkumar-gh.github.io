# /***********************************************/
#  * File dynamically created from IP: 08/24/2022 15:28:35
#  * DO NOT MANUALLY EDIT
# /***********************************************/

class Methods:
	def __init__(self):
		self._FIRST_AVAILABLE_LOG_RUN = -1
		self._LAST_AVAILABLE_LOG_RUN = -2

	def Depth(self, index):
		return self._IPProxy.GetCurveData(1, index)

	def PHI_DEN(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[0],0, index, True)

	def Array_PHI_DEN(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[0],0, index, xVal, yVal, True)

	def PHI_DEN_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[0], index)

	def Array_PHI_DEN_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[0], index, xVal, yVal)

	def get_PHI_DEN_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 1)

	PHI_DEN_Name = property(fget=get_PHI_DEN_Name)

	def get_PHI_DEN_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 2)

	PHI_DEN_Units = property(fget=get_PHI_DEN_Units)

	def get_PHI_DEN_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 3)

	PHI_DEN_Comments = property(fget=get_PHI_DEN_Comments)

	def Save_PHI_DEN_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[0], 3, str(newValue))

	def Get_PHI_DEN_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[0], attributeName)

	def Set_PHI_DEN_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[0], attributeName, str(newValue))

	def Save_PHI_DEN(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[0], index, float(value))

	def Save_Array_PHI_DEN(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[0], index, float(value), xVal, yVal)

	def Save_PHI_DEN_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[0], index, str(value))

	def Save_Array_PHI_DEN_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[0], index, str(value), xVal, yVal)

	def get_Array_PHI_DEN_MaxX(self):
		return self._inArrayX[0]

	Array_PHI_DEN_MaxX = property(fget=get_Array_PHI_DEN_MaxX)

	def get_Array_PHI_DEN_MaxY(self):
		return self._inArrayY[0]

	Array_PHI_DEN_MaxY = property(fget=get_Array_PHI_DEN_MaxY)

	def BFI_SHALE(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[1],1, index, True)

	def Array_BFI_SHALE(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[1],1, index, xVal, yVal, True)

	def BFI_SHALE_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[1], index)

	def Array_BFI_SHALE_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[1], index, xVal, yVal)

	def get_BFI_SHALE_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 1)

	BFI_SHALE_Name = property(fget=get_BFI_SHALE_Name)

	def get_BFI_SHALE_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 2)

	BFI_SHALE_Units = property(fget=get_BFI_SHALE_Units)

	def get_BFI_SHALE_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 3)

	BFI_SHALE_Comments = property(fget=get_BFI_SHALE_Comments)

	def Save_BFI_SHALE_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[1], 3, str(newValue))

	def Get_BFI_SHALE_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[1], attributeName)

	def Set_BFI_SHALE_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[1], attributeName, str(newValue))

	def Save_BFI_SHALE(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[1], index, float(value))

	def Save_Array_BFI_SHALE(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[1], index, float(value), xVal, yVal)

	def Save_BFI_SHALE_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[1], index, str(value))

	def Save_Array_BFI_SHALE_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[1], index, str(value), xVal, yVal)

	def get_Array_BFI_SHALE_MaxX(self):
		return self._inArrayX[1]

	Array_BFI_SHALE_MaxX = property(fget=get_Array_BFI_SHALE_MaxX)

	def get_Array_BFI_SHALE_MaxY(self):
		return self._inArrayY[1]

	Array_BFI_SHALE_MaxY = property(fget=get_Array_BFI_SHALE_MaxY)

	def PHIT_C(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[2],2, index, True)

	def Array_PHIT_C(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[2],2, index, xVal, yVal, True)

	def PHIT_C_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[2], index)

	def Array_PHIT_C_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[2], index, xVal, yVal)

	def get_PHIT_C_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 1)

	PHIT_C_Name = property(fget=get_PHIT_C_Name)

	def get_PHIT_C_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 2)

	PHIT_C_Units = property(fget=get_PHIT_C_Units)

	def get_PHIT_C_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 3)

	PHIT_C_Comments = property(fget=get_PHIT_C_Comments)

	def Save_PHIT_C_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[2], 3, str(newValue))

	def Get_PHIT_C_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[2], attributeName)

	def Set_PHIT_C_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[2], attributeName, str(newValue))

	def Save_PHIT_C(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[2], index, float(value))

	def Save_Array_PHIT_C(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[2], index, float(value), xVal, yVal)

	def Save_PHIT_C_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[2], index, str(value))

	def Save_Array_PHIT_C_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[2], index, str(value), xVal, yVal)

	def get_Array_PHIT_C_MaxX(self):
		return self._inArrayX[2]

	Array_PHIT_C_MaxX = property(fget=get_Array_PHIT_C_MaxX)

	def get_Array_PHIT_C_MaxY(self):
		return self._inArrayY[2]

	Array_PHIT_C_MaxY = property(fget=get_Array_PHIT_C_MaxY)

	def SWIRR_C(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[3],3, index, True)

	def Array_SWIRR_C(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[3],3, index, xVal, yVal, True)

	def SWIRR_C_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[3], index)

	def Array_SWIRR_C_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[3], index, xVal, yVal)

	def get_SWIRR_C_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 1)

	SWIRR_C_Name = property(fget=get_SWIRR_C_Name)

	def get_SWIRR_C_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 2)

	SWIRR_C_Units = property(fget=get_SWIRR_C_Units)

	def get_SWIRR_C_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 3)

	SWIRR_C_Comments = property(fget=get_SWIRR_C_Comments)

	def Save_SWIRR_C_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[3], 3, str(newValue))

	def Get_SWIRR_C_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[3], attributeName)

	def Set_SWIRR_C_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[3], attributeName, str(newValue))

	def Save_SWIRR_C(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[3], index, float(value))

	def Save_Array_SWIRR_C(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[3], index, float(value), xVal, yVal)

	def Save_SWIRR_C_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[3], index, str(value))

	def Save_Array_SWIRR_C_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[3], index, str(value), xVal, yVal)

	def get_Array_SWIRR_C_MaxX(self):
		return self._inArrayX[3]

	Array_SWIRR_C_MaxX = property(fget=get_Array_SWIRR_C_MaxX)

	def get_Array_SWIRR_C_MaxY(self):
		return self._inArrayY[3]

	Array_SWIRR_C_MaxY = property(fget=get_Array_SWIRR_C_MaxY)

	def PHIT_CL(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[4],4, index, True)

	def Array_PHIT_CL(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[4],4, index, xVal, yVal, True)

	def PHIT_CL_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[4], index)

	def Array_PHIT_CL_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[4], index, xVal, yVal)

	def get_PHIT_CL_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 1)

	PHIT_CL_Name = property(fget=get_PHIT_CL_Name)

	def get_PHIT_CL_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 2)

	PHIT_CL_Units = property(fget=get_PHIT_CL_Units)

	def get_PHIT_CL_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 3)

	PHIT_CL_Comments = property(fget=get_PHIT_CL_Comments)

	def Save_PHIT_CL_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[4], 3, str(newValue))

	def Get_PHIT_CL_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[4], attributeName)

	def Set_PHIT_CL_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[4], attributeName, str(newValue))

	def Save_PHIT_CL(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[4], index, float(value))

	def Save_Array_PHIT_CL(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[4], index, float(value), xVal, yVal)

	def Save_PHIT_CL_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[4], index, str(value))

	def Save_Array_PHIT_CL_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[4], index, str(value), xVal, yVal)

	def get_Array_PHIT_CL_MaxX(self):
		return self._inArrayX[4]

	Array_PHIT_CL_MaxX = property(fget=get_Array_PHIT_CL_MaxX)

	def get_Array_PHIT_CL_MaxY(self):
		return self._inArrayY[4]

	Array_PHIT_CL_MaxY = property(fget=get_Array_PHIT_CL_MaxY)

	def CBP1(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[5],5, index, True)

	def Array_CBP1(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[5],5, index, xVal, yVal, True)

	def CBP1_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[5], index)

	def Array_CBP1_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[5], index, xVal, yVal)

	def get_CBP1_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 1)

	CBP1_Name = property(fget=get_CBP1_Name)

	def get_CBP1_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 2)

	CBP1_Units = property(fget=get_CBP1_Units)

	def get_CBP1_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 3)

	CBP1_Comments = property(fget=get_CBP1_Comments)

	def Save_CBP1_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[5], 3, str(newValue))

	def Get_CBP1_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[5], attributeName)

	def Set_CBP1_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[5], attributeName, str(newValue))

	def Save_CBP1(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[5], index, float(value))

	def Save_Array_CBP1(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[5], index, float(value), xVal, yVal)

	def Save_CBP1_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[5], index, str(value))

	def Save_Array_CBP1_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[5], index, str(value), xVal, yVal)

	def get_Array_CBP1_MaxX(self):
		return self._inArrayX[5]

	Array_CBP1_MaxX = property(fget=get_Array_CBP1_MaxX)

	def get_Array_CBP1_MaxY(self):
		return self._inArrayY[5]

	Array_CBP1_MaxY = property(fget=get_Array_CBP1_MaxY)

	def CBP2(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[6],6, index, True)

	def Array_CBP2(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[6],6, index, xVal, yVal, True)

	def CBP2_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[6], index)

	def Array_CBP2_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[6], index, xVal, yVal)

	def get_CBP2_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[6], 1)

	CBP2_Name = property(fget=get_CBP2_Name)

	def get_CBP2_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[6], 2)

	CBP2_Units = property(fget=get_CBP2_Units)

	def get_CBP2_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[6], 3)

	CBP2_Comments = property(fget=get_CBP2_Comments)

	def Save_CBP2_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[6], 3, str(newValue))

	def Get_CBP2_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[6], attributeName)

	def Set_CBP2_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[6], attributeName, str(newValue))

	def Save_CBP2(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[6], index, float(value))

	def Save_Array_CBP2(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[6], index, float(value), xVal, yVal)

	def Save_CBP2_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[6], index, str(value))

	def Save_Array_CBP2_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[6], index, str(value), xVal, yVal)

	def get_Array_CBP2_MaxX(self):
		return self._inArrayX[6]

	Array_CBP2_MaxX = property(fget=get_Array_CBP2_MaxX)

	def get_Array_CBP2_MaxY(self):
		return self._inArrayY[6]

	Array_CBP2_MaxY = property(fget=get_Array_CBP2_MaxY)

	def CBP3(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[7],7, index, True)

	def Array_CBP3(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[7],7, index, xVal, yVal, True)

	def CBP3_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[7], index)

	def Array_CBP3_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[7], index, xVal, yVal)

	def get_CBP3_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[7], 1)

	CBP3_Name = property(fget=get_CBP3_Name)

	def get_CBP3_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[7], 2)

	CBP3_Units = property(fget=get_CBP3_Units)

	def get_CBP3_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[7], 3)

	CBP3_Comments = property(fget=get_CBP3_Comments)

	def Save_CBP3_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[7], 3, str(newValue))

	def Get_CBP3_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[7], attributeName)

	def Set_CBP3_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[7], attributeName, str(newValue))

	def Save_CBP3(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[7], index, float(value))

	def Save_Array_CBP3(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[7], index, float(value), xVal, yVal)

	def Save_CBP3_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[7], index, str(value))

	def Save_Array_CBP3_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[7], index, str(value), xVal, yVal)

	def get_Array_CBP3_MaxX(self):
		return self._inArrayX[7]

	Array_CBP3_MaxX = property(fget=get_Array_CBP3_MaxX)

	def get_Array_CBP3_MaxY(self):
		return self._inArrayY[7]

	Array_CBP3_MaxY = property(fget=get_Array_CBP3_MaxY)

	def CBP4(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[8],8, index, True)

	def Array_CBP4(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[8],8, index, xVal, yVal, True)

	def CBP4_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[8], index)

	def Array_CBP4_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[8], index, xVal, yVal)

	def get_CBP4_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[8], 1)

	CBP4_Name = property(fget=get_CBP4_Name)

	def get_CBP4_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[8], 2)

	CBP4_Units = property(fget=get_CBP4_Units)

	def get_CBP4_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[8], 3)

	CBP4_Comments = property(fget=get_CBP4_Comments)

	def Save_CBP4_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[8], 3, str(newValue))

	def Get_CBP4_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[8], attributeName)

	def Set_CBP4_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[8], attributeName, str(newValue))

	def Save_CBP4(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[8], index, float(value))

	def Save_Array_CBP4(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[8], index, float(value), xVal, yVal)

	def Save_CBP4_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[8], index, str(value))

	def Save_Array_CBP4_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[8], index, str(value), xVal, yVal)

	def get_Array_CBP4_MaxX(self):
		return self._inArrayX[8]

	Array_CBP4_MaxX = property(fget=get_Array_CBP4_MaxX)

	def get_Array_CBP4_MaxY(self):
		return self._inArrayY[8]

	Array_CBP4_MaxY = property(fget=get_Array_CBP4_MaxY)

	def CBP5(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[9],9, index, True)

	def Array_CBP5(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[9],9, index, xVal, yVal, True)

	def CBP5_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[9], index)

	def Array_CBP5_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[9], index, xVal, yVal)

	def get_CBP5_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[9], 1)

	CBP5_Name = property(fget=get_CBP5_Name)

	def get_CBP5_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[9], 2)

	CBP5_Units = property(fget=get_CBP5_Units)

	def get_CBP5_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[9], 3)

	CBP5_Comments = property(fget=get_CBP5_Comments)

	def Save_CBP5_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[9], 3, str(newValue))

	def Get_CBP5_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[9], attributeName)

	def Set_CBP5_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[9], attributeName, str(newValue))

	def Save_CBP5(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[9], index, float(value))

	def Save_Array_CBP5(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[9], index, float(value), xVal, yVal)

	def Save_CBP5_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[9], index, str(value))

	def Save_Array_CBP5_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[9], index, str(value), xVal, yVal)

	def get_Array_CBP5_MaxX(self):
		return self._inArrayX[9]

	Array_CBP5_MaxX = property(fget=get_Array_CBP5_MaxX)

	def get_Array_CBP5_MaxY(self):
		return self._inArrayY[9]

	Array_CBP5_MaxY = property(fget=get_Array_CBP5_MaxY)

	def CBP6(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[10],10, index, True)

	def Array_CBP6(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[10],10, index, xVal, yVal, True)

	def CBP6_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[10], index)

	def Array_CBP6_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[10], index, xVal, yVal)

	def get_CBP6_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[10], 1)

	CBP6_Name = property(fget=get_CBP6_Name)

	def get_CBP6_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[10], 2)

	CBP6_Units = property(fget=get_CBP6_Units)

	def get_CBP6_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[10], 3)

	CBP6_Comments = property(fget=get_CBP6_Comments)

	def Save_CBP6_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[10], 3, str(newValue))

	def Get_CBP6_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[10], attributeName)

	def Set_CBP6_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[10], attributeName, str(newValue))

	def Save_CBP6(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[10], index, float(value))

	def Save_Array_CBP6(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[10], index, float(value), xVal, yVal)

	def Save_CBP6_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[10], index, str(value))

	def Save_Array_CBP6_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[10], index, str(value), xVal, yVal)

	def get_Array_CBP6_MaxX(self):
		return self._inArrayX[10]

	Array_CBP6_MaxX = property(fget=get_Array_CBP6_MaxX)

	def get_Array_CBP6_MaxY(self):
		return self._inArrayY[10]

	Array_CBP6_MaxY = property(fget=get_Array_CBP6_MaxY)

	def CBP7(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[11],11, index, True)

	def Array_CBP7(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[11],11, index, xVal, yVal, True)

	def CBP7_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[11], index)

	def Array_CBP7_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[11], index, xVal, yVal)

	def get_CBP7_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[11], 1)

	CBP7_Name = property(fget=get_CBP7_Name)

	def get_CBP7_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[11], 2)

	CBP7_Units = property(fget=get_CBP7_Units)

	def get_CBP7_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[11], 3)

	CBP7_Comments = property(fget=get_CBP7_Comments)

	def Save_CBP7_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[11], 3, str(newValue))

	def Get_CBP7_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[11], attributeName)

	def Set_CBP7_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[11], attributeName, str(newValue))

	def Save_CBP7(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[11], index, float(value))

	def Save_Array_CBP7(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[11], index, float(value), xVal, yVal)

	def Save_CBP7_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[11], index, str(value))

	def Save_Array_CBP7_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[11], index, str(value), xVal, yVal)

	def get_Array_CBP7_MaxX(self):
		return self._inArrayX[11]

	Array_CBP7_MaxX = property(fget=get_Array_CBP7_MaxX)

	def get_Array_CBP7_MaxY(self):
		return self._inArrayY[11]

	Array_CBP7_MaxY = property(fget=get_Array_CBP7_MaxY)

	def CBP8(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[12],12, index, True)

	def Array_CBP8(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[12],12, index, xVal, yVal, True)

	def CBP8_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[12], index)

	def Array_CBP8_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[12], index, xVal, yVal)

	def get_CBP8_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[12], 1)

	CBP8_Name = property(fget=get_CBP8_Name)

	def get_CBP8_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[12], 2)

	CBP8_Units = property(fget=get_CBP8_Units)

	def get_CBP8_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[12], 3)

	CBP8_Comments = property(fget=get_CBP8_Comments)

	def Save_CBP8_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[12], 3, str(newValue))

	def Get_CBP8_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[12], attributeName)

	def Set_CBP8_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[12], attributeName, str(newValue))

	def Save_CBP8(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[12], index, float(value))

	def Save_Array_CBP8(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[12], index, float(value), xVal, yVal)

	def Save_CBP8_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[12], index, str(value))

	def Save_Array_CBP8_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[12], index, str(value), xVal, yVal)

	def get_Array_CBP8_MaxX(self):
		return self._inArrayX[12]

	Array_CBP8_MaxX = property(fget=get_Array_CBP8_MaxX)

	def get_Array_CBP8_MaxY(self):
		return self._inArrayY[12]

	Array_CBP8_MaxY = property(fget=get_Array_CBP8_MaxY)

	def Save_BFI(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, float(value))

	def Save_Array_BFI(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, float(value), xVal, yVal)

	def Save_BFI_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, str(value))

	def Save_Array_BFI_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, str(value), xVal, yVal)

	def BFI(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[0], index)

	def Array_BFI(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[0], index, xVal, yVal)

	def BFI_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[0], index)

	def Array_BFI_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[0], index, xVal, yVal)

	def get_BFI_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 1)

	BFI_Name = property(fget=get_BFI_Name)

	def get_BFI_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 2)

	BFI_Units = property(fget=get_BFI_Units)

	def get_BFI_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 3)

	BFI_Comments = property(fget=get_BFI_Comments)

	def Save_BFI_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[0], 3, str(newValue))

	def get_Array_BFI_MaxX(self):
		return self._outArrayX[0]

	Array_BFI_MaxX = property(fget=get_Array_BFI_MaxX)

	def get_Array_BFI_MaxY(self):
		return self._outArrayY[0]

	Array_BFI_MaxY = property(fget=get_Array_BFI_MaxY)

	def Get_BFI_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[0], attributeName)

	def Set_BFI_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[0], attributeName, str(newValue))

	def Save_BFVC(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value))

	def Save_Array_BFVC(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value), xVal, yVal)

	def Save_BFVC_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value))

	def Save_Array_BFVC_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value), xVal, yVal)

	def BFVC(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[1], index)

	def Array_BFVC(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[1], index, xVal, yVal)

	def BFVC_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[1], index)

	def Array_BFVC_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[1], index, xVal, yVal)

	def get_BFVC_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 1)

	BFVC_Name = property(fget=get_BFVC_Name)

	def get_BFVC_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 2)

	BFVC_Units = property(fget=get_BFVC_Units)

	def get_BFVC_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 3)

	BFVC_Comments = property(fget=get_BFVC_Comments)

	def Save_BFVC_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[1], 3, str(newValue))

	def get_Array_BFVC_MaxX(self):
		return self._outArrayX[1]

	Array_BFVC_MaxX = property(fget=get_Array_BFVC_MaxX)

	def get_Array_BFVC_MaxY(self):
		return self._outArrayY[1]

	Array_BFVC_MaxY = property(fget=get_Array_BFVC_MaxY)

	def Get_BFVC_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[1], attributeName)

	def Set_BFVC_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[1], attributeName, str(newValue))

	def Save_CMFF(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, float(value))

	def Save_Array_CMFF(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, float(value), xVal, yVal)

	def Save_CMFF_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, str(value))

	def Save_Array_CMFF_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, str(value), xVal, yVal)

	def CMFF(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[2], index)

	def Array_CMFF(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[2], index, xVal, yVal)

	def CMFF_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[2], index)

	def Array_CMFF_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[2], index, xVal, yVal)

	def get_CMFF_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 1)

	CMFF_Name = property(fget=get_CMFF_Name)

	def get_CMFF_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 2)

	CMFF_Units = property(fget=get_CMFF_Units)

	def get_CMFF_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 3)

	CMFF_Comments = property(fget=get_CMFF_Comments)

	def Save_CMFF_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[2], 3, str(newValue))

	def get_Array_CMFF_MaxX(self):
		return self._outArrayX[2]

	Array_CMFF_MaxX = property(fget=get_Array_CMFF_MaxX)

	def get_Array_CMFF_MaxY(self):
		return self._outArrayY[2]

	Array_CMFF_MaxY = property(fget=get_Array_CMFF_MaxY)

	def Get_CMFF_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[2], attributeName)

	def Set_CMFF_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[2], attributeName, str(newValue))

	def Save_BFV(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, float(value))

	def Save_Array_BFV(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, float(value), xVal, yVal)

	def Save_BFV_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, str(value))

	def Save_Array_BFV_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, str(value), xVal, yVal)

	def BFV(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[3], index)

	def Array_BFV(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[3], index, xVal, yVal)

	def BFV_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[3], index)

	def Array_BFV_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[3], index, xVal, yVal)

	def get_BFV_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 1)

	BFV_Name = property(fget=get_BFV_Name)

	def get_BFV_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 2)

	BFV_Units = property(fget=get_BFV_Units)

	def get_BFV_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 3)

	BFV_Comments = property(fget=get_BFV_Comments)

	def Save_BFV_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[3], 3, str(newValue))

	def get_Array_BFV_MaxX(self):
		return self._outArrayX[3]

	Array_BFV_MaxX = property(fget=get_Array_BFV_MaxX)

	def get_Array_BFV_MaxY(self):
		return self._outArrayY[3]

	Array_BFV_MaxY = property(fget=get_Array_BFV_MaxY)

	def Get_BFV_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[3], attributeName)

	def Set_BFV_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[3], attributeName, str(newValue))

	def Save_TCMR(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, float(value))

	def Save_Array_TCMR(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, float(value), xVal, yVal)

	def Save_TCMR_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, str(value))

	def Save_Array_TCMR_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, str(value), xVal, yVal)

	def TCMR(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[4], index)

	def Array_TCMR(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[4], index, xVal, yVal)

	def TCMR_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[4], index)

	def Array_TCMR_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[4], index, xVal, yVal)

	def get_TCMR_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 1)

	TCMR_Name = property(fget=get_TCMR_Name)

	def get_TCMR_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 2)

	TCMR_Units = property(fget=get_TCMR_Units)

	def get_TCMR_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 3)

	TCMR_Comments = property(fget=get_TCMR_Comments)

	def Save_TCMR_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[4], 3, str(newValue))

	def get_Array_TCMR_MaxX(self):
		return self._outArrayX[4]

	Array_TCMR_MaxX = property(fget=get_Array_TCMR_MaxX)

	def get_Array_TCMR_MaxY(self):
		return self._outArrayY[4]

	Array_TCMR_MaxY = property(fget=get_Array_TCMR_MaxY)

	def Get_TCMR_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[4], attributeName)

	def Set_TCMR_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[4], attributeName, str(newValue))

	def Save_DMRP(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[5], index, float(value))

	def Save_Array_DMRP(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[5], index, float(value), xVal, yVal)

	def Save_DMRP_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[5], index, str(value))

	def Save_Array_DMRP_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[5], index, str(value), xVal, yVal)

	def DMRP(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[5], index)

	def Array_DMRP(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[5], index, xVal, yVal)

	def DMRP_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[5], index)

	def Array_DMRP_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[5], index, xVal, yVal)

	def get_DMRP_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 1)

	DMRP_Name = property(fget=get_DMRP_Name)

	def get_DMRP_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 2)

	DMRP_Units = property(fget=get_DMRP_Units)

	def get_DMRP_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 3)

	DMRP_Comments = property(fget=get_DMRP_Comments)

	def Save_DMRP_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[5], 3, str(newValue))

	def get_Array_DMRP_MaxX(self):
		return self._outArrayX[5]

	Array_DMRP_MaxX = property(fget=get_Array_DMRP_MaxX)

	def get_Array_DMRP_MaxY(self):
		return self._outArrayY[5]

	Array_DMRP_MaxY = property(fget=get_Array_DMRP_MaxY)

	def Get_DMRP_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[5], attributeName)

	def Set_DMRP_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[5], attributeName, str(newValue))

	def Save_ECMR(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[6], index, float(value))

	def Save_Array_ECMR(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[6], index, float(value), xVal, yVal)

	def Save_ECMR_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[6], index, str(value))

	def Save_Array_ECMR_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[6], index, str(value), xVal, yVal)

	def ECMR(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[6], index)

	def Array_ECMR(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[6], index, xVal, yVal)

	def ECMR_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[6], index)

	def Array_ECMR_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[6], index, xVal, yVal)

	def get_ECMR_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 1)

	ECMR_Name = property(fget=get_ECMR_Name)

	def get_ECMR_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 2)

	ECMR_Units = property(fget=get_ECMR_Units)

	def get_ECMR_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 3)

	ECMR_Comments = property(fget=get_ECMR_Comments)

	def Save_ECMR_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[6], 3, str(newValue))

	def get_Array_ECMR_MaxX(self):
		return self._outArrayX[6]

	Array_ECMR_MaxX = property(fget=get_Array_ECMR_MaxX)

	def get_Array_ECMR_MaxY(self):
		return self._outArrayY[6]

	Array_ECMR_MaxY = property(fget=get_Array_ECMR_MaxY)

	def Get_ECMR_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[6], attributeName)

	def Set_ECMR_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[6], attributeName, str(newValue))

	def Save_SW_NMR(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[7], index, float(value))

	def Save_Array_SW_NMR(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[7], index, float(value), xVal, yVal)

	def Save_SW_NMR_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[7], index, str(value))

	def Save_Array_SW_NMR_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[7], index, str(value), xVal, yVal)

	def SW_NMR(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[7], index)

	def Array_SW_NMR(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[7], index, xVal, yVal)

	def SW_NMR_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[7], index)

	def Array_SW_NMR_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[7], index, xVal, yVal)

	def get_SW_NMR_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 1)

	SW_NMR_Name = property(fget=get_SW_NMR_Name)

	def get_SW_NMR_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 2)

	SW_NMR_Units = property(fget=get_SW_NMR_Units)

	def get_SW_NMR_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 3)

	SW_NMR_Comments = property(fget=get_SW_NMR_Comments)

	def Save_SW_NMR_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[7], 3, str(newValue))

	def get_Array_SW_NMR_MaxX(self):
		return self._outArrayX[7]

	Array_SW_NMR_MaxX = property(fget=get_Array_SW_NMR_MaxX)

	def get_Array_SW_NMR_MaxY(self):
		return self._outArrayY[7]

	Array_SW_NMR_MaxY = property(fget=get_Array_SW_NMR_MaxY)

	def Get_SW_NMR_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[7], attributeName)

	def Set_SW_NMR_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[7], attributeName, str(newValue))

	def Save_BVHC(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[8], index, float(value))

	def Save_Array_BVHC(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[8], index, float(value), xVal, yVal)

	def Save_BVHC_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[8], index, str(value))

	def Save_Array_BVHC_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[8], index, str(value), xVal, yVal)

	def BVHC(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[8], index)

	def Array_BVHC(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[8], index, xVal, yVal)

	def BVHC_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[8], index)

	def Array_BVHC_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[8], index, xVal, yVal)

	def get_BVHC_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 1)

	BVHC_Name = property(fget=get_BVHC_Name)

	def get_BVHC_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 2)

	BVHC_Units = property(fget=get_BVHC_Units)

	def get_BVHC_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 3)

	BVHC_Comments = property(fget=get_BVHC_Comments)

	def Save_BVHC_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[8], 3, str(newValue))

	def get_Array_BVHC_MaxX(self):
		return self._outArrayX[8]

	Array_BVHC_MaxX = property(fget=get_Array_BVHC_MaxX)

	def get_Array_BVHC_MaxY(self):
		return self._outArrayY[8]

	Array_BVHC_MaxY = property(fget=get_Array_BVHC_MaxY)

	def Get_BVHC_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[8], attributeName)

	def Set_BVHC_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[8], attributeName, str(newValue))

	def Save_VCL(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[9], index, float(value))

	def Save_Array_VCL(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[9], index, float(value), xVal, yVal)

	def Save_VCL_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[9], index, str(value))

	def Save_Array_VCL_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[9], index, str(value), xVal, yVal)

	def VCL(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[9], index)

	def Array_VCL(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[9], index, xVal, yVal)

	def VCL_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[9], index)

	def Array_VCL_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[9], index, xVal, yVal)

	def get_VCL_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[9], 1)

	VCL_Name = property(fget=get_VCL_Name)

	def get_VCL_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[9], 2)

	VCL_Units = property(fget=get_VCL_Units)

	def get_VCL_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[9], 3)

	VCL_Comments = property(fget=get_VCL_Comments)

	def Save_VCL_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[9], 3, str(newValue))

	def get_Array_VCL_MaxX(self):
		return self._outArrayX[9]

	Array_VCL_MaxX = property(fget=get_Array_VCL_MaxX)

	def get_Array_VCL_MaxY(self):
		return self._outArrayY[9]

	Array_VCL_MaxY = property(fget=get_Array_VCL_MaxY)

	def Get_VCL_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[9], attributeName)

	def Set_VCL_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[9], attributeName, str(newValue))

	def Save_VCL_GIE(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[10], index, float(value))

	def Save_Array_VCL_GIE(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[10], index, float(value), xVal, yVal)

	def Save_VCL_GIE_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[10], index, str(value))

	def Save_Array_VCL_GIE_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[10], index, str(value), xVal, yVal)

	def VCL_GIE(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[10], index)

	def Array_VCL_GIE(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[10], index, xVal, yVal)

	def VCL_GIE_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[10], index)

	def Array_VCL_GIE_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[10], index, xVal, yVal)

	def get_VCL_GIE_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[10], 1)

	VCL_GIE_Name = property(fget=get_VCL_GIE_Name)

	def get_VCL_GIE_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[10], 2)

	VCL_GIE_Units = property(fget=get_VCL_GIE_Units)

	def get_VCL_GIE_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[10], 3)

	VCL_GIE_Comments = property(fget=get_VCL_GIE_Comments)

	def Save_VCL_GIE_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[10], 3, str(newValue))

	def get_Array_VCL_GIE_MaxX(self):
		return self._outArrayX[10]

	Array_VCL_GIE_MaxX = property(fget=get_Array_VCL_GIE_MaxX)

	def get_Array_VCL_GIE_MaxY(self):
		return self._outArrayY[10]

	Array_VCL_GIE_MaxY = property(fget=get_Array_VCL_GIE_MaxY)

	def Get_VCL_GIE_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[10], attributeName)

	def Set_VCL_GIE_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[10], attributeName, str(newValue))

	def Save_VCL_BFI(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[11], index, float(value))

	def Save_Array_VCL_BFI(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[11], index, float(value), xVal, yVal)

	def Save_VCL_BFI_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[11], index, str(value))

	def Save_Array_VCL_BFI_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[11], index, str(value), xVal, yVal)

	def VCL_BFI(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[11], index)

	def Array_VCL_BFI(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[11], index, xVal, yVal)

	def VCL_BFI_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[11], index)

	def Array_VCL_BFI_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[11], index, xVal, yVal)

	def get_VCL_BFI_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[11], 1)

	VCL_BFI_Name = property(fget=get_VCL_BFI_Name)

	def get_VCL_BFI_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[11], 2)

	VCL_BFI_Units = property(fget=get_VCL_BFI_Units)

	def get_VCL_BFI_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[11], 3)

	VCL_BFI_Comments = property(fget=get_VCL_BFI_Comments)

	def Save_VCL_BFI_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[11], 3, str(newValue))

	def get_Array_VCL_BFI_MaxX(self):
		return self._outArrayX[11]

	Array_VCL_BFI_MaxX = property(fget=get_Array_VCL_BFI_MaxX)

	def get_Array_VCL_BFI_MaxY(self):
		return self._outArrayY[11]

	Array_VCL_BFI_MaxY = property(fget=get_Array_VCL_BFI_MaxY)

	def Get_VCL_BFI_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[11], attributeName)

	def Set_VCL_BFI_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[11], attributeName, str(newValue))

	def Save_VCL_NMR_PL(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[12], index, float(value))

	def Save_Array_VCL_NMR_PL(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[12], index, float(value), xVal, yVal)

	def Save_VCL_NMR_PL_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[12], index, str(value))

	def Save_Array_VCL_NMR_PL_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[12], index, str(value), xVal, yVal)

	def VCL_NMR_PL(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[12], index)

	def Array_VCL_NMR_PL(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[12], index, xVal, yVal)

	def VCL_NMR_PL_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[12], index)

	def Array_VCL_NMR_PL_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[12], index, xVal, yVal)

	def get_VCL_NMR_PL_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[12], 1)

	VCL_NMR_PL_Name = property(fget=get_VCL_NMR_PL_Name)

	def get_VCL_NMR_PL_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[12], 2)

	VCL_NMR_PL_Units = property(fget=get_VCL_NMR_PL_Units)

	def get_VCL_NMR_PL_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[12], 3)

	VCL_NMR_PL_Comments = property(fget=get_VCL_NMR_PL_Comments)

	def Save_VCL_NMR_PL_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[12], 3, str(newValue))

	def get_Array_VCL_NMR_PL_MaxX(self):
		return self._outArrayX[12]

	Array_VCL_NMR_PL_MaxX = property(fget=get_Array_VCL_NMR_PL_MaxX)

	def get_Array_VCL_NMR_PL_MaxY(self):
		return self._outArrayY[12]

	Array_VCL_NMR_PL_MaxY = property(fget=get_Array_VCL_NMR_PL_MaxY)

	def Get_VCL_NMR_PL_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[12], attributeName)

	def Set_VCL_NMR_PL_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[12], attributeName, str(newValue))

	def Save_VSH(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[13], index, float(value))

	def Save_Array_VSH(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[13], index, float(value), xVal, yVal)

	def Save_VSH_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[13], index, str(value))

	def Save_Array_VSH_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[13], index, str(value), xVal, yVal)

	def VSH(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[13], index)

	def Array_VSH(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[13], index, xVal, yVal)

	def VSH_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[13], index)

	def Array_VSH_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[13], index, xVal, yVal)

	def get_VSH_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[13], 1)

	VSH_Name = property(fget=get_VSH_Name)

	def get_VSH_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[13], 2)

	VSH_Units = property(fget=get_VSH_Units)

	def get_VSH_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[13], 3)

	VSH_Comments = property(fget=get_VSH_Comments)

	def Save_VSH_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[13], 3, str(newValue))

	def get_Array_VSH_MaxX(self):
		return self._outArrayX[13]

	Array_VSH_MaxX = property(fget=get_Array_VSH_MaxX)

	def get_Array_VSH_MaxY(self):
		return self._outArrayY[13]

	Array_VSH_MaxY = property(fget=get_Array_VSH_MaxY)

	def Get_VSH_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[13], attributeName)

	def Set_VSH_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[13], attributeName, str(newValue))

	def Save_VSH_CMR(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[14], index, float(value))

	def Save_Array_VSH_CMR(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[14], index, float(value), xVal, yVal)

	def Save_VSH_CMR_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[14], index, str(value))

	def Save_Array_VSH_CMR_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[14], index, str(value), xVal, yVal)

	def VSH_CMR(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[14], index)

	def Array_VSH_CMR(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[14], index, xVal, yVal)

	def VSH_CMR_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[14], index)

	def Array_VSH_CMR_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[14], index, xVal, yVal)

	def get_VSH_CMR_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[14], 1)

	VSH_CMR_Name = property(fget=get_VSH_CMR_Name)

	def get_VSH_CMR_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[14], 2)

	VSH_CMR_Units = property(fget=get_VSH_CMR_Units)

	def get_VSH_CMR_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[14], 3)

	VSH_CMR_Comments = property(fget=get_VSH_CMR_Comments)

	def Save_VSH_CMR_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[14], 3, str(newValue))

	def get_Array_VSH_CMR_MaxX(self):
		return self._outArrayX[14]

	Array_VSH_CMR_MaxX = property(fget=get_Array_VSH_CMR_MaxX)

	def get_Array_VSH_CMR_MaxY(self):
		return self._outArrayY[14]

	Array_VSH_CMR_MaxY = property(fget=get_Array_VSH_CMR_MaxY)

	def Get_VSH_CMR_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[14], attributeName)

	def Set_VSH_CMR_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[14], attributeName, str(newValue))

	def CK(self, index):
		if self._parCnIn[0] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[0], index)
		else:
			return self._inputParameters[0]

	def Save_CK(self, index, value):
		if self._parCnIn[0] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[0], index, float(value))
		else:
			self._IPProxy.SetNumericParam(1, float(value))
			self._inputParameters[0] = float(value)

	def get_CK_Name(self):
		if self._parCnIn[0] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[0], 1)
		else:
			return str(self._inputParameters[0])

	CK_Name = property(fget=get_CK_Name)

	def KK(self, index):
		if self._parCnIn[1] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[1], index)
		else:
			return self._inputParameters[1]

	def Save_KK(self, index, value):
		if self._parCnIn[1] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[1], index, float(value))
		else:
			self._IPProxy.SetNumericParam(2, float(value))
			self._inputParameters[1] = float(value)

	def get_KK_Name(self):
		if self._parCnIn[1] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[1], 1)
		else:
			return str(self._inputParameters[1])

	KK_Name = property(fget=get_KK_Name)

	def BFVMIN(self, index):
		if self._parCnIn[2] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[2], index)
		else:
			return self._inputParameters[2]

	def Save_BFVMIN(self, index, value):
		if self._parCnIn[2] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[2], index, float(value))
		else:
			self._IPProxy.SetNumericParam(3, float(value))
			self._inputParameters[2] = float(value)

	def get_BFVMIN_Name(self):
		if self._parCnIn[2] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[2], 1)
		else:
			return str(self._inputParameters[2])

	BFVMIN_Name = property(fget=get_BFVMIN_Name)

	def BFVMAX(self, index):
		if self._parCnIn[3] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[3], index)
		else:
			return self._inputParameters[3]

	def Save_BFVMAX(self, index, value):
		if self._parCnIn[3] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[3], index, float(value))
		else:
			self._IPProxy.SetNumericParam(4, float(value))
			self._inputParameters[3] = float(value)

	def get_BFVMAX_Name(self):
		if self._parCnIn[3] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[3], 1)
		else:
			return str(self._inputParameters[3])

	BFVMAX_Name = property(fget=get_BFVMAX_Name)

