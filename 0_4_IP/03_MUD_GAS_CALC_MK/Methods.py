# /***********************************************/
#  * File dynamically created from IP: 10/26/2022 14:59:06
#  * DO NOT MANUALLY EDIT
# /***********************************************/

class Methods:
	def __init__(self):
		self._FIRST_AVAILABLE_LOG_RUN = -1
		self._LAST_AVAILABLE_LOG_RUN = -2

	def Depth(self, index):
		return self._IPProxy.GetCurveData(1, index)

	def C1(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[0],0, index, True)

	def Array_C1(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[0],0, index, xVal, yVal, True)

	def C1_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[0], index)

	def Array_C1_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[0], index, xVal, yVal)

	def get_C1_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 1)

	C1_Name = property(fget=get_C1_Name)

	def get_C1_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 2)

	C1_Units = property(fget=get_C1_Units)

	def get_C1_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 3)

	C1_Comments = property(fget=get_C1_Comments)

	def Save_C1_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[0], 3, str(newValue))

	def Get_C1_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[0], attributeName)

	def Set_C1_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[0], attributeName, str(newValue))

	def Save_C1(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[0], index, float(value))

	def Save_Array_C1(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[0], index, float(value), xVal, yVal)

	def Save_C1_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[0], index, str(value))

	def Save_Array_C1_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[0], index, str(value), xVal, yVal)

	def get_Array_C1_MaxX(self):
		return self._inArrayX[0]

	Array_C1_MaxX = property(fget=get_Array_C1_MaxX)

	def get_Array_C1_MaxY(self):
		return self._inArrayY[0]

	Array_C1_MaxY = property(fget=get_Array_C1_MaxY)

	def C2(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[1],1, index, True)

	def Array_C2(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[1],1, index, xVal, yVal, True)

	def C2_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[1], index)

	def Array_C2_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[1], index, xVal, yVal)

	def get_C2_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 1)

	C2_Name = property(fget=get_C2_Name)

	def get_C2_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 2)

	C2_Units = property(fget=get_C2_Units)

	def get_C2_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 3)

	C2_Comments = property(fget=get_C2_Comments)

	def Save_C2_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[1], 3, str(newValue))

	def Get_C2_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[1], attributeName)

	def Set_C2_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[1], attributeName, str(newValue))

	def Save_C2(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[1], index, float(value))

	def Save_Array_C2(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[1], index, float(value), xVal, yVal)

	def Save_C2_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[1], index, str(value))

	def Save_Array_C2_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[1], index, str(value), xVal, yVal)

	def get_Array_C2_MaxX(self):
		return self._inArrayX[1]

	Array_C2_MaxX = property(fget=get_Array_C2_MaxX)

	def get_Array_C2_MaxY(self):
		return self._inArrayY[1]

	Array_C2_MaxY = property(fget=get_Array_C2_MaxY)

	def C3(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[2],2, index, True)

	def Array_C3(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[2],2, index, xVal, yVal, True)

	def C3_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[2], index)

	def Array_C3_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[2], index, xVal, yVal)

	def get_C3_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 1)

	C3_Name = property(fget=get_C3_Name)

	def get_C3_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 2)

	C3_Units = property(fget=get_C3_Units)

	def get_C3_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 3)

	C3_Comments = property(fget=get_C3_Comments)

	def Save_C3_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[2], 3, str(newValue))

	def Get_C3_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[2], attributeName)

	def Set_C3_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[2], attributeName, str(newValue))

	def Save_C3(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[2], index, float(value))

	def Save_Array_C3(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[2], index, float(value), xVal, yVal)

	def Save_C3_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[2], index, str(value))

	def Save_Array_C3_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[2], index, str(value), xVal, yVal)

	def get_Array_C3_MaxX(self):
		return self._inArrayX[2]

	Array_C3_MaxX = property(fget=get_Array_C3_MaxX)

	def get_Array_C3_MaxY(self):
		return self._inArrayY[2]

	Array_C3_MaxY = property(fget=get_Array_C3_MaxY)

	def IC4(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[3],3, index, True)

	def Array_IC4(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[3],3, index, xVal, yVal, True)

	def IC4_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[3], index)

	def Array_IC4_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[3], index, xVal, yVal)

	def get_IC4_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 1)

	IC4_Name = property(fget=get_IC4_Name)

	def get_IC4_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 2)

	IC4_Units = property(fget=get_IC4_Units)

	def get_IC4_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 3)

	IC4_Comments = property(fget=get_IC4_Comments)

	def Save_IC4_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[3], 3, str(newValue))

	def Get_IC4_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[3], attributeName)

	def Set_IC4_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[3], attributeName, str(newValue))

	def Save_IC4(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[3], index, float(value))

	def Save_Array_IC4(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[3], index, float(value), xVal, yVal)

	def Save_IC4_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[3], index, str(value))

	def Save_Array_IC4_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[3], index, str(value), xVal, yVal)

	def get_Array_IC4_MaxX(self):
		return self._inArrayX[3]

	Array_IC4_MaxX = property(fget=get_Array_IC4_MaxX)

	def get_Array_IC4_MaxY(self):
		return self._inArrayY[3]

	Array_IC4_MaxY = property(fget=get_Array_IC4_MaxY)

	def NC4(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[4],4, index, True)

	def Array_NC4(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[4],4, index, xVal, yVal, True)

	def NC4_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[4], index)

	def Array_NC4_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[4], index, xVal, yVal)

	def get_NC4_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 1)

	NC4_Name = property(fget=get_NC4_Name)

	def get_NC4_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 2)

	NC4_Units = property(fget=get_NC4_Units)

	def get_NC4_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 3)

	NC4_Comments = property(fget=get_NC4_Comments)

	def Save_NC4_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[4], 3, str(newValue))

	def Get_NC4_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[4], attributeName)

	def Set_NC4_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[4], attributeName, str(newValue))

	def Save_NC4(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[4], index, float(value))

	def Save_Array_NC4(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[4], index, float(value), xVal, yVal)

	def Save_NC4_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[4], index, str(value))

	def Save_Array_NC4_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[4], index, str(value), xVal, yVal)

	def get_Array_NC4_MaxX(self):
		return self._inArrayX[4]

	Array_NC4_MaxX = property(fget=get_Array_NC4_MaxX)

	def get_Array_NC4_MaxY(self):
		return self._inArrayY[4]

	Array_NC4_MaxY = property(fget=get_Array_NC4_MaxY)

	def IC5(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[5],5, index, True)

	def Array_IC5(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[5],5, index, xVal, yVal, True)

	def IC5_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[5], index)

	def Array_IC5_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[5], index, xVal, yVal)

	def get_IC5_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 1)

	IC5_Name = property(fget=get_IC5_Name)

	def get_IC5_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 2)

	IC5_Units = property(fget=get_IC5_Units)

	def get_IC5_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 3)

	IC5_Comments = property(fget=get_IC5_Comments)

	def Save_IC5_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[5], 3, str(newValue))

	def Get_IC5_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[5], attributeName)

	def Set_IC5_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[5], attributeName, str(newValue))

	def Save_IC5(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[5], index, float(value))

	def Save_Array_IC5(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[5], index, float(value), xVal, yVal)

	def Save_IC5_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[5], index, str(value))

	def Save_Array_IC5_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[5], index, str(value), xVal, yVal)

	def get_Array_IC5_MaxX(self):
		return self._inArrayX[5]

	Array_IC5_MaxX = property(fget=get_Array_IC5_MaxX)

	def get_Array_IC5_MaxY(self):
		return self._inArrayY[5]

	Array_IC5_MaxY = property(fget=get_Array_IC5_MaxY)

	def NC5(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[6],6, index, True)

	def Array_NC5(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[6],6, index, xVal, yVal, True)

	def NC5_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[6], index)

	def Array_NC5_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[6], index, xVal, yVal)

	def get_NC5_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[6], 1)

	NC5_Name = property(fget=get_NC5_Name)

	def get_NC5_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[6], 2)

	NC5_Units = property(fget=get_NC5_Units)

	def get_NC5_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[6], 3)

	NC5_Comments = property(fget=get_NC5_Comments)

	def Save_NC5_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[6], 3, str(newValue))

	def Get_NC5_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[6], attributeName)

	def Set_NC5_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[6], attributeName, str(newValue))

	def Save_NC5(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[6], index, float(value))

	def Save_Array_NC5(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[6], index, float(value), xVal, yVal)

	def Save_NC5_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[6], index, str(value))

	def Save_Array_NC5_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[6], index, str(value), xVal, yVal)

	def get_Array_NC5_MaxX(self):
		return self._inArrayX[6]

	Array_NC5_MaxX = property(fget=get_Array_NC5_MaxX)

	def get_Array_NC5_MaxY(self):
		return self._inArrayY[6]

	Array_NC5_MaxY = property(fget=get_Array_NC5_MaxY)

	def Save_FLAG(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, float(value))

	def Save_Array_FLAG(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, float(value), xVal, yVal)

	def Save_FLAG_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, str(value))

	def Save_Array_FLAG_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, str(value), xVal, yVal)

	def FLAG(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[0], index)

	def Array_FLAG(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[0], index, xVal, yVal)

	def FLAG_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[0], index)

	def Array_FLAG_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[0], index, xVal, yVal)

	def get_FLAG_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 1)

	FLAG_Name = property(fget=get_FLAG_Name)

	def get_FLAG_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 2)

	FLAG_Units = property(fget=get_FLAG_Units)

	def get_FLAG_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 3)

	FLAG_Comments = property(fget=get_FLAG_Comments)

	def Save_FLAG_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[0], 3, str(newValue))

	def get_Array_FLAG_MaxX(self):
		return self._outArrayX[0]

	Array_FLAG_MaxX = property(fget=get_Array_FLAG_MaxX)

	def get_Array_FLAG_MaxY(self):
		return self._outArrayY[0]

	Array_FLAG_MaxY = property(fget=get_Array_FLAG_MaxY)

	def Get_FLAG_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[0], attributeName)

	def Set_FLAG_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[0], attributeName, str(newValue))

	def Save_FLAG_HC(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value))

	def Save_Array_FLAG_HC(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value), xVal, yVal)

	def Save_FLAG_HC_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value))

	def Save_Array_FLAG_HC_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value), xVal, yVal)

	def FLAG_HC(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[1], index)

	def Array_FLAG_HC(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[1], index, xVal, yVal)

	def FLAG_HC_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[1], index)

	def Array_FLAG_HC_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[1], index, xVal, yVal)

	def get_FLAG_HC_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 1)

	FLAG_HC_Name = property(fget=get_FLAG_HC_Name)

	def get_FLAG_HC_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 2)

	FLAG_HC_Units = property(fget=get_FLAG_HC_Units)

	def get_FLAG_HC_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 3)

	FLAG_HC_Comments = property(fget=get_FLAG_HC_Comments)

	def Save_FLAG_HC_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[1], 3, str(newValue))

	def get_Array_FLAG_HC_MaxX(self):
		return self._outArrayX[1]

	Array_FLAG_HC_MaxX = property(fget=get_Array_FLAG_HC_MaxX)

	def get_Array_FLAG_HC_MaxY(self):
		return self._outArrayY[1]

	Array_FLAG_HC_MaxY = property(fget=get_Array_FLAG_HC_MaxY)

	def Get_FLAG_HC_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[1], attributeName)

	def Set_FLAG_HC_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[1], attributeName, str(newValue))

	def Save_Bh(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, float(value))

	def Save_Array_Bh(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, float(value), xVal, yVal)

	def Save_Bh_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, str(value))

	def Save_Array_Bh_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, str(value), xVal, yVal)

	def Bh(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[2], index)

	def Array_Bh(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[2], index, xVal, yVal)

	def Bh_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[2], index)

	def Array_Bh_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[2], index, xVal, yVal)

	def get_Bh_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 1)

	Bh_Name = property(fget=get_Bh_Name)

	def get_Bh_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 2)

	Bh_Units = property(fget=get_Bh_Units)

	def get_Bh_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 3)

	Bh_Comments = property(fget=get_Bh_Comments)

	def Save_Bh_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[2], 3, str(newValue))

	def get_Array_Bh_MaxX(self):
		return self._outArrayX[2]

	Array_Bh_MaxX = property(fget=get_Array_Bh_MaxX)

	def get_Array_Bh_MaxY(self):
		return self._outArrayY[2]

	Array_Bh_MaxY = property(fget=get_Array_Bh_MaxY)

	def Get_Bh_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[2], attributeName)

	def Set_Bh_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[2], attributeName, str(newValue))

	def Save_Wh(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, float(value))

	def Save_Array_Wh(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, float(value), xVal, yVal)

	def Save_Wh_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, str(value))

	def Save_Array_Wh_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, str(value), xVal, yVal)

	def Wh(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[3], index)

	def Array_Wh(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[3], index, xVal, yVal)

	def Wh_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[3], index)

	def Array_Wh_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[3], index, xVal, yVal)

	def get_Wh_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 1)

	Wh_Name = property(fget=get_Wh_Name)

	def get_Wh_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 2)

	Wh_Units = property(fget=get_Wh_Units)

	def get_Wh_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 3)

	Wh_Comments = property(fget=get_Wh_Comments)

	def Save_Wh_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[3], 3, str(newValue))

	def get_Array_Wh_MaxX(self):
		return self._outArrayX[3]

	Array_Wh_MaxX = property(fget=get_Array_Wh_MaxX)

	def get_Array_Wh_MaxY(self):
		return self._outArrayY[3]

	Array_Wh_MaxY = property(fget=get_Array_Wh_MaxY)

	def Get_Wh_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[3], attributeName)

	def Set_Wh_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[3], attributeName, str(newValue))

	def Save_Ch(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, float(value))

	def Save_Array_Ch(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, float(value), xVal, yVal)

	def Save_Ch_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, str(value))

	def Save_Array_Ch_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, str(value), xVal, yVal)

	def Ch(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[4], index)

	def Array_Ch(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[4], index, xVal, yVal)

	def Ch_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[4], index)

	def Array_Ch_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[4], index, xVal, yVal)

	def get_Ch_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 1)

	Ch_Name = property(fget=get_Ch_Name)

	def get_Ch_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 2)

	Ch_Units = property(fget=get_Ch_Units)

	def get_Ch_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 3)

	Ch_Comments = property(fget=get_Ch_Comments)

	def Save_Ch_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[4], 3, str(newValue))

	def get_Array_Ch_MaxX(self):
		return self._outArrayX[4]

	Array_Ch_MaxX = property(fget=get_Array_Ch_MaxX)

	def get_Array_Ch_MaxY(self):
		return self._outArrayY[4]

	Array_Ch_MaxY = property(fget=get_Array_Ch_MaxY)

	def Get_Ch_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[4], attributeName)

	def Set_Ch_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[4], attributeName, str(newValue))

	def get_GASUNITS(self):
		return self._textInputParameters[0]

	GASUNITS = property(fget=get_GASUNITS)

