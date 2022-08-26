# /***********************************************/
#  * File dynamically created from IP: 08/24/2022 15:29:25
#  * DO NOT MANUALLY EDIT
# /***********************************************/

class Methods:
	def __init__(self):
		self._FIRST_AVAILABLE_LOG_RUN = -1
		self._LAST_AVAILABLE_LOG_RUN = -2

	def Depth(self, index):
		return self._IPProxy.GetCurveData(1, index)

	def DEPTH_TVDSS(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[0],0, index, True)

	def Array_DEPTH_TVDSS(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[0],0, index, xVal, yVal, True)

	def DEPTH_TVDSS_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[0], index)

	def Array_DEPTH_TVDSS_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[0], index, xVal, yVal)

	def get_DEPTH_TVDSS_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 1)

	DEPTH_TVDSS_Name = property(fget=get_DEPTH_TVDSS_Name)

	def get_DEPTH_TVDSS_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 2)

	DEPTH_TVDSS_Units = property(fget=get_DEPTH_TVDSS_Units)

	def get_DEPTH_TVDSS_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 3)

	DEPTH_TVDSS_Comments = property(fget=get_DEPTH_TVDSS_Comments)

	def Save_DEPTH_TVDSS_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[0], 3, str(newValue))

	def Get_DEPTH_TVDSS_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[0], attributeName)

	def Set_DEPTH_TVDSS_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[0], attributeName, str(newValue))

	def Save_DEPTH_TVDSS(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[0], index, float(value))

	def Save_Array_DEPTH_TVDSS(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[0], index, float(value), xVal, yVal)

	def Save_DEPTH_TVDSS_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[0], index, str(value))

	def Save_Array_DEPTH_TVDSS_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[0], index, str(value), xVal, yVal)

	def get_Array_DEPTH_TVDSS_MaxX(self):
		return self._inArrayX[0]

	Array_DEPTH_TVDSS_MaxX = property(fget=get_Array_DEPTH_TVDSS_MaxX)

	def get_Array_DEPTH_TVDSS_MaxY(self):
		return self._inArrayY[0]

	Array_DEPTH_TVDSS_MaxY = property(fget=get_Array_DEPTH_TVDSS_MaxY)

	def TEMPERATUREOF(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[1],1, index, True)

	def Array_TEMPERATUREOF(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[1],1, index, xVal, yVal, True)

	def TEMPERATUREOF_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[1], index)

	def Array_TEMPERATUREOF_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[1], index, xVal, yVal)

	def get_TEMPERATUREOF_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 1)

	TEMPERATUREOF_Name = property(fget=get_TEMPERATUREOF_Name)

	def get_TEMPERATUREOF_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 2)

	TEMPERATUREOF_Units = property(fget=get_TEMPERATUREOF_Units)

	def get_TEMPERATUREOF_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 3)

	TEMPERATUREOF_Comments = property(fget=get_TEMPERATUREOF_Comments)

	def Save_TEMPERATUREOF_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[1], 3, str(newValue))

	def Get_TEMPERATUREOF_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[1], attributeName)

	def Set_TEMPERATUREOF_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[1], attributeName, str(newValue))

	def Save_TEMPERATUREOF(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[1], index, float(value))

	def Save_Array_TEMPERATUREOF(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[1], index, float(value), xVal, yVal)

	def Save_TEMPERATUREOF_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[1], index, str(value))

	def Save_Array_TEMPERATUREOF_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[1], index, str(value), xVal, yVal)

	def get_Array_TEMPERATUREOF_MaxX(self):
		return self._inArrayX[1]

	Array_TEMPERATUREOF_MaxX = property(fget=get_Array_TEMPERATUREOF_MaxX)

	def get_Array_TEMPERATUREOF_MaxY(self):
		return self._inArrayY[1]

	Array_TEMPERATUREOF_MaxY = property(fget=get_Array_TEMPERATUREOF_MaxY)

	def TEMPERATUREOC(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[2],2, index, True)

	def Array_TEMPERATUREOC(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[2],2, index, xVal, yVal, True)

	def TEMPERATUREOC_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[2], index)

	def Array_TEMPERATUREOC_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[2], index, xVal, yVal)

	def get_TEMPERATUREOC_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 1)

	TEMPERATUREOC_Name = property(fget=get_TEMPERATUREOC_Name)

	def get_TEMPERATUREOC_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 2)

	TEMPERATUREOC_Units = property(fget=get_TEMPERATUREOC_Units)

	def get_TEMPERATUREOC_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 3)

	TEMPERATUREOC_Comments = property(fget=get_TEMPERATUREOC_Comments)

	def Save_TEMPERATUREOC_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[2], 3, str(newValue))

	def Get_TEMPERATUREOC_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[2], attributeName)

	def Set_TEMPERATUREOC_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[2], attributeName, str(newValue))

	def Save_TEMPERATUREOC(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[2], index, float(value))

	def Save_Array_TEMPERATUREOC(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[2], index, float(value), xVal, yVal)

	def Save_TEMPERATUREOC_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[2], index, str(value))

	def Save_Array_TEMPERATUREOC_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[2], index, str(value), xVal, yVal)

	def get_Array_TEMPERATUREOC_MaxX(self):
		return self._inArrayX[2]

	Array_TEMPERATUREOC_MaxX = property(fget=get_Array_TEMPERATUREOC_MaxX)

	def get_Array_TEMPERATUREOC_MaxY(self):
		return self._inArrayY[2]

	Array_TEMPERATUREOC_MaxY = property(fget=get_Array_TEMPERATUREOC_MaxY)

	def GR(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[3],3, index, True)

	def Array_GR(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[3],3, index, xVal, yVal, True)

	def GR_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[3], index)

	def Array_GR_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[3], index, xVal, yVal)

	def get_GR_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 1)

	GR_Name = property(fget=get_GR_Name)

	def get_GR_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 2)

	GR_Units = property(fget=get_GR_Units)

	def get_GR_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 3)

	GR_Comments = property(fget=get_GR_Comments)

	def Save_GR_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[3], 3, str(newValue))

	def Get_GR_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[3], attributeName)

	def Set_GR_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[3], attributeName, str(newValue))

	def Save_GR(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[3], index, float(value))

	def Save_Array_GR(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[3], index, float(value), xVal, yVal)

	def Save_GR_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[3], index, str(value))

	def Save_Array_GR_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[3], index, str(value), xVal, yVal)

	def get_Array_GR_MaxX(self):
		return self._inArrayX[3]

	Array_GR_MaxX = property(fget=get_Array_GR_MaxX)

	def get_Array_GR_MaxY(self):
		return self._inArrayY[3]

	Array_GR_MaxY = property(fget=get_Array_GR_MaxY)

	def RT(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[4],4, index, True)

	def Array_RT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[4],4, index, xVal, yVal, True)

	def RT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[4], index)

	def Array_RT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[4], index, xVal, yVal)

	def get_RT_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 1)

	RT_Name = property(fget=get_RT_Name)

	def get_RT_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 2)

	RT_Units = property(fget=get_RT_Units)

	def get_RT_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 3)

	RT_Comments = property(fget=get_RT_Comments)

	def Save_RT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[4], 3, str(newValue))

	def Get_RT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[4], attributeName)

	def Set_RT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[4], attributeName, str(newValue))

	def Save_RT(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[4], index, float(value))

	def Save_Array_RT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[4], index, float(value), xVal, yVal)

	def Save_RT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[4], index, str(value))

	def Save_Array_RT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[4], index, str(value), xVal, yVal)

	def get_Array_RT_MaxX(self):
		return self._inArrayX[4]

	Array_RT_MaxX = property(fget=get_Array_RT_MaxX)

	def get_Array_RT_MaxY(self):
		return self._inArrayY[4]

	Array_RT_MaxY = property(fget=get_Array_RT_MaxY)

	def NEUT(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[5],5, index, True)

	def Array_NEUT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[5],5, index, xVal, yVal, True)

	def NEUT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[5], index)

	def Array_NEUT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[5], index, xVal, yVal)

	def get_NEUT_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 1)

	NEUT_Name = property(fget=get_NEUT_Name)

	def get_NEUT_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 2)

	NEUT_Units = property(fget=get_NEUT_Units)

	def get_NEUT_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 3)

	NEUT_Comments = property(fget=get_NEUT_Comments)

	def Save_NEUT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[5], 3, str(newValue))

	def Get_NEUT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[5], attributeName)

	def Set_NEUT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[5], attributeName, str(newValue))

	def Save_NEUT(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[5], index, float(value))

	def Save_Array_NEUT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[5], index, float(value), xVal, yVal)

	def Save_NEUT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[5], index, str(value))

	def Save_Array_NEUT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[5], index, str(value), xVal, yVal)

	def get_Array_NEUT_MaxX(self):
		return self._inArrayX[5]

	Array_NEUT_MaxX = property(fget=get_Array_NEUT_MaxX)

	def get_Array_NEUT_MaxY(self):
		return self._inArrayY[5]

	Array_NEUT_MaxY = property(fget=get_Array_NEUT_MaxY)

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

	def Save_VCL(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value))

	def Save_Array_VCL(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value), xVal, yVal)

	def Save_VCL_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value))

	def Save_Array_VCL_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value), xVal, yVal)

	def VCL(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[1], index)

	def Array_VCL(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[1], index, xVal, yVal)

	def VCL_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[1], index)

	def Array_VCL_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[1], index, xVal, yVal)

	def get_VCL_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 1)

	VCL_Name = property(fget=get_VCL_Name)

	def get_VCL_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 2)

	VCL_Units = property(fget=get_VCL_Units)

	def get_VCL_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 3)

	VCL_Comments = property(fget=get_VCL_Comments)

	def Save_VCL_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[1], 3, str(newValue))

	def get_Array_VCL_MaxX(self):
		return self._outArrayX[1]

	Array_VCL_MaxX = property(fget=get_Array_VCL_MaxX)

	def get_Array_VCL_MaxY(self):
		return self._outArrayY[1]

	Array_VCL_MaxY = property(fget=get_Array_VCL_MaxY)

	def Get_VCL_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[1], attributeName)

	def Set_VCL_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[1], attributeName, str(newValue))

	def Save_SLOPE(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, float(value))

	def Save_Array_SLOPE(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, float(value), xVal, yVal)

	def Save_SLOPE_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, str(value))

	def Save_Array_SLOPE_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, str(value), xVal, yVal)

	def SLOPE(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[2], index)

	def Array_SLOPE(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[2], index, xVal, yVal)

	def SLOPE_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[2], index)

	def Array_SLOPE_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[2], index, xVal, yVal)

	def get_SLOPE_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 1)

	SLOPE_Name = property(fget=get_SLOPE_Name)

	def get_SLOPE_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 2)

	SLOPE_Units = property(fget=get_SLOPE_Units)

	def get_SLOPE_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 3)

	SLOPE_Comments = property(fget=get_SLOPE_Comments)

	def Save_SLOPE_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[2], 3, str(newValue))

	def get_Array_SLOPE_MaxX(self):
		return self._outArrayX[2]

	Array_SLOPE_MaxX = property(fget=get_Array_SLOPE_MaxX)

	def get_Array_SLOPE_MaxY(self):
		return self._outArrayY[2]

	Array_SLOPE_MaxY = property(fget=get_Array_SLOPE_MaxY)

	def Get_SLOPE_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[2], attributeName)

	def Set_SLOPE_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[2], attributeName, str(newValue))

	def Save_INTCPT(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, float(value))

	def Save_Array_INTCPT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, float(value), xVal, yVal)

	def Save_INTCPT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, str(value))

	def Save_Array_INTCPT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, str(value), xVal, yVal)

	def INTCPT(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[3], index)

	def Array_INTCPT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[3], index, xVal, yVal)

	def INTCPT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[3], index)

	def Array_INTCPT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[3], index, xVal, yVal)

	def get_INTCPT_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 1)

	INTCPT_Name = property(fget=get_INTCPT_Name)

	def get_INTCPT_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 2)

	INTCPT_Units = property(fget=get_INTCPT_Units)

	def get_INTCPT_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 3)

	INTCPT_Comments = property(fget=get_INTCPT_Comments)

	def Save_INTCPT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[3], 3, str(newValue))

	def get_Array_INTCPT_MaxX(self):
		return self._outArrayX[3]

	Array_INTCPT_MaxX = property(fget=get_Array_INTCPT_MaxX)

	def get_Array_INTCPT_MaxY(self):
		return self._outArrayY[3]

	Array_INTCPT_MaxY = property(fget=get_Array_INTCPT_MaxY)

	def Get_INTCPT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[3], attributeName)

	def Set_INTCPT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[3], attributeName, str(newValue))

	def Save_PHIn(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, float(value))

	def Save_Array_PHIn(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, float(value), xVal, yVal)

	def Save_PHIn_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, str(value))

	def Save_Array_PHIn_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, str(value), xVal, yVal)

	def PHIn(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[4], index)

	def Array_PHIn(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[4], index, xVal, yVal)

	def PHIn_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[4], index)

	def Array_PHIn_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[4], index, xVal, yVal)

	def get_PHIn_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 1)

	PHIn_Name = property(fget=get_PHIn_Name)

	def get_PHIn_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 2)

	PHIn_Units = property(fget=get_PHIn_Units)

	def get_PHIn_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 3)

	PHIn_Comments = property(fget=get_PHIn_Comments)

	def Save_PHIn_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[4], 3, str(newValue))

	def get_Array_PHIn_MaxX(self):
		return self._outArrayX[4]

	Array_PHIn_MaxX = property(fget=get_Array_PHIn_MaxX)

	def get_Array_PHIn_MaxY(self):
		return self._outArrayY[4]

	Array_PHIn_MaxY = property(fget=get_Array_PHIn_MaxY)

	def Get_PHIn_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[4], attributeName)

	def Set_PHIn_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[4], attributeName, str(newValue))

	def Save_PHIE(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[5], index, float(value))

	def Save_Array_PHIE(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[5], index, float(value), xVal, yVal)

	def Save_PHIE_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[5], index, str(value))

	def Save_Array_PHIE_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[5], index, str(value), xVal, yVal)

	def PHIE(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[5], index)

	def Array_PHIE(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[5], index, xVal, yVal)

	def PHIE_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[5], index)

	def Array_PHIE_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[5], index, xVal, yVal)

	def get_PHIE_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 1)

	PHIE_Name = property(fget=get_PHIE_Name)

	def get_PHIE_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 2)

	PHIE_Units = property(fget=get_PHIE_Units)

	def get_PHIE_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 3)

	PHIE_Comments = property(fget=get_PHIE_Comments)

	def Save_PHIE_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[5], 3, str(newValue))

	def get_Array_PHIE_MaxX(self):
		return self._outArrayX[5]

	Array_PHIE_MaxX = property(fget=get_Array_PHIE_MaxX)

	def get_Array_PHIE_MaxY(self):
		return self._outArrayY[5]

	Array_PHIE_MaxY = property(fget=get_Array_PHIE_MaxY)

	def Get_PHIE_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[5], attributeName)

	def Set_PHIE_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[5], attributeName, str(newValue))

	def Save_SWT(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[6], index, float(value))

	def Save_Array_SWT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[6], index, float(value), xVal, yVal)

	def Save_SWT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[6], index, str(value))

	def Save_Array_SWT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[6], index, str(value), xVal, yVal)

	def SWT(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[6], index)

	def Array_SWT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[6], index, xVal, yVal)

	def SWT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[6], index)

	def Array_SWT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[6], index, xVal, yVal)

	def get_SWT_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 1)

	SWT_Name = property(fget=get_SWT_Name)

	def get_SWT_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 2)

	SWT_Units = property(fget=get_SWT_Units)

	def get_SWT_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 3)

	SWT_Comments = property(fget=get_SWT_Comments)

	def Save_SWT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[6], 3, str(newValue))

	def get_Array_SWT_MaxX(self):
		return self._outArrayX[6]

	Array_SWT_MaxX = property(fget=get_Array_SWT_MaxX)

	def get_Array_SWT_MaxY(self):
		return self._outArrayY[6]

	Array_SWT_MaxY = property(fget=get_Array_SWT_MaxY)

	def Get_SWT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[6], attributeName)

	def Set_SWT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[6], attributeName, str(newValue))

	def Save_SWE(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[7], index, float(value))

	def Save_Array_SWE(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[7], index, float(value), xVal, yVal)

	def Save_SWE_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[7], index, str(value))

	def Save_Array_SWE_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[7], index, str(value), xVal, yVal)

	def SWE(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[7], index)

	def Array_SWE(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[7], index, xVal, yVal)

	def SWE_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[7], index)

	def Array_SWE_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[7], index, xVal, yVal)

	def get_SWE_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 1)

	SWE_Name = property(fget=get_SWE_Name)

	def get_SWE_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 2)

	SWE_Units = property(fget=get_SWE_Units)

	def get_SWE_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 3)

	SWE_Comments = property(fget=get_SWE_Comments)

	def Save_SWE_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[7], 3, str(newValue))

	def get_Array_SWE_MaxX(self):
		return self._outArrayX[7]

	Array_SWE_MaxX = property(fget=get_Array_SWE_MaxX)

	def get_Array_SWE_MaxY(self):
		return self._outArrayY[7]

	Array_SWE_MaxY = property(fget=get_Array_SWE_MaxY)

	def Get_SWE_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[7], attributeName)

	def Set_SWE_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[7], attributeName, str(newValue))

	def PHIHI(self, index):
		if self._parCnIn[0] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[0], index)
		else:
			return self._inputParameters[0]

	def Save_PHIHI(self, index, value):
		if self._parCnIn[0] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[0], index, float(value))
		else:
			self._IPProxy.SetNumericParam(1, float(value))
			self._inputParameters[0] = float(value)

	def get_PHIHI_Name(self):
		if self._parCnIn[0] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[0], 1)
		else:
			return str(self._inputParameters[0])

	PHIHI_Name = property(fget=get_PHIHI_Name)

	def PHILO(self, index):
		if self._parCnIn[1] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[1], index)
		else:
			return self._inputParameters[1]

	def Save_PHILO(self, index, value):
		if self._parCnIn[1] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[1], index, float(value))
		else:
			self._IPProxy.SetNumericParam(2, float(value))
			self._inputParameters[1] = float(value)

	def get_PHILO_Name(self):
		if self._parCnIn[1] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[1], 1)
		else:
			return str(self._inputParameters[1])

	PHILO_Name = property(fget=get_PHILO_Name)

	def MULT(self, index):
		if self._parCnIn[2] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[2], index)
		else:
			return self._inputParameters[2]

	def Save_MULT(self, index, value):
		if self._parCnIn[2] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[2], index, float(value))
		else:
			self._IPProxy.SetNumericParam(3, float(value))
			self._inputParameters[2] = float(value)

	def get_MULT_Name(self):
		if self._parCnIn[2] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[2], 1)
		else:
			return str(self._inputParameters[2])

	MULT_Name = property(fget=get_MULT_Name)

	def CPSHI(self, index):
		if self._parCnIn[3] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[3], index)
		else:
			return self._inputParameters[3]

	def Save_CPSHI(self, index, value):
		if self._parCnIn[3] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[3], index, float(value))
		else:
			self._IPProxy.SetNumericParam(4, float(value))
			self._inputParameters[3] = float(value)

	def get_CPSHI_Name(self):
		if self._parCnIn[3] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[3], 1)
		else:
			return str(self._inputParameters[3])

	CPSHI_Name = property(fget=get_CPSHI_Name)

	def CPSLO(self, index):
		if self._parCnIn[4] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[4], index)
		else:
			return self._inputParameters[4]

	def Save_CPSLO(self, index, value):
		if self._parCnIn[4] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[4], index, float(value))
		else:
			self._IPProxy.SetNumericParam(5, float(value))
			self._inputParameters[4] = float(value)

	def get_CPSLO_Name(self):
		if self._parCnIn[4] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[4], 1)
		else:
			return str(self._inputParameters[4])

	CPSLO_Name = property(fget=get_CPSLO_Name)

	def M(self, index):
		if self._parCnIn[5] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[5], index)
		else:
			return self._inputParameters[5]

	def Save_M(self, index, value):
		if self._parCnIn[5] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[5], index, float(value))
		else:
			self._IPProxy.SetNumericParam(6, float(value))
			self._inputParameters[5] = float(value)

	def get_M_Name(self):
		if self._parCnIn[5] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[5], 1)
		else:
			return str(self._inputParameters[5])

	M_Name = property(fget=get_M_Name)

	def N(self, index):
		if self._parCnIn[6] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[6], index)
		else:
			return self._inputParameters[6]

	def Save_N(self, index, value):
		if self._parCnIn[6] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[6], index, float(value))
		else:
			self._IPProxy.SetNumericParam(7, float(value))
			self._inputParameters[6] = float(value)

	def get_N_Name(self):
		if self._parCnIn[6] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[6], 1)
		else:
			return str(self._inputParameters[6])

	N_Name = property(fget=get_N_Name)

	def GRmin(self, index):
		if self._parCnIn[7] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[7], index)
		else:
			return self._inputParameters[7]

	def Save_GRmin(self, index, value):
		if self._parCnIn[7] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[7], index, float(value))
		else:
			self._IPProxy.SetNumericParam(8, float(value))
			self._inputParameters[7] = float(value)

	def get_GRmin_Name(self):
		if self._parCnIn[7] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[7], 1)
		else:
			return str(self._inputParameters[7])

	GRmin_Name = property(fget=get_GRmin_Name)

	def GRmax(self, index):
		if self._parCnIn[8] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[8], index)
		else:
			return self._inputParameters[8]

	def Save_GRmax(self, index, value):
		if self._parCnIn[8] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[8], index, float(value))
		else:
			self._IPProxy.SetNumericParam(9, float(value))
			self._inputParameters[8] = float(value)

	def get_GRmax_Name(self):
		if self._parCnIn[8] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[8], 1)
		else:
			return str(self._inputParameters[8])

	GRmax_Name = property(fget=get_GRmax_Name)

	def shale_coeff(self, index):
		if self._parCnIn[9] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[9], index)
		else:
			return self._inputParameters[9]

	def Save_shale_coeff(self, index, value):
		if self._parCnIn[9] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[9], index, float(value))
		else:
			self._IPProxy.SetNumericParam(10, float(value))
			self._inputParameters[9] = float(value)

	def get_shale_coeff_Name(self):
		if self._parCnIn[9] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[9], 1)
		else:
			return str(self._inputParameters[9])

	shale_coeff_Name = property(fget=get_shale_coeff_Name)

	def shale_intcp(self, index):
		if self._parCnIn[10] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[10], index)
		else:
			return self._inputParameters[10]

	def Save_shale_intcp(self, index, value):
		if self._parCnIn[10] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[10], index, float(value))
		else:
			self._IPProxy.SetNumericParam(11, float(value))
			self._inputParameters[10] = float(value)

	def get_shale_intcp_Name(self):
		if self._parCnIn[10] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[10], 1)
		else:
			return str(self._inputParameters[10])

	shale_intcp_Name = property(fget=get_shale_intcp_Name)

	def SALINITY(self, index):
		if self._parCnIn[11] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[11], index)
		else:
			return self._inputParameters[11]

	def Save_SALINITY(self, index, value):
		if self._parCnIn[11] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[11], index, float(value))
		else:
			self._IPProxy.SetNumericParam(12, float(value))
			self._inputParameters[11] = float(value)

	def get_SALINITY_Name(self):
		if self._parCnIn[11] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[11], 1)
		else:
			return str(self._inputParameters[11])

	SALINITY_Name = property(fget=get_SALINITY_Name)

	def BHT(self, index):
		if self._parCnIn[12] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[12], index)
		else:
			return self._inputParameters[12]

	def Save_BHT(self, index, value):
		if self._parCnIn[12] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[12], index, float(value))
		else:
			self._IPProxy.SetNumericParam(13, float(value))
			self._inputParameters[12] = float(value)

	def get_BHT_Name(self):
		if self._parCnIn[12] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[12], 1)
		else:
			return str(self._inputParameters[12])

	BHT_Name = property(fget=get_BHT_Name)

	def SBT(self, index):
		if self._parCnIn[13] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[13], index)
		else:
			return self._inputParameters[13]

	def Save_SBT(self, index, value):
		if self._parCnIn[13] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[13], index, float(value))
		else:
			self._IPProxy.SetNumericParam(14, float(value))
			self._inputParameters[13] = float(value)

	def get_SBT_Name(self):
		if self._parCnIn[13] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[13], 1)
		else:
			return str(self._inputParameters[13])

	SBT_Name = property(fget=get_SBT_Name)

	def WD(self, index):
		if self._parCnIn[14] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[14], index)
		else:
			return self._inputParameters[14]

	def Save_WD(self, index, value):
		if self._parCnIn[14] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[14], index, float(value))
		else:
			self._IPProxy.SetNumericParam(15, float(value))
			self._inputParameters[14] = float(value)

	def get_WD_Name(self):
		if self._parCnIn[14] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[14], 1)
		else:
			return str(self._inputParameters[14])

	WD_Name = property(fget=get_WD_Name)

	def RTE(self, index):
		if self._parCnIn[15] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[15], index)
		else:
			return self._inputParameters[15]

	def Save_RTE(self, index, value):
		if self._parCnIn[15] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[15], index, float(value))
		else:
			self._IPProxy.SetNumericParam(16, float(value))
			self._inputParameters[15] = float(value)

	def get_RTE_Name(self):
		if self._parCnIn[15] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[15], 1)
		else:
			return str(self._inputParameters[15])

	RTE_Name = property(fget=get_RTE_Name)

