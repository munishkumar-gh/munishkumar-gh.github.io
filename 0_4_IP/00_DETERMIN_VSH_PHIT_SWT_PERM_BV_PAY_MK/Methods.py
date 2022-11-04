# /***********************************************/
#  * File dynamically created from IP: 10/13/2022 11:08:55
#  * DO NOT MANUALLY EDIT
# /***********************************************/

class Methods:
	def __init__(self):
		self._FIRST_AVAILABLE_LOG_RUN = -1
		self._LAST_AVAILABLE_LOG_RUN = -2

	def Depth(self, index):
		return self._IPProxy.GetCurveData(1, index)

	def DEPTH_TVD(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[0],0, index, True)

	def Array_DEPTH_TVD(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[0],0, index, xVal, yVal, True)

	def DEPTH_TVD_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[0], index)

	def Array_DEPTH_TVD_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[0], index, xVal, yVal)

	def get_DEPTH_TVD_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 1)

	DEPTH_TVD_Name = property(fget=get_DEPTH_TVD_Name)

	def get_DEPTH_TVD_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 2)

	DEPTH_TVD_Units = property(fget=get_DEPTH_TVD_Units)

	def get_DEPTH_TVD_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 3)

	DEPTH_TVD_Comments = property(fget=get_DEPTH_TVD_Comments)

	def Save_DEPTH_TVD_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[0], 3, str(newValue))

	def Get_DEPTH_TVD_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[0], attributeName)

	def Set_DEPTH_TVD_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[0], attributeName, str(newValue))

	def Save_DEPTH_TVD(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[0], index, float(value))

	def Save_Array_DEPTH_TVD(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[0], index, float(value), xVal, yVal)

	def Save_DEPTH_TVD_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[0], index, str(value))

	def Save_Array_DEPTH_TVD_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[0], index, str(value), xVal, yVal)

	def get_Array_DEPTH_TVD_MaxX(self):
		return self._inArrayX[0]

	Array_DEPTH_TVD_MaxX = property(fget=get_Array_DEPTH_TVD_MaxX)

	def get_Array_DEPTH_TVD_MaxY(self):
		return self._inArrayY[0]

	Array_DEPTH_TVD_MaxY = property(fget=get_Array_DEPTH_TVD_MaxY)

	def GR(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[1],1, index, True)

	def Array_GR(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[1],1, index, xVal, yVal, True)

	def GR_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[1], index)

	def Array_GR_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[1], index, xVal, yVal)

	def get_GR_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 1)

	GR_Name = property(fget=get_GR_Name)

	def get_GR_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 2)

	GR_Units = property(fget=get_GR_Units)

	def get_GR_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 3)

	GR_Comments = property(fget=get_GR_Comments)

	def Save_GR_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[1], 3, str(newValue))

	def Get_GR_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[1], attributeName)

	def Set_GR_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[1], attributeName, str(newValue))

	def Save_GR(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[1], index, float(value))

	def Save_Array_GR(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[1], index, float(value), xVal, yVal)

	def Save_GR_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[1], index, str(value))

	def Save_Array_GR_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[1], index, str(value), xVal, yVal)

	def get_Array_GR_MaxX(self):
		return self._inArrayX[1]

	Array_GR_MaxX = property(fget=get_Array_GR_MaxX)

	def get_Array_GR_MaxY(self):
		return self._inArrayY[1]

	Array_GR_MaxY = property(fget=get_Array_GR_MaxY)

	def SP(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[2],2, index, True)

	def Array_SP(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[2],2, index, xVal, yVal, True)

	def SP_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[2], index)

	def Array_SP_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[2], index, xVal, yVal)

	def get_SP_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 1)

	SP_Name = property(fget=get_SP_Name)

	def get_SP_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 2)

	SP_Units = property(fget=get_SP_Units)

	def get_SP_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 3)

	SP_Comments = property(fget=get_SP_Comments)

	def Save_SP_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[2], 3, str(newValue))

	def Get_SP_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[2], attributeName)

	def Set_SP_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[2], attributeName, str(newValue))

	def Save_SP(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[2], index, float(value))

	def Save_Array_SP(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[2], index, float(value), xVal, yVal)

	def Save_SP_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[2], index, str(value))

	def Save_Array_SP_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[2], index, str(value), xVal, yVal)

	def get_Array_SP_MaxX(self):
		return self._inArrayX[2]

	Array_SP_MaxX = property(fget=get_Array_SP_MaxX)

	def get_Array_SP_MaxY(self):
		return self._inArrayY[2]

	Array_SP_MaxY = property(fget=get_Array_SP_MaxY)

	def RHOB(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[3],3, index, True)

	def Array_RHOB(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[3],3, index, xVal, yVal, True)

	def RHOB_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[3], index)

	def Array_RHOB_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[3], index, xVal, yVal)

	def get_RHOB_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 1)

	RHOB_Name = property(fget=get_RHOB_Name)

	def get_RHOB_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 2)

	RHOB_Units = property(fget=get_RHOB_Units)

	def get_RHOB_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 3)

	RHOB_Comments = property(fget=get_RHOB_Comments)

	def Save_RHOB_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[3], 3, str(newValue))

	def Get_RHOB_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[3], attributeName)

	def Set_RHOB_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[3], attributeName, str(newValue))

	def Save_RHOB(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[3], index, float(value))

	def Save_Array_RHOB(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[3], index, float(value), xVal, yVal)

	def Save_RHOB_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[3], index, str(value))

	def Save_Array_RHOB_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[3], index, str(value), xVal, yVal)

	def get_Array_RHOB_MaxX(self):
		return self._inArrayX[3]

	Array_RHOB_MaxX = property(fget=get_Array_RHOB_MaxX)

	def get_Array_RHOB_MaxY(self):
		return self._inArrayY[3]

	Array_RHOB_MaxY = property(fget=get_Array_RHOB_MaxY)

	def NPHI(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[4],4, index, True)

	def Array_NPHI(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[4],4, index, xVal, yVal, True)

	def NPHI_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[4], index)

	def Array_NPHI_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[4], index, xVal, yVal)

	def get_NPHI_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 1)

	NPHI_Name = property(fget=get_NPHI_Name)

	def get_NPHI_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 2)

	NPHI_Units = property(fget=get_NPHI_Units)

	def get_NPHI_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 3)

	NPHI_Comments = property(fget=get_NPHI_Comments)

	def Save_NPHI_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[4], 3, str(newValue))

	def Get_NPHI_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[4], attributeName)

	def Set_NPHI_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[4], attributeName, str(newValue))

	def Save_NPHI(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[4], index, float(value))

	def Save_Array_NPHI(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[4], index, float(value), xVal, yVal)

	def Save_NPHI_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[4], index, str(value))

	def Save_Array_NPHI_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[4], index, str(value), xVal, yVal)

	def get_Array_NPHI_MaxX(self):
		return self._inArrayX[4]

	Array_NPHI_MaxX = property(fget=get_Array_NPHI_MaxX)

	def get_Array_NPHI_MaxY(self):
		return self._inArrayY[4]

	Array_NPHI_MaxY = property(fget=get_Array_NPHI_MaxY)

	def RT(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[5],5, index, True)

	def Array_RT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[5],5, index, xVal, yVal, True)

	def RT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[5], index)

	def Array_RT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[5], index, xVal, yVal)

	def get_RT_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 1)

	RT_Name = property(fget=get_RT_Name)

	def get_RT_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 2)

	RT_Units = property(fget=get_RT_Units)

	def get_RT_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 3)

	RT_Comments = property(fget=get_RT_Comments)

	def Save_RT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[5], 3, str(newValue))

	def Get_RT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[5], attributeName)

	def Set_RT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[5], attributeName, str(newValue))

	def Save_RT(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[5], index, float(value))

	def Save_Array_RT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[5], index, float(value), xVal, yVal)

	def Save_RT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[5], index, str(value))

	def Save_Array_RT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[5], index, str(value), xVal, yVal)

	def get_Array_RT_MaxX(self):
		return self._inArrayX[5]

	Array_RT_MaxX = property(fget=get_Array_RT_MaxX)

	def get_Array_RT_MaxY(self):
		return self._inArrayY[5]

	Array_RT_MaxY = property(fget=get_Array_RT_MaxY)

	def RXO(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[6],6, index, True)

	def Array_RXO(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[6],6, index, xVal, yVal, True)

	def RXO_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[6], index)

	def Array_RXO_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[6], index, xVal, yVal)

	def get_RXO_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[6], 1)

	RXO_Name = property(fget=get_RXO_Name)

	def get_RXO_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[6], 2)

	RXO_Units = property(fget=get_RXO_Units)

	def get_RXO_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[6], 3)

	RXO_Comments = property(fget=get_RXO_Comments)

	def Save_RXO_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[6], 3, str(newValue))

	def Get_RXO_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[6], attributeName)

	def Set_RXO_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[6], attributeName, str(newValue))

	def Save_RXO(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[6], index, float(value))

	def Save_Array_RXO(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[6], index, float(value), xVal, yVal)

	def Save_RXO_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[6], index, str(value))

	def Save_Array_RXO_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[6], index, str(value), xVal, yVal)

	def get_Array_RXO_MaxX(self):
		return self._inArrayX[6]

	Array_RXO_MaxX = property(fget=get_Array_RXO_MaxX)

	def get_Array_RXO_MaxY(self):
		return self._inArrayY[6]

	Array_RXO_MaxY = property(fget=get_Array_RXO_MaxY)

	def DTCO(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[7],7, index, True)

	def Array_DTCO(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[7],7, index, xVal, yVal, True)

	def DTCO_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[7], index)

	def Array_DTCO_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[7], index, xVal, yVal)

	def get_DTCO_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[7], 1)

	DTCO_Name = property(fget=get_DTCO_Name)

	def get_DTCO_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[7], 2)

	DTCO_Units = property(fget=get_DTCO_Units)

	def get_DTCO_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[7], 3)

	DTCO_Comments = property(fget=get_DTCO_Comments)

	def Save_DTCO_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[7], 3, str(newValue))

	def Get_DTCO_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[7], attributeName)

	def Set_DTCO_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[7], attributeName, str(newValue))

	def Save_DTCO(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[7], index, float(value))

	def Save_Array_DTCO(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[7], index, float(value), xVal, yVal)

	def Save_DTCO_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[7], index, str(value))

	def Save_Array_DTCO_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[7], index, str(value), xVal, yVal)

	def get_Array_DTCO_MaxX(self):
		return self._inArrayX[7]

	Array_DTCO_MaxX = property(fget=get_Array_DTCO_MaxX)

	def get_Array_DTCO_MaxY(self):
		return self._inArrayY[7]

	Array_DTCO_MaxY = property(fget=get_Array_DTCO_MaxY)

	def FLAG_COAL(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[8],8, index, True)

	def Array_FLAG_COAL(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[8],8, index, xVal, yVal, True)

	def FLAG_COAL_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[8], index)

	def Array_FLAG_COAL_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[8], index, xVal, yVal)

	def get_FLAG_COAL_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[8], 1)

	FLAG_COAL_Name = property(fget=get_FLAG_COAL_Name)

	def get_FLAG_COAL_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[8], 2)

	FLAG_COAL_Units = property(fget=get_FLAG_COAL_Units)

	def get_FLAG_COAL_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[8], 3)

	FLAG_COAL_Comments = property(fget=get_FLAG_COAL_Comments)

	def Save_FLAG_COAL_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[8], 3, str(newValue))

	def Get_FLAG_COAL_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[8], attributeName)

	def Set_FLAG_COAL_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[8], attributeName, str(newValue))

	def Save_FLAG_COAL(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[8], index, float(value))

	def Save_Array_FLAG_COAL(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[8], index, float(value), xVal, yVal)

	def Save_FLAG_COAL_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[8], index, str(value))

	def Save_Array_FLAG_COAL_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[8], index, str(value), xVal, yVal)

	def get_Array_FLAG_COAL_MaxX(self):
		return self._inArrayX[8]

	Array_FLAG_COAL_MaxX = property(fget=get_Array_FLAG_COAL_MaxX)

	def get_Array_FLAG_COAL_MaxY(self):
		return self._inArrayY[8]

	Array_FLAG_COAL_MaxY = property(fget=get_Array_FLAG_COAL_MaxY)

	def FLAG_VOLC(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[9],9, index, True)

	def Array_FLAG_VOLC(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[9],9, index, xVal, yVal, True)

	def FLAG_VOLC_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[9], index)

	def Array_FLAG_VOLC_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[9], index, xVal, yVal)

	def get_FLAG_VOLC_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[9], 1)

	FLAG_VOLC_Name = property(fget=get_FLAG_VOLC_Name)

	def get_FLAG_VOLC_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[9], 2)

	FLAG_VOLC_Units = property(fget=get_FLAG_VOLC_Units)

	def get_FLAG_VOLC_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[9], 3)

	FLAG_VOLC_Comments = property(fget=get_FLAG_VOLC_Comments)

	def Save_FLAG_VOLC_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[9], 3, str(newValue))

	def Get_FLAG_VOLC_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[9], attributeName)

	def Set_FLAG_VOLC_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[9], attributeName, str(newValue))

	def Save_FLAG_VOLC(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[9], index, float(value))

	def Save_Array_FLAG_VOLC(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[9], index, float(value), xVal, yVal)

	def Save_FLAG_VOLC_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[9], index, str(value))

	def Save_Array_FLAG_VOLC_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[9], index, str(value), xVal, yVal)

	def get_Array_FLAG_VOLC_MaxX(self):
		return self._inArrayX[9]

	Array_FLAG_VOLC_MaxX = property(fget=get_Array_FLAG_VOLC_MaxX)

	def get_Array_FLAG_VOLC_MaxY(self):
		return self._inArrayY[9]

	Array_FLAG_VOLC_MaxY = property(fget=get_Array_FLAG_VOLC_MaxY)

	def Save_VSH(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, float(value))

	def Save_Array_VSH(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, float(value), xVal, yVal)

	def Save_VSH_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, str(value))

	def Save_Array_VSH_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, str(value), xVal, yVal)

	def VSH(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[0], index)

	def Array_VSH(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[0], index, xVal, yVal)

	def VSH_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[0], index)

	def Array_VSH_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[0], index, xVal, yVal)

	def get_VSH_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 1)

	VSH_Name = property(fget=get_VSH_Name)

	def get_VSH_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 2)

	VSH_Units = property(fget=get_VSH_Units)

	def get_VSH_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 3)

	VSH_Comments = property(fget=get_VSH_Comments)

	def Save_VSH_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[0], 3, str(newValue))

	def get_Array_VSH_MaxX(self):
		return self._outArrayX[0]

	Array_VSH_MaxX = property(fget=get_Array_VSH_MaxX)

	def get_Array_VSH_MaxY(self):
		return self._outArrayY[0]

	Array_VSH_MaxY = property(fget=get_Array_VSH_MaxY)

	def Get_VSH_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[0], attributeName)

	def Set_VSH_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[0], attributeName, str(newValue))

	def Save_VSH_ND(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value))

	def Save_Array_VSH_ND(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value), xVal, yVal)

	def Save_VSH_ND_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value))

	def Save_Array_VSH_ND_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value), xVal, yVal)

	def VSH_ND(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[1], index)

	def Array_VSH_ND(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[1], index, xVal, yVal)

	def VSH_ND_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[1], index)

	def Array_VSH_ND_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[1], index, xVal, yVal)

	def get_VSH_ND_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 1)

	VSH_ND_Name = property(fget=get_VSH_ND_Name)

	def get_VSH_ND_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 2)

	VSH_ND_Units = property(fget=get_VSH_ND_Units)

	def get_VSH_ND_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 3)

	VSH_ND_Comments = property(fget=get_VSH_ND_Comments)

	def Save_VSH_ND_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[1], 3, str(newValue))

	def get_Array_VSH_ND_MaxX(self):
		return self._outArrayX[1]

	Array_VSH_ND_MaxX = property(fget=get_Array_VSH_ND_MaxX)

	def get_Array_VSH_ND_MaxY(self):
		return self._outArrayY[1]

	Array_VSH_ND_MaxY = property(fget=get_Array_VSH_ND_MaxY)

	def Get_VSH_ND_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[1], attributeName)

	def Set_VSH_ND_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[1], attributeName, str(newValue))

	def Save_VSH_GR(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, float(value))

	def Save_Array_VSH_GR(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, float(value), xVal, yVal)

	def Save_VSH_GR_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, str(value))

	def Save_Array_VSH_GR_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, str(value), xVal, yVal)

	def VSH_GR(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[2], index)

	def Array_VSH_GR(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[2], index, xVal, yVal)

	def VSH_GR_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[2], index)

	def Array_VSH_GR_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[2], index, xVal, yVal)

	def get_VSH_GR_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 1)

	VSH_GR_Name = property(fget=get_VSH_GR_Name)

	def get_VSH_GR_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 2)

	VSH_GR_Units = property(fget=get_VSH_GR_Units)

	def get_VSH_GR_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 3)

	VSH_GR_Comments = property(fget=get_VSH_GR_Comments)

	def Save_VSH_GR_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[2], 3, str(newValue))

	def get_Array_VSH_GR_MaxX(self):
		return self._outArrayX[2]

	Array_VSH_GR_MaxX = property(fget=get_Array_VSH_GR_MaxX)

	def get_Array_VSH_GR_MaxY(self):
		return self._outArrayY[2]

	Array_VSH_GR_MaxY = property(fget=get_Array_VSH_GR_MaxY)

	def Get_VSH_GR_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[2], attributeName)

	def Set_VSH_GR_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[2], attributeName, str(newValue))

	def Save_VSH_RES(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, float(value))

	def Save_Array_VSH_RES(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, float(value), xVal, yVal)

	def Save_VSH_RES_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, str(value))

	def Save_Array_VSH_RES_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, str(value), xVal, yVal)

	def VSH_RES(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[3], index)

	def Array_VSH_RES(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[3], index, xVal, yVal)

	def VSH_RES_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[3], index)

	def Array_VSH_RES_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[3], index, xVal, yVal)

	def get_VSH_RES_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 1)

	VSH_RES_Name = property(fget=get_VSH_RES_Name)

	def get_VSH_RES_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 2)

	VSH_RES_Units = property(fget=get_VSH_RES_Units)

	def get_VSH_RES_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 3)

	VSH_RES_Comments = property(fget=get_VSH_RES_Comments)

	def Save_VSH_RES_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[3], 3, str(newValue))

	def get_Array_VSH_RES_MaxX(self):
		return self._outArrayX[3]

	Array_VSH_RES_MaxX = property(fget=get_Array_VSH_RES_MaxX)

	def get_Array_VSH_RES_MaxY(self):
		return self._outArrayY[3]

	Array_VSH_RES_MaxY = property(fget=get_Array_VSH_RES_MaxY)

	def Get_VSH_RES_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[3], attributeName)

	def Set_VSH_RES_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[3], attributeName, str(newValue))

	def Save_VSH_SP(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, float(value))

	def Save_Array_VSH_SP(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, float(value), xVal, yVal)

	def Save_VSH_SP_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, str(value))

	def Save_Array_VSH_SP_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, str(value), xVal, yVal)

	def VSH_SP(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[4], index)

	def Array_VSH_SP(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[4], index, xVal, yVal)

	def VSH_SP_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[4], index)

	def Array_VSH_SP_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[4], index, xVal, yVal)

	def get_VSH_SP_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 1)

	VSH_SP_Name = property(fget=get_VSH_SP_Name)

	def get_VSH_SP_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 2)

	VSH_SP_Units = property(fget=get_VSH_SP_Units)

	def get_VSH_SP_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 3)

	VSH_SP_Comments = property(fget=get_VSH_SP_Comments)

	def Save_VSH_SP_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[4], 3, str(newValue))

	def get_Array_VSH_SP_MaxX(self):
		return self._outArrayX[4]

	Array_VSH_SP_MaxX = property(fget=get_Array_VSH_SP_MaxX)

	def get_Array_VSH_SP_MaxY(self):
		return self._outArrayY[4]

	Array_VSH_SP_MaxY = property(fget=get_Array_VSH_SP_MaxY)

	def Get_VSH_SP_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[4], attributeName)

	def Set_VSH_SP_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[4], attributeName, str(newValue))

	def Save_VCL(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[5], index, float(value))

	def Save_Array_VCL(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[5], index, float(value), xVal, yVal)

	def Save_VCL_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[5], index, str(value))

	def Save_Array_VCL_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[5], index, str(value), xVal, yVal)

	def VCL(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[5], index)

	def Array_VCL(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[5], index, xVal, yVal)

	def VCL_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[5], index)

	def Array_VCL_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[5], index, xVal, yVal)

	def get_VCL_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 1)

	VCL_Name = property(fget=get_VCL_Name)

	def get_VCL_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 2)

	VCL_Units = property(fget=get_VCL_Units)

	def get_VCL_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 3)

	VCL_Comments = property(fget=get_VCL_Comments)

	def Save_VCL_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[5], 3, str(newValue))

	def get_Array_VCL_MaxX(self):
		return self._outArrayX[5]

	Array_VCL_MaxX = property(fget=get_Array_VCL_MaxX)

	def get_Array_VCL_MaxY(self):
		return self._outArrayY[5]

	Array_VCL_MaxY = property(fget=get_Array_VCL_MaxY)

	def Get_VCL_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[5], attributeName)

	def Set_VCL_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[5], attributeName, str(newValue))

	def Save_PHIE(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[6], index, float(value))

	def Save_Array_PHIE(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[6], index, float(value), xVal, yVal)

	def Save_PHIE_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[6], index, str(value))

	def Save_Array_PHIE_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[6], index, str(value), xVal, yVal)

	def PHIE(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[6], index)

	def Array_PHIE(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[6], index, xVal, yVal)

	def PHIE_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[6], index)

	def Array_PHIE_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[6], index, xVal, yVal)

	def get_PHIE_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 1)

	PHIE_Name = property(fget=get_PHIE_Name)

	def get_PHIE_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 2)

	PHIE_Units = property(fget=get_PHIE_Units)

	def get_PHIE_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 3)

	PHIE_Comments = property(fget=get_PHIE_Comments)

	def Save_PHIE_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[6], 3, str(newValue))

	def get_Array_PHIE_MaxX(self):
		return self._outArrayX[6]

	Array_PHIE_MaxX = property(fget=get_Array_PHIE_MaxX)

	def get_Array_PHIE_MaxY(self):
		return self._outArrayY[6]

	Array_PHIE_MaxY = property(fget=get_Array_PHIE_MaxY)

	def Get_PHIE_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[6], attributeName)

	def Set_PHIE_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[6], attributeName, str(newValue))

	def Save_PHID_A(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[7], index, float(value))

	def Save_Array_PHID_A(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[7], index, float(value), xVal, yVal)

	def Save_PHID_A_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[7], index, str(value))

	def Save_Array_PHID_A_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[7], index, str(value), xVal, yVal)

	def PHID_A(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[7], index)

	def Array_PHID_A(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[7], index, xVal, yVal)

	def PHID_A_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[7], index)

	def Array_PHID_A_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[7], index, xVal, yVal)

	def get_PHID_A_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 1)

	PHID_A_Name = property(fget=get_PHID_A_Name)

	def get_PHID_A_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 2)

	PHID_A_Units = property(fget=get_PHID_A_Units)

	def get_PHID_A_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 3)

	PHID_A_Comments = property(fget=get_PHID_A_Comments)

	def Save_PHID_A_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[7], 3, str(newValue))

	def get_Array_PHID_A_MaxX(self):
		return self._outArrayX[7]

	Array_PHID_A_MaxX = property(fget=get_Array_PHID_A_MaxX)

	def get_Array_PHID_A_MaxY(self):
		return self._outArrayY[7]

	Array_PHID_A_MaxY = property(fget=get_Array_PHID_A_MaxY)

	def Get_PHID_A_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[7], attributeName)

	def Set_PHID_A_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[7], attributeName, str(newValue))

	def Save_PHIT_HC(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[8], index, float(value))

	def Save_Array_PHIT_HC(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[8], index, float(value), xVal, yVal)

	def Save_PHIT_HC_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[8], index, str(value))

	def Save_Array_PHIT_HC_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[8], index, str(value), xVal, yVal)

	def PHIT_HC(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[8], index)

	def Array_PHIT_HC(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[8], index, xVal, yVal)

	def PHIT_HC_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[8], index)

	def Array_PHIT_HC_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[8], index, xVal, yVal)

	def get_PHIT_HC_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 1)

	PHIT_HC_Name = property(fget=get_PHIT_HC_Name)

	def get_PHIT_HC_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 2)

	PHIT_HC_Units = property(fget=get_PHIT_HC_Units)

	def get_PHIT_HC_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 3)

	PHIT_HC_Comments = property(fget=get_PHIT_HC_Comments)

	def Save_PHIT_HC_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[8], 3, str(newValue))

	def get_Array_PHIT_HC_MaxX(self):
		return self._outArrayX[8]

	Array_PHIT_HC_MaxX = property(fget=get_Array_PHIT_HC_MaxX)

	def get_Array_PHIT_HC_MaxY(self):
		return self._outArrayY[8]

	Array_PHIT_HC_MaxY = property(fget=get_Array_PHIT_HC_MaxY)

	def Get_PHIT_HC_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[8], attributeName)

	def Set_PHIT_HC_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[8], attributeName, str(newValue))

	def Save_PHIT(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[9], index, float(value))

	def Save_Array_PHIT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[9], index, float(value), xVal, yVal)

	def Save_PHIT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[9], index, str(value))

	def Save_Array_PHIT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[9], index, str(value), xVal, yVal)

	def PHIT(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[9], index)

	def Array_PHIT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[9], index, xVal, yVal)

	def PHIT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[9], index)

	def Array_PHIT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[9], index, xVal, yVal)

	def get_PHIT_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[9], 1)

	PHIT_Name = property(fget=get_PHIT_Name)

	def get_PHIT_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[9], 2)

	PHIT_Units = property(fget=get_PHIT_Units)

	def get_PHIT_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[9], 3)

	PHIT_Comments = property(fget=get_PHIT_Comments)

	def Save_PHIT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[9], 3, str(newValue))

	def get_Array_PHIT_MaxX(self):
		return self._outArrayX[9]

	Array_PHIT_MaxX = property(fget=get_Array_PHIT_MaxX)

	def get_Array_PHIT_MaxY(self):
		return self._outArrayY[9]

	Array_PHIT_MaxY = property(fget=get_Array_PHIT_MaxY)

	def Get_PHIT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[9], attributeName)

	def Set_PHIT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[9], attributeName, str(newValue))

	def Save_SWTU(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[10], index, float(value))

	def Save_Array_SWTU(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[10], index, float(value), xVal, yVal)

	def Save_SWTU_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[10], index, str(value))

	def Save_Array_SWTU_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[10], index, str(value), xVal, yVal)

	def SWTU(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[10], index)

	def Array_SWTU(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[10], index, xVal, yVal)

	def SWTU_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[10], index)

	def Array_SWTU_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[10], index, xVal, yVal)

	def get_SWTU_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[10], 1)

	SWTU_Name = property(fget=get_SWTU_Name)

	def get_SWTU_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[10], 2)

	SWTU_Units = property(fget=get_SWTU_Units)

	def get_SWTU_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[10], 3)

	SWTU_Comments = property(fget=get_SWTU_Comments)

	def Save_SWTU_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[10], 3, str(newValue))

	def get_Array_SWTU_MaxX(self):
		return self._outArrayX[10]

	Array_SWTU_MaxX = property(fget=get_Array_SWTU_MaxX)

	def get_Array_SWTU_MaxY(self):
		return self._outArrayY[10]

	Array_SWTU_MaxY = property(fget=get_Array_SWTU_MaxY)

	def Get_SWTU_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[10], attributeName)

	def Set_SWTU_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[10], attributeName, str(newValue))

	def Save_SWT(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[11], index, float(value))

	def Save_Array_SWT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[11], index, float(value), xVal, yVal)

	def Save_SWT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[11], index, str(value))

	def Save_Array_SWT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[11], index, str(value), xVal, yVal)

	def SWT(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[11], index)

	def Array_SWT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[11], index, xVal, yVal)

	def SWT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[11], index)

	def Array_SWT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[11], index, xVal, yVal)

	def get_SWT_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[11], 1)

	SWT_Name = property(fget=get_SWT_Name)

	def get_SWT_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[11], 2)

	SWT_Units = property(fget=get_SWT_Units)

	def get_SWT_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[11], 3)

	SWT_Comments = property(fget=get_SWT_Comments)

	def Save_SWT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[11], 3, str(newValue))

	def get_Array_SWT_MaxX(self):
		return self._outArrayX[11]

	Array_SWT_MaxX = property(fget=get_Array_SWT_MaxX)

	def get_Array_SWT_MaxY(self):
		return self._outArrayY[11]

	Array_SWT_MaxY = property(fget=get_Array_SWT_MaxY)

	def Get_SWT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[11], attributeName)

	def Set_SWT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[11], attributeName, str(newValue))

	def Save_SWE(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[12], index, float(value))

	def Save_Array_SWE(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[12], index, float(value), xVal, yVal)

	def Save_SWE_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[12], index, str(value))

	def Save_Array_SWE_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[12], index, str(value), xVal, yVal)

	def SWE(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[12], index)

	def Array_SWE(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[12], index, xVal, yVal)

	def SWE_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[12], index)

	def Array_SWE_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[12], index, xVal, yVal)

	def get_SWE_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[12], 1)

	SWE_Name = property(fget=get_SWE_Name)

	def get_SWE_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[12], 2)

	SWE_Units = property(fget=get_SWE_Units)

	def get_SWE_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[12], 3)

	SWE_Comments = property(fget=get_SWE_Comments)

	def Save_SWE_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[12], 3, str(newValue))

	def get_Array_SWE_MaxX(self):
		return self._outArrayX[12]

	Array_SWE_MaxX = property(fget=get_Array_SWE_MaxX)

	def get_Array_SWE_MaxY(self):
		return self._outArrayY[12]

	Array_SWE_MaxY = property(fget=get_Array_SWE_MaxY)

	def Get_SWE_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[12], attributeName)

	def Set_SWE_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[12], attributeName, str(newValue))

	def Save_SXOT(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[13], index, float(value))

	def Save_Array_SXOT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[13], index, float(value), xVal, yVal)

	def Save_SXOT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[13], index, str(value))

	def Save_Array_SXOT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[13], index, str(value), xVal, yVal)

	def SXOT(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[13], index)

	def Array_SXOT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[13], index, xVal, yVal)

	def SXOT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[13], index)

	def Array_SXOT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[13], index, xVal, yVal)

	def get_SXOT_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[13], 1)

	SXOT_Name = property(fget=get_SXOT_Name)

	def get_SXOT_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[13], 2)

	SXOT_Units = property(fget=get_SXOT_Units)

	def get_SXOT_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[13], 3)

	SXOT_Comments = property(fget=get_SXOT_Comments)

	def Save_SXOT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[13], 3, str(newValue))

	def get_Array_SXOT_MaxX(self):
		return self._outArrayX[13]

	Array_SXOT_MaxX = property(fget=get_Array_SXOT_MaxX)

	def get_Array_SXOT_MaxY(self):
		return self._outArrayY[13]

	Array_SXOT_MaxY = property(fget=get_Array_SXOT_MaxY)

	def Get_SXOT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[13], attributeName)

	def Set_SXOT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[13], attributeName, str(newValue))

	def Save_SXOE(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[14], index, float(value))

	def Save_Array_SXOE(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[14], index, float(value), xVal, yVal)

	def Save_SXOE_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[14], index, str(value))

	def Save_Array_SXOE_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[14], index, str(value), xVal, yVal)

	def SXOE(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[14], index)

	def Array_SXOE(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[14], index, xVal, yVal)

	def SXOE_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[14], index)

	def Array_SXOE_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[14], index, xVal, yVal)

	def get_SXOE_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[14], 1)

	SXOE_Name = property(fget=get_SXOE_Name)

	def get_SXOE_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[14], 2)

	SXOE_Units = property(fget=get_SXOE_Units)

	def get_SXOE_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[14], 3)

	SXOE_Comments = property(fget=get_SXOE_Comments)

	def Save_SXOE_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[14], 3, str(newValue))

	def get_Array_SXOE_MaxX(self):
		return self._outArrayX[14]

	Array_SXOE_MaxX = property(fget=get_Array_SXOE_MaxX)

	def get_Array_SXOE_MaxY(self):
		return self._outArrayY[14]

	Array_SXOE_MaxY = property(fget=get_Array_SXOE_MaxY)

	def Get_SXOE_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[14], attributeName)

	def Set_SXOE_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[14], attributeName, str(newValue))

	def Save_RHOGM(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[15], index, float(value))

	def Save_Array_RHOGM(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[15], index, float(value), xVal, yVal)

	def Save_RHOGM_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[15], index, str(value))

	def Save_Array_RHOGM_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[15], index, str(value), xVal, yVal)

	def RHOGM(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[15], index)

	def Array_RHOGM(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[15], index, xVal, yVal)

	def RHOGM_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[15], index)

	def Array_RHOGM_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[15], index, xVal, yVal)

	def get_RHOGM_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[15], 1)

	RHOGM_Name = property(fget=get_RHOGM_Name)

	def get_RHOGM_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[15], 2)

	RHOGM_Units = property(fget=get_RHOGM_Units)

	def get_RHOGM_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[15], 3)

	RHOGM_Comments = property(fget=get_RHOGM_Comments)

	def Save_RHOGM_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[15], 3, str(newValue))

	def get_Array_RHOGM_MaxX(self):
		return self._outArrayX[15]

	Array_RHOGM_MaxX = property(fget=get_Array_RHOGM_MaxX)

	def get_Array_RHOGM_MaxY(self):
		return self._outArrayY[15]

	Array_RHOGM_MaxY = property(fget=get_Array_RHOGM_MaxY)

	def Get_RHOGM_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[15], attributeName)

	def Set_RHOGM_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[15], attributeName, str(newValue))

	def Save_RHOGC(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[16], index, float(value))

	def Save_Array_RHOGC(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[16], index, float(value), xVal, yVal)

	def Save_RHOGC_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[16], index, str(value))

	def Save_Array_RHOGC_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[16], index, str(value), xVal, yVal)

	def RHOGC(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[16], index)

	def Array_RHOGC(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[16], index, xVal, yVal)

	def RHOGC_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[16], index)

	def Array_RHOGC_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[16], index, xVal, yVal)

	def get_RHOGC_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[16], 1)

	RHOGC_Name = property(fget=get_RHOGC_Name)

	def get_RHOGC_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[16], 2)

	RHOGC_Units = property(fget=get_RHOGC_Units)

	def get_RHOGC_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[16], 3)

	RHOGC_Comments = property(fget=get_RHOGC_Comments)

	def Save_RHOGC_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[16], 3, str(newValue))

	def get_Array_RHOGC_MaxX(self):
		return self._outArrayX[16]

	Array_RHOGC_MaxX = property(fget=get_Array_RHOGC_MaxX)

	def get_Array_RHOGC_MaxY(self):
		return self._outArrayY[16]

	Array_RHOGC_MaxY = property(fget=get_Array_RHOGC_MaxY)

	def Get_RHOGC_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[16], attributeName)

	def Set_RHOGC_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[16], attributeName, str(newValue))

	def Save_BVW(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[17], index, float(value))

	def Save_Array_BVW(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[17], index, float(value), xVal, yVal)

	def Save_BVW_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[17], index, str(value))

	def Save_Array_BVW_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[17], index, str(value), xVal, yVal)

	def BVW(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[17], index)

	def Array_BVW(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[17], index, xVal, yVal)

	def BVW_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[17], index)

	def Array_BVW_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[17], index, xVal, yVal)

	def get_BVW_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[17], 1)

	BVW_Name = property(fget=get_BVW_Name)

	def get_BVW_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[17], 2)

	BVW_Units = property(fget=get_BVW_Units)

	def get_BVW_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[17], 3)

	BVW_Comments = property(fget=get_BVW_Comments)

	def Save_BVW_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[17], 3, str(newValue))

	def get_Array_BVW_MaxX(self):
		return self._outArrayX[17]

	Array_BVW_MaxX = property(fget=get_Array_BVW_MaxX)

	def get_Array_BVW_MaxY(self):
		return self._outArrayY[17]

	Array_BVW_MaxY = property(fget=get_Array_BVW_MaxY)

	def Get_BVW_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[17], attributeName)

	def Set_BVW_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[17], attributeName, str(newValue))

	def Save_PHIA(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[18], index, float(value))

	def Save_Array_PHIA(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[18], index, float(value), xVal, yVal)

	def Save_PHIA_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[18], index, str(value))

	def Save_Array_PHIA_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[18], index, str(value), xVal, yVal)

	def PHIA(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[18], index)

	def Array_PHIA(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[18], index, xVal, yVal)

	def PHIA_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[18], index)

	def Array_PHIA_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[18], index, xVal, yVal)

	def get_PHIA_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[18], 1)

	PHIA_Name = property(fget=get_PHIA_Name)

	def get_PHIA_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[18], 2)

	PHIA_Units = property(fget=get_PHIA_Units)

	def get_PHIA_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[18], 3)

	PHIA_Comments = property(fget=get_PHIA_Comments)

	def Save_PHIA_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[18], 3, str(newValue))

	def get_Array_PHIA_MaxX(self):
		return self._outArrayX[18]

	Array_PHIA_MaxX = property(fget=get_Array_PHIA_MaxX)

	def get_Array_PHIA_MaxY(self):
		return self._outArrayY[18]

	Array_PHIA_MaxY = property(fget=get_Array_PHIA_MaxY)

	def Get_PHIA_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[18], attributeName)

	def Set_PHIA_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[18], attributeName, str(newValue))

	def Save_BVSH(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[19], index, float(value))

	def Save_Array_BVSH(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[19], index, float(value), xVal, yVal)

	def Save_BVSH_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[19], index, str(value))

	def Save_Array_BVSH_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[19], index, str(value), xVal, yVal)

	def BVSH(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[19], index)

	def Array_BVSH(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[19], index, xVal, yVal)

	def BVSH_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[19], index)

	def Array_BVSH_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[19], index, xVal, yVal)

	def get_BVSH_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[19], 1)

	BVSH_Name = property(fget=get_BVSH_Name)

	def get_BVSH_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[19], 2)

	BVSH_Units = property(fget=get_BVSH_Units)

	def get_BVSH_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[19], 3)

	BVSH_Comments = property(fget=get_BVSH_Comments)

	def Save_BVSH_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[19], 3, str(newValue))

	def get_Array_BVSH_MaxX(self):
		return self._outArrayX[19]

	Array_BVSH_MaxX = property(fget=get_Array_BVSH_MaxX)

	def get_Array_BVSH_MaxY(self):
		return self._outArrayY[19]

	Array_BVSH_MaxY = property(fget=get_Array_BVSH_MaxY)

	def Get_BVSH_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[19], attributeName)

	def Set_BVSH_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[19], attributeName, str(newValue))

	def Save_BVO(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[20], index, float(value))

	def Save_Array_BVO(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[20], index, float(value), xVal, yVal)

	def Save_BVO_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[20], index, str(value))

	def Save_Array_BVO_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[20], index, str(value), xVal, yVal)

	def BVO(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[20], index)

	def Array_BVO(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[20], index, xVal, yVal)

	def BVO_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[20], index)

	def Array_BVO_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[20], index, xVal, yVal)

	def get_BVO_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[20], 1)

	BVO_Name = property(fget=get_BVO_Name)

	def get_BVO_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[20], 2)

	BVO_Units = property(fget=get_BVO_Units)

	def get_BVO_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[20], 3)

	BVO_Comments = property(fget=get_BVO_Comments)

	def Save_BVO_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[20], 3, str(newValue))

	def get_Array_BVO_MaxX(self):
		return self._outArrayX[20]

	Array_BVO_MaxX = property(fget=get_Array_BVO_MaxX)

	def get_Array_BVO_MaxY(self):
		return self._outArrayY[20]

	Array_BVO_MaxY = property(fget=get_Array_BVO_MaxY)

	def Get_BVO_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[20], attributeName)

	def Set_BVO_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[20], attributeName, str(newValue))

	def Save_BVSAND(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[21], index, float(value))

	def Save_Array_BVSAND(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[21], index, float(value), xVal, yVal)

	def Save_BVSAND_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[21], index, str(value))

	def Save_Array_BVSAND_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[21], index, str(value), xVal, yVal)

	def BVSAND(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[21], index)

	def Array_BVSAND(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[21], index, xVal, yVal)

	def BVSAND_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[21], index)

	def Array_BVSAND_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[21], index, xVal, yVal)

	def get_BVSAND_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[21], 1)

	BVSAND_Name = property(fget=get_BVSAND_Name)

	def get_BVSAND_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[21], 2)

	BVSAND_Units = property(fget=get_BVSAND_Units)

	def get_BVSAND_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[21], 3)

	BVSAND_Comments = property(fget=get_BVSAND_Comments)

	def Save_BVSAND_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[21], 3, str(newValue))

	def get_Array_BVSAND_MaxX(self):
		return self._outArrayX[21]

	Array_BVSAND_MaxX = property(fget=get_Array_BVSAND_MaxX)

	def get_Array_BVSAND_MaxY(self):
		return self._outArrayY[21]

	Array_BVSAND_MaxY = property(fget=get_Array_BVSAND_MaxY)

	def Get_BVSAND_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[21], attributeName)

	def Set_BVSAND_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[21], attributeName, str(newValue))

	def Save_BVSILT(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[22], index, float(value))

	def Save_Array_BVSILT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[22], index, float(value), xVal, yVal)

	def Save_BVSILT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[22], index, str(value))

	def Save_Array_BVSILT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[22], index, str(value), xVal, yVal)

	def BVSILT(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[22], index)

	def Array_BVSILT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[22], index, xVal, yVal)

	def BVSILT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[22], index)

	def Array_BVSILT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[22], index, xVal, yVal)

	def get_BVSILT_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[22], 1)

	BVSILT_Name = property(fget=get_BVSILT_Name)

	def get_BVSILT_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[22], 2)

	BVSILT_Units = property(fget=get_BVSILT_Units)

	def get_BVSILT_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[22], 3)

	BVSILT_Comments = property(fget=get_BVSILT_Comments)

	def Save_BVSILT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[22], 3, str(newValue))

	def get_Array_BVSILT_MaxX(self):
		return self._outArrayX[22]

	Array_BVSILT_MaxX = property(fget=get_Array_BVSILT_MaxX)

	def get_Array_BVSILT_MaxY(self):
		return self._outArrayY[22]

	Array_BVSILT_MaxY = property(fget=get_Array_BVSILT_MaxY)

	def Get_BVSILT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[22], attributeName)

	def Set_BVSILT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[22], attributeName, str(newValue))

	def Save_BVLIM(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[23], index, float(value))

	def Save_Array_BVLIM(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[23], index, float(value), xVal, yVal)

	def Save_BVLIM_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[23], index, str(value))

	def Save_Array_BVLIM_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[23], index, str(value), xVal, yVal)

	def BVLIM(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[23], index)

	def Array_BVLIM(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[23], index, xVal, yVal)

	def BVLIM_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[23], index)

	def Array_BVLIM_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[23], index, xVal, yVal)

	def get_BVLIM_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[23], 1)

	BVLIM_Name = property(fget=get_BVLIM_Name)

	def get_BVLIM_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[23], 2)

	BVLIM_Units = property(fget=get_BVLIM_Units)

	def get_BVLIM_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[23], 3)

	BVLIM_Comments = property(fget=get_BVLIM_Comments)

	def Save_BVLIM_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[23], 3, str(newValue))

	def get_Array_BVLIM_MaxX(self):
		return self._outArrayX[23]

	Array_BVLIM_MaxX = property(fget=get_Array_BVLIM_MaxX)

	def get_Array_BVLIM_MaxY(self):
		return self._outArrayY[23]

	Array_BVLIM_MaxY = property(fget=get_Array_BVLIM_MaxY)

	def Get_BVLIM_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[23], attributeName)

	def Set_BVLIM_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[23], attributeName, str(newValue))

	def Save_BVCLAY(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[24], index, float(value))

	def Save_Array_BVCLAY(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[24], index, float(value), xVal, yVal)

	def Save_BVCLAY_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[24], index, str(value))

	def Save_Array_BVCLAY_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[24], index, str(value), xVal, yVal)

	def BVCLAY(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[24], index)

	def Array_BVCLAY(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[24], index, xVal, yVal)

	def BVCLAY_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[24], index)

	def Array_BVCLAY_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[24], index, xVal, yVal)

	def get_BVCLAY_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[24], 1)

	BVCLAY_Name = property(fget=get_BVCLAY_Name)

	def get_BVCLAY_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[24], 2)

	BVCLAY_Units = property(fget=get_BVCLAY_Units)

	def get_BVCLAY_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[24], 3)

	BVCLAY_Comments = property(fget=get_BVCLAY_Comments)

	def Save_BVCLAY_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[24], 3, str(newValue))

	def get_Array_BVCLAY_MaxX(self):
		return self._outArrayX[24]

	Array_BVCLAY_MaxX = property(fget=get_Array_BVCLAY_MaxX)

	def get_Array_BVCLAY_MaxY(self):
		return self._outArrayY[24]

	Array_BVCLAY_MaxY = property(fget=get_Array_BVCLAY_MaxY)

	def Get_BVCLAY_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[24], attributeName)

	def Set_BVCLAY_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[24], attributeName, str(newValue))

	def Save_SALINITY_SP(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[25], index, float(value))

	def Save_Array_SALINITY_SP(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[25], index, float(value), xVal, yVal)

	def Save_SALINITY_SP_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[25], index, str(value))

	def Save_Array_SALINITY_SP_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[25], index, str(value), xVal, yVal)

	def SALINITY_SP(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[25], index)

	def Array_SALINITY_SP(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[25], index, xVal, yVal)

	def SALINITY_SP_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[25], index)

	def Array_SALINITY_SP_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[25], index, xVal, yVal)

	def get_SALINITY_SP_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[25], 1)

	SALINITY_SP_Name = property(fget=get_SALINITY_SP_Name)

	def get_SALINITY_SP_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[25], 2)

	SALINITY_SP_Units = property(fget=get_SALINITY_SP_Units)

	def get_SALINITY_SP_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[25], 3)

	SALINITY_SP_Comments = property(fget=get_SALINITY_SP_Comments)

	def Save_SALINITY_SP_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[25], 3, str(newValue))

	def get_Array_SALINITY_SP_MaxX(self):
		return self._outArrayX[25]

	Array_SALINITY_SP_MaxX = property(fget=get_Array_SALINITY_SP_MaxX)

	def get_Array_SALINITY_SP_MaxY(self):
		return self._outArrayY[25]

	Array_SALINITY_SP_MaxY = property(fget=get_Array_SALINITY_SP_MaxY)

	def Get_SALINITY_SP_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[25], attributeName)

	def Set_SALINITY_SP_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[25], attributeName, str(newValue))

	def Save_RW_SP(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[26], index, float(value))

	def Save_Array_RW_SP(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[26], index, float(value), xVal, yVal)

	def Save_RW_SP_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[26], index, str(value))

	def Save_Array_RW_SP_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[26], index, str(value), xVal, yVal)

	def RW_SP(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[26], index)

	def Array_RW_SP(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[26], index, xVal, yVal)

	def RW_SP_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[26], index)

	def Array_RW_SP_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[26], index, xVal, yVal)

	def get_RW_SP_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[26], 1)

	RW_SP_Name = property(fget=get_RW_SP_Name)

	def get_RW_SP_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[26], 2)

	RW_SP_Units = property(fget=get_RW_SP_Units)

	def get_RW_SP_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[26], 3)

	RW_SP_Comments = property(fget=get_RW_SP_Comments)

	def Save_RW_SP_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[26], 3, str(newValue))

	def get_Array_RW_SP_MaxX(self):
		return self._outArrayX[26]

	Array_RW_SP_MaxX = property(fget=get_Array_RW_SP_MaxX)

	def get_Array_RW_SP_MaxY(self):
		return self._outArrayY[26]

	Array_RW_SP_MaxY = property(fget=get_Array_RW_SP_MaxY)

	def Get_RW_SP_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[26], attributeName)

	def Set_RW_SP_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[26], attributeName, str(newValue))

	def Save_SALINITY(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[27], index, float(value))

	def Save_Array_SALINITY(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[27], index, float(value), xVal, yVal)

	def Save_SALINITY_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[27], index, str(value))

	def Save_Array_SALINITY_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[27], index, str(value), xVal, yVal)

	def SALINITY(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[27], index)

	def Array_SALINITY(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[27], index, xVal, yVal)

	def SALINITY_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[27], index)

	def Array_SALINITY_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[27], index, xVal, yVal)

	def get_SALINITY_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[27], 1)

	SALINITY_Name = property(fget=get_SALINITY_Name)

	def get_SALINITY_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[27], 2)

	SALINITY_Units = property(fget=get_SALINITY_Units)

	def get_SALINITY_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[27], 3)

	SALINITY_Comments = property(fget=get_SALINITY_Comments)

	def Save_SALINITY_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[27], 3, str(newValue))

	def get_Array_SALINITY_MaxX(self):
		return self._outArrayX[27]

	Array_SALINITY_MaxX = property(fget=get_Array_SALINITY_MaxX)

	def get_Array_SALINITY_MaxY(self):
		return self._outArrayY[27]

	Array_SALINITY_MaxY = property(fget=get_Array_SALINITY_MaxY)

	def Get_SALINITY_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[27], attributeName)

	def Set_SALINITY_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[27], attributeName, str(newValue))

	def Save_RW(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[28], index, float(value))

	def Save_Array_RW(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[28], index, float(value), xVal, yVal)

	def Save_RW_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[28], index, str(value))

	def Save_Array_RW_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[28], index, str(value), xVal, yVal)

	def RW(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[28], index)

	def Array_RW(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[28], index, xVal, yVal)

	def RW_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[28], index)

	def Array_RW_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[28], index, xVal, yVal)

	def get_RW_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[28], 1)

	RW_Name = property(fget=get_RW_Name)

	def get_RW_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[28], 2)

	RW_Units = property(fget=get_RW_Units)

	def get_RW_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[28], 3)

	RW_Comments = property(fget=get_RW_Comments)

	def Save_RW_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[28], 3, str(newValue))

	def get_Array_RW_MaxX(self):
		return self._outArrayX[28]

	Array_RW_MaxX = property(fget=get_Array_RW_MaxX)

	def get_Array_RW_MaxY(self):
		return self._outArrayY[28]

	Array_RW_MaxY = property(fget=get_Array_RW_MaxY)

	def Get_RW_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[28], attributeName)

	def Set_RW_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[28], attributeName, str(newValue))

	def Save_PHIX(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[29], index, float(value))

	def Save_Array_PHIX(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[29], index, float(value), xVal, yVal)

	def Save_PHIX_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[29], index, str(value))

	def Save_Array_PHIX_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[29], index, str(value), xVal, yVal)

	def PHIX(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[29], index)

	def Array_PHIX(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[29], index, xVal, yVal)

	def PHIX_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[29], index)

	def Array_PHIX_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[29], index, xVal, yVal)

	def get_PHIX_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[29], 1)

	PHIX_Name = property(fget=get_PHIX_Name)

	def get_PHIX_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[29], 2)

	PHIX_Units = property(fget=get_PHIX_Units)

	def get_PHIX_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[29], 3)

	PHIX_Comments = property(fget=get_PHIX_Comments)

	def Save_PHIX_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[29], 3, str(newValue))

	def get_Array_PHIX_MaxX(self):
		return self._outArrayX[29]

	Array_PHIX_MaxX = property(fget=get_Array_PHIX_MaxX)

	def get_Array_PHIX_MaxY(self):
		return self._outArrayY[29]

	Array_PHIX_MaxY = property(fget=get_Array_PHIX_MaxY)

	def Get_PHIX_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[29], attributeName)

	def Set_PHIX_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[29], attributeName, str(newValue))

	def Save_NPHIH(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[30], index, float(value))

	def Save_Array_NPHIH(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[30], index, float(value), xVal, yVal)

	def Save_NPHIH_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[30], index, str(value))

	def Save_Array_NPHIH_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[30], index, str(value), xVal, yVal)

	def NPHIH(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[30], index)

	def Array_NPHIH(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[30], index, xVal, yVal)

	def NPHIH_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[30], index)

	def Array_NPHIH_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[30], index, xVal, yVal)

	def get_NPHIH_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[30], 1)

	NPHIH_Name = property(fget=get_NPHIH_Name)

	def get_NPHIH_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[30], 2)

	NPHIH_Units = property(fget=get_NPHIH_Units)

	def get_NPHIH_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[30], 3)

	NPHIH_Comments = property(fget=get_NPHIH_Comments)

	def Save_NPHIH_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[30], 3, str(newValue))

	def get_Array_NPHIH_MaxX(self):
		return self._outArrayX[30]

	Array_NPHIH_MaxX = property(fget=get_Array_NPHIH_MaxX)

	def get_Array_NPHIH_MaxY(self):
		return self._outArrayY[30]

	Array_NPHIH_MaxY = property(fget=get_Array_NPHIH_MaxY)

	def Get_NPHIH_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[30], attributeName)

	def Set_NPHIH_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[30], attributeName, str(newValue))

	def Save_RHOBH(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[31], index, float(value))

	def Save_Array_RHOBH(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[31], index, float(value), xVal, yVal)

	def Save_RHOBH_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[31], index, str(value))

	def Save_Array_RHOBH_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[31], index, str(value), xVal, yVal)

	def RHOBH(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[31], index)

	def Array_RHOBH(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[31], index, xVal, yVal)

	def RHOBH_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[31], index)

	def Array_RHOBH_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[31], index, xVal, yVal)

	def get_RHOBH_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[31], 1)

	RHOBH_Name = property(fget=get_RHOBH_Name)

	def get_RHOBH_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[31], 2)

	RHOBH_Units = property(fget=get_RHOBH_Units)

	def get_RHOBH_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[31], 3)

	RHOBH_Comments = property(fget=get_RHOBH_Comments)

	def Save_RHOBH_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[31], 3, str(newValue))

	def get_Array_RHOBH_MaxX(self):
		return self._outArrayX[31]

	Array_RHOBH_MaxX = property(fget=get_Array_RHOBH_MaxX)

	def get_Array_RHOBH_MaxY(self):
		return self._outArrayY[31]

	Array_RHOBH_MaxY = property(fget=get_Array_RHOBH_MaxY)

	def Get_RHOBH_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[31], attributeName)

	def Set_RHOBH_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[31], attributeName, str(newValue))

	def Save_SUM_TOT(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[32], index, float(value))

	def Save_Array_SUM_TOT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[32], index, float(value), xVal, yVal)

	def Save_SUM_TOT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[32], index, str(value))

	def Save_Array_SUM_TOT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[32], index, str(value), xVal, yVal)

	def SUM_TOT(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[32], index)

	def Array_SUM_TOT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[32], index, xVal, yVal)

	def SUM_TOT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[32], index)

	def Array_SUM_TOT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[32], index, xVal, yVal)

	def get_SUM_TOT_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[32], 1)

	SUM_TOT_Name = property(fget=get_SUM_TOT_Name)

	def get_SUM_TOT_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[32], 2)

	SUM_TOT_Units = property(fget=get_SUM_TOT_Units)

	def get_SUM_TOT_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[32], 3)

	SUM_TOT_Comments = property(fget=get_SUM_TOT_Comments)

	def Save_SUM_TOT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[32], 3, str(newValue))

	def get_Array_SUM_TOT_MaxX(self):
		return self._outArrayX[32]

	Array_SUM_TOT_MaxX = property(fget=get_Array_SUM_TOT_MaxX)

	def get_Array_SUM_TOT_MaxY(self):
		return self._outArrayY[32]

	Array_SUM_TOT_MaxY = property(fget=get_Array_SUM_TOT_MaxY)

	def Get_SUM_TOT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[32], attributeName)

	def Set_SUM_TOT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[32], attributeName, str(newValue))

	def Save_SD(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[33], index, float(value))

	def Save_Array_SD(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[33], index, float(value), xVal, yVal)

	def Save_SD_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[33], index, str(value))

	def Save_Array_SD_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[33], index, str(value), xVal, yVal)

	def SD(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[33], index)

	def Array_SD(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[33], index, xVal, yVal)

	def SD_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[33], index)

	def Array_SD_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[33], index, xVal, yVal)

	def get_SD_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[33], 1)

	SD_Name = property(fget=get_SD_Name)

	def get_SD_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[33], 2)

	SD_Units = property(fget=get_SD_Units)

	def get_SD_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[33], 3)

	SD_Comments = property(fget=get_SD_Comments)

	def Save_SD_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[33], 3, str(newValue))

	def get_Array_SD_MaxX(self):
		return self._outArrayX[33]

	Array_SD_MaxX = property(fget=get_Array_SD_MaxX)

	def get_Array_SD_MaxY(self):
		return self._outArrayY[33]

	Array_SD_MaxY = property(fget=get_Array_SD_MaxY)

	def Get_SD_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[33], attributeName)

	def Set_SD_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[33], attributeName, str(newValue))

	def Save_RESV(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[34], index, float(value))

	def Save_Array_RESV(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[34], index, float(value), xVal, yVal)

	def Save_RESV_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[34], index, str(value))

	def Save_Array_RESV_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[34], index, str(value), xVal, yVal)

	def RESV(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[34], index)

	def Array_RESV(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[34], index, xVal, yVal)

	def RESV_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[34], index)

	def Array_RESV_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[34], index, xVal, yVal)

	def get_RESV_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[34], 1)

	RESV_Name = property(fget=get_RESV_Name)

	def get_RESV_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[34], 2)

	RESV_Units = property(fget=get_RESV_Units)

	def get_RESV_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[34], 3)

	RESV_Comments = property(fget=get_RESV_Comments)

	def Save_RESV_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[34], 3, str(newValue))

	def get_Array_RESV_MaxX(self):
		return self._outArrayX[34]

	Array_RESV_MaxX = property(fget=get_Array_RESV_MaxX)

	def get_Array_RESV_MaxY(self):
		return self._outArrayY[34]

	Array_RESV_MaxY = property(fget=get_Array_RESV_MaxY)

	def Get_RESV_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[34], attributeName)

	def Set_RESV_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[34], attributeName, str(newValue))

	def Save_PAY(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[35], index, float(value))

	def Save_Array_PAY(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[35], index, float(value), xVal, yVal)

	def Save_PAY_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[35], index, str(value))

	def Save_Array_PAY_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[35], index, str(value), xVal, yVal)

	def PAY(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[35], index)

	def Array_PAY(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[35], index, xVal, yVal)

	def PAY_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[35], index)

	def Array_PAY_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[35], index, xVal, yVal)

	def get_PAY_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[35], 1)

	PAY_Name = property(fget=get_PAY_Name)

	def get_PAY_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[35], 2)

	PAY_Units = property(fget=get_PAY_Units)

	def get_PAY_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[35], 3)

	PAY_Comments = property(fget=get_PAY_Comments)

	def Save_PAY_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[35], 3, str(newValue))

	def get_Array_PAY_MaxX(self):
		return self._outArrayX[35]

	Array_PAY_MaxX = property(fget=get_Array_PAY_MaxX)

	def get_Array_PAY_MaxY(self):
		return self._outArrayY[35]

	Array_PAY_MaxY = property(fget=get_Array_PAY_MaxY)

	def Get_PAY_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[35], attributeName)

	def Set_PAY_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[35], attributeName, str(newValue))

	def Save_BVWE(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[36], index, float(value))

	def Save_Array_BVWE(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[36], index, float(value), xVal, yVal)

	def Save_BVWE_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[36], index, str(value))

	def Save_Array_BVWE_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[36], index, str(value), xVal, yVal)

	def BVWE(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[36], index)

	def Array_BVWE(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[36], index, xVal, yVal)

	def BVWE_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[36], index)

	def Array_BVWE_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[36], index, xVal, yVal)

	def get_BVWE_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[36], 1)

	BVWE_Name = property(fget=get_BVWE_Name)

	def get_BVWE_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[36], 2)

	BVWE_Units = property(fget=get_BVWE_Units)

	def get_BVWE_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[36], 3)

	BVWE_Comments = property(fget=get_BVWE_Comments)

	def Save_BVWE_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[36], 3, str(newValue))

	def get_Array_BVWE_MaxX(self):
		return self._outArrayX[36]

	Array_BVWE_MaxX = property(fget=get_Array_BVWE_MaxX)

	def get_Array_BVWE_MaxY(self):
		return self._outArrayY[36]

	Array_BVWE_MaxY = property(fget=get_Array_BVWE_MaxY)

	def Get_BVWE_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[36], attributeName)

	def Set_BVWE_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[36], attributeName, str(newValue))

	def TVD(self, index):
		if self._parCnIn[0] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[0], index)
		else:
			return self._inputParameters[0]

	def Save_TVD(self, index, value):
		if self._parCnIn[0] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[0], index, float(value))
		else:
			self._IPProxy.SetNumericParam(1, float(value))
			self._inputParameters[0] = float(value)

	def get_TVD_Name(self):
		if self._parCnIn[0] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[0], 1)
		else:
			return str(self._inputParameters[0])

	TVD_Name = property(fget=get_TVD_Name)

	def WD(self, index):
		if self._parCnIn[1] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[1], index)
		else:
			return self._inputParameters[1]

	def Save_WD(self, index, value):
		if self._parCnIn[1] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[1], index, float(value))
		else:
			self._IPProxy.SetNumericParam(2, float(value))
			self._inputParameters[1] = float(value)

	def get_WD_Name(self):
		if self._parCnIn[1] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[1], 1)
		else:
			return str(self._inputParameters[1])

	WD_Name = property(fget=get_WD_Name)

	def FTEMP_L(self, index):
		if self._parCnIn[2] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[2], index)
		else:
			return self._inputParameters[2]

	def Save_FTEMP_L(self, index, value):
		if self._parCnIn[2] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[2], index, float(value))
		else:
			self._IPProxy.SetNumericParam(3, float(value))
			self._inputParameters[2] = float(value)

	def get_FTEMP_L_Name(self):
		if self._parCnIn[2] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[2], 1)
		else:
			return str(self._inputParameters[2])

	FTEMP_L_Name = property(fget=get_FTEMP_L_Name)

	def BHT(self, index):
		if self._parCnIn[3] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[3], index)
		else:
			return self._inputParameters[3]

	def Save_BHT(self, index, value):
		if self._parCnIn[3] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[3], index, float(value))
		else:
			self._IPProxy.SetNumericParam(4, float(value))
			self._inputParameters[3] = float(value)

	def get_BHT_Name(self):
		if self._parCnIn[3] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[3], 1)
		else:
			return str(self._inputParameters[3])

	BHT_Name = property(fget=get_BHT_Name)

	def SBT(self, index):
		if self._parCnIn[4] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[4], index)
		else:
			return self._inputParameters[4]

	def Save_SBT(self, index, value):
		if self._parCnIn[4] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[4], index, float(value))
		else:
			self._IPProxy.SetNumericParam(5, float(value))
			self._inputParameters[4] = float(value)

	def get_SBT_Name(self):
		if self._parCnIn[4] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[4], 1)
		else:
			return str(self._inputParameters[4])

	SBT_Name = property(fget=get_SBT_Name)

	def RTE(self, index):
		if self._parCnIn[5] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[5], index)
		else:
			return self._inputParameters[5]

	def Save_RTE(self, index, value):
		if self._parCnIn[5] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[5], index, float(value))
		else:
			self._IPProxy.SetNumericParam(6, float(value))
			self._inputParameters[5] = float(value)

	def get_RTE_Name(self):
		if self._parCnIn[5] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[5], 1)
		else:
			return str(self._inputParameters[5])

	RTE_Name = property(fget=get_RTE_Name)

	def GRMIN_L(self, index):
		if self._parCnIn[6] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[6], index)
		else:
			return self._inputParameters[6]

	def Save_GRMIN_L(self, index, value):
		if self._parCnIn[6] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[6], index, float(value))
		else:
			self._IPProxy.SetNumericParam(7, float(value))
			self._inputParameters[6] = float(value)

	def get_GRMIN_L_Name(self):
		if self._parCnIn[6] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[6], 1)
		else:
			return str(self._inputParameters[6])

	GRMIN_L_Name = property(fget=get_GRMIN_L_Name)

	def GRMAX_L(self, index):
		if self._parCnIn[7] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[7], index)
		else:
			return self._inputParameters[7]

	def Save_GRMAX_L(self, index, value):
		if self._parCnIn[7] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[7], index, float(value))
		else:
			self._IPProxy.SetNumericParam(8, float(value))
			self._inputParameters[7] = float(value)

	def get_GRMAX_L_Name(self):
		if self._parCnIn[7] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[7], 1)
		else:
			return str(self._inputParameters[7])

	GRMAX_L_Name = property(fget=get_GRMAX_L_Name)

	def RSAND_L(self, index):
		if self._parCnIn[8] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[8], index)
		else:
			return self._inputParameters[8]

	def Save_RSAND_L(self, index, value):
		if self._parCnIn[8] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[8], index, float(value))
		else:
			self._IPProxy.SetNumericParam(9, float(value))
			self._inputParameters[8] = float(value)

	def get_RSAND_L_Name(self):
		if self._parCnIn[8] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[8], 1)
		else:
			return str(self._inputParameters[8])

	RSAND_L_Name = property(fget=get_RSAND_L_Name)

	def RSHALE_L(self, index):
		if self._parCnIn[9] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[9], index)
		else:
			return self._inputParameters[9]

	def Save_RSHALE_L(self, index, value):
		if self._parCnIn[9] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[9], index, float(value))
		else:
			self._IPProxy.SetNumericParam(10, float(value))
			self._inputParameters[9] = float(value)

	def get_RSHALE_L_Name(self):
		if self._parCnIn[9] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[9], 1)
		else:
			return str(self._inputParameters[9])

	RSHALE_L_Name = property(fget=get_RSHALE_L_Name)

	def SPSAND_L(self, index):
		if self._parCnIn[10] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[10], index)
		else:
			return self._inputParameters[10]

	def Save_SPSAND_L(self, index, value):
		if self._parCnIn[10] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[10], index, float(value))
		else:
			self._IPProxy.SetNumericParam(11, float(value))
			self._inputParameters[10] = float(value)

	def get_SPSAND_L_Name(self):
		if self._parCnIn[10] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[10], 1)
		else:
			return str(self._inputParameters[10])

	SPSAND_L_Name = property(fget=get_SPSAND_L_Name)

	def SPSHALE_L(self, index):
		if self._parCnIn[11] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[11], index)
		else:
			return self._inputParameters[11]

	def Save_SPSHALE_L(self, index, value):
		if self._parCnIn[11] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[11], index, float(value))
		else:
			self._IPProxy.SetNumericParam(12, float(value))
			self._inputParameters[11] = float(value)

	def get_SPSHALE_L_Name(self):
		if self._parCnIn[11] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[11], 1)
		else:
			return str(self._inputParameters[11])

	SPSHALE_L_Name = property(fget=get_SPSHALE_L_Name)

	def RHOBWSH(self, index):
		if self._parCnIn[12] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[12], index)
		else:
			return self._inputParameters[12]

	def Save_RHOBWSH(self, index, value):
		if self._parCnIn[12] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[12], index, float(value))
		else:
			self._IPProxy.SetNumericParam(13, float(value))
			self._inputParameters[12] = float(value)

	def get_RHOBWSH_Name(self):
		if self._parCnIn[12] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[12], 1)
		else:
			return str(self._inputParameters[12])

	RHOBWSH_Name = property(fget=get_RHOBWSH_Name)

	def NPHIWSH(self, index):
		if self._parCnIn[13] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[13], index)
		else:
			return self._inputParameters[13]

	def Save_NPHIWSH(self, index, value):
		if self._parCnIn[13] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[13], index, float(value))
		else:
			self._IPProxy.SetNumericParam(14, float(value))
			self._inputParameters[13] = float(value)

	def get_NPHIWSH_Name(self):
		if self._parCnIn[13] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[13], 1)
		else:
			return str(self._inputParameters[13])

	NPHIWSH_Name = property(fget=get_NPHIWSH_Name)

	def RHOBQ(self, index):
		if self._parCnIn[14] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[14], index)
		else:
			return self._inputParameters[14]

	def Save_RHOBQ(self, index, value):
		if self._parCnIn[14] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[14], index, float(value))
		else:
			self._IPProxy.SetNumericParam(15, float(value))
			self._inputParameters[14] = float(value)

	def get_RHOBQ_Name(self):
		if self._parCnIn[14] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[14], 1)
		else:
			return str(self._inputParameters[14])

	RHOBQ_Name = property(fget=get_RHOBQ_Name)

	def NPHIQ(self, index):
		if self._parCnIn[15] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[15], index)
		else:
			return self._inputParameters[15]

	def Save_NPHIQ(self, index, value):
		if self._parCnIn[15] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[15], index, float(value))
		else:
			self._IPProxy.SetNumericParam(16, float(value))
			self._inputParameters[15] = float(value)

	def get_NPHIQ_Name(self):
		if self._parCnIn[15] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[15], 1)
		else:
			return str(self._inputParameters[15])

	NPHIQ_Name = property(fget=get_NPHIQ_Name)

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

	def TRMF(self, index):
		if self._parCnIn[17] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[17], index)
		else:
			return self._inputParameters[17]

	def Save_TRMF(self, index, value):
		if self._parCnIn[17] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[17], index, float(value))
		else:
			self._IPProxy.SetNumericParam(18, float(value))
			self._inputParameters[17] = float(value)

	def get_TRMF_Name(self):
		if self._parCnIn[17] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[17], 1)
		else:
			return str(self._inputParameters[17])

	TRMF_Name = property(fget=get_TRMF_Name)

	def SPB_L(self, index):
		if self._parCnIn[18] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[18], index)
		else:
			return self._inputParameters[18]

	def Save_SPB_L(self, index, value):
		if self._parCnIn[18] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[18], index, float(value))
		else:
			self._IPProxy.SetNumericParam(19, float(value))
			self._inputParameters[18] = float(value)

	def get_SPB_L_Name(self):
		if self._parCnIn[18] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[18], 1)
		else:
			return str(self._inputParameters[18])

	SPB_L_Name = property(fget=get_SPB_L_Name)

	def FMSAL_L(self, index):
		if self._parCnIn[19] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[19], index)
		else:
			return self._inputParameters[19]

	def Save_FMSAL_L(self, index, value):
		if self._parCnIn[19] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[19], index, float(value))
		else:
			self._IPProxy.SetNumericParam(20, float(value))
			self._inputParameters[19] = float(value)

	def get_FMSAL_L_Name(self):
		if self._parCnIn[19] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[19], 1)
		else:
			return str(self._inputParameters[19])

	FMSAL_L_Name = property(fget=get_FMSAL_L_Name)

	def RWI(self, index):
		if self._parCnIn[20] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[20], index)
		else:
			return self._inputParameters[20]

	def Save_RWI(self, index, value):
		if self._parCnIn[20] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[20], index, float(value))
		else:
			self._IPProxy.SetNumericParam(21, float(value))
			self._inputParameters[20] = float(value)

	def get_RWI_Name(self):
		if self._parCnIn[20] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[20], 1)
		else:
			return str(self._inputParameters[20])

	RWI_Name = property(fget=get_RWI_Name)

	def T_RWI(self, index):
		if self._parCnIn[21] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[21], index)
		else:
			return self._inputParameters[21]

	def Save_T_RWI(self, index, value):
		if self._parCnIn[21] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[21], index, float(value))
		else:
			self._IPProxy.SetNumericParam(22, float(value))
			self._inputParameters[21] = float(value)

	def get_T_RWI_Name(self):
		if self._parCnIn[21] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[21], 1)
		else:
			return str(self._inputParameters[21])

	T_RWI_Name = property(fget=get_T_RWI_Name)

	def RHOFL(self, index):
		if self._parCnIn[22] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[22], index)
		else:
			return self._inputParameters[22]

	def Save_RHOFL(self, index, value):
		if self._parCnIn[22] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[22], index, float(value))
		else:
			self._IPProxy.SetNumericParam(23, float(value))
			self._inputParameters[22] = float(value)

	def get_RHOFL_Name(self):
		if self._parCnIn[22] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[22], 1)
		else:
			return str(self._inputParameters[22])

	RHOFL_Name = property(fget=get_RHOFL_Name)

	def VSH_IP(self, index):
		if self._parCnIn[23] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[23], index)
		else:
			return self._inputParameters[23]

	def Save_VSH_IP(self, index, value):
		if self._parCnIn[23] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[23], index, float(value))
		else:
			self._IPProxy.SetNumericParam(24, float(value))
			self._inputParameters[23] = float(value)

	def get_VSH_IP_Name(self):
		if self._parCnIn[23] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[23], 1)
		else:
			return str(self._inputParameters[23])

	VSH_IP_Name = property(fget=get_VSH_IP_Name)

	def VSHCO(self, index):
		if self._parCnIn[24] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[24], index)
		else:
			return self._inputParameters[24]

	def Save_VSHCO(self, index, value):
		if self._parCnIn[24] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[24], index, float(value))
		else:
			self._IPProxy.SetNumericParam(25, float(value))
			self._inputParameters[24] = float(value)

	def get_VSHCO_Name(self):
		if self._parCnIn[24] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[24], 1)
		else:
			return str(self._inputParameters[24])

	VSHCO_Name = property(fget=get_VSHCO_Name)

	def PHIECO(self, index):
		if self._parCnIn[25] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[25], index)
		else:
			return self._inputParameters[25]

	def Save_PHIECO(self, index, value):
		if self._parCnIn[25] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[25], index, float(value))
		else:
			self._IPProxy.SetNumericParam(26, float(value))
			self._inputParameters[25] = float(value)

	def get_PHIECO_Name(self):
		if self._parCnIn[25] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[25], 1)
		else:
			return str(self._inputParameters[25])

	PHIECO_Name = property(fget=get_PHIECO_Name)

	def PHITCO(self, index):
		if self._parCnIn[26] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[26], index)
		else:
			return self._inputParameters[26]

	def Save_PHITCO(self, index, value):
		if self._parCnIn[26] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[26], index, float(value))
		else:
			self._IPProxy.SetNumericParam(27, float(value))
			self._inputParameters[26] = float(value)

	def get_PHITCO_Name(self):
		if self._parCnIn[26] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[26], 1)
		else:
			return str(self._inputParameters[26])

	PHITCO_Name = property(fget=get_PHITCO_Name)

	def SWTCO(self, index):
		if self._parCnIn[27] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[27], index)
		else:
			return self._inputParameters[27]

	def Save_SWTCO(self, index, value):
		if self._parCnIn[27] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[27], index, float(value))
		else:
			self._IPProxy.SetNumericParam(28, float(value))
			self._inputParameters[27] = float(value)

	def get_SWTCO_Name(self):
		if self._parCnIn[27] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[27], 1)
		else:
			return str(self._inputParameters[27])

	SWTCO_Name = property(fget=get_SWTCO_Name)

	def DTM(self, index):
		if self._parCnIn[28] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[28], index)
		else:
			return self._inputParameters[28]

	def Save_DTM(self, index, value):
		if self._parCnIn[28] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[28], index, float(value))
		else:
			self._IPProxy.SetNumericParam(29, float(value))
			self._inputParameters[28] = float(value)

	def get_DTM_Name(self):
		if self._parCnIn[28] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[28], 1)
		else:
			return str(self._inputParameters[28])

	DTM_Name = property(fget=get_DTM_Name)

	def DTF(self, index):
		if self._parCnIn[29] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[29], index)
		else:
			return self._inputParameters[29]

	def Save_DTF(self, index, value):
		if self._parCnIn[29] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[29], index, float(value))
		else:
			self._IPProxy.SetNumericParam(30, float(value))
			self._inputParameters[29] = float(value)

	def get_DTF_Name(self):
		if self._parCnIn[29] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[29], 1)
		else:
			return str(self._inputParameters[29])

	DTF_Name = property(fget=get_DTF_Name)

	def DTSH(self, index):
		if self._parCnIn[30] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[30], index)
		else:
			return self._inputParameters[30]

	def Save_DTSH(self, index, value):
		if self._parCnIn[30] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[30], index, float(value))
		else:
			self._IPProxy.SetNumericParam(31, float(value))
			self._inputParameters[30] = float(value)

	def get_DTSH_Name(self):
		if self._parCnIn[30] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[30], 1)
		else:
			return str(self._inputParameters[30])

	DTSH_Name = property(fget=get_DTSH_Name)

	def CF(self, index):
		if self._parCnIn[31] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[31], index)
		else:
			return self._inputParameters[31]

	def Save_CF(self, index, value):
		if self._parCnIn[31] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[31], index, float(value))
		else:
			self._IPProxy.SetNumericParam(32, float(value))
			self._inputParameters[31] = float(value)

	def get_CF_Name(self):
		if self._parCnIn[31] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[31], 1)
		else:
			return str(self._inputParameters[31])

	CF_Name = property(fget=get_CF_Name)

	def A(self, index):
		if self._parCnIn[32] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[32], index)
		else:
			return self._inputParameters[32]

	def Save_A(self, index, value):
		if self._parCnIn[32] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[32], index, float(value))
		else:
			self._IPProxy.SetNumericParam(33, float(value))
			self._inputParameters[32] = float(value)

	def get_A_Name(self):
		if self._parCnIn[32] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[32], 1)
		else:
			return str(self._inputParameters[32])

	A_Name = property(fget=get_A_Name)

	def M(self, index):
		if self._parCnIn[33] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[33], index)
		else:
			return self._inputParameters[33]

	def Save_M(self, index, value):
		if self._parCnIn[33] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[33], index, float(value))
		else:
			self._IPProxy.SetNumericParam(34, float(value))
			self._inputParameters[33] = float(value)

	def get_M_Name(self):
		if self._parCnIn[33] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[33], 1)
		else:
			return str(self._inputParameters[33])

	M_Name = property(fget=get_M_Name)

	def N(self, index):
		if self._parCnIn[34] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[34], index)
		else:
			return self._inputParameters[34]

	def Save_N(self, index, value):
		if self._parCnIn[34] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[34], index, float(value))
		else:
			self._IPProxy.SetNumericParam(35, float(value))
			self._inputParameters[34] = float(value)

	def get_N_Name(self):
		if self._parCnIn[34] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[34], 1)
		else:
			return str(self._inputParameters[34])

	N_Name = property(fget=get_N_Name)

	def Z(self, index):
		if self._parCnIn[35] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[35], index)
		else:
			return self._inputParameters[35]

	def Save_Z(self, index, value):
		if self._parCnIn[35] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[35], index, float(value))
		else:
			self._IPProxy.SetNumericParam(36, float(value))
			self._inputParameters[35] = float(value)

	def get_Z_Name(self):
		if self._parCnIn[35] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[35], 1)
		else:
			return str(self._inputParameters[35])

	Z_Name = property(fget=get_Z_Name)

	def a1(self, index):
		if self._parCnIn[36] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[36], index)
		else:
			return self._inputParameters[36]

	def Save_a1(self, index, value):
		if self._parCnIn[36] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[36], index, float(value))
		else:
			self._IPProxy.SetNumericParam(37, float(value))
			self._inputParameters[36] = float(value)

	def get_a1_Name(self):
		if self._parCnIn[36] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[36], 1)
		else:
			return str(self._inputParameters[36])

	a1_Name = property(fget=get_a1_Name)

	def b1(self, index):
		if self._parCnIn[37] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[37], index)
		else:
			return self._inputParameters[37]

	def Save_b1(self, index, value):
		if self._parCnIn[37] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[37], index, float(value))
		else:
			self._IPProxy.SetNumericParam(38, float(value))
			self._inputParameters[37] = float(value)

	def get_b1_Name(self):
		if self._parCnIn[37] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[37], 1)
		else:
			return str(self._inputParameters[37])

	b1_Name = property(fget=get_b1_Name)

	def SHRT(self, index):
		if self._parCnIn[38] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[38], index)
		else:
			return self._inputParameters[38]

	def Save_SHRT(self, index, value):
		if self._parCnIn[38] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[38], index, float(value))
		else:
			self._IPProxy.SetNumericParam(39, float(value))
			self._inputParameters[38] = float(value)

	def get_SHRT_Name(self):
		if self._parCnIn[38] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[38], 1)
		else:
			return str(self._inputParameters[38])

	SHRT_Name = property(fget=get_SHRT_Name)

	def FRAC_NPHI(self, index):
		if self._parCnIn[39] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[39], index)
		else:
			return self._inputParameters[39]

	def Save_FRAC_NPHI(self, index, value):
		if self._parCnIn[39] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[39], index, float(value))
		else:
			self._IPProxy.SetNumericParam(40, float(value))
			self._inputParameters[39] = float(value)

	def get_FRAC_NPHI_Name(self):
		if self._parCnIn[39] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[39], 1)
		else:
			return str(self._inputParameters[39])

	FRAC_NPHI_Name = property(fget=get_FRAC_NPHI_Name)

	def RHOGA(self, index):
		if self._parCnIn[40] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[40], index)
		else:
			return self._inputParameters[40]

	def Save_RHOGA(self, index, value):
		if self._parCnIn[40] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[40], index, float(value))
		else:
			self._IPProxy.SetNumericParam(41, float(value))
			self._inputParameters[40] = float(value)

	def get_RHOGA_Name(self):
		if self._parCnIn[40] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[40], 1)
		else:
			return str(self._inputParameters[40])

	RHOGA_Name = property(fget=get_RHOGA_Name)

	def V_KAO(self, index):
		if self._parCnIn[41] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[41], index)
		else:
			return self._inputParameters[41]

	def Save_V_KAO(self, index, value):
		if self._parCnIn[41] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[41], index, float(value))
		else:
			self._IPProxy.SetNumericParam(42, float(value))
			self._inputParameters[41] = float(value)

	def get_V_KAO_Name(self):
		if self._parCnIn[41] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[41], 1)
		else:
			return str(self._inputParameters[41])

	V_KAO_Name = property(fget=get_V_KAO_Name)

	def V_CH(self, index):
		if self._parCnIn[42] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[42], index)
		else:
			return self._inputParameters[42]

	def Save_V_CH(self, index, value):
		if self._parCnIn[42] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[42], index, float(value))
		else:
			self._IPProxy.SetNumericParam(43, float(value))
			self._inputParameters[42] = float(value)

	def get_V_CH_Name(self):
		if self._parCnIn[42] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[42], 1)
		else:
			return str(self._inputParameters[42])

	V_CH_Name = property(fget=get_V_CH_Name)

	def V_SMC(self, index):
		if self._parCnIn[43] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[43], index)
		else:
			return self._inputParameters[43]

	def Save_V_SMC(self, index, value):
		if self._parCnIn[43] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[43], index, float(value))
		else:
			self._IPProxy.SetNumericParam(44, float(value))
			self._inputParameters[43] = float(value)

	def get_V_SMC_Name(self):
		if self._parCnIn[43] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[43], 1)
		else:
			return str(self._inputParameters[43])

	V_SMC_Name = property(fget=get_V_SMC_Name)

	def SWIRR(self, index):
		if self._parCnIn[44] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[44], index)
		else:
			return self._inputParameters[44]

	def Save_SWIRR(self, index, value):
		if self._parCnIn[44] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[44], index, float(value))
		else:
			self._IPProxy.SetNumericParam(45, float(value))
			self._inputParameters[44] = float(value)

	def get_SWIRR_Name(self):
		if self._parCnIn[44] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[44], 1)
		else:
			return str(self._inputParameters[44])

	SWIRR_Name = property(fget=get_SWIRR_Name)

	def RHOGL(self, index):
		if self._parCnIn[45] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[45], index)
		else:
			return self._inputParameters[45]

	def Save_RHOGL(self, index, value):
		if self._parCnIn[45] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[45], index, float(value))
		else:
			self._IPProxy.SetNumericParam(46, float(value))
			self._inputParameters[45] = float(value)

	def get_RHOGL_Name(self):
		if self._parCnIn[45] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[45], 1)
		else:
			return str(self._inputParameters[45])

	RHOGL_Name = property(fget=get_RHOGL_Name)

	def RHOGU(self, index):
		if self._parCnIn[46] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[46], index)
		else:
			return self._inputParameters[46]

	def Save_RHOGU(self, index, value):
		if self._parCnIn[46] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[46], index, float(value))
		else:
			self._IPProxy.SetNumericParam(47, float(value))
			self._inputParameters[46] = float(value)

	def get_RHOGU_Name(self):
		if self._parCnIn[46] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[46], 1)
		else:
			return str(self._inputParameters[46])

	RHOGU_Name = property(fget=get_RHOGU_Name)

	def RHOHC(self, index):
		if self._parCnIn[47] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[47], index)
		else:
			return self._inputParameters[47]

	def Save_RHOHC(self, index, value):
		if self._parCnIn[47] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[47], index, float(value))
		else:
			self._IPProxy.SetNumericParam(48, float(value))
			self._inputParameters[47] = float(value)

	def get_RHOHC_Name(self):
		if self._parCnIn[47] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[47], 1)
		else:
			return str(self._inputParameters[47])

	RHOHC_Name = property(fget=get_RHOHC_Name)

	def SAND_FRAC(self, index):
		if self._parCnIn[48] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[48], index)
		else:
			return self._inputParameters[48]

	def Save_SAND_FRAC(self, index, value):
		if self._parCnIn[48] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[48], index, float(value))
		else:
			self._IPProxy.SetNumericParam(49, float(value))
			self._inputParameters[48] = float(value)

	def get_SAND_FRAC_Name(self):
		if self._parCnIn[48] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[48], 1)
		else:
			return str(self._inputParameters[48])

	SAND_FRAC_Name = property(fget=get_SAND_FRAC_Name)

	def CLAY_FRAC(self, index):
		if self._parCnIn[49] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[49], index)
		else:
			return self._inputParameters[49]

	def Save_CLAY_FRAC(self, index, value):
		if self._parCnIn[49] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[49], index, float(value))
		else:
			self._IPProxy.SetNumericParam(50, float(value))
			self._inputParameters[49] = float(value)

	def get_CLAY_FRAC_Name(self):
		if self._parCnIn[49] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[49], 1)
		else:
			return str(self._inputParameters[49])

	CLAY_FRAC_Name = property(fget=get_CLAY_FRAC_Name)

	def GRD_CLAY(self, index):
		if self._parCnIn[50] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[50], index)
		else:
			return self._inputParameters[50]

	def Save_GRD_CLAY(self, index, value):
		if self._parCnIn[50] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[50], index, float(value))
		else:
			self._IPProxy.SetNumericParam(51, float(value))
			self._inputParameters[50] = float(value)

	def get_GRD_CLAY_Name(self):
		if self._parCnIn[50] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[50], 1)
		else:
			return str(self._inputParameters[50])

	GRD_CLAY_Name = property(fget=get_GRD_CLAY_Name)

	def get_FLAG_LITH(self):
		return self._textInputParameters[0]

	FLAG_LITH = property(fget=get_FLAG_LITH)

	def get_OPT_TEMPLOG(self):
		return self._textInputParameters[1]

	OPT_TEMPLOG = property(fget=get_OPT_TEMPLOG)

	def get_OPT_TEMP_UNITS(self):
		return self._textInputParameters[2]

	OPT_TEMP_UNITS = property(fget=get_OPT_TEMP_UNITS)

	def get_OPT_SONIC_METHOD(self):
		return self._textInputParameters[3]

	OPT_SONIC_METHOD = property(fget=get_OPT_SONIC_METHOD)

	def get_OPT_VSH(self):
		return self._textInputParameters[4]

	OPT_VSH = property(fget=get_OPT_VSH)

	def get_OPT_VSH_CORR(self):
		return self._textInputParameters[5]

	OPT_VSH_CORR = property(fget=get_OPT_VSH_CORR)

	def get_OPT_RW(self):
		return self._textInputParameters[6]

	OPT_RW = property(fget=get_OPT_RW)

	def get_OPT_MUD_TYPE(self):
		return self._textInputParameters[7]

	OPT_MUD_TYPE = property(fget=get_OPT_MUD_TYPE)

	def get_OPT_SW_TECH(self):
		return self._textInputParameters[8]

	OPT_SW_TECH = property(fget=get_OPT_SW_TECH)

	def get_OPT_RXO(self):
		return self._textInputParameters[9]

	OPT_RXO = property(fget=get_OPT_RXO)

	def get_OPT_CLAY_SILT(self):
		return self._textInputParameters[10]

	OPT_CLAY_SILT = property(fget=get_OPT_CLAY_SILT)

	def get_FLAG_VOLC(self):
		return self._flagInputParameters[0]

	FLAG_VOLC = property(fget=get_FLAG_VOLC)

	def get_FLAG_COAL(self):
		return self._flagInputParameters[1]

	FLAG_COAL = property(fget=get_FLAG_COAL)

