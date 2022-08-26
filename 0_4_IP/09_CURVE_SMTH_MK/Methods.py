# /***********************************************/
#  * File dynamically created from IP: 08/24/2022 15:41:13
#  * DO NOT MANUALLY EDIT
# /***********************************************/

class Methods:
	def __init__(self):
		self._FIRST_AVAILABLE_LOG_RUN = -1
		self._LAST_AVAILABLE_LOG_RUN = -2

	def Depth(self, index):
		return self._IPProxy.GetCurveData(1, index)

	def input(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[0],0, index, True)

	def Array_input(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[0],0, index, xVal, yVal, True)

	def input_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[0], index)

	def Array_input_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[0], index, xVal, yVal)

	def get_input_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 1)

	input_Name = property(fget=get_input_Name)

	def get_input_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 2)

	input_Units = property(fget=get_input_Units)

	def get_input_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 3)

	input_Comments = property(fget=get_input_Comments)

	def Save_input_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[0], 3, str(newValue))

	def Get_input_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[0], attributeName)

	def Set_input_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[0], attributeName, str(newValue))

	def Save_input(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[0], index, float(value))

	def Save_Array_input(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[0], index, float(value), xVal, yVal)

	def Save_input_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[0], index, str(value))

	def Save_Array_input_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[0], index, str(value), xVal, yVal)

	def get_Array_input_MaxX(self):
		return self._inArrayX[0]

	Array_input_MaxX = property(fget=get_Array_input_MaxX)

	def get_Array_input_MaxY(self):
		return self._inArrayY[0]

	Array_input_MaxY = property(fget=get_Array_input_MaxY)

	def Save_OutCurve(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, float(value))

	def Save_Array_OutCurve(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, float(value), xVal, yVal)

	def Save_OutCurve_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, str(value))

	def Save_Array_OutCurve_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, str(value), xVal, yVal)

	def OutCurve(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[0], index)

	def Array_OutCurve(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[0], index, xVal, yVal)

	def OutCurve_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[0], index)

	def Array_OutCurve_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[0], index, xVal, yVal)

	def get_OutCurve_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 1)

	OutCurve_Name = property(fget=get_OutCurve_Name)

	def get_OutCurve_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 2)

	OutCurve_Units = property(fget=get_OutCurve_Units)

	def get_OutCurve_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 3)

	OutCurve_Comments = property(fget=get_OutCurve_Comments)

	def Save_OutCurve_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[0], 3, str(newValue))

	def get_Array_OutCurve_MaxX(self):
		return self._outArrayX[0]

	Array_OutCurve_MaxX = property(fget=get_Array_OutCurve_MaxX)

	def get_Array_OutCurve_MaxY(self):
		return self._outArrayY[0]

	Array_OutCurve_MaxY = property(fget=get_Array_OutCurve_MaxY)

	def Get_OutCurve_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[0], attributeName)

	def Set_OutCurve_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[0], attributeName, str(newValue))

	def Save_SumAbove(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value))

	def Save_Array_SumAbove(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value), xVal, yVal)

	def Save_SumAbove_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value))

	def Save_Array_SumAbove_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value), xVal, yVal)

	def SumAbove(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[1], index)

	def Array_SumAbove(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[1], index, xVal, yVal)

	def SumAbove_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[1], index)

	def Array_SumAbove_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[1], index, xVal, yVal)

	def get_SumAbove_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 1)

	SumAbove_Name = property(fget=get_SumAbove_Name)

	def get_SumAbove_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 2)

	SumAbove_Units = property(fget=get_SumAbove_Units)

	def get_SumAbove_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 3)

	SumAbove_Comments = property(fget=get_SumAbove_Comments)

	def Save_SumAbove_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[1], 3, str(newValue))

	def get_Array_SumAbove_MaxX(self):
		return self._outArrayX[1]

	Array_SumAbove_MaxX = property(fget=get_Array_SumAbove_MaxX)

	def get_Array_SumAbove_MaxY(self):
		return self._outArrayY[1]

	Array_SumAbove_MaxY = property(fget=get_Array_SumAbove_MaxY)

	def Get_SumAbove_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[1], attributeName)

	def Set_SumAbove_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[1], attributeName, str(newValue))

	def Save_SumBelow(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, float(value))

	def Save_Array_SumBelow(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, float(value), xVal, yVal)

	def Save_SumBelow_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, str(value))

	def Save_Array_SumBelow_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, str(value), xVal, yVal)

	def SumBelow(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[2], index)

	def Array_SumBelow(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[2], index, xVal, yVal)

	def SumBelow_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[2], index)

	def Array_SumBelow_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[2], index, xVal, yVal)

	def get_SumBelow_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 1)

	SumBelow_Name = property(fget=get_SumBelow_Name)

	def get_SumBelow_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 2)

	SumBelow_Units = property(fget=get_SumBelow_Units)

	def get_SumBelow_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 3)

	SumBelow_Comments = property(fget=get_SumBelow_Comments)

	def Save_SumBelow_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[2], 3, str(newValue))

	def get_Array_SumBelow_MaxX(self):
		return self._outArrayX[2]

	Array_SumBelow_MaxX = property(fget=get_Array_SumBelow_MaxX)

	def get_Array_SumBelow_MaxY(self):
		return self._outArrayY[2]

	Array_SumBelow_MaxY = property(fget=get_Array_SumBelow_MaxY)

	def Get_SumBelow_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[2], attributeName)

	def Set_SumBelow_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[2], attributeName, str(newValue))

	def Save_SumDiffBelowAbove(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, float(value))

	def Save_Array_SumDiffBelowAbove(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, float(value), xVal, yVal)

	def Save_SumDiffBelowAbove_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, str(value))

	def Save_Array_SumDiffBelowAbove_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, str(value), xVal, yVal)

	def SumDiffBelowAbove(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[3], index)

	def Array_SumDiffBelowAbove(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[3], index, xVal, yVal)

	def SumDiffBelowAbove_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[3], index)

	def Array_SumDiffBelowAbove_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[3], index, xVal, yVal)

	def get_SumDiffBelowAbove_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 1)

	SumDiffBelowAbove_Name = property(fget=get_SumDiffBelowAbove_Name)

	def get_SumDiffBelowAbove_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 2)

	SumDiffBelowAbove_Units = property(fget=get_SumDiffBelowAbove_Units)

	def get_SumDiffBelowAbove_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 3)

	SumDiffBelowAbove_Comments = property(fget=get_SumDiffBelowAbove_Comments)

	def Save_SumDiffBelowAbove_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[3], 3, str(newValue))

	def get_Array_SumDiffBelowAbove_MaxX(self):
		return self._outArrayX[3]

	Array_SumDiffBelowAbove_MaxX = property(fget=get_Array_SumDiffBelowAbove_MaxX)

	def get_Array_SumDiffBelowAbove_MaxY(self):
		return self._outArrayY[3]

	Array_SumDiffBelowAbove_MaxY = property(fget=get_Array_SumDiffBelowAbove_MaxY)

	def Get_SumDiffBelowAbove_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[3], attributeName)

	def Set_SumDiffBelowAbove_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[3], attributeName, str(newValue))

	def Save_DiffBelowAbove(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, float(value))

	def Save_Array_DiffBelowAbove(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, float(value), xVal, yVal)

	def Save_DiffBelowAbove_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, str(value))

	def Save_Array_DiffBelowAbove_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, str(value), xVal, yVal)

	def DiffBelowAbove(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[4], index)

	def Array_DiffBelowAbove(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[4], index, xVal, yVal)

	def DiffBelowAbove_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[4], index)

	def Array_DiffBelowAbove_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[4], index, xVal, yVal)

	def get_DiffBelowAbove_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 1)

	DiffBelowAbove_Name = property(fget=get_DiffBelowAbove_Name)

	def get_DiffBelowAbove_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 2)

	DiffBelowAbove_Units = property(fget=get_DiffBelowAbove_Units)

	def get_DiffBelowAbove_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 3)

	DiffBelowAbove_Comments = property(fget=get_DiffBelowAbove_Comments)

	def Save_DiffBelowAbove_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[4], 3, str(newValue))

	def get_Array_DiffBelowAbove_MaxX(self):
		return self._outArrayX[4]

	Array_DiffBelowAbove_MaxX = property(fget=get_Array_DiffBelowAbove_MaxX)

	def get_Array_DiffBelowAbove_MaxY(self):
		return self._outArrayY[4]

	Array_DiffBelowAbove_MaxY = property(fget=get_Array_DiffBelowAbove_MaxY)

	def Get_DiffBelowAbove_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[4], attributeName)

	def Set_DiffBelowAbove_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[4], attributeName, str(newValue))

	def Save_ProdAbove(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[5], index, float(value))

	def Save_Array_ProdAbove(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[5], index, float(value), xVal, yVal)

	def Save_ProdAbove_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[5], index, str(value))

	def Save_Array_ProdAbove_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[5], index, str(value), xVal, yVal)

	def ProdAbove(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[5], index)

	def Array_ProdAbove(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[5], index, xVal, yVal)

	def ProdAbove_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[5], index)

	def Array_ProdAbove_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[5], index, xVal, yVal)

	def get_ProdAbove_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 1)

	ProdAbove_Name = property(fget=get_ProdAbove_Name)

	def get_ProdAbove_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 2)

	ProdAbove_Units = property(fget=get_ProdAbove_Units)

	def get_ProdAbove_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 3)

	ProdAbove_Comments = property(fget=get_ProdAbove_Comments)

	def Save_ProdAbove_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[5], 3, str(newValue))

	def get_Array_ProdAbove_MaxX(self):
		return self._outArrayX[5]

	Array_ProdAbove_MaxX = property(fget=get_Array_ProdAbove_MaxX)

	def get_Array_ProdAbove_MaxY(self):
		return self._outArrayY[5]

	Array_ProdAbove_MaxY = property(fget=get_Array_ProdAbove_MaxY)

	def Get_ProdAbove_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[5], attributeName)

	def Set_ProdAbove_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[5], attributeName, str(newValue))

	def Save_ProdBelow(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[6], index, float(value))

	def Save_Array_ProdBelow(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[6], index, float(value), xVal, yVal)

	def Save_ProdBelow_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[6], index, str(value))

	def Save_Array_ProdBelow_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[6], index, str(value), xVal, yVal)

	def ProdBelow(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[6], index)

	def Array_ProdBelow(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[6], index, xVal, yVal)

	def ProdBelow_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[6], index)

	def Array_ProdBelow_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[6], index, xVal, yVal)

	def get_ProdBelow_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 1)

	ProdBelow_Name = property(fget=get_ProdBelow_Name)

	def get_ProdBelow_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 2)

	ProdBelow_Units = property(fget=get_ProdBelow_Units)

	def get_ProdBelow_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 3)

	ProdBelow_Comments = property(fget=get_ProdBelow_Comments)

	def Save_ProdBelow_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[6], 3, str(newValue))

	def get_Array_ProdBelow_MaxX(self):
		return self._outArrayX[6]

	Array_ProdBelow_MaxX = property(fget=get_Array_ProdBelow_MaxX)

	def get_Array_ProdBelow_MaxY(self):
		return self._outArrayY[6]

	Array_ProdBelow_MaxY = property(fget=get_Array_ProdBelow_MaxY)

	def Get_ProdBelow_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[6], attributeName)

	def Set_ProdBelow_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[6], attributeName, str(newValue))

	def Save_HarmAbove(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[7], index, float(value))

	def Save_Array_HarmAbove(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[7], index, float(value), xVal, yVal)

	def Save_HarmAbove_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[7], index, str(value))

	def Save_Array_HarmAbove_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[7], index, str(value), xVal, yVal)

	def HarmAbove(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[7], index)

	def Array_HarmAbove(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[7], index, xVal, yVal)

	def HarmAbove_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[7], index)

	def Array_HarmAbove_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[7], index, xVal, yVal)

	def get_HarmAbove_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 1)

	HarmAbove_Name = property(fget=get_HarmAbove_Name)

	def get_HarmAbove_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 2)

	HarmAbove_Units = property(fget=get_HarmAbove_Units)

	def get_HarmAbove_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 3)

	HarmAbove_Comments = property(fget=get_HarmAbove_Comments)

	def Save_HarmAbove_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[7], 3, str(newValue))

	def get_Array_HarmAbove_MaxX(self):
		return self._outArrayX[7]

	Array_HarmAbove_MaxX = property(fget=get_Array_HarmAbove_MaxX)

	def get_Array_HarmAbove_MaxY(self):
		return self._outArrayY[7]

	Array_HarmAbove_MaxY = property(fget=get_Array_HarmAbove_MaxY)

	def Get_HarmAbove_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[7], attributeName)

	def Set_HarmAbove_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[7], attributeName, str(newValue))

	def Save_HarmBelow(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[8], index, float(value))

	def Save_Array_HarmBelow(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[8], index, float(value), xVal, yVal)

	def Save_HarmBelow_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[8], index, str(value))

	def Save_Array_HarmBelow_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[8], index, str(value), xVal, yVal)

	def HarmBelow(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[8], index)

	def Array_HarmBelow(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[8], index, xVal, yVal)

	def HarmBelow_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[8], index)

	def Array_HarmBelow_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[8], index, xVal, yVal)

	def get_HarmBelow_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 1)

	HarmBelow_Name = property(fget=get_HarmBelow_Name)

	def get_HarmBelow_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 2)

	HarmBelow_Units = property(fget=get_HarmBelow_Units)

	def get_HarmBelow_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 3)

	HarmBelow_Comments = property(fget=get_HarmBelow_Comments)

	def Save_HarmBelow_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[8], 3, str(newValue))

	def get_Array_HarmBelow_MaxX(self):
		return self._outArrayX[8]

	Array_HarmBelow_MaxX = property(fget=get_Array_HarmBelow_MaxX)

	def get_Array_HarmBelow_MaxY(self):
		return self._outArrayY[8]

	Array_HarmBelow_MaxY = property(fget=get_Array_HarmBelow_MaxY)

	def Get_HarmBelow_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[8], attributeName)

	def Set_HarmBelow_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[8], attributeName, str(newValue))

	def depthAbove(self, index):
		if self._parCnIn[0] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[0], index)
		else:
			return self._inputParameters[0]

	def Save_depthAbove(self, index, value):
		if self._parCnIn[0] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[0], index, float(value))
		else:
			self._IPProxy.SetNumericParam(1, float(value))
			self._inputParameters[0] = float(value)

	def get_depthAbove_Name(self):
		if self._parCnIn[0] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[0], 1)
		else:
			return str(self._inputParameters[0])

	depthAbove_Name = property(fget=get_depthAbove_Name)

	def depthBelow(self, index):
		if self._parCnIn[1] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[1], index)
		else:
			return self._inputParameters[1]

	def Save_depthBelow(self, index, value):
		if self._parCnIn[1] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[1], index, float(value))
		else:
			self._IPProxy.SetNumericParam(2, float(value))
			self._inputParameters[1] = float(value)

	def get_depthBelow_Name(self):
		if self._parCnIn[1] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[1], 1)
		else:
			return str(self._inputParameters[1])

	depthBelow_Name = property(fget=get_depthBelow_Name)

	def get_OPT_MEAN_MTD(self):
		return self._textInputParameters[0]

	OPT_MEAN_MTD = property(fget=get_OPT_MEAN_MTD)

	def get_nullCheck(self):
		return self._flagInputParameters[0]

	nullCheck = property(fget=get_nullCheck)

