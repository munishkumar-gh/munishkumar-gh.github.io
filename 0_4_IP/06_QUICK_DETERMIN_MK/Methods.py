# /***********************************************/
#  * File dynamically created from IP: 08/24/2022 15:19:01
#  * DO NOT MANUALLY EDIT
# /***********************************************/

class Methods:
	def __init__(self):
		self._FIRST_AVAILABLE_LOG_RUN = -1
		self._LAST_AVAILABLE_LOG_RUN = -2

	def Depth(self, index):
		return self._IPProxy.GetCurveData(1, index)

	def BADHOLE(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[0],0, index, True)

	def Array_BADHOLE(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[0],0, index, xVal, yVal, True)

	def BADHOLE_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[0], index)

	def Array_BADHOLE_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[0], index, xVal, yVal)

	def get_BADHOLE_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 1)

	BADHOLE_Name = property(fget=get_BADHOLE_Name)

	def get_BADHOLE_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 2)

	BADHOLE_Units = property(fget=get_BADHOLE_Units)

	def get_BADHOLE_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 3)

	BADHOLE_Comments = property(fget=get_BADHOLE_Comments)

	def Save_BADHOLE_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[0], 3, str(newValue))

	def Get_BADHOLE_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[0], attributeName)

	def Set_BADHOLE_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[0], attributeName, str(newValue))

	def Save_BADHOLE(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[0], index, float(value))

	def Save_Array_BADHOLE(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[0], index, float(value), xVal, yVal)

	def Save_BADHOLE_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[0], index, str(value))

	def Save_Array_BADHOLE_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[0], index, str(value), xVal, yVal)

	def get_Array_BADHOLE_MaxX(self):
		return self._inArrayX[0]

	Array_BADHOLE_MaxX = property(fget=get_Array_BADHOLE_MaxX)

	def get_Array_BADHOLE_MaxY(self):
		return self._inArrayY[0]

	Array_BADHOLE_MaxY = property(fget=get_Array_BADHOLE_MaxY)

	def COAL(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[1],1, index, True)

	def Array_COAL(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[1],1, index, xVal, yVal, True)

	def COAL_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[1], index)

	def Array_COAL_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[1], index, xVal, yVal)

	def get_COAL_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 1)

	COAL_Name = property(fget=get_COAL_Name)

	def get_COAL_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 2)

	COAL_Units = property(fget=get_COAL_Units)

	def get_COAL_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 3)

	COAL_Comments = property(fget=get_COAL_Comments)

	def Save_COAL_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[1], 3, str(newValue))

	def Get_COAL_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[1], attributeName)

	def Set_COAL_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[1], attributeName, str(newValue))

	def Save_COAL(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[1], index, float(value))

	def Save_Array_COAL(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[1], index, float(value), xVal, yVal)

	def Save_COAL_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[1], index, str(value))

	def Save_Array_COAL_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[1], index, str(value), xVal, yVal)

	def get_Array_COAL_MaxX(self):
		return self._inArrayX[1]

	Array_COAL_MaxX = property(fget=get_Array_COAL_MaxX)

	def get_Array_COAL_MaxY(self):
		return self._inArrayY[1]

	Array_COAL_MaxY = property(fget=get_Array_COAL_MaxY)

	def VOLC(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[2],2, index, True)

	def Array_VOLC(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[2],2, index, xVal, yVal, True)

	def VOLC_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[2], index)

	def Array_VOLC_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[2], index, xVal, yVal)

	def get_VOLC_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 1)

	VOLC_Name = property(fget=get_VOLC_Name)

	def get_VOLC_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 2)

	VOLC_Units = property(fget=get_VOLC_Units)

	def get_VOLC_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 3)

	VOLC_Comments = property(fget=get_VOLC_Comments)

	def Save_VOLC_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[2], 3, str(newValue))

	def Get_VOLC_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[2], attributeName)

	def Set_VOLC_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[2], attributeName, str(newValue))

	def Save_VOLC(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[2], index, float(value))

	def Save_Array_VOLC(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[2], index, float(value), xVal, yVal)

	def Save_VOLC_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[2], index, str(value))

	def Save_Array_VOLC_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[2], index, str(value), xVal, yVal)

	def get_Array_VOLC_MaxX(self):
		return self._inArrayX[2]

	Array_VOLC_MaxX = property(fget=get_Array_VOLC_MaxX)

	def get_Array_VOLC_MaxY(self):
		return self._inArrayY[2]

	Array_VOLC_MaxY = property(fget=get_Array_VOLC_MaxY)

	def DEPTH_TVDSS(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[3],3, index, True)

	def Array_DEPTH_TVDSS(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[3],3, index, xVal, yVal, True)

	def DEPTH_TVDSS_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[3], index)

	def Array_DEPTH_TVDSS_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[3], index, xVal, yVal)

	def get_DEPTH_TVDSS_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 1)

	DEPTH_TVDSS_Name = property(fget=get_DEPTH_TVDSS_Name)

	def get_DEPTH_TVDSS_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 2)

	DEPTH_TVDSS_Units = property(fget=get_DEPTH_TVDSS_Units)

	def get_DEPTH_TVDSS_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 3)

	DEPTH_TVDSS_Comments = property(fget=get_DEPTH_TVDSS_Comments)

	def Save_DEPTH_TVDSS_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[3], 3, str(newValue))

	def Get_DEPTH_TVDSS_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[3], attributeName)

	def Set_DEPTH_TVDSS_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[3], attributeName, str(newValue))

	def Save_DEPTH_TVDSS(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[3], index, float(value))

	def Save_Array_DEPTH_TVDSS(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[3], index, float(value), xVal, yVal)

	def Save_DEPTH_TVDSS_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[3], index, str(value))

	def Save_Array_DEPTH_TVDSS_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[3], index, str(value), xVal, yVal)

	def get_Array_DEPTH_TVDSS_MaxX(self):
		return self._inArrayX[3]

	Array_DEPTH_TVDSS_MaxX = property(fget=get_Array_DEPTH_TVDSS_MaxX)

	def get_Array_DEPTH_TVDSS_MaxY(self):
		return self._inArrayY[3]

	Array_DEPTH_TVDSS_MaxY = property(fget=get_Array_DEPTH_TVDSS_MaxY)

	def TEMPERATUREOF(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[4],4, index, True)

	def Array_TEMPERATUREOF(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[4],4, index, xVal, yVal, True)

	def TEMPERATUREOF_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[4], index)

	def Array_TEMPERATUREOF_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[4], index, xVal, yVal)

	def get_TEMPERATUREOF_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 1)

	TEMPERATUREOF_Name = property(fget=get_TEMPERATUREOF_Name)

	def get_TEMPERATUREOF_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 2)

	TEMPERATUREOF_Units = property(fget=get_TEMPERATUREOF_Units)

	def get_TEMPERATUREOF_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 3)

	TEMPERATUREOF_Comments = property(fget=get_TEMPERATUREOF_Comments)

	def Save_TEMPERATUREOF_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[4], 3, str(newValue))

	def Get_TEMPERATUREOF_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[4], attributeName)

	def Set_TEMPERATUREOF_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[4], attributeName, str(newValue))

	def Save_TEMPERATUREOF(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[4], index, float(value))

	def Save_Array_TEMPERATUREOF(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[4], index, float(value), xVal, yVal)

	def Save_TEMPERATUREOF_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[4], index, str(value))

	def Save_Array_TEMPERATUREOF_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[4], index, str(value), xVal, yVal)

	def get_Array_TEMPERATUREOF_MaxX(self):
		return self._inArrayX[4]

	Array_TEMPERATUREOF_MaxX = property(fget=get_Array_TEMPERATUREOF_MaxX)

	def get_Array_TEMPERATUREOF_MaxY(self):
		return self._inArrayY[4]

	Array_TEMPERATUREOF_MaxY = property(fget=get_Array_TEMPERATUREOF_MaxY)

	def TEMPERATUREOC(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[5],5, index, True)

	def Array_TEMPERATUREOC(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[5],5, index, xVal, yVal, True)

	def TEMPERATUREOC_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[5], index)

	def Array_TEMPERATUREOC_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[5], index, xVal, yVal)

	def get_TEMPERATUREOC_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 1)

	TEMPERATUREOC_Name = property(fget=get_TEMPERATUREOC_Name)

	def get_TEMPERATUREOC_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 2)

	TEMPERATUREOC_Units = property(fget=get_TEMPERATUREOC_Units)

	def get_TEMPERATUREOC_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 3)

	TEMPERATUREOC_Comments = property(fget=get_TEMPERATUREOC_Comments)

	def Save_TEMPERATUREOC_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[5], 3, str(newValue))

	def Get_TEMPERATUREOC_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[5], attributeName)

	def Set_TEMPERATUREOC_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[5], attributeName, str(newValue))

	def Save_TEMPERATUREOC(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[5], index, float(value))

	def Save_Array_TEMPERATUREOC(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[5], index, float(value), xVal, yVal)

	def Save_TEMPERATUREOC_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[5], index, str(value))

	def Save_Array_TEMPERATUREOC_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[5], index, str(value), xVal, yVal)

	def get_Array_TEMPERATUREOC_MaxX(self):
		return self._inArrayX[5]

	Array_TEMPERATUREOC_MaxX = property(fget=get_Array_TEMPERATUREOC_MaxX)

	def get_Array_TEMPERATUREOC_MaxY(self):
		return self._inArrayY[5]

	Array_TEMPERATUREOC_MaxY = property(fget=get_Array_TEMPERATUREOC_MaxY)

	def GR(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[6],6, index, True)

	def Array_GR(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[6],6, index, xVal, yVal, True)

	def GR_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[6], index)

	def Array_GR_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[6], index, xVal, yVal)

	def get_GR_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[6], 1)

	GR_Name = property(fget=get_GR_Name)

	def get_GR_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[6], 2)

	GR_Units = property(fget=get_GR_Units)

	def get_GR_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[6], 3)

	GR_Comments = property(fget=get_GR_Comments)

	def Save_GR_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[6], 3, str(newValue))

	def Get_GR_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[6], attributeName)

	def Set_GR_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[6], attributeName, str(newValue))

	def Save_GR(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[6], index, float(value))

	def Save_Array_GR(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[6], index, float(value), xVal, yVal)

	def Save_GR_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[6], index, str(value))

	def Save_Array_GR_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[6], index, str(value), xVal, yVal)

	def get_Array_GR_MaxX(self):
		return self._inArrayX[6]

	Array_GR_MaxX = property(fget=get_Array_GR_MaxX)

	def get_Array_GR_MaxY(self):
		return self._inArrayY[6]

	Array_GR_MaxY = property(fget=get_Array_GR_MaxY)

	def NPHI(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[7],7, index, True)

	def Array_NPHI(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[7],7, index, xVal, yVal, True)

	def NPHI_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[7], index)

	def Array_NPHI_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[7], index, xVal, yVal)

	def get_NPHI_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[7], 1)

	NPHI_Name = property(fget=get_NPHI_Name)

	def get_NPHI_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[7], 2)

	NPHI_Units = property(fget=get_NPHI_Units)

	def get_NPHI_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[7], 3)

	NPHI_Comments = property(fget=get_NPHI_Comments)

	def Save_NPHI_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[7], 3, str(newValue))

	def Get_NPHI_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[7], attributeName)

	def Set_NPHI_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[7], attributeName, str(newValue))

	def Save_NPHI(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[7], index, float(value))

	def Save_Array_NPHI(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[7], index, float(value), xVal, yVal)

	def Save_NPHI_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[7], index, str(value))

	def Save_Array_NPHI_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[7], index, str(value), xVal, yVal)

	def get_Array_NPHI_MaxX(self):
		return self._inArrayX[7]

	Array_NPHI_MaxX = property(fget=get_Array_NPHI_MaxX)

	def get_Array_NPHI_MaxY(self):
		return self._inArrayY[7]

	Array_NPHI_MaxY = property(fget=get_Array_NPHI_MaxY)

	def RHOB(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[8],8, index, True)

	def Array_RHOB(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[8],8, index, xVal, yVal, True)

	def RHOB_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[8], index)

	def Array_RHOB_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[8], index, xVal, yVal)

	def get_RHOB_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[8], 1)

	RHOB_Name = property(fget=get_RHOB_Name)

	def get_RHOB_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[8], 2)

	RHOB_Units = property(fget=get_RHOB_Units)

	def get_RHOB_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[8], 3)

	RHOB_Comments = property(fget=get_RHOB_Comments)

	def Save_RHOB_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[8], 3, str(newValue))

	def Get_RHOB_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[8], attributeName)

	def Set_RHOB_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[8], attributeName, str(newValue))

	def Save_RHOB(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[8], index, float(value))

	def Save_Array_RHOB(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[8], index, float(value), xVal, yVal)

	def Save_RHOB_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[8], index, str(value))

	def Save_Array_RHOB_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[8], index, str(value), xVal, yVal)

	def get_Array_RHOB_MaxX(self):
		return self._inArrayX[8]

	Array_RHOB_MaxX = property(fget=get_Array_RHOB_MaxX)

	def get_Array_RHOB_MaxY(self):
		return self._inArrayY[8]

	Array_RHOB_MaxY = property(fget=get_Array_RHOB_MaxY)

	def DT(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[9],9, index, True)

	def Array_DT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[9],9, index, xVal, yVal, True)

	def DT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[9], index)

	def Array_DT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[9], index, xVal, yVal)

	def get_DT_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[9], 1)

	DT_Name = property(fget=get_DT_Name)

	def get_DT_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[9], 2)

	DT_Units = property(fget=get_DT_Units)

	def get_DT_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[9], 3)

	DT_Comments = property(fget=get_DT_Comments)

	def Save_DT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[9], 3, str(newValue))

	def Get_DT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[9], attributeName)

	def Set_DT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[9], attributeName, str(newValue))

	def Save_DT(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[9], index, float(value))

	def Save_Array_DT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[9], index, float(value), xVal, yVal)

	def Save_DT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[9], index, str(value))

	def Save_Array_DT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[9], index, str(value), xVal, yVal)

	def get_Array_DT_MaxX(self):
		return self._inArrayX[9]

	Array_DT_MaxX = property(fget=get_Array_DT_MaxX)

	def get_Array_DT_MaxY(self):
		return self._inArrayY[9]

	Array_DT_MaxY = property(fget=get_Array_DT_MaxY)

	def RT(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[10],10, index, True)

	def Array_RT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[10],10, index, xVal, yVal, True)

	def RT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[10], index)

	def Array_RT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[10], index, xVal, yVal)

	def get_RT_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[10], 1)

	RT_Name = property(fget=get_RT_Name)

	def get_RT_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[10], 2)

	RT_Units = property(fget=get_RT_Units)

	def get_RT_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[10], 3)

	RT_Comments = property(fget=get_RT_Comments)

	def Save_RT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[10], 3, str(newValue))

	def Get_RT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[10], attributeName)

	def Set_RT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[10], attributeName, str(newValue))

	def Save_RT(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[10], index, float(value))

	def Save_Array_RT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[10], index, float(value), xVal, yVal)

	def Save_RT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[10], index, str(value))

	def Save_Array_RT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[10], index, str(value), xVal, yVal)

	def get_Array_RT_MaxX(self):
		return self._inArrayX[10]

	Array_RT_MaxX = property(fget=get_Array_RT_MaxX)

	def get_Array_RT_MaxY(self):
		return self._inArrayY[10]

	Array_RT_MaxY = property(fget=get_Array_RT_MaxY)

	def Save_FT(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, float(value))

	def Save_Array_FT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, float(value), xVal, yVal)

	def Save_FT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, str(value))

	def Save_Array_FT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, str(value), xVal, yVal)

	def FT(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[0], index)

	def Array_FT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[0], index, xVal, yVal)

	def FT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[0], index)

	def Array_FT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[0], index, xVal, yVal)

	def get_FT_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 1)

	FT_Name = property(fget=get_FT_Name)

	def get_FT_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 2)

	FT_Units = property(fget=get_FT_Units)

	def get_FT_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 3)

	FT_Comments = property(fget=get_FT_Comments)

	def Save_FT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[0], 3, str(newValue))

	def get_Array_FT_MaxX(self):
		return self._outArrayX[0]

	Array_FT_MaxX = property(fget=get_Array_FT_MaxX)

	def get_Array_FT_MaxY(self):
		return self._outArrayY[0]

	Array_FT_MaxY = property(fget=get_Array_FT_MaxY)

	def Get_FT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[0], attributeName)

	def Set_FT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[0], attributeName, str(newValue))

	def Save_RW(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value))

	def Save_Array_RW(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value), xVal, yVal)

	def Save_RW_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value))

	def Save_Array_RW_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value), xVal, yVal)

	def RW(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[1], index)

	def Array_RW(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[1], index, xVal, yVal)

	def RW_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[1], index)

	def Array_RW_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[1], index, xVal, yVal)

	def get_RW_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 1)

	RW_Name = property(fget=get_RW_Name)

	def get_RW_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 2)

	RW_Units = property(fget=get_RW_Units)

	def get_RW_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 3)

	RW_Comments = property(fget=get_RW_Comments)

	def Save_RW_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[1], 3, str(newValue))

	def get_Array_RW_MaxX(self):
		return self._outArrayX[1]

	Array_RW_MaxX = property(fget=get_Array_RW_MaxX)

	def get_Array_RW_MaxY(self):
		return self._outArrayY[1]

	Array_RW_MaxY = property(fget=get_Array_RW_MaxY)

	def Get_RW_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[1], attributeName)

	def Set_RW_Attribute(self, attributeName, newValue):
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

	def Save_VCL_GR(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, float(value))

	def Save_Array_VCL_GR(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, float(value), xVal, yVal)

	def Save_VCL_GR_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, str(value))

	def Save_Array_VCL_GR_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, str(value), xVal, yVal)

	def VCL_GR(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[3], index)

	def Array_VCL_GR(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[3], index, xVal, yVal)

	def VCL_GR_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[3], index)

	def Array_VCL_GR_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[3], index, xVal, yVal)

	def get_VCL_GR_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 1)

	VCL_GR_Name = property(fget=get_VCL_GR_Name)

	def get_VCL_GR_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 2)

	VCL_GR_Units = property(fget=get_VCL_GR_Units)

	def get_VCL_GR_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 3)

	VCL_GR_Comments = property(fget=get_VCL_GR_Comments)

	def Save_VCL_GR_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[3], 3, str(newValue))

	def get_Array_VCL_GR_MaxX(self):
		return self._outArrayX[3]

	Array_VCL_GR_MaxX = property(fget=get_Array_VCL_GR_MaxX)

	def get_Array_VCL_GR_MaxY(self):
		return self._outArrayY[3]

	Array_VCL_GR_MaxY = property(fget=get_Array_VCL_GR_MaxY)

	def Get_VCL_GR_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[3], attributeName)

	def Set_VCL_GR_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[3], attributeName, str(newValue))

	def Save_DELTA_ND(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, float(value))

	def Save_Array_DELTA_ND(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, float(value), xVal, yVal)

	def Save_DELTA_ND_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, str(value))

	def Save_Array_DELTA_ND_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, str(value), xVal, yVal)

	def DELTA_ND(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[4], index)

	def Array_DELTA_ND(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[4], index, xVal, yVal)

	def DELTA_ND_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[4], index)

	def Array_DELTA_ND_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[4], index, xVal, yVal)

	def get_DELTA_ND_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 1)

	DELTA_ND_Name = property(fget=get_DELTA_ND_Name)

	def get_DELTA_ND_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 2)

	DELTA_ND_Units = property(fget=get_DELTA_ND_Units)

	def get_DELTA_ND_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 3)

	DELTA_ND_Comments = property(fget=get_DELTA_ND_Comments)

	def Save_DELTA_ND_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[4], 3, str(newValue))

	def get_Array_DELTA_ND_MaxX(self):
		return self._outArrayX[4]

	Array_DELTA_ND_MaxX = property(fget=get_Array_DELTA_ND_MaxX)

	def get_Array_DELTA_ND_MaxY(self):
		return self._outArrayY[4]

	Array_DELTA_ND_MaxY = property(fget=get_Array_DELTA_ND_MaxY)

	def Get_DELTA_ND_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[4], attributeName)

	def Set_DELTA_ND_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[4], attributeName, str(newValue))

	def Save_VSH_ND(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[5], index, float(value))

	def Save_Array_VSH_ND(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[5], index, float(value), xVal, yVal)

	def Save_VSH_ND_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[5], index, str(value))

	def Save_Array_VSH_ND_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[5], index, str(value), xVal, yVal)

	def VSH_ND(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[5], index)

	def Array_VSH_ND(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[5], index, xVal, yVal)

	def VSH_ND_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[5], index)

	def Array_VSH_ND_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[5], index, xVal, yVal)

	def get_VSH_ND_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 1)

	VSH_ND_Name = property(fget=get_VSH_ND_Name)

	def get_VSH_ND_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 2)

	VSH_ND_Units = property(fget=get_VSH_ND_Units)

	def get_VSH_ND_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 3)

	VSH_ND_Comments = property(fget=get_VSH_ND_Comments)

	def Save_VSH_ND_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[5], 3, str(newValue))

	def get_Array_VSH_ND_MaxX(self):
		return self._outArrayX[5]

	Array_VSH_ND_MaxX = property(fget=get_Array_VSH_ND_MaxX)

	def get_Array_VSH_ND_MaxY(self):
		return self._outArrayY[5]

	Array_VSH_ND_MaxY = property(fget=get_Array_VSH_ND_MaxY)

	def Get_VSH_ND_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[5], attributeName)

	def Set_VSH_ND_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[5], attributeName, str(newValue))

	def Save_VSH(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[6], index, float(value))

	def Save_Array_VSH(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[6], index, float(value), xVal, yVal)

	def Save_VSH_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[6], index, str(value))

	def Save_Array_VSH_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[6], index, str(value), xVal, yVal)

	def VSH(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[6], index)

	def Array_VSH(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[6], index, xVal, yVal)

	def VSH_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[6], index)

	def Array_VSH_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[6], index, xVal, yVal)

	def get_VSH_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 1)

	VSH_Name = property(fget=get_VSH_Name)

	def get_VSH_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 2)

	VSH_Units = property(fget=get_VSH_Units)

	def get_VSH_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 3)

	VSH_Comments = property(fget=get_VSH_Comments)

	def Save_VSH_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[6], 3, str(newValue))

	def get_Array_VSH_MaxX(self):
		return self._outArrayX[6]

	Array_VSH_MaxX = property(fget=get_Array_VSH_MaxX)

	def get_Array_VSH_MaxY(self):
		return self._outArrayY[6]

	Array_VSH_MaxY = property(fget=get_Array_VSH_MaxY)

	def Get_VSH_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[6], attributeName)

	def Set_VSH_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[6], attributeName, str(newValue))

	def Save_VCL(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[7], index, float(value))

	def Save_Array_VCL(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[7], index, float(value), xVal, yVal)

	def Save_VCL_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[7], index, str(value))

	def Save_Array_VCL_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[7], index, str(value), xVal, yVal)

	def VCL(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[7], index)

	def Array_VCL(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[7], index, xVal, yVal)

	def VCL_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[7], index)

	def Array_VCL_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[7], index, xVal, yVal)

	def get_VCL_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 1)

	VCL_Name = property(fget=get_VCL_Name)

	def get_VCL_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 2)

	VCL_Units = property(fget=get_VCL_Units)

	def get_VCL_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 3)

	VCL_Comments = property(fget=get_VCL_Comments)

	def Save_VCL_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[7], 3, str(newValue))

	def get_Array_VCL_MaxX(self):
		return self._outArrayX[7]

	Array_VCL_MaxX = property(fget=get_Array_VCL_MaxX)

	def get_Array_VCL_MaxY(self):
		return self._outArrayY[7]

	Array_VCL_MaxY = property(fget=get_Array_VCL_MaxY)

	def Get_VCL_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[7], attributeName)

	def Set_VCL_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[7], attributeName, str(newValue))

	def Save_RHOMA(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[8], index, float(value))

	def Save_Array_RHOMA(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[8], index, float(value), xVal, yVal)

	def Save_RHOMA_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[8], index, str(value))

	def Save_Array_RHOMA_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[8], index, str(value), xVal, yVal)

	def RHOMA(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[8], index)

	def Array_RHOMA(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[8], index, xVal, yVal)

	def RHOMA_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[8], index)

	def Array_RHOMA_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[8], index, xVal, yVal)

	def get_RHOMA_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 1)

	RHOMA_Name = property(fget=get_RHOMA_Name)

	def get_RHOMA_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 2)

	RHOMA_Units = property(fget=get_RHOMA_Units)

	def get_RHOMA_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 3)

	RHOMA_Comments = property(fget=get_RHOMA_Comments)

	def Save_RHOMA_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[8], 3, str(newValue))

	def get_Array_RHOMA_MaxX(self):
		return self._outArrayX[8]

	Array_RHOMA_MaxX = property(fget=get_Array_RHOMA_MaxX)

	def get_Array_RHOMA_MaxY(self):
		return self._outArrayY[8]

	Array_RHOMA_MaxY = property(fget=get_Array_RHOMA_MaxY)

	def Get_RHOMA_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[8], attributeName)

	def Set_RHOMA_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[8], attributeName, str(newValue))

	def Save_PHID(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[9], index, float(value))

	def Save_Array_PHID(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[9], index, float(value), xVal, yVal)

	def Save_PHID_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[9], index, str(value))

	def Save_Array_PHID_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[9], index, str(value), xVal, yVal)

	def PHID(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[9], index)

	def Array_PHID(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[9], index, xVal, yVal)

	def PHID_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[9], index)

	def Array_PHID_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[9], index, xVal, yVal)

	def get_PHID_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[9], 1)

	PHID_Name = property(fget=get_PHID_Name)

	def get_PHID_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[9], 2)

	PHID_Units = property(fget=get_PHID_Units)

	def get_PHID_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[9], 3)

	PHID_Comments = property(fget=get_PHID_Comments)

	def Save_PHID_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[9], 3, str(newValue))

	def get_Array_PHID_MaxX(self):
		return self._outArrayX[9]

	Array_PHID_MaxX = property(fget=get_Array_PHID_MaxX)

	def get_Array_PHID_MaxY(self):
		return self._outArrayY[9]

	Array_PHID_MaxY = property(fget=get_Array_PHID_MaxY)

	def Get_PHID_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[9], attributeName)

	def Set_PHID_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[9], attributeName, str(newValue))

	def Save_PHIT_HC(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[10], index, float(value))

	def Save_Array_PHIT_HC(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[10], index, float(value), xVal, yVal)

	def Save_PHIT_HC_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[10], index, str(value))

	def Save_Array_PHIT_HC_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[10], index, str(value), xVal, yVal)

	def PHIT_HC(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[10], index)

	def Array_PHIT_HC(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[10], index, xVal, yVal)

	def PHIT_HC_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[10], index)

	def Array_PHIT_HC_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[10], index, xVal, yVal)

	def get_PHIT_HC_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[10], 1)

	PHIT_HC_Name = property(fget=get_PHIT_HC_Name)

	def get_PHIT_HC_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[10], 2)

	PHIT_HC_Units = property(fget=get_PHIT_HC_Units)

	def get_PHIT_HC_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[10], 3)

	PHIT_HC_Comments = property(fget=get_PHIT_HC_Comments)

	def Save_PHIT_HC_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[10], 3, str(newValue))

	def get_Array_PHIT_HC_MaxX(self):
		return self._outArrayX[10]

	Array_PHIT_HC_MaxX = property(fget=get_Array_PHIT_HC_MaxX)

	def get_Array_PHIT_HC_MaxY(self):
		return self._outArrayY[10]

	Array_PHIT_HC_MaxY = property(fget=get_Array_PHIT_HC_MaxY)

	def Get_PHIT_HC_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[10], attributeName)

	def Set_PHIT_HC_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[10], attributeName, str(newValue))

	def Save_PHIT_ND(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[11], index, float(value))

	def Save_Array_PHIT_ND(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[11], index, float(value), xVal, yVal)

	def Save_PHIT_ND_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[11], index, str(value))

	def Save_Array_PHIT_ND_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[11], index, str(value), xVal, yVal)

	def PHIT_ND(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[11], index)

	def Array_PHIT_ND(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[11], index, xVal, yVal)

	def PHIT_ND_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[11], index)

	def Array_PHIT_ND_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[11], index, xVal, yVal)

	def get_PHIT_ND_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[11], 1)

	PHIT_ND_Name = property(fget=get_PHIT_ND_Name)

	def get_PHIT_ND_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[11], 2)

	PHIT_ND_Units = property(fget=get_PHIT_ND_Units)

	def get_PHIT_ND_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[11], 3)

	PHIT_ND_Comments = property(fget=get_PHIT_ND_Comments)

	def Save_PHIT_ND_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[11], 3, str(newValue))

	def get_Array_PHIT_ND_MaxX(self):
		return self._outArrayX[11]

	Array_PHIT_ND_MaxX = property(fget=get_Array_PHIT_ND_MaxX)

	def get_Array_PHIT_ND_MaxY(self):
		return self._outArrayY[11]

	Array_PHIT_ND_MaxY = property(fget=get_Array_PHIT_ND_MaxY)

	def Get_PHIT_ND_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[11], attributeName)

	def Set_PHIT_ND_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[11], attributeName, str(newValue))

	def Save_PHIT_DT_RHG(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[12], index, float(value))

	def Save_Array_PHIT_DT_RHG(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[12], index, float(value), xVal, yVal)

	def Save_PHIT_DT_RHG_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[12], index, str(value))

	def Save_Array_PHIT_DT_RHG_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[12], index, str(value), xVal, yVal)

	def PHIT_DT_RHG(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[12], index)

	def Array_PHIT_DT_RHG(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[12], index, xVal, yVal)

	def PHIT_DT_RHG_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[12], index)

	def Array_PHIT_DT_RHG_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[12], index, xVal, yVal)

	def get_PHIT_DT_RHG_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[12], 1)

	PHIT_DT_RHG_Name = property(fget=get_PHIT_DT_RHG_Name)

	def get_PHIT_DT_RHG_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[12], 2)

	PHIT_DT_RHG_Units = property(fget=get_PHIT_DT_RHG_Units)

	def get_PHIT_DT_RHG_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[12], 3)

	PHIT_DT_RHG_Comments = property(fget=get_PHIT_DT_RHG_Comments)

	def Save_PHIT_DT_RHG_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[12], 3, str(newValue))

	def get_Array_PHIT_DT_RHG_MaxX(self):
		return self._outArrayX[12]

	Array_PHIT_DT_RHG_MaxX = property(fget=get_Array_PHIT_DT_RHG_MaxX)

	def get_Array_PHIT_DT_RHG_MaxY(self):
		return self._outArrayY[12]

	Array_PHIT_DT_RHG_MaxY = property(fget=get_Array_PHIT_DT_RHG_MaxY)

	def Get_PHIT_DT_RHG_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[12], attributeName)

	def Set_PHIT_DT_RHG_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[12], attributeName, str(newValue))

	def Save_PHIT_DT_W(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[13], index, float(value))

	def Save_Array_PHIT_DT_W(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[13], index, float(value), xVal, yVal)

	def Save_PHIT_DT_W_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[13], index, str(value))

	def Save_Array_PHIT_DT_W_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[13], index, str(value), xVal, yVal)

	def PHIT_DT_W(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[13], index)

	def Array_PHIT_DT_W(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[13], index, xVal, yVal)

	def PHIT_DT_W_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[13], index)

	def Array_PHIT_DT_W_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[13], index, xVal, yVal)

	def get_PHIT_DT_W_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[13], 1)

	PHIT_DT_W_Name = property(fget=get_PHIT_DT_W_Name)

	def get_PHIT_DT_W_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[13], 2)

	PHIT_DT_W_Units = property(fget=get_PHIT_DT_W_Units)

	def get_PHIT_DT_W_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[13], 3)

	PHIT_DT_W_Comments = property(fget=get_PHIT_DT_W_Comments)

	def Save_PHIT_DT_W_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[13], 3, str(newValue))

	def get_Array_PHIT_DT_W_MaxX(self):
		return self._outArrayX[13]

	Array_PHIT_DT_W_MaxX = property(fget=get_Array_PHIT_DT_W_MaxX)

	def get_Array_PHIT_DT_W_MaxY(self):
		return self._outArrayY[13]

	Array_PHIT_DT_W_MaxY = property(fget=get_Array_PHIT_DT_W_MaxY)

	def Get_PHIT_DT_W_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[13], attributeName)

	def Set_PHIT_DT_W_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[13], attributeName, str(newValue))

	def Save_PHIT(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[14], index, float(value))

	def Save_Array_PHIT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[14], index, float(value), xVal, yVal)

	def Save_PHIT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[14], index, str(value))

	def Save_Array_PHIT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[14], index, str(value), xVal, yVal)

	def PHIT(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[14], index)

	def Array_PHIT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[14], index, xVal, yVal)

	def PHIT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[14], index)

	def Array_PHIT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[14], index, xVal, yVal)

	def get_PHIT_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[14], 1)

	PHIT_Name = property(fget=get_PHIT_Name)

	def get_PHIT_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[14], 2)

	PHIT_Units = property(fget=get_PHIT_Units)

	def get_PHIT_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[14], 3)

	PHIT_Comments = property(fget=get_PHIT_Comments)

	def Save_PHIT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[14], 3, str(newValue))

	def get_Array_PHIT_MaxX(self):
		return self._outArrayX[14]

	Array_PHIT_MaxX = property(fget=get_Array_PHIT_MaxX)

	def get_Array_PHIT_MaxY(self):
		return self._outArrayY[14]

	Array_PHIT_MaxY = property(fget=get_Array_PHIT_MaxY)

	def Get_PHIT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[14], attributeName)

	def Set_PHIT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[14], attributeName, str(newValue))

	def Save_SWT(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[15], index, float(value))

	def Save_Array_SWT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[15], index, float(value), xVal, yVal)

	def Save_SWT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[15], index, str(value))

	def Save_Array_SWT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[15], index, str(value), xVal, yVal)

	def SWT(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[15], index)

	def Array_SWT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[15], index, xVal, yVal)

	def SWT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[15], index)

	def Array_SWT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[15], index, xVal, yVal)

	def get_SWT_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[15], 1)

	SWT_Name = property(fget=get_SWT_Name)

	def get_SWT_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[15], 2)

	SWT_Units = property(fget=get_SWT_Units)

	def get_SWT_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[15], 3)

	SWT_Comments = property(fget=get_SWT_Comments)

	def Save_SWT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[15], 3, str(newValue))

	def get_Array_SWT_MaxX(self):
		return self._outArrayX[15]

	Array_SWT_MaxX = property(fget=get_Array_SWT_MaxX)

	def get_Array_SWT_MaxY(self):
		return self._outArrayY[15]

	Array_SWT_MaxY = property(fget=get_Array_SWT_MaxY)

	def Get_SWT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[15], attributeName)

	def Set_SWT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[15], attributeName, str(newValue))

	def Save_PHIE(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[16], index, float(value))

	def Save_Array_PHIE(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[16], index, float(value), xVal, yVal)

	def Save_PHIE_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[16], index, str(value))

	def Save_Array_PHIE_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[16], index, str(value), xVal, yVal)

	def PHIE(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[16], index)

	def Array_PHIE(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[16], index, xVal, yVal)

	def PHIE_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[16], index)

	def Array_PHIE_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[16], index, xVal, yVal)

	def get_PHIE_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[16], 1)

	PHIE_Name = property(fget=get_PHIE_Name)

	def get_PHIE_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[16], 2)

	PHIE_Units = property(fget=get_PHIE_Units)

	def get_PHIE_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[16], 3)

	PHIE_Comments = property(fget=get_PHIE_Comments)

	def Save_PHIE_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[16], 3, str(newValue))

	def get_Array_PHIE_MaxX(self):
		return self._outArrayX[16]

	Array_PHIE_MaxX = property(fget=get_Array_PHIE_MaxX)

	def get_Array_PHIE_MaxY(self):
		return self._outArrayY[16]

	Array_PHIE_MaxY = property(fget=get_Array_PHIE_MaxY)

	def Get_PHIE_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[16], attributeName)

	def Set_PHIE_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[16], attributeName, str(newValue))

	def Save_SWE(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[17], index, float(value))

	def Save_Array_SWE(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[17], index, float(value), xVal, yVal)

	def Save_SWE_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[17], index, str(value))

	def Save_Array_SWE_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[17], index, str(value), xVal, yVal)

	def SWE(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[17], index)

	def Array_SWE(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[17], index, xVal, yVal)

	def SWE_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[17], index)

	def Array_SWE_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[17], index, xVal, yVal)

	def get_SWE_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[17], 1)

	SWE_Name = property(fget=get_SWE_Name)

	def get_SWE_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[17], 2)

	SWE_Units = property(fget=get_SWE_Units)

	def get_SWE_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[17], 3)

	SWE_Comments = property(fget=get_SWE_Comments)

	def Save_SWE_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[17], 3, str(newValue))

	def get_Array_SWE_MaxX(self):
		return self._outArrayX[17]

	Array_SWE_MaxX = property(fget=get_Array_SWE_MaxX)

	def get_Array_SWE_MaxY(self):
		return self._outArrayY[17]

	Array_SWE_MaxY = property(fget=get_Array_SWE_MaxY)

	def Get_SWE_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[17], attributeName)

	def Set_SWE_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[17], attributeName, str(newValue))

	def Save_RO(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[18], index, float(value))

	def Save_Array_RO(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[18], index, float(value), xVal, yVal)

	def Save_RO_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[18], index, str(value))

	def Save_Array_RO_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[18], index, str(value), xVal, yVal)

	def RO(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[18], index)

	def Array_RO(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[18], index, xVal, yVal)

	def RO_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[18], index)

	def Array_RO_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[18], index, xVal, yVal)

	def get_RO_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[18], 1)

	RO_Name = property(fget=get_RO_Name)

	def get_RO_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[18], 2)

	RO_Units = property(fget=get_RO_Units)

	def get_RO_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[18], 3)

	RO_Comments = property(fget=get_RO_Comments)

	def Save_RO_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[18], 3, str(newValue))

	def get_Array_RO_MaxX(self):
		return self._outArrayX[18]

	Array_RO_MaxX = property(fget=get_Array_RO_MaxX)

	def get_Array_RO_MaxY(self):
		return self._outArrayY[18]

	Array_RO_MaxY = property(fget=get_Array_RO_MaxY)

	def Get_RO_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[18], attributeName)

	def Set_RO_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[18], attributeName, str(newValue))

	def Save_BVW(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[19], index, float(value))

	def Save_Array_BVW(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[19], index, float(value), xVal, yVal)

	def Save_BVW_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[19], index, str(value))

	def Save_Array_BVW_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[19], index, str(value), xVal, yVal)

	def BVW(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[19], index)

	def Array_BVW(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[19], index, xVal, yVal)

	def BVW_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[19], index)

	def Array_BVW_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[19], index, xVal, yVal)

	def get_BVW_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[19], 1)

	BVW_Name = property(fget=get_BVW_Name)

	def get_BVW_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[19], 2)

	BVW_Units = property(fget=get_BVW_Units)

	def get_BVW_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[19], 3)

	BVW_Comments = property(fget=get_BVW_Comments)

	def Save_BVW_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[19], 3, str(newValue))

	def get_Array_BVW_MaxX(self):
		return self._outArrayX[19]

	Array_BVW_MaxX = property(fget=get_Array_BVW_MaxX)

	def get_Array_BVW_MaxY(self):
		return self._outArrayY[19]

	Array_BVW_MaxY = property(fget=get_Array_BVW_MaxY)

	def Get_BVW_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[19], attributeName)

	def Set_BVW_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[19], attributeName, str(newValue))

	def Save_BVG(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[20], index, float(value))

	def Save_Array_BVG(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[20], index, float(value), xVal, yVal)

	def Save_BVG_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[20], index, str(value))

	def Save_Array_BVG_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[20], index, str(value), xVal, yVal)

	def BVG(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[20], index)

	def Array_BVG(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[20], index, xVal, yVal)

	def BVG_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[20], index)

	def Array_BVG_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[20], index, xVal, yVal)

	def get_BVG_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[20], 1)

	BVG_Name = property(fget=get_BVG_Name)

	def get_BVG_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[20], 2)

	BVG_Units = property(fget=get_BVG_Units)

	def get_BVG_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[20], 3)

	BVG_Comments = property(fget=get_BVG_Comments)

	def Save_BVG_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[20], 3, str(newValue))

	def get_Array_BVG_MaxX(self):
		return self._outArrayX[20]

	Array_BVG_MaxX = property(fget=get_Array_BVG_MaxX)

	def get_Array_BVG_MaxY(self):
		return self._outArrayY[20]

	Array_BVG_MaxY = property(fget=get_Array_BVG_MaxY)

	def Get_BVG_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[20], attributeName)

	def Set_BVG_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[20], attributeName, str(newValue))

	def BHT(self, index):
		if self._parCnIn[0] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[0], index)
		else:
			return self._inputParameters[0]

	def Save_BHT(self, index, value):
		if self._parCnIn[0] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[0], index, float(value))
		else:
			self._IPProxy.SetNumericParam(1, float(value))
			self._inputParameters[0] = float(value)

	def get_BHT_Name(self):
		if self._parCnIn[0] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[0], 1)
		else:
			return str(self._inputParameters[0])

	BHT_Name = property(fget=get_BHT_Name)

	def SBT(self, index):
		if self._parCnIn[1] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[1], index)
		else:
			return self._inputParameters[1]

	def Save_SBT(self, index, value):
		if self._parCnIn[1] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[1], index, float(value))
		else:
			self._IPProxy.SetNumericParam(2, float(value))
			self._inputParameters[1] = float(value)

	def get_SBT_Name(self):
		if self._parCnIn[1] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[1], 1)
		else:
			return str(self._inputParameters[1])

	SBT_Name = property(fget=get_SBT_Name)

	def WD(self, index):
		if self._parCnIn[2] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[2], index)
		else:
			return self._inputParameters[2]

	def Save_WD(self, index, value):
		if self._parCnIn[2] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[2], index, float(value))
		else:
			self._IPProxy.SetNumericParam(3, float(value))
			self._inputParameters[2] = float(value)

	def get_WD_Name(self):
		if self._parCnIn[2] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[2], 1)
		else:
			return str(self._inputParameters[2])

	WD_Name = property(fget=get_WD_Name)

	def RTE(self, index):
		if self._parCnIn[3] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[3], index)
		else:
			return self._inputParameters[3]

	def Save_RTE(self, index, value):
		if self._parCnIn[3] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[3], index, float(value))
		else:
			self._IPProxy.SetNumericParam(4, float(value))
			self._inputParameters[3] = float(value)

	def get_RTE_Name(self):
		if self._parCnIn[3] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[3], 1)
		else:
			return str(self._inputParameters[3])

	RTE_Name = property(fget=get_RTE_Name)

	def SALINITY(self, index):
		if self._parCnIn[4] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[4], index)
		else:
			return self._inputParameters[4]

	def Save_SALINITY(self, index, value):
		if self._parCnIn[4] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[4], index, float(value))
		else:
			self._IPProxy.SetNumericParam(5, float(value))
			self._inputParameters[4] = float(value)

	def get_SALINITY_Name(self):
		if self._parCnIn[4] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[4], 1)
		else:
			return str(self._inputParameters[4])

	SALINITY_Name = property(fget=get_SALINITY_Name)

	def RW_PARM(self, index):
		if self._parCnIn[5] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[5], index)
		else:
			return self._inputParameters[5]

	def Save_RW_PARM(self, index, value):
		if self._parCnIn[5] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[5], index, float(value))
		else:
			self._IPProxy.SetNumericParam(6, float(value))
			self._inputParameters[5] = float(value)

	def get_RW_PARM_Name(self):
		if self._parCnIn[5] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[5], 1)
		else:
			return str(self._inputParameters[5])

	RW_PARM_Name = property(fget=get_RW_PARM_Name)

	def RHOFL(self, index):
		if self._parCnIn[6] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[6], index)
		else:
			return self._inputParameters[6]

	def Save_RHOFL(self, index, value):
		if self._parCnIn[6] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[6], index, float(value))
		else:
			self._IPProxy.SetNumericParam(7, float(value))
			self._inputParameters[6] = float(value)

	def get_RHOFL_Name(self):
		if self._parCnIn[6] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[6], 1)
		else:
			return str(self._inputParameters[6])

	RHOFL_Name = property(fget=get_RHOFL_Name)

	def SWIRR(self, index):
		if self._parCnIn[7] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[7], index)
		else:
			return self._inputParameters[7]

	def Save_SWIRR(self, index, value):
		if self._parCnIn[7] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[7], index, float(value))
		else:
			self._IPProxy.SetNumericParam(8, float(value))
			self._inputParameters[7] = float(value)

	def get_SWIRR_Name(self):
		if self._parCnIn[7] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[7], 1)
		else:
			return str(self._inputParameters[7])

	SWIRR_Name = property(fget=get_SWIRR_Name)

	def RHOCL(self, index):
		if self._parCnIn[8] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[8], index)
		else:
			return self._inputParameters[8]

	def Save_RHOCL(self, index, value):
		if self._parCnIn[8] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[8], index, float(value))
		else:
			self._IPProxy.SetNumericParam(9, float(value))
			self._inputParameters[8] = float(value)

	def get_RHOCL_Name(self):
		if self._parCnIn[8] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[8], 1)
		else:
			return str(self._inputParameters[8])

	RHOCL_Name = property(fget=get_RHOCL_Name)

	def RHOSA(self, index):
		if self._parCnIn[9] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[9], index)
		else:
			return self._inputParameters[9]

	def Save_RHOSA(self, index, value):
		if self._parCnIn[9] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[9], index, float(value))
		else:
			self._IPProxy.SetNumericParam(10, float(value))
			self._inputParameters[9] = float(value)

	def get_RHOSA_Name(self):
		if self._parCnIn[9] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[9], 1)
		else:
			return str(self._inputParameters[9])

	RHOSA_Name = property(fget=get_RHOSA_Name)

	def PHISH_LOG(self, index):
		if self._parCnIn[10] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[10], index)
		else:
			return self._inputParameters[10]

	def Save_PHISH_LOG(self, index, value):
		if self._parCnIn[10] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[10], index, float(value))
		else:
			self._IPProxy.SetNumericParam(11, float(value))
			self._inputParameters[10] = float(value)

	def get_PHISH_LOG_Name(self):
		if self._parCnIn[10] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[10], 1)
		else:
			return str(self._inputParameters[10])

	PHISH_LOG_Name = property(fget=get_PHISH_LOG_Name)

	def SS_LITH_CORR(self, index):
		if self._parCnIn[11] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[11], index)
		else:
			return self._inputParameters[11]

	def Save_SS_LITH_CORR(self, index, value):
		if self._parCnIn[11] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[11], index, float(value))
		else:
			self._IPProxy.SetNumericParam(12, float(value))
			self._inputParameters[11] = float(value)

	def get_SS_LITH_CORR_Name(self):
		if self._parCnIn[11] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[11], 1)
		else:
			return str(self._inputParameters[11])

	SS_LITH_CORR_Name = property(fget=get_SS_LITH_CORR_Name)

	def B(self, index):
		if self._parCnIn[12] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[12], index)
		else:
			return self._inputParameters[12]

	def Save_B(self, index, value):
		if self._parCnIn[12] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[12], index, float(value))
		else:
			self._IPProxy.SetNumericParam(13, float(value))
			self._inputParameters[12] = float(value)

	def get_B_Name(self):
		if self._parCnIn[12] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[12], 1)
		else:
			return str(self._inputParameters[12])

	B_Name = property(fget=get_B_Name)

	def VSHCO(self, index):
		if self._parCnIn[13] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[13], index)
		else:
			return self._inputParameters[13]

	def Save_VSHCO(self, index, value):
		if self._parCnIn[13] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[13], index, float(value))
		else:
			self._IPProxy.SetNumericParam(14, float(value))
			self._inputParameters[13] = float(value)

	def get_VSHCO_Name(self):
		if self._parCnIn[13] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[13], 1)
		else:
			return str(self._inputParameters[13])

	VSHCO_Name = property(fget=get_VSHCO_Name)

	def CLAY(self, index):
		if self._parCnIn[14] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[14], index)
		else:
			return self._inputParameters[14]

	def Save_CLAY(self, index, value):
		if self._parCnIn[14] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[14], index, float(value))
		else:
			self._IPProxy.SetNumericParam(15, float(value))
			self._inputParameters[14] = float(value)

	def get_CLAY_Name(self):
		if self._parCnIn[14] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[14], 1)
		else:
			return str(self._inputParameters[14])

	CLAY_Name = property(fget=get_CLAY_Name)

	def GRMIN(self, index):
		if self._parCnIn[15] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[15], index)
		else:
			return self._inputParameters[15]

	def Save_GRMIN(self, index, value):
		if self._parCnIn[15] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[15], index, float(value))
		else:
			self._IPProxy.SetNumericParam(16, float(value))
			self._inputParameters[15] = float(value)

	def get_GRMIN_Name(self):
		if self._parCnIn[15] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[15], 1)
		else:
			return str(self._inputParameters[15])

	GRMIN_Name = property(fget=get_GRMIN_Name)

	def GRMAX(self, index):
		if self._parCnIn[16] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[16], index)
		else:
			return self._inputParameters[16]

	def Save_GRMAX(self, index, value):
		if self._parCnIn[16] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[16], index, float(value))
		else:
			self._IPProxy.SetNumericParam(17, float(value))
			self._inputParameters[16] = float(value)

	def get_GRMAX_Name(self):
		if self._parCnIn[16] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[16], 1)
		else:
			return str(self._inputParameters[16])

	GRMAX_Name = property(fget=get_GRMAX_Name)

	def DELTA_MIN_IN(self, index):
		if self._parCnIn[17] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[17], index)
		else:
			return self._inputParameters[17]

	def Save_DELTA_MIN_IN(self, index, value):
		if self._parCnIn[17] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[17], index, float(value))
		else:
			self._IPProxy.SetNumericParam(18, float(value))
			self._inputParameters[17] = float(value)

	def get_DELTA_MIN_IN_Name(self):
		if self._parCnIn[17] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[17], 1)
		else:
			return str(self._inputParameters[17])

	DELTA_MIN_IN_Name = property(fget=get_DELTA_MIN_IN_Name)

	def DELTA_MAX_IN(self, index):
		if self._parCnIn[18] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[18], index)
		else:
			return self._inputParameters[18]

	def Save_DELTA_MAX_IN(self, index, value):
		if self._parCnIn[18] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[18], index, float(value))
		else:
			self._IPProxy.SetNumericParam(19, float(value))
			self._inputParameters[18] = float(value)

	def get_DELTA_MAX_IN_Name(self):
		if self._parCnIn[18] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[18], 1)
		else:
			return str(self._inputParameters[18])

	DELTA_MAX_IN_Name = property(fget=get_DELTA_MAX_IN_Name)

	def DT_MASD(self, index):
		if self._parCnIn[19] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[19], index)
		else:
			return self._inputParameters[19]

	def Save_DT_MASD(self, index, value):
		if self._parCnIn[19] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[19], index, float(value))
		else:
			self._IPProxy.SetNumericParam(20, float(value))
			self._inputParameters[19] = float(value)

	def get_DT_MASD_Name(self):
		if self._parCnIn[19] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[19], 1)
		else:
			return str(self._inputParameters[19])

	DT_MASD_Name = property(fget=get_DT_MASD_Name)

	def DT_F(self, index):
		if self._parCnIn[20] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[20], index)
		else:
			return self._inputParameters[20]

	def Save_DT_F(self, index, value):
		if self._parCnIn[20] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[20], index, float(value))
		else:
			self._IPProxy.SetNumericParam(21, float(value))
			self._inputParameters[20] = float(value)

	def get_DT_F_Name(self):
		if self._parCnIn[20] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[20], 1)
		else:
			return str(self._inputParameters[20])

	DT_F_Name = property(fget=get_DT_F_Name)

	def M(self, index):
		if self._parCnIn[21] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[21], index)
		else:
			return self._inputParameters[21]

	def Save_M(self, index, value):
		if self._parCnIn[21] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[21], index, float(value))
		else:
			self._IPProxy.SetNumericParam(22, float(value))
			self._inputParameters[21] = float(value)

	def get_M_Name(self):
		if self._parCnIn[21] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[21], 1)
		else:
			return str(self._inputParameters[21])

	M_Name = property(fget=get_M_Name)

	def N(self, index):
		if self._parCnIn[22] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[22], index)
		else:
			return self._inputParameters[22]

	def Save_N(self, index, value):
		if self._parCnIn[22] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[22], index, float(value))
		else:
			self._IPProxy.SetNumericParam(23, float(value))
			self._inputParameters[22] = float(value)

	def get_N_Name(self):
		if self._parCnIn[22] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[22], 1)
		else:
			return str(self._inputParameters[22])

	N_Name = property(fget=get_N_Name)

	def PHISH_COEF(self, index):
		if self._parCnIn[23] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[23], index)
		else:
			return self._inputParameters[23]

	def Save_PHISH_COEF(self, index, value):
		if self._parCnIn[23] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[23], index, float(value))
		else:
			self._IPProxy.SetNumericParam(24, float(value))
			self._inputParameters[23] = float(value)

	def get_PHISH_COEF_Name(self):
		if self._parCnIn[23] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[23], 1)
		else:
			return str(self._inputParameters[23])

	PHISH_COEF_Name = property(fget=get_PHISH_COEF_Name)

	def PHISH_INT(self, index):
		if self._parCnIn[24] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[24], index)
		else:
			return self._inputParameters[24]

	def Save_PHISH_INT(self, index, value):
		if self._parCnIn[24] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[24], index, float(value))
		else:
			self._IPProxy.SetNumericParam(25, float(value))
			self._inputParameters[24] = float(value)

	def get_PHISH_INT_Name(self):
		if self._parCnIn[24] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[24], 1)
		else:
			return str(self._inputParameters[24])

	PHISH_INT_Name = property(fget=get_PHISH_INT_Name)

	def get_VSH_METHOD(self):
		return self._textInputParameters[0]

	VSH_METHOD = property(fget=get_VSH_METHOD)

	def get_PHIT_METHOD(self):
		return self._textInputParameters[1]

	PHIT_METHOD = property(fget=get_PHIT_METHOD)

	def get_X(self):
		return self._textInputParameters[2]

	X = property(fget=get_X)

