# /***********************************************/
#  * File dynamically created from IP: 08/24/2022 15:10:05
#  * DO NOT MANUALLY EDIT
# /***********************************************/

class Methods:
	def __init__(self):
		self._FIRST_AVAILABLE_LOG_RUN = -1
		self._LAST_AVAILABLE_LOG_RUN = -2

	def Depth(self, index):
		return self._IPProxy.GetCurveData(1, index)

	def RHOB(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[0],0, index, True)

	def Array_RHOB(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[0],0, index, xVal, yVal, True)

	def RHOB_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[0], index)

	def Array_RHOB_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[0], index, xVal, yVal)

	def get_RHOB_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 1)

	RHOB_Name = property(fget=get_RHOB_Name)

	def get_RHOB_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 2)

	RHOB_Units = property(fget=get_RHOB_Units)

	def get_RHOB_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 3)

	RHOB_Comments = property(fget=get_RHOB_Comments)

	def Save_RHOB_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[0], 3, str(newValue))

	def Get_RHOB_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[0], attributeName)

	def Set_RHOB_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[0], attributeName, str(newValue))

	def Save_RHOB(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[0], index, float(value))

	def Save_Array_RHOB(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[0], index, float(value), xVal, yVal)

	def Save_RHOB_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[0], index, str(value))

	def Save_Array_RHOB_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[0], index, str(value), xVal, yVal)

	def get_Array_RHOB_MaxX(self):
		return self._inArrayX[0]

	Array_RHOB_MaxX = property(fget=get_Array_RHOB_MaxX)

	def get_Array_RHOB_MaxY(self):
		return self._inArrayY[0]

	Array_RHOB_MaxY = property(fget=get_Array_RHOB_MaxY)

	def DT(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[1],1, index, True)

	def Array_DT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[1],1, index, xVal, yVal, True)

	def DT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[1], index)

	def Array_DT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[1], index, xVal, yVal)

	def get_DT_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 1)

	DT_Name = property(fget=get_DT_Name)

	def get_DT_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 2)

	DT_Units = property(fget=get_DT_Units)

	def get_DT_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 3)

	DT_Comments = property(fget=get_DT_Comments)

	def Save_DT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[1], 3, str(newValue))

	def Get_DT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[1], attributeName)

	def Set_DT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[1], attributeName, str(newValue))

	def Save_DT(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[1], index, float(value))

	def Save_Array_DT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[1], index, float(value), xVal, yVal)

	def Save_DT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[1], index, str(value))

	def Save_Array_DT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[1], index, str(value), xVal, yVal)

	def get_Array_DT_MaxX(self):
		return self._inArrayX[1]

	Array_DT_MaxX = property(fget=get_Array_DT_MaxX)

	def get_Array_DT_MaxY(self):
		return self._inArrayY[1]

	Array_DT_MaxY = property(fget=get_Array_DT_MaxY)

	def RT(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[2],2, index, True)

	def Array_RT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[2],2, index, xVal, yVal, True)

	def RT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[2], index)

	def Array_RT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[2], index, xVal, yVal)

	def get_RT_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 1)

	RT_Name = property(fget=get_RT_Name)

	def get_RT_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 2)

	RT_Units = property(fget=get_RT_Units)

	def get_RT_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 3)

	RT_Comments = property(fget=get_RT_Comments)

	def Save_RT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[2], 3, str(newValue))

	def Get_RT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[2], attributeName)

	def Set_RT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[2], attributeName, str(newValue))

	def Save_RT(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[2], index, float(value))

	def Save_Array_RT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[2], index, float(value), xVal, yVal)

	def Save_RT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[2], index, str(value))

	def Save_Array_RT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[2], index, str(value), xVal, yVal)

	def get_Array_RT_MaxX(self):
		return self._inArrayX[2]

	Array_RT_MaxX = property(fget=get_Array_RT_MaxX)

	def get_Array_RT_MaxY(self):
		return self._inArrayY[2]

	Array_RT_MaxY = property(fget=get_Array_RT_MaxY)

	def NPHI(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[3],3, index, True)

	def Array_NPHI(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[3],3, index, xVal, yVal, True)

	def NPHI_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[3], index)

	def Array_NPHI_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[3], index, xVal, yVal)

	def get_NPHI_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 1)

	NPHI_Name = property(fget=get_NPHI_Name)

	def get_NPHI_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 2)

	NPHI_Units = property(fget=get_NPHI_Units)

	def get_NPHI_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 3)

	NPHI_Comments = property(fget=get_NPHI_Comments)

	def Save_NPHI_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[3], 3, str(newValue))

	def Get_NPHI_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[3], attributeName)

	def Set_NPHI_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[3], attributeName, str(newValue))

	def Save_NPHI(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[3], index, float(value))

	def Save_Array_NPHI(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[3], index, float(value), xVal, yVal)

	def Save_NPHI_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[3], index, str(value))

	def Save_Array_NPHI_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[3], index, str(value), xVal, yVal)

	def get_Array_NPHI_MaxX(self):
		return self._inArrayX[3]

	Array_NPHI_MaxX = property(fget=get_Array_NPHI_MaxX)

	def get_Array_NPHI_MaxY(self):
		return self._inArrayY[3]

	Array_NPHI_MaxY = property(fget=get_Array_NPHI_MaxY)

	def NPHIWSH_L(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[4],4, index, True)

	def Array_NPHIWSH_L(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[4],4, index, xVal, yVal, True)

	def NPHIWSH_L_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[4], index)

	def Array_NPHIWSH_L_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[4], index, xVal, yVal)

	def get_NPHIWSH_L_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 1)

	NPHIWSH_L_Name = property(fget=get_NPHIWSH_L_Name)

	def get_NPHIWSH_L_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 2)

	NPHIWSH_L_Units = property(fget=get_NPHIWSH_L_Units)

	def get_NPHIWSH_L_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 3)

	NPHIWSH_L_Comments = property(fget=get_NPHIWSH_L_Comments)

	def Save_NPHIWSH_L_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[4], 3, str(newValue))

	def Get_NPHIWSH_L_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[4], attributeName)

	def Set_NPHIWSH_L_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[4], attributeName, str(newValue))

	def Save_NPHIWSH_L(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[4], index, float(value))

	def Save_Array_NPHIWSH_L(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[4], index, float(value), xVal, yVal)

	def Save_NPHIWSH_L_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[4], index, str(value))

	def Save_Array_NPHIWSH_L_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[4], index, str(value), xVal, yVal)

	def get_Array_NPHIWSH_L_MaxX(self):
		return self._inArrayX[4]

	Array_NPHIWSH_L_MaxX = property(fget=get_Array_NPHIWSH_L_MaxX)

	def get_Array_NPHIWSH_L_MaxY(self):
		return self._inArrayY[4]

	Array_NPHIWSH_L_MaxY = property(fget=get_Array_NPHIWSH_L_MaxY)

	def RHOBWSH_L(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[5],5, index, True)

	def Array_RHOBWSH_L(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[5],5, index, xVal, yVal, True)

	def RHOBWSH_L_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[5], index)

	def Array_RHOBWSH_L_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[5], index, xVal, yVal)

	def get_RHOBWSH_L_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 1)

	RHOBWSH_L_Name = property(fget=get_RHOBWSH_L_Name)

	def get_RHOBWSH_L_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 2)

	RHOBWSH_L_Units = property(fget=get_RHOBWSH_L_Units)

	def get_RHOBWSH_L_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 3)

	RHOBWSH_L_Comments = property(fget=get_RHOBWSH_L_Comments)

	def Save_RHOBWSH_L_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[5], 3, str(newValue))

	def Get_RHOBWSH_L_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[5], attributeName)

	def Set_RHOBWSH_L_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[5], attributeName, str(newValue))

	def Save_RHOBWSH_L(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[5], index, float(value))

	def Save_Array_RHOBWSH_L(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[5], index, float(value), xVal, yVal)

	def Save_RHOBWSH_L_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[5], index, str(value))

	def Save_Array_RHOBWSH_L_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[5], index, str(value), xVal, yVal)

	def get_Array_RHOBWSH_L_MaxX(self):
		return self._inArrayX[5]

	Array_RHOBWSH_L_MaxX = property(fget=get_Array_RHOBWSH_L_MaxX)

	def get_Array_RHOBWSH_L_MaxY(self):
		return self._inArrayY[5]

	Array_RHOBWSH_L_MaxY = property(fget=get_Array_RHOBWSH_L_MaxY)

	def FTEMP_L(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[6],6, index, True)

	def Array_FTEMP_L(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[6],6, index, xVal, yVal, True)

	def FTEMP_L_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[6], index)

	def Array_FTEMP_L_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[6], index, xVal, yVal)

	def get_FTEMP_L_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[6], 1)

	FTEMP_L_Name = property(fget=get_FTEMP_L_Name)

	def get_FTEMP_L_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[6], 2)

	FTEMP_L_Units = property(fget=get_FTEMP_L_Units)

	def get_FTEMP_L_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[6], 3)

	FTEMP_L_Comments = property(fget=get_FTEMP_L_Comments)

	def Save_FTEMP_L_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[6], 3, str(newValue))

	def Get_FTEMP_L_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[6], attributeName)

	def Set_FTEMP_L_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[6], attributeName, str(newValue))

	def Save_FTEMP_L(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[6], index, float(value))

	def Save_Array_FTEMP_L(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[6], index, float(value), xVal, yVal)

	def Save_FTEMP_L_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[6], index, str(value))

	def Save_Array_FTEMP_L_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[6], index, str(value), xVal, yVal)

	def get_Array_FTEMP_L_MaxX(self):
		return self._inArrayX[6]

	Array_FTEMP_L_MaxX = property(fget=get_Array_FTEMP_L_MaxX)

	def get_Array_FTEMP_L_MaxY(self):
		return self._inArrayY[6]

	Array_FTEMP_L_MaxY = property(fget=get_Array_FTEMP_L_MaxY)

	def FLAG_COAL(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[7],7, index, True)

	def Array_FLAG_COAL(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[7],7, index, xVal, yVal, True)

	def FLAG_COAL_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[7], index)

	def Array_FLAG_COAL_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[7], index, xVal, yVal)

	def get_FLAG_COAL_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[7], 1)

	FLAG_COAL_Name = property(fget=get_FLAG_COAL_Name)

	def get_FLAG_COAL_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[7], 2)

	FLAG_COAL_Units = property(fget=get_FLAG_COAL_Units)

	def get_FLAG_COAL_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[7], 3)

	FLAG_COAL_Comments = property(fget=get_FLAG_COAL_Comments)

	def Save_FLAG_COAL_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[7], 3, str(newValue))

	def Get_FLAG_COAL_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[7], attributeName)

	def Set_FLAG_COAL_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[7], attributeName, str(newValue))

	def Save_FLAG_COAL(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[7], index, float(value))

	def Save_Array_FLAG_COAL(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[7], index, float(value), xVal, yVal)

	def Save_FLAG_COAL_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[7], index, str(value))

	def Save_Array_FLAG_COAL_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[7], index, str(value), xVal, yVal)

	def get_Array_FLAG_COAL_MaxX(self):
		return self._inArrayX[7]

	Array_FLAG_COAL_MaxX = property(fget=get_Array_FLAG_COAL_MaxX)

	def get_Array_FLAG_COAL_MaxY(self):
		return self._inArrayY[7]

	Array_FLAG_COAL_MaxY = property(fget=get_Array_FLAG_COAL_MaxY)

	def FLAG_VOLC(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[8],8, index, True)

	def Array_FLAG_VOLC(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[8],8, index, xVal, yVal, True)

	def FLAG_VOLC_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[8], index)

	def Array_FLAG_VOLC_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[8], index, xVal, yVal)

	def get_FLAG_VOLC_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[8], 1)

	FLAG_VOLC_Name = property(fget=get_FLAG_VOLC_Name)

	def get_FLAG_VOLC_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[8], 2)

	FLAG_VOLC_Units = property(fget=get_FLAG_VOLC_Units)

	def get_FLAG_VOLC_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[8], 3)

	FLAG_VOLC_Comments = property(fget=get_FLAG_VOLC_Comments)

	def Save_FLAG_VOLC_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[8], 3, str(newValue))

	def Get_FLAG_VOLC_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[8], attributeName)

	def Set_FLAG_VOLC_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[8], attributeName, str(newValue))

	def Save_FLAG_VOLC(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[8], index, float(value))

	def Save_Array_FLAG_VOLC(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[8], index, float(value), xVal, yVal)

	def Save_FLAG_VOLC_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[8], index, str(value))

	def Save_Array_FLAG_VOLC_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[8], index, str(value), xVal, yVal)

	def get_Array_FLAG_VOLC_MaxX(self):
		return self._inArrayX[8]

	Array_FLAG_VOLC_MaxX = property(fget=get_Array_FLAG_VOLC_MaxX)

	def get_Array_FLAG_VOLC_MaxY(self):
		return self._inArrayY[8]

	Array_FLAG_VOLC_MaxY = property(fget=get_Array_FLAG_VOLC_MaxY)

	def SPB_L(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[9],9, index, True)

	def Array_SPB_L(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[9],9, index, xVal, yVal, True)

	def SPB_L_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[9], index)

	def Array_SPB_L_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[9], index, xVal, yVal)

	def get_SPB_L_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[9], 1)

	SPB_L_Name = property(fget=get_SPB_L_Name)

	def get_SPB_L_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[9], 2)

	SPB_L_Units = property(fget=get_SPB_L_Units)

	def get_SPB_L_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[9], 3)

	SPB_L_Comments = property(fget=get_SPB_L_Comments)

	def Save_SPB_L_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[9], 3, str(newValue))

	def Get_SPB_L_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[9], attributeName)

	def Set_SPB_L_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[9], attributeName, str(newValue))

	def Save_SPB_L(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[9], index, float(value))

	def Save_Array_SPB_L(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[9], index, float(value), xVal, yVal)

	def Save_SPB_L_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[9], index, str(value))

	def Save_Array_SPB_L_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[9], index, str(value), xVal, yVal)

	def get_Array_SPB_L_MaxX(self):
		return self._inArrayX[9]

	Array_SPB_L_MaxX = property(fget=get_Array_SPB_L_MaxX)

	def get_Array_SPB_L_MaxY(self):
		return self._inArrayY[9]

	Array_SPB_L_MaxY = property(fget=get_Array_SPB_L_MaxY)

	def SP(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[10],10, index, True)

	def Array_SP(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[10],10, index, xVal, yVal, True)

	def SP_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[10], index)

	def Array_SP_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[10], index, xVal, yVal)

	def get_SP_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[10], 1)

	SP_Name = property(fget=get_SP_Name)

	def get_SP_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[10], 2)

	SP_Units = property(fget=get_SP_Units)

	def get_SP_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[10], 3)

	SP_Comments = property(fget=get_SP_Comments)

	def Save_SP_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[10], 3, str(newValue))

	def Get_SP_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[10], attributeName)

	def Set_SP_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[10], attributeName, str(newValue))

	def Save_SP(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[10], index, float(value))

	def Save_Array_SP(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[10], index, float(value), xVal, yVal)

	def Save_SP_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[10], index, str(value))

	def Save_Array_SP_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[10], index, str(value), xVal, yVal)

	def get_Array_SP_MaxX(self):
		return self._inArrayX[10]

	Array_SP_MaxX = property(fget=get_Array_SP_MaxX)

	def get_Array_SP_MaxY(self):
		return self._inArrayY[10]

	Array_SP_MaxY = property(fget=get_Array_SP_MaxY)

	def Save_RW_SP(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, float(value))

	def Save_Array_RW_SP(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, float(value), xVal, yVal)

	def Save_RW_SP_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, str(value))

	def Save_Array_RW_SP_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, str(value), xVal, yVal)

	def RW_SP(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[0], index)

	def Array_RW_SP(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[0], index, xVal, yVal)

	def RW_SP_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[0], index)

	def Array_RW_SP_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[0], index, xVal, yVal)

	def get_RW_SP_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 1)

	RW_SP_Name = property(fget=get_RW_SP_Name)

	def get_RW_SP_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 2)

	RW_SP_Units = property(fget=get_RW_SP_Units)

	def get_RW_SP_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 3)

	RW_SP_Comments = property(fget=get_RW_SP_Comments)

	def Save_RW_SP_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[0], 3, str(newValue))

	def get_Array_RW_SP_MaxX(self):
		return self._outArrayX[0]

	Array_RW_SP_MaxX = property(fget=get_Array_RW_SP_MaxX)

	def get_Array_RW_SP_MaxY(self):
		return self._outArrayY[0]

	Array_RW_SP_MaxY = property(fget=get_Array_RW_SP_MaxY)

	def Get_RW_SP_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[0], attributeName)

	def Set_RW_SP_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[0], attributeName, str(newValue))

	def Save_SALINITY_SP(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value))

	def Save_Array_SALINITY_SP(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value), xVal, yVal)

	def Save_SALINITY_SP_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value))

	def Save_Array_SALINITY_SP_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value), xVal, yVal)

	def SALINITY_SP(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[1], index)

	def Array_SALINITY_SP(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[1], index, xVal, yVal)

	def SALINITY_SP_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[1], index)

	def Array_SALINITY_SP_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[1], index, xVal, yVal)

	def get_SALINITY_SP_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 1)

	SALINITY_SP_Name = property(fget=get_SALINITY_SP_Name)

	def get_SALINITY_SP_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 2)

	SALINITY_SP_Units = property(fget=get_SALINITY_SP_Units)

	def get_SALINITY_SP_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 3)

	SALINITY_SP_Comments = property(fget=get_SALINITY_SP_Comments)

	def Save_SALINITY_SP_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[1], 3, str(newValue))

	def get_Array_SALINITY_SP_MaxX(self):
		return self._outArrayX[1]

	Array_SALINITY_SP_MaxX = property(fget=get_Array_SALINITY_SP_MaxX)

	def get_Array_SALINITY_SP_MaxY(self):
		return self._outArrayY[1]

	Array_SALINITY_SP_MaxY = property(fget=get_Array_SALINITY_SP_MaxY)

	def Get_SALINITY_SP_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[1], attributeName)

	def Set_SALINITY_SP_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[1], attributeName, str(newValue))

	def Save_PHIX(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, float(value))

	def Save_Array_PHIX(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, float(value), xVal, yVal)

	def Save_PHIX_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, str(value))

	def Save_Array_PHIX_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, str(value), xVal, yVal)

	def PHIX(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[2], index)

	def Array_PHIX(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[2], index, xVal, yVal)

	def PHIX_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[2], index)

	def Array_PHIX_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[2], index, xVal, yVal)

	def get_PHIX_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 1)

	PHIX_Name = property(fget=get_PHIX_Name)

	def get_PHIX_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 2)

	PHIX_Units = property(fget=get_PHIX_Units)

	def get_PHIX_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 3)

	PHIX_Comments = property(fget=get_PHIX_Comments)

	def Save_PHIX_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[2], 3, str(newValue))

	def get_Array_PHIX_MaxX(self):
		return self._outArrayX[2]

	Array_PHIX_MaxX = property(fget=get_Array_PHIX_MaxX)

	def get_Array_PHIX_MaxY(self):
		return self._outArrayY[2]

	Array_PHIX_MaxY = property(fget=get_Array_PHIX_MaxY)

	def Get_PHIX_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[2], attributeName)

	def Set_PHIX_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[2], attributeName, str(newValue))

	def Save_PHIA(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, float(value))

	def Save_Array_PHIA(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, float(value), xVal, yVal)

	def Save_PHIA_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, str(value))

	def Save_Array_PHIA_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, str(value), xVal, yVal)

	def PHIA(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[3], index)

	def Array_PHIA(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[3], index, xVal, yVal)

	def PHIA_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[3], index)

	def Array_PHIA_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[3], index, xVal, yVal)

	def get_PHIA_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 1)

	PHIA_Name = property(fget=get_PHIA_Name)

	def get_PHIA_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 2)

	PHIA_Units = property(fget=get_PHIA_Units)

	def get_PHIA_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 3)

	PHIA_Comments = property(fget=get_PHIA_Comments)

	def Save_PHIA_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[3], 3, str(newValue))

	def get_Array_PHIA_MaxX(self):
		return self._outArrayX[3]

	Array_PHIA_MaxX = property(fget=get_Array_PHIA_MaxX)

	def get_Array_PHIA_MaxY(self):
		return self._outArrayY[3]

	Array_PHIA_MaxY = property(fget=get_Array_PHIA_MaxY)

	def Get_PHIA_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[3], attributeName)

	def Set_PHIA_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[3], attributeName, str(newValue))

	def Save_PHIT_HC(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, float(value))

	def Save_Array_PHIT_HC(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, float(value), xVal, yVal)

	def Save_PHIT_HC_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, str(value))

	def Save_Array_PHIT_HC_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, str(value), xVal, yVal)

	def PHIT_HC(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[4], index)

	def Array_PHIT_HC(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[4], index, xVal, yVal)

	def PHIT_HC_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[4], index)

	def Array_PHIT_HC_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[4], index, xVal, yVal)

	def get_PHIT_HC_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 1)

	PHIT_HC_Name = property(fget=get_PHIT_HC_Name)

	def get_PHIT_HC_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 2)

	PHIT_HC_Units = property(fget=get_PHIT_HC_Units)

	def get_PHIT_HC_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 3)

	PHIT_HC_Comments = property(fget=get_PHIT_HC_Comments)

	def Save_PHIT_HC_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[4], 3, str(newValue))

	def get_Array_PHIT_HC_MaxX(self):
		return self._outArrayX[4]

	Array_PHIT_HC_MaxX = property(fget=get_Array_PHIT_HC_MaxX)

	def get_Array_PHIT_HC_MaxY(self):
		return self._outArrayY[4]

	Array_PHIT_HC_MaxY = property(fget=get_Array_PHIT_HC_MaxY)

	def Get_PHIT_HC_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[4], attributeName)

	def Set_PHIT_HC_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[4], attributeName, str(newValue))

	def Save_PHIT(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[5], index, float(value))

	def Save_Array_PHIT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[5], index, float(value), xVal, yVal)

	def Save_PHIT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[5], index, str(value))

	def Save_Array_PHIT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[5], index, str(value), xVal, yVal)

	def PHIT(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[5], index)

	def Array_PHIT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[5], index, xVal, yVal)

	def PHIT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[5], index)

	def Array_PHIT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[5], index, xVal, yVal)

	def get_PHIT_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 1)

	PHIT_Name = property(fget=get_PHIT_Name)

	def get_PHIT_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 2)

	PHIT_Units = property(fget=get_PHIT_Units)

	def get_PHIT_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 3)

	PHIT_Comments = property(fget=get_PHIT_Comments)

	def Save_PHIT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[5], 3, str(newValue))

	def get_Array_PHIT_MaxX(self):
		return self._outArrayX[5]

	Array_PHIT_MaxX = property(fget=get_Array_PHIT_MaxX)

	def get_Array_PHIT_MaxY(self):
		return self._outArrayY[5]

	Array_PHIT_MaxY = property(fget=get_Array_PHIT_MaxY)

	def Get_PHIT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[5], attributeName)

	def Set_PHIT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[5], attributeName, str(newValue))

	def Save_PHID(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[6], index, float(value))

	def Save_Array_PHID(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[6], index, float(value), xVal, yVal)

	def Save_PHID_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[6], index, str(value))

	def Save_Array_PHID_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[6], index, str(value), xVal, yVal)

	def PHID(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[6], index)

	def Array_PHID(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[6], index, xVal, yVal)

	def PHID_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[6], index)

	def Array_PHID_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[6], index, xVal, yVal)

	def get_PHID_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 1)

	PHID_Name = property(fget=get_PHID_Name)

	def get_PHID_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 2)

	PHID_Units = property(fget=get_PHID_Units)

	def get_PHID_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 3)

	PHID_Comments = property(fget=get_PHID_Comments)

	def Save_PHID_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[6], 3, str(newValue))

	def get_Array_PHID_MaxX(self):
		return self._outArrayX[6]

	Array_PHID_MaxX = property(fget=get_Array_PHID_MaxX)

	def get_Array_PHID_MaxY(self):
		return self._outArrayY[6]

	Array_PHID_MaxY = property(fget=get_Array_PHID_MaxY)

	def Get_PHID_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[6], attributeName)

	def Set_PHID_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[6], attributeName, str(newValue))

	def Save_CWA(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[7], index, float(value))

	def Save_Array_CWA(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[7], index, float(value), xVal, yVal)

	def Save_CWA_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[7], index, str(value))

	def Save_Array_CWA_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[7], index, str(value), xVal, yVal)

	def CWA(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[7], index)

	def Array_CWA(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[7], index, xVal, yVal)

	def CWA_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[7], index)

	def Array_CWA_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[7], index, xVal, yVal)

	def get_CWA_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 1)

	CWA_Name = property(fget=get_CWA_Name)

	def get_CWA_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 2)

	CWA_Units = property(fget=get_CWA_Units)

	def get_CWA_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 3)

	CWA_Comments = property(fget=get_CWA_Comments)

	def Save_CWA_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[7], 3, str(newValue))

	def get_Array_CWA_MaxX(self):
		return self._outArrayX[7]

	Array_CWA_MaxX = property(fget=get_Array_CWA_MaxX)

	def get_Array_CWA_MaxY(self):
		return self._outArrayY[7]

	Array_CWA_MaxY = property(fget=get_Array_CWA_MaxY)

	def Get_CWA_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[7], attributeName)

	def Set_CWA_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[7], attributeName, str(newValue))

	def Save_RWA(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[8], index, float(value))

	def Save_Array_RWA(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[8], index, float(value), xVal, yVal)

	def Save_RWA_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[8], index, str(value))

	def Save_Array_RWA_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[8], index, str(value), xVal, yVal)

	def RWA(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[8], index)

	def Array_RWA(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[8], index, xVal, yVal)

	def RWA_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[8], index)

	def Array_RWA_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[8], index, xVal, yVal)

	def get_RWA_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 1)

	RWA_Name = property(fget=get_RWA_Name)

	def get_RWA_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 2)

	RWA_Units = property(fget=get_RWA_Units)

	def get_RWA_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 3)

	RWA_Comments = property(fget=get_RWA_Comments)

	def Save_RWA_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[8], 3, str(newValue))

	def get_Array_RWA_MaxX(self):
		return self._outArrayX[8]

	Array_RWA_MaxX = property(fget=get_Array_RWA_MaxX)

	def get_Array_RWA_MaxY(self):
		return self._outArrayY[8]

	Array_RWA_MaxY = property(fget=get_Array_RWA_MaxY)

	def Get_RWA_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[8], attributeName)

	def Set_RWA_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[8], attributeName, str(newValue))

	def Save_RHOGM(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[9], index, float(value))

	def Save_Array_RHOGM(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[9], index, float(value), xVal, yVal)

	def Save_RHOGM_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[9], index, str(value))

	def Save_Array_RHOGM_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[9], index, str(value), xVal, yVal)

	def RHOGM(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[9], index)

	def Array_RHOGM(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[9], index, xVal, yVal)

	def RHOGM_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[9], index)

	def Array_RHOGM_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[9], index, xVal, yVal)

	def get_RHOGM_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[9], 1)

	RHOGM_Name = property(fget=get_RHOGM_Name)

	def get_RHOGM_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[9], 2)

	RHOGM_Units = property(fget=get_RHOGM_Units)

	def get_RHOGM_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[9], 3)

	RHOGM_Comments = property(fget=get_RHOGM_Comments)

	def Save_RHOGM_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[9], 3, str(newValue))

	def get_Array_RHOGM_MaxX(self):
		return self._outArrayX[9]

	Array_RHOGM_MaxX = property(fget=get_Array_RHOGM_MaxX)

	def get_Array_RHOGM_MaxY(self):
		return self._outArrayY[9]

	Array_RHOGM_MaxY = property(fget=get_Array_RHOGM_MaxY)

	def Get_RHOGM_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[9], attributeName)

	def Set_RHOGM_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[9], attributeName, str(newValue))

	def Save_SALINITY(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[10], index, float(value))

	def Save_Array_SALINITY(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[10], index, float(value), xVal, yVal)

	def Save_SALINITY_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[10], index, str(value))

	def Save_Array_SALINITY_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[10], index, str(value), xVal, yVal)

	def SALINITY(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[10], index)

	def Array_SALINITY(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[10], index, xVal, yVal)

	def SALINITY_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[10], index)

	def Array_SALINITY_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[10], index, xVal, yVal)

	def get_SALINITY_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[10], 1)

	SALINITY_Name = property(fget=get_SALINITY_Name)

	def get_SALINITY_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[10], 2)

	SALINITY_Units = property(fget=get_SALINITY_Units)

	def get_SALINITY_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[10], 3)

	SALINITY_Comments = property(fget=get_SALINITY_Comments)

	def Save_SALINITY_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[10], 3, str(newValue))

	def get_Array_SALINITY_MaxX(self):
		return self._outArrayX[10]

	Array_SALINITY_MaxX = property(fget=get_Array_SALINITY_MaxX)

	def get_Array_SALINITY_MaxY(self):
		return self._outArrayY[10]

	Array_SALINITY_MaxY = property(fget=get_Array_SALINITY_MaxY)

	def Get_SALINITY_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[10], attributeName)

	def Set_SALINITY_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[10], attributeName, str(newValue))

	def RHOFL(self, index):
		if self._parCnIn[0] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[0], index)
		else:
			return self._inputParameters[0]

	def Save_RHOFL(self, index, value):
		if self._parCnIn[0] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[0], index, float(value))
		else:
			self._IPProxy.SetNumericParam(1, float(value))
			self._inputParameters[0] = float(value)

	def get_RHOFL_Name(self):
		if self._parCnIn[0] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[0], 1)
		else:
			return str(self._inputParameters[0])

	RHOFL_Name = property(fget=get_RHOFL_Name)

	def DTM(self, index):
		if self._parCnIn[1] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[1], index)
		else:
			return self._inputParameters[1]

	def Save_DTM(self, index, value):
		if self._parCnIn[1] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[1], index, float(value))
		else:
			self._IPProxy.SetNumericParam(2, float(value))
			self._inputParameters[1] = float(value)

	def get_DTM_Name(self):
		if self._parCnIn[1] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[1], 1)
		else:
			return str(self._inputParameters[1])

	DTM_Name = property(fget=get_DTM_Name)

	def DTF(self, index):
		if self._parCnIn[2] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[2], index)
		else:
			return self._inputParameters[2]

	def Save_DTF(self, index, value):
		if self._parCnIn[2] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[2], index, float(value))
		else:
			self._IPProxy.SetNumericParam(3, float(value))
			self._inputParameters[2] = float(value)

	def get_DTF_Name(self):
		if self._parCnIn[2] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[2], 1)
		else:
			return str(self._inputParameters[2])

	DTF_Name = property(fget=get_DTF_Name)

	def RHOBQ(self, index):
		if self._parCnIn[3] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[3], index)
		else:
			return self._inputParameters[3]

	def Save_RHOBQ(self, index, value):
		if self._parCnIn[3] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[3], index, float(value))
		else:
			self._IPProxy.SetNumericParam(4, float(value))
			self._inputParameters[3] = float(value)

	def get_RHOBQ_Name(self):
		if self._parCnIn[3] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[3], 1)
		else:
			return str(self._inputParameters[3])

	RHOBQ_Name = property(fget=get_RHOBQ_Name)

	def NPHIQ(self, index):
		if self._parCnIn[4] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[4], index)
		else:
			return self._inputParameters[4]

	def Save_NPHIQ(self, index, value):
		if self._parCnIn[4] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[4], index, float(value))
		else:
			self._IPProxy.SetNumericParam(5, float(value))
			self._inputParameters[4] = float(value)

	def get_NPHIQ_Name(self):
		if self._parCnIn[4] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[4], 1)
		else:
			return str(self._inputParameters[4])

	NPHIQ_Name = property(fget=get_NPHIQ_Name)

	def RHOBWSH_C(self, index):
		if self._parCnIn[5] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[5], index)
		else:
			return self._inputParameters[5]

	def Save_RHOBWSH_C(self, index, value):
		if self._parCnIn[5] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[5], index, float(value))
		else:
			self._IPProxy.SetNumericParam(6, float(value))
			self._inputParameters[5] = float(value)

	def get_RHOBWSH_C_Name(self):
		if self._parCnIn[5] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[5], 1)
		else:
			return str(self._inputParameters[5])

	RHOBWSH_C_Name = property(fget=get_RHOBWSH_C_Name)

	def NPHIWSH_C(self, index):
		if self._parCnIn[6] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[6], index)
		else:
			return self._inputParameters[6]

	def Save_NPHIWSH_C(self, index, value):
		if self._parCnIn[6] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[6], index, float(value))
		else:
			self._IPProxy.SetNumericParam(7, float(value))
			self._inputParameters[6] = float(value)

	def get_NPHIWSH_C_Name(self):
		if self._parCnIn[6] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[6], 1)
		else:
			return str(self._inputParameters[6])

	NPHIWSH_C_Name = property(fget=get_NPHIWSH_C_Name)

	def CLAY_FRACTION(self, index):
		if self._parCnIn[7] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[7], index)
		else:
			return self._inputParameters[7]

	def Save_CLAY_FRACTION(self, index, value):
		if self._parCnIn[7] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[7], index, float(value))
		else:
			self._IPProxy.SetNumericParam(8, float(value))
			self._inputParameters[7] = float(value)

	def get_CLAY_FRACTION_Name(self):
		if self._parCnIn[7] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[7], 1)
		else:
			return str(self._inputParameters[7])

	CLAY_FRACTION_Name = property(fget=get_CLAY_FRACTION_Name)

	def GRD_CLAY(self, index):
		if self._parCnIn[8] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[8], index)
		else:
			return self._inputParameters[8]

	def Save_GRD_CLAY(self, index, value):
		if self._parCnIn[8] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[8], index, float(value))
		else:
			self._IPProxy.SetNumericParam(9, float(value))
			self._inputParameters[8] = float(value)

	def get_GRD_CLAY_Name(self):
		if self._parCnIn[8] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[8], 1)
		else:
			return str(self._inputParameters[8])

	GRD_CLAY_Name = property(fget=get_GRD_CLAY_Name)

	def M(self, index):
		if self._parCnIn[9] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[9], index)
		else:
			return self._inputParameters[9]

	def Save_M(self, index, value):
		if self._parCnIn[9] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[9], index, float(value))
		else:
			self._IPProxy.SetNumericParam(10, float(value))
			self._inputParameters[9] = float(value)

	def get_M_Name(self):
		if self._parCnIn[9] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[9], 1)
		else:
			return str(self._inputParameters[9])

	M_Name = property(fget=get_M_Name)

	def BHT(self, index):
		if self._parCnIn[10] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[10], index)
		else:
			return self._inputParameters[10]

	def Save_BHT(self, index, value):
		if self._parCnIn[10] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[10], index, float(value))
		else:
			self._IPProxy.SetNumericParam(11, float(value))
			self._inputParameters[10] = float(value)

	def get_BHT_Name(self):
		if self._parCnIn[10] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[10], 1)
		else:
			return str(self._inputParameters[10])

	BHT_Name = property(fget=get_BHT_Name)

	def TD(self, index):
		if self._parCnIn[11] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[11], index)
		else:
			return self._inputParameters[11]

	def Save_TD(self, index, value):
		if self._parCnIn[11] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[11], index, float(value))
		else:
			self._IPProxy.SetNumericParam(12, float(value))
			self._inputParameters[11] = float(value)

	def get_TD_Name(self):
		if self._parCnIn[11] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[11], 1)
		else:
			return str(self._inputParameters[11])

	TD_Name = property(fget=get_TD_Name)

	def SBT(self, index):
		if self._parCnIn[12] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[12], index)
		else:
			return self._inputParameters[12]

	def Save_SBT(self, index, value):
		if self._parCnIn[12] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[12], index, float(value))
		else:
			self._IPProxy.SetNumericParam(13, float(value))
			self._inputParameters[12] = float(value)

	def get_SBT_Name(self):
		if self._parCnIn[12] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[12], 1)
		else:
			return str(self._inputParameters[12])

	SBT_Name = property(fget=get_SBT_Name)

	def WD(self, index):
		if self._parCnIn[13] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[13], index)
		else:
			return self._inputParameters[13]

	def Save_WD(self, index, value):
		if self._parCnIn[13] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[13], index, float(value))
		else:
			self._IPProxy.SetNumericParam(14, float(value))
			self._inputParameters[13] = float(value)

	def get_WD_Name(self):
		if self._parCnIn[13] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[13], 1)
		else:
			return str(self._inputParameters[13])

	WD_Name = property(fget=get_WD_Name)

	def RTE(self, index):
		if self._parCnIn[14] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[14], index)
		else:
			return self._inputParameters[14]

	def Save_RTE(self, index, value):
		if self._parCnIn[14] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[14], index, float(value))
		else:
			self._IPProxy.SetNumericParam(15, float(value))
			self._inputParameters[14] = float(value)

	def get_RTE_Name(self):
		if self._parCnIn[14] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[14], 1)
		else:
			return str(self._inputParameters[14])

	RTE_Name = property(fget=get_RTE_Name)

	def TRMF(self, index):
		if self._parCnIn[15] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[15], index)
		else:
			return self._inputParameters[15]

	def Save_TRMF(self, index, value):
		if self._parCnIn[15] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[15], index, float(value))
		else:
			self._IPProxy.SetNumericParam(16, float(value))
			self._inputParameters[15] = float(value)

	def get_TRMF_Name(self):
		if self._parCnIn[15] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[15], 1)
		else:
			return str(self._inputParameters[15])

	TRMF_Name = property(fget=get_TRMF_Name)

	def RMF(self, index):
		if self._parCnIn[16] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[16], index)
		else:
			return self._inputParameters[16]

	def Save_RMF(self, index, value):
		if self._parCnIn[16] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[16], index, float(value))
		else:
			self._IPProxy.SetNumericParam(17, float(value))
			self._inputParameters[16] = float(value)

	def get_RMF_Name(self):
		if self._parCnIn[16] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[16], 1)
		else:
			return str(self._inputParameters[16])

	RMF_Name = property(fget=get_RMF_Name)

	def SPB_C(self, index):
		if self._parCnIn[17] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[17], index)
		else:
			return self._inputParameters[17]

	def Save_SPB_C(self, index, value):
		if self._parCnIn[17] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[17], index, float(value))
		else:
			self._IPProxy.SetNumericParam(18, float(value))
			self._inputParameters[17] = float(value)

	def get_SPB_C_Name(self):
		if self._parCnIn[17] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[17], 1)
		else:
			return str(self._inputParameters[17])

	SPB_C_Name = property(fget=get_SPB_C_Name)

	def CF(self, index):
		if self._parCnIn[18] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[18], index)
		else:
			return self._inputParameters[18]

	def Save_CF(self, index, value):
		if self._parCnIn[18] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[18], index, float(value))
		else:
			self._IPProxy.SetNumericParam(19, float(value))
			self._inputParameters[18] = float(value)

	def get_CF_Name(self):
		if self._parCnIn[18] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[18], 1)
		else:
			return str(self._inputParameters[18])

	CF_Name = property(fget=get_CF_Name)

	def RHOGA(self, index):
		if self._parCnIn[19] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[19], index)
		else:
			return self._inputParameters[19]

	def Save_RHOGA(self, index, value):
		if self._parCnIn[19] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[19], index, float(value))
		else:
			self._IPProxy.SetNumericParam(20, float(value))
			self._inputParameters[19] = float(value)

	def get_RHOGA_Name(self):
		if self._parCnIn[19] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[19], 1)
		else:
			return str(self._inputParameters[19])

	RHOGA_Name = property(fget=get_RHOGA_Name)

	def get_OPT_SONIC_METHOD(self):
		return self._textInputParameters[0]

	OPT_SONIC_METHOD = property(fget=get_OPT_SONIC_METHOD)

	def get_OPT_TEMPLOG(self):
		return self._textInputParameters[1]

	OPT_TEMPLOG = property(fget=get_OPT_TEMPLOG)

	def get_OPT_TEMP_UNITS(self):
		return self._textInputParameters[2]

	OPT_TEMP_UNITS = property(fget=get_OPT_TEMP_UNITS)

	def get_OPT_MUD_TYPE(self):
		return self._textInputParameters[3]

	OPT_MUD_TYPE = property(fget=get_OPT_MUD_TYPE)

