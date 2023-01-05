# /***********************************************/
#  * File dynamically created from IP: 10/07/2022 10:19:03
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

	def VSH_ND(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[1],1, index, True)

	def Array_VSH_ND(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[1],1, index, xVal, yVal, True)

	def VSH_ND_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[1], index)

	def Array_VSH_ND_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[1], index, xVal, yVal)

	def get_VSH_ND_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 1)

	VSH_ND_Name = property(fget=get_VSH_ND_Name)

	def get_VSH_ND_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 2)

	VSH_ND_Units = property(fget=get_VSH_ND_Units)

	def get_VSH_ND_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 3)

	VSH_ND_Comments = property(fget=get_VSH_ND_Comments)

	def Save_VSH_ND_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[1], 3, str(newValue))

	def Get_VSH_ND_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[1], attributeName)

	def Set_VSH_ND_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[1], attributeName, str(newValue))

	def get_Array_VSH_ND_MaxX(self):
		return self._inArrayX[1]

	Array_VSH_ND_MaxX = property(fget=get_Array_VSH_ND_MaxX)

	def get_Array_VSH_ND_MaxY(self):
		return self._inArrayY[1]

	Array_VSH_ND_MaxY = property(fget=get_Array_VSH_ND_MaxY)

	def VSH_GR(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[2],2, index, True)

	def Array_VSH_GR(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[2],2, index, xVal, yVal, True)

	def VSH_GR_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[2], index)

	def Array_VSH_GR_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[2], index, xVal, yVal)

	def get_VSH_GR_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 1)

	VSH_GR_Name = property(fget=get_VSH_GR_Name)

	def get_VSH_GR_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 2)

	VSH_GR_Units = property(fget=get_VSH_GR_Units)

	def get_VSH_GR_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 3)

	VSH_GR_Comments = property(fget=get_VSH_GR_Comments)

	def Save_VSH_GR_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[2], 3, str(newValue))

	def Get_VSH_GR_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[2], attributeName)

	def Set_VSH_GR_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[2], attributeName, str(newValue))

	def get_Array_VSH_GR_MaxX(self):
		return self._inArrayX[2]

	Array_VSH_GR_MaxX = property(fget=get_Array_VSH_GR_MaxX)

	def get_Array_VSH_GR_MaxY(self):
		return self._inArrayY[2]

	Array_VSH_GR_MaxY = property(fget=get_Array_VSH_GR_MaxY)

	def VSH_RES(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[3],3, index, True)

	def Array_VSH_RES(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[3],3, index, xVal, yVal, True)

	def VSH_RES_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[3], index)

	def Array_VSH_RES_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[3], index, xVal, yVal)

	def get_VSH_RES_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 1)

	VSH_RES_Name = property(fget=get_VSH_RES_Name)

	def get_VSH_RES_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 2)

	VSH_RES_Units = property(fget=get_VSH_RES_Units)

	def get_VSH_RES_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 3)

	VSH_RES_Comments = property(fget=get_VSH_RES_Comments)

	def Save_VSH_RES_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[3], 3, str(newValue))

	def Get_VSH_RES_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[3], attributeName)

	def Set_VSH_RES_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[3], attributeName, str(newValue))

	def get_Array_VSH_RES_MaxX(self):
		return self._inArrayX[3]

	Array_VSH_RES_MaxX = property(fget=get_Array_VSH_RES_MaxX)

	def get_Array_VSH_RES_MaxY(self):
		return self._inArrayY[3]

	Array_VSH_RES_MaxY = property(fget=get_Array_VSH_RES_MaxY)

	def VSH_SP(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[4],4, index, True)

	def Array_VSH_SP(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[4],4, index, xVal, yVal, True)

	def VSH_SP_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[4], index)

	def Array_VSH_SP_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[4], index, xVal, yVal)

	def get_VSH_SP_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 1)

	VSH_SP_Name = property(fget=get_VSH_SP_Name)

	def get_VSH_SP_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 2)

	VSH_SP_Units = property(fget=get_VSH_SP_Units)

	def get_VSH_SP_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 3)

	VSH_SP_Comments = property(fget=get_VSH_SP_Comments)

	def Save_VSH_SP_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[4], 3, str(newValue))

	def Get_VSH_SP_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[4], attributeName)

	def Set_VSH_SP_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[4], attributeName, str(newValue))

	def get_Array_VSH_SP_MaxX(self):
		return self._inArrayX[4]

	Array_VSH_SP_MaxX = property(fget=get_Array_VSH_SP_MaxX)

	def get_Array_VSH_SP_MaxY(self):
		return self._inArrayY[4]

	Array_VSH_SP_MaxY = property(fget=get_Array_VSH_SP_MaxY)

	def PHIX(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[5],5, index, True)

	def Array_PHIX(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[5],5, index, xVal, yVal, True)

	def PHIX_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[5], index)

	def Array_PHIX_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[5], index, xVal, yVal)

	def get_PHIX_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 1)

	PHIX_Name = property(fget=get_PHIX_Name)

	def get_PHIX_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 2)

	PHIX_Units = property(fget=get_PHIX_Units)

	def get_PHIX_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 3)

	PHIX_Comments = property(fget=get_PHIX_Comments)

	def Save_PHIX_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[5], 3, str(newValue))

	def Get_PHIX_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[5], attributeName)

	def Set_PHIX_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[5], attributeName, str(newValue))

	def get_Array_PHIX_MaxX(self):
		return self._inArrayX[5]

	Array_PHIX_MaxX = property(fget=get_Array_PHIX_MaxX)

	def get_Array_PHIX_MaxY(self):
		return self._inArrayY[5]

	Array_PHIX_MaxY = property(fget=get_Array_PHIX_MaxY)

	def PHIA(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[6],6, index, True)

	def Array_PHIA(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[6],6, index, xVal, yVal, True)

	def PHIA_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[6], index)

	def Array_PHIA_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[6], index, xVal, yVal)

	def get_PHIA_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[6], 1)

	PHIA_Name = property(fget=get_PHIA_Name)

	def get_PHIA_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[6], 2)

	PHIA_Units = property(fget=get_PHIA_Units)

	def get_PHIA_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[6], 3)

	PHIA_Comments = property(fget=get_PHIA_Comments)

	def Save_PHIA_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[6], 3, str(newValue))

	def Get_PHIA_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[6], attributeName)

	def Set_PHIA_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[6], attributeName, str(newValue))

	def get_Array_PHIA_MaxX(self):
		return self._inArrayX[6]

	Array_PHIA_MaxX = property(fget=get_Array_PHIA_MaxX)

	def get_Array_PHIA_MaxY(self):
		return self._inArrayY[6]

	Array_PHIA_MaxY = property(fget=get_Array_PHIA_MaxY)

	def PHIT_HC(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[7],7, index, True)

	def Array_PHIT_HC(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[7],7, index, xVal, yVal, True)

	def PHIT_HC_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[7], index)

	def Array_PHIT_HC_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[7], index, xVal, yVal)

	def get_PHIT_HC_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[7], 1)

	PHIT_HC_Name = property(fget=get_PHIT_HC_Name)

	def get_PHIT_HC_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[7], 2)

	PHIT_HC_Units = property(fget=get_PHIT_HC_Units)

	def get_PHIT_HC_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[7], 3)

	PHIT_HC_Comments = property(fget=get_PHIT_HC_Comments)

	def Save_PHIT_HC_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[7], 3, str(newValue))

	def Get_PHIT_HC_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[7], attributeName)

	def Set_PHIT_HC_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[7], attributeName, str(newValue))

	def get_Array_PHIT_HC_MaxX(self):
		return self._inArrayX[7]

	Array_PHIT_HC_MaxX = property(fget=get_Array_PHIT_HC_MaxX)

	def get_Array_PHIT_HC_MaxY(self):
		return self._inArrayY[7]

	Array_PHIT_HC_MaxY = property(fget=get_Array_PHIT_HC_MaxY)

	def PHIT(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[8],8, index, True)

	def Array_PHIT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[8],8, index, xVal, yVal, True)

	def PHIT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[8], index)

	def Array_PHIT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[8], index, xVal, yVal)

	def get_PHIT_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[8], 1)

	PHIT_Name = property(fget=get_PHIT_Name)

	def get_PHIT_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[8], 2)

	PHIT_Units = property(fget=get_PHIT_Units)

	def get_PHIT_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[8], 3)

	PHIT_Comments = property(fget=get_PHIT_Comments)

	def Save_PHIT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[8], 3, str(newValue))

	def Get_PHIT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[8], attributeName)

	def Set_PHIT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[8], attributeName, str(newValue))

	def get_Array_PHIT_MaxX(self):
		return self._inArrayX[8]

	Array_PHIT_MaxX = property(fget=get_Array_PHIT_MaxX)

	def get_Array_PHIT_MaxY(self):
		return self._inArrayY[8]

	Array_PHIT_MaxY = property(fget=get_Array_PHIT_MaxY)

	def PHID_A(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[9],9, index, True)

	def Array_PHID_A(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[9],9, index, xVal, yVal, True)

	def PHID_A_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[9], index)

	def Array_PHID_A_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[9], index, xVal, yVal)

	def get_PHID_A_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[9], 1)

	PHID_A_Name = property(fget=get_PHID_A_Name)

	def get_PHID_A_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[9], 2)

	PHID_A_Units = property(fget=get_PHID_A_Units)

	def get_PHID_A_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[9], 3)

	PHID_A_Comments = property(fget=get_PHID_A_Comments)

	def Save_PHID_A_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[9], 3, str(newValue))

	def Get_PHID_A_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[9], attributeName)

	def Set_PHID_A_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[9], attributeName, str(newValue))

	def get_Array_PHID_A_MaxX(self):
		return self._inArrayX[9]

	Array_PHID_A_MaxX = property(fget=get_Array_PHID_A_MaxX)

	def get_Array_PHID_A_MaxY(self):
		return self._inArrayY[9]

	Array_PHID_A_MaxY = property(fget=get_Array_PHID_A_MaxY)

	def PHIE(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[10],10, index, True)

	def Array_PHIE(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[10],10, index, xVal, yVal, True)

	def PHIE_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[10], index)

	def Array_PHIE_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[10], index, xVal, yVal)

	def get_PHIE_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[10], 1)

	PHIE_Name = property(fget=get_PHIE_Name)

	def get_PHIE_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[10], 2)

	PHIE_Units = property(fget=get_PHIE_Units)

	def get_PHIE_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[10], 3)

	PHIE_Comments = property(fget=get_PHIE_Comments)

	def Save_PHIE_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[10], 3, str(newValue))

	def Get_PHIE_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[10], attributeName)

	def Set_PHIE_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[10], attributeName, str(newValue))

	def get_Array_PHIE_MaxX(self):
		return self._inArrayX[10]

	Array_PHIE_MaxX = property(fget=get_Array_PHIE_MaxX)

	def get_Array_PHIE_MaxY(self):
		return self._inArrayY[10]

	Array_PHIE_MaxY = property(fget=get_Array_PHIE_MaxY)

	def RW_SP(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[11],11, index, True)

	def Array_RW_SP(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[11],11, index, xVal, yVal, True)

	def RW_SP_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[11], index)

	def Array_RW_SP_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[11], index, xVal, yVal)

	def get_RW_SP_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[11], 1)

	RW_SP_Name = property(fget=get_RW_SP_Name)

	def get_RW_SP_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[11], 2)

	RW_SP_Units = property(fget=get_RW_SP_Units)

	def get_RW_SP_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[11], 3)

	RW_SP_Comments = property(fget=get_RW_SP_Comments)

	def Save_RW_SP_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[11], 3, str(newValue))

	def Get_RW_SP_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[11], attributeName)

	def Set_RW_SP_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[11], attributeName, str(newValue))

	def get_Array_RW_SP_MaxX(self):
		return self._inArrayX[11]

	Array_RW_SP_MaxX = property(fget=get_Array_RW_SP_MaxX)

	def get_Array_RW_SP_MaxY(self):
		return self._inArrayY[11]

	Array_RW_SP_MaxY = property(fget=get_Array_RW_SP_MaxY)

	def SALINITY_SP(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[12],12, index, True)

	def Array_SALINITY_SP(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[12],12, index, xVal, yVal, True)

	def SALINITY_SP_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[12], index)

	def Array_SALINITY_SP_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[12], index, xVal, yVal)

	def get_SALINITY_SP_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[12], 1)

	SALINITY_SP_Name = property(fget=get_SALINITY_SP_Name)

	def get_SALINITY_SP_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[12], 2)

	SALINITY_SP_Units = property(fget=get_SALINITY_SP_Units)

	def get_SALINITY_SP_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[12], 3)

	SALINITY_SP_Comments = property(fget=get_SALINITY_SP_Comments)

	def Save_SALINITY_SP_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[12], 3, str(newValue))

	def Get_SALINITY_SP_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[12], attributeName)

	def Set_SALINITY_SP_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[12], attributeName, str(newValue))

	def get_Array_SALINITY_SP_MaxX(self):
		return self._inArrayX[12]

	Array_SALINITY_SP_MaxX = property(fget=get_Array_SALINITY_SP_MaxX)

	def get_Array_SALINITY_SP_MaxY(self):
		return self._inArrayY[12]

	Array_SALINITY_SP_MaxY = property(fget=get_Array_SALINITY_SP_MaxY)

	def RW(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[13],13, index, True)

	def Array_RW(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[13],13, index, xVal, yVal, True)

	def RW_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[13], index)

	def Array_RW_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[13], index, xVal, yVal)

	def get_RW_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[13], 1)

	RW_Name = property(fget=get_RW_Name)

	def get_RW_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[13], 2)

	RW_Units = property(fget=get_RW_Units)

	def get_RW_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[13], 3)

	RW_Comments = property(fget=get_RW_Comments)

	def Save_RW_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[13], 3, str(newValue))

	def Get_RW_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[13], attributeName)

	def Set_RW_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[13], attributeName, str(newValue))

	def get_Array_RW_MaxX(self):
		return self._inArrayX[13]

	Array_RW_MaxX = property(fget=get_Array_RW_MaxX)

	def get_Array_RW_MaxY(self):
		return self._inArrayY[13]

	Array_RW_MaxY = property(fget=get_Array_RW_MaxY)

	def SALINITY(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[14],14, index, True)

	def Array_SALINITY(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[14],14, index, xVal, yVal, True)

	def SALINITY_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[14], index)

	def Array_SALINITY_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[14], index, xVal, yVal)

	def get_SALINITY_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[14], 1)

	SALINITY_Name = property(fget=get_SALINITY_Name)

	def get_SALINITY_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[14], 2)

	SALINITY_Units = property(fget=get_SALINITY_Units)

	def get_SALINITY_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[14], 3)

	SALINITY_Comments = property(fget=get_SALINITY_Comments)

	def Save_SALINITY_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[14], 3, str(newValue))

	def Get_SALINITY_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[14], attributeName)

	def Set_SALINITY_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[14], attributeName, str(newValue))

	def get_Array_SALINITY_MaxX(self):
		return self._inArrayX[14]

	Array_SALINITY_MaxX = property(fget=get_Array_SALINITY_MaxX)

	def get_Array_SALINITY_MaxY(self):
		return self._inArrayY[14]

	Array_SALINITY_MaxY = property(fget=get_Array_SALINITY_MaxY)

	def RHOGM(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[15],15, index, True)

	def Array_RHOGM(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[15],15, index, xVal, yVal, True)

	def RHOGM_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[15], index)

	def Array_RHOGM_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[15], index, xVal, yVal)

	def get_RHOGM_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[15], 1)

	RHOGM_Name = property(fget=get_RHOGM_Name)

	def get_RHOGM_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[15], 2)

	RHOGM_Units = property(fget=get_RHOGM_Units)

	def get_RHOGM_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[15], 3)

	RHOGM_Comments = property(fget=get_RHOGM_Comments)

	def Save_RHOGM_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[15], 3, str(newValue))

	def Get_RHOGM_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[15], attributeName)

	def Set_RHOGM_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[15], attributeName, str(newValue))

	def get_Array_RHOGM_MaxX(self):
		return self._inArrayX[15]

	Array_RHOGM_MaxX = property(fget=get_Array_RHOGM_MaxX)

	def get_Array_RHOGM_MaxY(self):
		return self._inArrayY[15]

	Array_RHOGM_MaxY = property(fget=get_Array_RHOGM_MaxY)

	def RHOGC(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[16],16, index, True)

	def Array_RHOGC(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[16],16, index, xVal, yVal, True)

	def RHOGC_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[16], index)

	def Array_RHOGC_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[16], index, xVal, yVal)

	def get_RHOGC_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[16], 1)

	RHOGC_Name = property(fget=get_RHOGC_Name)

	def get_RHOGC_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[16], 2)

	RHOGC_Units = property(fget=get_RHOGC_Units)

	def get_RHOGC_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[16], 3)

	RHOGC_Comments = property(fget=get_RHOGC_Comments)

	def Save_RHOGC_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[16], 3, str(newValue))

	def Get_RHOGC_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[16], attributeName)

	def Set_RHOGC_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[16], attributeName, str(newValue))

	def get_Array_RHOGC_MaxX(self):
		return self._inArrayX[16]

	Array_RHOGC_MaxX = property(fget=get_Array_RHOGC_MaxX)

	def get_Array_RHOGC_MaxY(self):
		return self._inArrayY[16]

	Array_RHOGC_MaxY = property(fget=get_Array_RHOGC_MaxY)

	def SWT(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[17],17, index, True)

	def Array_SWT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[17],17, index, xVal, yVal, True)

	def SWT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[17], index)

	def Array_SWT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[17], index, xVal, yVal)

	def get_SWT_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[17], 1)

	SWT_Name = property(fget=get_SWT_Name)

	def get_SWT_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[17], 2)

	SWT_Units = property(fget=get_SWT_Units)

	def get_SWT_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[17], 3)

	SWT_Comments = property(fget=get_SWT_Comments)

	def Save_SWT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[17], 3, str(newValue))

	def Get_SWT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[17], attributeName)

	def Set_SWT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[17], attributeName, str(newValue))

	def get_Array_SWT_MaxX(self):
		return self._inArrayX[17]

	Array_SWT_MaxX = property(fget=get_Array_SWT_MaxX)

	def get_Array_SWT_MaxY(self):
		return self._inArrayY[17]

	Array_SWT_MaxY = property(fget=get_Array_SWT_MaxY)

	def SWE(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[18],18, index, True)

	def Array_SWE(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[18],18, index, xVal, yVal, True)

	def SWE_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[18], index)

	def Array_SWE_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[18], index, xVal, yVal)

	def get_SWE_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[18], 1)

	SWE_Name = property(fget=get_SWE_Name)

	def get_SWE_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[18], 2)

	SWE_Units = property(fget=get_SWE_Units)

	def get_SWE_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[18], 3)

	SWE_Comments = property(fget=get_SWE_Comments)

	def Save_SWE_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[18], 3, str(newValue))

	def Get_SWE_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[18], attributeName)

	def Set_SWE_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[18], attributeName, str(newValue))

	def get_Array_SWE_MaxX(self):
		return self._inArrayX[18]

	Array_SWE_MaxX = property(fget=get_Array_SWE_MaxX)

	def get_Array_SWE_MaxY(self):
		return self._inArrayY[18]

	Array_SWE_MaxY = property(fget=get_Array_SWE_MaxY)

	def SXOT(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[19],19, index, True)

	def Array_SXOT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[19],19, index, xVal, yVal, True)

	def SXOT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[19], index)

	def Array_SXOT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[19], index, xVal, yVal)

	def get_SXOT_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[19], 1)

	SXOT_Name = property(fget=get_SXOT_Name)

	def get_SXOT_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[19], 2)

	SXOT_Units = property(fget=get_SXOT_Units)

	def get_SXOT_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[19], 3)

	SXOT_Comments = property(fget=get_SXOT_Comments)

	def Save_SXOT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[19], 3, str(newValue))

	def Get_SXOT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[19], attributeName)

	def Set_SXOT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[19], attributeName, str(newValue))

	def get_Array_SXOT_MaxX(self):
		return self._inArrayX[19]

	Array_SXOT_MaxX = property(fget=get_Array_SXOT_MaxX)

	def get_Array_SXOT_MaxY(self):
		return self._inArrayY[19]

	Array_SXOT_MaxY = property(fget=get_Array_SXOT_MaxY)

	def SXOE(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[20],20, index, True)

	def Array_SXOE(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[20],20, index, xVal, yVal, True)

	def SXOE_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[20], index)

	def Array_SXOE_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[20], index, xVal, yVal)

	def get_SXOE_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[20], 1)

	SXOE_Name = property(fget=get_SXOE_Name)

	def get_SXOE_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[20], 2)

	SXOE_Units = property(fget=get_SXOE_Units)

	def get_SXOE_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[20], 3)

	SXOE_Comments = property(fget=get_SXOE_Comments)

	def Save_SXOE_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[20], 3, str(newValue))

	def Get_SXOE_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[20], attributeName)

	def Set_SXOE_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[20], attributeName, str(newValue))

	def get_Array_SXOE_MaxX(self):
		return self._inArrayX[20]

	Array_SXOE_MaxX = property(fget=get_Array_SXOE_MaxX)

	def get_Array_SXOE_MaxY(self):
		return self._inArrayY[20]

	Array_SXOE_MaxY = property(fget=get_Array_SXOE_MaxY)

	def BVW(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[21],21, index, True)

	def Array_BVW(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[21],21, index, xVal, yVal, True)

	def BVW_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[21], index)

	def Array_BVW_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[21], index, xVal, yVal)

	def get_BVW_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[21], 1)

	BVW_Name = property(fget=get_BVW_Name)

	def get_BVW_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[21], 2)

	BVW_Units = property(fget=get_BVW_Units)

	def get_BVW_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[21], 3)

	BVW_Comments = property(fget=get_BVW_Comments)

	def Save_BVW_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[21], 3, str(newValue))

	def Get_BVW_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[21], attributeName)

	def Set_BVW_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[21], attributeName, str(newValue))

	def get_Array_BVW_MaxX(self):
		return self._inArrayX[21]

	Array_BVW_MaxX = property(fget=get_Array_BVW_MaxX)

	def get_Array_BVW_MaxY(self):
		return self._inArrayY[21]

	Array_BVW_MaxY = property(fget=get_Array_BVW_MaxY)

	def BVWE(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[22],22, index, True)

	def Array_BVWE(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[22],22, index, xVal, yVal, True)

	def BVWE_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[22], index)

	def Array_BVWE_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[22], index, xVal, yVal)

	def get_BVWE_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[22], 1)

	BVWE_Name = property(fget=get_BVWE_Name)

	def get_BVWE_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[22], 2)

	BVWE_Units = property(fget=get_BVWE_Units)

	def get_BVWE_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[22], 3)

	BVWE_Comments = property(fget=get_BVWE_Comments)

	def Save_BVWE_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[22], 3, str(newValue))

	def Get_BVWE_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[22], attributeName)

	def Set_BVWE_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[22], attributeName, str(newValue))

	def get_Array_BVWE_MaxX(self):
		return self._inArrayX[22]

	Array_BVWE_MaxX = property(fget=get_Array_BVWE_MaxX)

	def get_Array_BVWE_MaxY(self):
		return self._inArrayY[22]

	Array_BVWE_MaxY = property(fget=get_Array_BVWE_MaxY)

	def BVSH(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[23],23, index, True)

	def Array_BVSH(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[23],23, index, xVal, yVal, True)

	def BVSH_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[23], index)

	def Array_BVSH_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[23], index, xVal, yVal)

	def get_BVSH_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[23], 1)

	BVSH_Name = property(fget=get_BVSH_Name)

	def get_BVSH_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[23], 2)

	BVSH_Units = property(fget=get_BVSH_Units)

	def get_BVSH_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[23], 3)

	BVSH_Comments = property(fget=get_BVSH_Comments)

	def Save_BVSH_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[23], 3, str(newValue))

	def Get_BVSH_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[23], attributeName)

	def Set_BVSH_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[23], attributeName, str(newValue))

	def get_Array_BVSH_MaxX(self):
		return self._inArrayX[23]

	Array_BVSH_MaxX = property(fget=get_Array_BVSH_MaxX)

	def get_Array_BVSH_MaxY(self):
		return self._inArrayY[23]

	Array_BVSH_MaxY = property(fget=get_Array_BVSH_MaxY)

	def BVHC(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[24],24, index, True)

	def Array_BVHC(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[24],24, index, xVal, yVal, True)

	def BVHC_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[24], index)

	def Array_BVHC_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[24], index, xVal, yVal)

	def get_BVHC_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[24], 1)

	BVHC_Name = property(fget=get_BVHC_Name)

	def get_BVHC_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[24], 2)

	BVHC_Units = property(fget=get_BVHC_Units)

	def get_BVHC_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[24], 3)

	BVHC_Comments = property(fget=get_BVHC_Comments)

	def Save_BVHC_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[24], 3, str(newValue))

	def Get_BVHC_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[24], attributeName)

	def Set_BVHC_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[24], attributeName, str(newValue))

	def get_Array_BVHC_MaxX(self):
		return self._inArrayX[24]

	Array_BVHC_MaxX = property(fget=get_Array_BVHC_MaxX)

	def get_Array_BVHC_MaxY(self):
		return self._inArrayY[24]

	Array_BVHC_MaxY = property(fget=get_Array_BVHC_MaxY)

	def BVSAND(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[25],25, index, True)

	def Array_BVSAND(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[25],25, index, xVal, yVal, True)

	def BVSAND_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[25], index)

	def Array_BVSAND_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[25], index, xVal, yVal)

	def get_BVSAND_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[25], 1)

	BVSAND_Name = property(fget=get_BVSAND_Name)

	def get_BVSAND_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[25], 2)

	BVSAND_Units = property(fget=get_BVSAND_Units)

	def get_BVSAND_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[25], 3)

	BVSAND_Comments = property(fget=get_BVSAND_Comments)

	def Save_BVSAND_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[25], 3, str(newValue))

	def Get_BVSAND_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[25], attributeName)

	def Set_BVSAND_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[25], attributeName, str(newValue))

	def get_Array_BVSAND_MaxX(self):
		return self._inArrayX[25]

	Array_BVSAND_MaxX = property(fget=get_Array_BVSAND_MaxX)

	def get_Array_BVSAND_MaxY(self):
		return self._inArrayY[25]

	Array_BVSAND_MaxY = property(fget=get_Array_BVSAND_MaxY)

	def BVLIM(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[26],26, index, True)

	def Array_BVLIM(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[26],26, index, xVal, yVal, True)

	def BVLIM_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[26], index)

	def Array_BVLIM_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[26], index, xVal, yVal)

	def get_BVLIM_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[26], 1)

	BVLIM_Name = property(fget=get_BVLIM_Name)

	def get_BVLIM_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[26], 2)

	BVLIM_Units = property(fget=get_BVLIM_Units)

	def get_BVLIM_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[26], 3)

	BVLIM_Comments = property(fget=get_BVLIM_Comments)

	def Save_BVLIM_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[26], 3, str(newValue))

	def Get_BVLIM_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[26], attributeName)

	def Set_BVLIM_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[26], attributeName, str(newValue))

	def get_Array_BVLIM_MaxX(self):
		return self._inArrayX[26]

	Array_BVLIM_MaxX = property(fget=get_Array_BVLIM_MaxX)

	def get_Array_BVLIM_MaxY(self):
		return self._inArrayY[26]

	Array_BVLIM_MaxY = property(fget=get_Array_BVLIM_MaxY)

	def BVSILT(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[27],27, index, True)

	def Array_BVSILT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[27],27, index, xVal, yVal, True)

	def BVSILT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[27], index)

	def Array_BVSILT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[27], index, xVal, yVal)

	def get_BVSILT_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[27], 1)

	BVSILT_Name = property(fget=get_BVSILT_Name)

	def get_BVSILT_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[27], 2)

	BVSILT_Units = property(fget=get_BVSILT_Units)

	def get_BVSILT_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[27], 3)

	BVSILT_Comments = property(fget=get_BVSILT_Comments)

	def Save_BVSILT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[27], 3, str(newValue))

	def Get_BVSILT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[27], attributeName)

	def Set_BVSILT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[27], attributeName, str(newValue))

	def get_Array_BVSILT_MaxX(self):
		return self._inArrayX[27]

	Array_BVSILT_MaxX = property(fget=get_Array_BVSILT_MaxX)

	def get_Array_BVSILT_MaxY(self):
		return self._inArrayY[27]

	Array_BVSILT_MaxY = property(fget=get_Array_BVSILT_MaxY)

	def BVCLAY(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[28],28, index, True)

	def Array_BVCLAY(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[28],28, index, xVal, yVal, True)

	def BVCLAY_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[28], index)

	def Array_BVCLAY_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[28], index, xVal, yVal)

	def get_BVCLAY_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[28], 1)

	BVCLAY_Name = property(fget=get_BVCLAY_Name)

	def get_BVCLAY_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[28], 2)

	BVCLAY_Units = property(fget=get_BVCLAY_Units)

	def get_BVCLAY_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[28], 3)

	BVCLAY_Comments = property(fget=get_BVCLAY_Comments)

	def Save_BVCLAY_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[28], 3, str(newValue))

	def Get_BVCLAY_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[28], attributeName)

	def Set_BVCLAY_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[28], attributeName, str(newValue))

	def get_Array_BVCLAY_MaxX(self):
		return self._inArrayX[28]

	Array_BVCLAY_MaxX = property(fget=get_Array_BVCLAY_MaxX)

	def get_Array_BVCLAY_MaxY(self):
		return self._inArrayY[28]

	Array_BVCLAY_MaxY = property(fget=get_Array_BVCLAY_MaxY)

	def SD(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[29],29, index, True)

	def Array_SD(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[29],29, index, xVal, yVal, True)

	def SD_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[29], index)

	def Array_SD_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[29], index, xVal, yVal)

	def get_SD_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[29], 1)

	SD_Name = property(fget=get_SD_Name)

	def get_SD_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[29], 2)

	SD_Units = property(fget=get_SD_Units)

	def get_SD_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[29], 3)

	SD_Comments = property(fget=get_SD_Comments)

	def Save_SD_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[29], 3, str(newValue))

	def Get_SD_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[29], attributeName)

	def Set_SD_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[29], attributeName, str(newValue))

	def get_Array_SD_MaxX(self):
		return self._inArrayX[29]

	Array_SD_MaxX = property(fget=get_Array_SD_MaxX)

	def get_Array_SD_MaxY(self):
		return self._inArrayY[29]

	Array_SD_MaxY = property(fget=get_Array_SD_MaxY)

	def RESV(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[30],30, index, True)

	def Array_RESV(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[30],30, index, xVal, yVal, True)

	def RESV_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[30], index)

	def Array_RESV_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[30], index, xVal, yVal)

	def get_RESV_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[30], 1)

	RESV_Name = property(fget=get_RESV_Name)

	def get_RESV_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[30], 2)

	RESV_Units = property(fget=get_RESV_Units)

	def get_RESV_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[30], 3)

	RESV_Comments = property(fget=get_RESV_Comments)

	def Save_RESV_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[30], 3, str(newValue))

	def Get_RESV_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[30], attributeName)

	def Set_RESV_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[30], attributeName, str(newValue))

	def get_Array_RESV_MaxX(self):
		return self._inArrayX[30]

	Array_RESV_MaxX = property(fget=get_Array_RESV_MaxX)

	def get_Array_RESV_MaxY(self):
		return self._inArrayY[30]

	Array_RESV_MaxY = property(fget=get_Array_RESV_MaxY)

	def PAY(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[31],31, index, True)

	def Array_PAY(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[31],31, index, xVal, yVal, True)

	def PAY_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[31], index)

	def Array_PAY_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[31], index, xVal, yVal)

	def get_PAY_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[31], 1)

	PAY_Name = property(fget=get_PAY_Name)

	def get_PAY_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[31], 2)

	PAY_Units = property(fget=get_PAY_Units)

	def get_PAY_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[31], 3)

	PAY_Comments = property(fget=get_PAY_Comments)

	def Save_PAY_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[31], 3, str(newValue))

	def Get_PAY_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[31], attributeName)

	def Set_PAY_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[31], attributeName, str(newValue))

	def get_Array_PAY_MaxX(self):
		return self._inArrayX[31]

	Array_PAY_MaxX = property(fget=get_Array_PAY_MaxX)

	def get_Array_PAY_MaxY(self):
		return self._inArrayY[31]

	Array_PAY_MaxY = property(fget=get_Array_PAY_MaxY)

	def BADHOLE(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[32],32, index, True)

	def Array_BADHOLE(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[32],32, index, xVal, yVal, True)

	def BADHOLE_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[32], index)

	def Array_BADHOLE_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[32], index, xVal, yVal)

	def get_BADHOLE_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[32], 1)

	BADHOLE_Name = property(fget=get_BADHOLE_Name)

	def get_BADHOLE_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[32], 2)

	BADHOLE_Units = property(fget=get_BADHOLE_Units)

	def get_BADHOLE_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[32], 3)

	BADHOLE_Comments = property(fget=get_BADHOLE_Comments)

	def Save_BADHOLE_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[32], 3, str(newValue))

	def Get_BADHOLE_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[32], attributeName)

	def Set_BADHOLE_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[32], attributeName, str(newValue))

	def Save_BADHOLE(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[32], index, float(value))

	def Save_Array_BADHOLE(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[32], index, float(value), xVal, yVal)

	def Save_BADHOLE_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[32], index, str(value))

	def Save_Array_BADHOLE_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[32], index, str(value), xVal, yVal)

	def get_Array_BADHOLE_MaxX(self):
		return self._inArrayX[32]

	Array_BADHOLE_MaxX = property(fget=get_Array_BADHOLE_MaxX)

	def get_Array_BADHOLE_MaxY(self):
		return self._inArrayY[32]

	Array_BADHOLE_MaxY = property(fget=get_Array_BADHOLE_MaxY)

	def Save_VSH(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, float(value))

	def Save_Array_VSH(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, float(value), xVal, yVal)

	def Save_VSH_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, str(value))

	def Save_Array_VSH_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, str(value), xVal, yVal)

	def Save_VSH_ND(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value))

	def Save_Array_VSH_ND(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value), xVal, yVal)

	def Save_VSH_ND_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value))

	def Save_Array_VSH_ND_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value), xVal, yVal)

	def Save_VSH_GR(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, float(value))

	def Save_Array_VSH_GR(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, float(value), xVal, yVal)

	def Save_VSH_GR_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, str(value))

	def Save_Array_VSH_GR_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, str(value), xVal, yVal)

	def Save_VSH_RES(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, float(value))

	def Save_Array_VSH_RES(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, float(value), xVal, yVal)

	def Save_VSH_RES_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, str(value))

	def Save_Array_VSH_RES_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, str(value), xVal, yVal)

	def Save_VSH_SP(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, float(value))

	def Save_Array_VSH_SP(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, float(value), xVal, yVal)

	def Save_VSH_SP_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, str(value))

	def Save_Array_VSH_SP_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, str(value), xVal, yVal)

	def Save_PHIT(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[5], index, float(value))

	def Save_Array_PHIT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[5], index, float(value), xVal, yVal)

	def Save_PHIT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[5], index, str(value))

	def Save_Array_PHIT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[5], index, str(value), xVal, yVal)

	def Save_PHIE(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[6], index, float(value))

	def Save_Array_PHIE(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[6], index, float(value), xVal, yVal)

	def Save_PHIE_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[6], index, str(value))

	def Save_Array_PHIE_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[6], index, str(value), xVal, yVal)

	def Save_PHID_A(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[7], index, float(value))

	def Save_Array_PHID_A(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[7], index, float(value), xVal, yVal)

	def Save_PHID_A_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[7], index, str(value))

	def Save_Array_PHID_A_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[7], index, str(value), xVal, yVal)

	def Save_PHIT_HC(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[8], index, float(value))

	def Save_Array_PHIT_HC(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[8], index, float(value), xVal, yVal)

	def Save_PHIT_HC_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[8], index, str(value))

	def Save_Array_PHIT_HC_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[8], index, str(value), xVal, yVal)

	def Save_PHIA(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[9], index, float(value))

	def Save_Array_PHIA(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[9], index, float(value), xVal, yVal)

	def Save_PHIA_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[9], index, str(value))

	def Save_Array_PHIA_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[9], index, str(value), xVal, yVal)

	def Save_SWT(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[10], index, float(value))

	def Save_Array_SWT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[10], index, float(value), xVal, yVal)

	def Save_SWT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[10], index, str(value))

	def Save_Array_SWT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[10], index, str(value), xVal, yVal)

	def Save_SWE(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[11], index, float(value))

	def Save_Array_SWE(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[11], index, float(value), xVal, yVal)

	def Save_SWE_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[11], index, str(value))

	def Save_Array_SWE_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[11], index, str(value), xVal, yVal)

	def Save_SXOT(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[12], index, float(value))

	def Save_Array_SXOT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[12], index, float(value), xVal, yVal)

	def Save_SXOT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[12], index, str(value))

	def Save_Array_SXOT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[12], index, str(value), xVal, yVal)

	def Save_SXOE(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[13], index, float(value))

	def Save_Array_SXOE(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[13], index, float(value), xVal, yVal)

	def Save_SXOE_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[13], index, str(value))

	def Save_Array_SXOE_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[13], index, str(value), xVal, yVal)

	def Save_RHOGM(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[14], index, float(value))

	def Save_Array_RHOGM(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[14], index, float(value), xVal, yVal)

	def Save_RHOGM_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[14], index, str(value))

	def Save_Array_RHOGM_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[14], index, str(value), xVal, yVal)

	def Save_RHOGC(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[15], index, float(value))

	def Save_Array_RHOGC(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[15], index, float(value), xVal, yVal)

	def Save_RHOGC_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[15], index, str(value))

	def Save_Array_RHOGC_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[15], index, str(value), xVal, yVal)

	def Save_BVW(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[16], index, float(value))

	def Save_Array_BVW(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[16], index, float(value), xVal, yVal)

	def Save_BVW_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[16], index, str(value))

	def Save_Array_BVW_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[16], index, str(value), xVal, yVal)

	def Save_BVWE(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[17], index, float(value))

	def Save_Array_BVWE(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[17], index, float(value), xVal, yVal)

	def Save_BVWE_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[17], index, str(value))

	def Save_Array_BVWE_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[17], index, str(value), xVal, yVal)

	def Save_BVSH(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[18], index, float(value))

	def Save_Array_BVSH(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[18], index, float(value), xVal, yVal)

	def Save_BVSH_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[18], index, str(value))

	def Save_Array_BVSH_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[18], index, str(value), xVal, yVal)

	def Save_BVHC(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[19], index, float(value))

	def Save_Array_BVHC(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[19], index, float(value), xVal, yVal)

	def Save_BVHC_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[19], index, str(value))

	def Save_Array_BVHC_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[19], index, str(value), xVal, yVal)

	def Save_BVSAND(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[20], index, float(value))

	def Save_Array_BVSAND(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[20], index, float(value), xVal, yVal)

	def Save_BVSAND_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[20], index, str(value))

	def Save_Array_BVSAND_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[20], index, str(value), xVal, yVal)

	def Save_BVSILT(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[21], index, float(value))

	def Save_Array_BVSILT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[21], index, float(value), xVal, yVal)

	def Save_BVSILT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[21], index, str(value))

	def Save_Array_BVSILT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[21], index, str(value), xVal, yVal)

	def Save_BVLIM(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[22], index, float(value))

	def Save_Array_BVLIM(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[22], index, float(value), xVal, yVal)

	def Save_BVLIM_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[22], index, str(value))

	def Save_Array_BVLIM_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[22], index, str(value), xVal, yVal)

	def Save_BVCLAY(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[23], index, float(value))

	def Save_Array_BVCLAY(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[23], index, float(value), xVal, yVal)

	def Save_BVCLAY_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[23], index, str(value))

	def Save_Array_BVCLAY_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[23], index, str(value), xVal, yVal)

	def Save_SALINITY_SP(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[24], index, float(value))

	def Save_Array_SALINITY_SP(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[24], index, float(value), xVal, yVal)

	def Save_SALINITY_SP_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[24], index, str(value))

	def Save_Array_SALINITY_SP_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[24], index, str(value), xVal, yVal)

	def Save_RW_SP(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[25], index, float(value))

	def Save_Array_RW_SP(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[25], index, float(value), xVal, yVal)

	def Save_RW_SP_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[25], index, str(value))

	def Save_Array_RW_SP_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[25], index, str(value), xVal, yVal)

	def Save_SALINITY(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[26], index, float(value))

	def Save_Array_SALINITY(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[26], index, float(value), xVal, yVal)

	def Save_SALINITY_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[26], index, str(value))

	def Save_Array_SALINITY_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[26], index, str(value), xVal, yVal)

	def Save_RW(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[27], index, float(value))

	def Save_Array_RW(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[27], index, float(value), xVal, yVal)

	def Save_RW_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[27], index, str(value))

	def Save_Array_RW_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[27], index, str(value), xVal, yVal)

	def Save_PHIX(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[28], index, float(value))

	def Save_Array_PHIX(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[28], index, float(value), xVal, yVal)

	def Save_PHIX_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[28], index, str(value))

	def Save_Array_PHIX_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[28], index, str(value), xVal, yVal)

	def Save_SD(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[29], index, float(value))

	def Save_Array_SD(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[29], index, float(value), xVal, yVal)

	def Save_SD_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[29], index, str(value))

	def Save_Array_SD_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[29], index, str(value), xVal, yVal)

	def Save_RESV(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[30], index, float(value))

	def Save_Array_RESV(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[30], index, float(value), xVal, yVal)

	def Save_RESV_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[30], index, str(value))

	def Save_Array_RESV_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[30], index, str(value), xVal, yVal)

	def Save_PAY(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[31], index, float(value))

	def Save_Array_PAY(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[31], index, float(value), xVal, yVal)

	def Save_PAY_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[31], index, str(value))

	def Save_Array_PAY_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[31], index, str(value), xVal, yVal)

