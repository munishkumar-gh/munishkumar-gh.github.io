# /***********************************************/
#  * File dynamically created from IP: 07/09/2021 08:11:18
#  * DO NOT MANUALLY EDIT
# /***********************************************/

class Methods:
	def __init__(self):
		self._FIRST_AVAILABLE_LOG_RUN = -1
		self._LAST_AVAILABLE_LOG_RUN = -2

	def Depth(self, index):
		return self._IPProxy.GetCurveData(1, index)

	def DTC(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[0],0, index, True)

	def Array_DTC(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[0],0, index, xVal, yVal, True)

	def DTC_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[0], index)

	def Array_DTC_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[0], index, xVal, yVal)

	def get_DTC_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 1)

	DTC_Name = property(fget=get_DTC_Name)

	def get_DTC_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 2)

	DTC_Units = property(fget=get_DTC_Units)

	def get_DTC_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 3)

	DTC_Comments = property(fget=get_DTC_Comments)

	def Save_DTC_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[0], 3, str(newValue))

	def Get_DTC_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[0], attributeName)

	def Set_DTC_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[0], attributeName, str(newValue))

	def Save_DTC(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[0], index, float(value))

	def Save_Array_DTC(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[0], index, float(value), xVal, yVal)

	def Save_DTC_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[0], index, str(value))

	def Save_Array_DTC_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[0], index, str(value), xVal, yVal)

	def get_Array_DTC_MaxX(self):
		return self._inArrayX[0]

	Array_DTC_MaxX = property(fget=get_Array_DTC_MaxX)

	def get_Array_DTC_MaxY(self):
		return self._inArrayY[0]

	Array_DTC_MaxY = property(fget=get_Array_DTC_MaxY)

	def DTS(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[1],1, index, True)

	def Array_DTS(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[1],1, index, xVal, yVal, True)

	def DTS_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[1], index)

	def Array_DTS_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[1], index, xVal, yVal)

	def get_DTS_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 1)

	DTS_Name = property(fget=get_DTS_Name)

	def get_DTS_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 2)

	DTS_Units = property(fget=get_DTS_Units)

	def get_DTS_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 3)

	DTS_Comments = property(fget=get_DTS_Comments)

	def Save_DTS_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[1], 3, str(newValue))

	def Get_DTS_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[1], attributeName)

	def Set_DTS_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[1], attributeName, str(newValue))

	def Save_DTS(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[1], index, float(value))

	def Save_Array_DTS(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[1], index, float(value), xVal, yVal)

	def Save_DTS_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[1], index, str(value))

	def Save_Array_DTS_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[1], index, str(value), xVal, yVal)

	def get_Array_DTS_MaxX(self):
		return self._inArrayX[1]

	Array_DTS_MaxX = property(fget=get_Array_DTS_MaxX)

	def get_Array_DTS_MaxY(self):
		return self._inArrayY[1]

	Array_DTS_MaxY = property(fget=get_Array_DTS_MaxY)

	def RHOB(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[2],2, index, True)

	def Array_RHOB(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[2],2, index, xVal, yVal, True)

	def RHOB_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[2], index)

	def Array_RHOB_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[2], index, xVal, yVal)

	def get_RHOB_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 1)

	RHOB_Name = property(fget=get_RHOB_Name)

	def get_RHOB_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 2)

	RHOB_Units = property(fget=get_RHOB_Units)

	def get_RHOB_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 3)

	RHOB_Comments = property(fget=get_RHOB_Comments)

	def Save_RHOB_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[2], 3, str(newValue))

	def Get_RHOB_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[2], attributeName)

	def Set_RHOB_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[2], attributeName, str(newValue))

	def Save_RHOB(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[2], index, float(value))

	def Save_Array_RHOB(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[2], index, float(value), xVal, yVal)

	def Save_RHOB_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[2], index, str(value))

	def Save_Array_RHOB_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[2], index, str(value), xVal, yVal)

	def get_Array_RHOB_MaxX(self):
		return self._inArrayX[2]

	Array_RHOB_MaxX = property(fget=get_Array_RHOB_MaxX)

	def get_Array_RHOB_MaxY(self):
		return self._inArrayY[2]

	Array_RHOB_MaxY = property(fget=get_Array_RHOB_MaxY)

	def PHIT(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[3],3, index, True)

	def Array_PHIT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[3],3, index, xVal, yVal, True)

	def PHIT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[3], index)

	def Array_PHIT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[3], index, xVal, yVal)

	def get_PHIT_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 1)

	PHIT_Name = property(fget=get_PHIT_Name)

	def get_PHIT_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 2)

	PHIT_Units = property(fget=get_PHIT_Units)

	def get_PHIT_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 3)

	PHIT_Comments = property(fget=get_PHIT_Comments)

	def Save_PHIT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[3], 3, str(newValue))

	def Get_PHIT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[3], attributeName)

	def Set_PHIT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[3], attributeName, str(newValue))

	def Save_PHIT(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[3], index, float(value))

	def Save_Array_PHIT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[3], index, float(value), xVal, yVal)

	def Save_PHIT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[3], index, str(value))

	def Save_Array_PHIT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[3], index, str(value), xVal, yVal)

	def get_Array_PHIT_MaxX(self):
		return self._inArrayX[3]

	Array_PHIT_MaxX = property(fget=get_Array_PHIT_MaxX)

	def get_Array_PHIT_MaxY(self):
		return self._inArrayY[3]

	Array_PHIT_MaxY = property(fget=get_Array_PHIT_MaxY)

	def VSH(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[4],4, index, True)

	def Array_VSH(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[4],4, index, xVal, yVal, True)

	def VSH_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[4], index)

	def Array_VSH_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[4], index, xVal, yVal)

	def get_VSH_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 1)

	VSH_Name = property(fget=get_VSH_Name)

	def get_VSH_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 2)

	VSH_Units = property(fget=get_VSH_Units)

	def get_VSH_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 3)

	VSH_Comments = property(fget=get_VSH_Comments)

	def Save_VSH_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[4], 3, str(newValue))

	def Get_VSH_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[4], attributeName)

	def Set_VSH_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[4], attributeName, str(newValue))

	def Save_VSH(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[4], index, float(value))

	def Save_Array_VSH(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[4], index, float(value), xVal, yVal)

	def Save_VSH_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[4], index, str(value))

	def Save_Array_VSH_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[4], index, str(value), xVal, yVal)

	def get_Array_VSH_MaxX(self):
		return self._inArrayX[4]

	Array_VSH_MaxX = property(fget=get_Array_VSH_MaxX)

	def get_Array_VSH_MaxY(self):
		return self._inArrayY[4]

	Array_VSH_MaxY = property(fget=get_Array_VSH_MaxY)

	def Save_POI_RAT_DYN(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, float(value))

	def Save_Array_POI_RAT_DYN(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, float(value), xVal, yVal)

	def Save_POI_RAT_DYN_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, str(value))

	def Save_Array_POI_RAT_DYN_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, str(value), xVal, yVal)

	def POI_RAT_DYN(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[0], index)

	def Array_POI_RAT_DYN(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[0], index, xVal, yVal)

	def POI_RAT_DYN_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[0], index)

	def Array_POI_RAT_DYN_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[0], index, xVal, yVal)

	def get_POI_RAT_DYN_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 1)

	POI_RAT_DYN_Name = property(fget=get_POI_RAT_DYN_Name)

	def get_POI_RAT_DYN_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 2)

	POI_RAT_DYN_Units = property(fget=get_POI_RAT_DYN_Units)

	def get_POI_RAT_DYN_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 3)

	POI_RAT_DYN_Comments = property(fget=get_POI_RAT_DYN_Comments)

	def Save_POI_RAT_DYN_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[0], 3, str(newValue))

	def get_Array_POI_RAT_DYN_MaxX(self):
		return self._outArrayX[0]

	Array_POI_RAT_DYN_MaxX = property(fget=get_Array_POI_RAT_DYN_MaxX)

	def get_Array_POI_RAT_DYN_MaxY(self):
		return self._outArrayY[0]

	Array_POI_RAT_DYN_MaxY = property(fget=get_Array_POI_RAT_DYN_MaxY)

	def Get_POI_RAT_DYN_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[0], attributeName)

	def Set_POI_RAT_DYN_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[0], attributeName, str(newValue))

	def Save_SHE_MOD_DYN(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value))

	def Save_Array_SHE_MOD_DYN(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value), xVal, yVal)

	def Save_SHE_MOD_DYN_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value))

	def Save_Array_SHE_MOD_DYN_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value), xVal, yVal)

	def SHE_MOD_DYN(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[1], index)

	def Array_SHE_MOD_DYN(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[1], index, xVal, yVal)

	def SHE_MOD_DYN_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[1], index)

	def Array_SHE_MOD_DYN_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[1], index, xVal, yVal)

	def get_SHE_MOD_DYN_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 1)

	SHE_MOD_DYN_Name = property(fget=get_SHE_MOD_DYN_Name)

	def get_SHE_MOD_DYN_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 2)

	SHE_MOD_DYN_Units = property(fget=get_SHE_MOD_DYN_Units)

	def get_SHE_MOD_DYN_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 3)

	SHE_MOD_DYN_Comments = property(fget=get_SHE_MOD_DYN_Comments)

	def Save_SHE_MOD_DYN_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[1], 3, str(newValue))

	def get_Array_SHE_MOD_DYN_MaxX(self):
		return self._outArrayX[1]

	Array_SHE_MOD_DYN_MaxX = property(fget=get_Array_SHE_MOD_DYN_MaxX)

	def get_Array_SHE_MOD_DYN_MaxY(self):
		return self._outArrayY[1]

	Array_SHE_MOD_DYN_MaxY = property(fget=get_Array_SHE_MOD_DYN_MaxY)

	def Get_SHE_MOD_DYN_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[1], attributeName)

	def Set_SHE_MOD_DYN_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[1], attributeName, str(newValue))

	def Save_YNG_MOD_DYN(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, float(value))

	def Save_Array_YNG_MOD_DYN(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, float(value), xVal, yVal)

	def Save_YNG_MOD_DYN_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, str(value))

	def Save_Array_YNG_MOD_DYN_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, str(value), xVal, yVal)

	def YNG_MOD_DYN(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[2], index)

	def Array_YNG_MOD_DYN(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[2], index, xVal, yVal)

	def YNG_MOD_DYN_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[2], index)

	def Array_YNG_MOD_DYN_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[2], index, xVal, yVal)

	def get_YNG_MOD_DYN_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 1)

	YNG_MOD_DYN_Name = property(fget=get_YNG_MOD_DYN_Name)

	def get_YNG_MOD_DYN_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 2)

	YNG_MOD_DYN_Units = property(fget=get_YNG_MOD_DYN_Units)

	def get_YNG_MOD_DYN_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 3)

	YNG_MOD_DYN_Comments = property(fget=get_YNG_MOD_DYN_Comments)

	def Save_YNG_MOD_DYN_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[2], 3, str(newValue))

	def get_Array_YNG_MOD_DYN_MaxX(self):
		return self._outArrayX[2]

	Array_YNG_MOD_DYN_MaxX = property(fget=get_Array_YNG_MOD_DYN_MaxX)

	def get_Array_YNG_MOD_DYN_MaxY(self):
		return self._outArrayY[2]

	Array_YNG_MOD_DYN_MaxY = property(fget=get_Array_YNG_MOD_DYN_MaxY)

	def Get_YNG_MOD_DYN_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[2], attributeName)

	def Set_YNG_MOD_DYN_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[2], attributeName, str(newValue))

	def Save_BULK_MOD_DYN(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, float(value))

	def Save_Array_BULK_MOD_DYN(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, float(value), xVal, yVal)

	def Save_BULK_MOD_DYN_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, str(value))

	def Save_Array_BULK_MOD_DYN_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, str(value), xVal, yVal)

	def BULK_MOD_DYN(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[3], index)

	def Array_BULK_MOD_DYN(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[3], index, xVal, yVal)

	def BULK_MOD_DYN_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[3], index)

	def Array_BULK_MOD_DYN_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[3], index, xVal, yVal)

	def get_BULK_MOD_DYN_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 1)

	BULK_MOD_DYN_Name = property(fget=get_BULK_MOD_DYN_Name)

	def get_BULK_MOD_DYN_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 2)

	BULK_MOD_DYN_Units = property(fget=get_BULK_MOD_DYN_Units)

	def get_BULK_MOD_DYN_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 3)

	BULK_MOD_DYN_Comments = property(fget=get_BULK_MOD_DYN_Comments)

	def Save_BULK_MOD_DYN_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[3], 3, str(newValue))

	def get_Array_BULK_MOD_DYN_MaxX(self):
		return self._outArrayX[3]

	Array_BULK_MOD_DYN_MaxX = property(fget=get_Array_BULK_MOD_DYN_MaxX)

	def get_Array_BULK_MOD_DYN_MaxY(self):
		return self._outArrayY[3]

	Array_BULK_MOD_DYN_MaxY = property(fget=get_Array_BULK_MOD_DYN_MaxY)

	def Get_BULK_MOD_DYN_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[3], attributeName)

	def Set_BULK_MOD_DYN_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[3], attributeName, str(newValue))

	def Save_SPI(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, float(value))

	def Save_Array_SPI(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, float(value), xVal, yVal)

	def Save_SPI_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, str(value))

	def Save_Array_SPI_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, str(value), xVal, yVal)

	def SPI(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[4], index)

	def Array_SPI(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[4], index, xVal, yVal)

	def SPI_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[4], index)

	def Array_SPI_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[4], index, xVal, yVal)

	def get_SPI_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 1)

	SPI_Name = property(fget=get_SPI_Name)

	def get_SPI_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 2)

	SPI_Units = property(fget=get_SPI_Units)

	def get_SPI_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 3)

	SPI_Comments = property(fget=get_SPI_Comments)

	def Save_SPI_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[4], 3, str(newValue))

	def get_Array_SPI_MaxX(self):
		return self._outArrayX[4]

	Array_SPI_MaxX = property(fget=get_Array_SPI_MaxX)

	def get_Array_SPI_MaxY(self):
		return self._outArrayY[4]

	Array_SPI_MaxY = property(fget=get_Array_SPI_MaxY)

	def Get_SPI_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[4], attributeName)

	def Set_SPI_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[4], attributeName, str(newValue))

	def Save_UCS_COATES(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[5], index, float(value))

	def Save_Array_UCS_COATES(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[5], index, float(value), xVal, yVal)

	def Save_UCS_COATES_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[5], index, str(value))

	def Save_Array_UCS_COATES_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[5], index, str(value), xVal, yVal)

	def UCS_COATES(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[5], index)

	def Array_UCS_COATES(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[5], index, xVal, yVal)

	def UCS_COATES_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[5], index)

	def Array_UCS_COATES_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[5], index, xVal, yVal)

	def get_UCS_COATES_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 1)

	UCS_COATES_Name = property(fget=get_UCS_COATES_Name)

	def get_UCS_COATES_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 2)

	UCS_COATES_Units = property(fget=get_UCS_COATES_Units)

	def get_UCS_COATES_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 3)

	UCS_COATES_Comments = property(fget=get_UCS_COATES_Comments)

	def Save_UCS_COATES_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[5], 3, str(newValue))

	def get_Array_UCS_COATES_MaxX(self):
		return self._outArrayX[5]

	Array_UCS_COATES_MaxX = property(fget=get_Array_UCS_COATES_MaxX)

	def get_Array_UCS_COATES_MaxY(self):
		return self._outArrayY[5]

	Array_UCS_COATES_MaxY = property(fget=get_Array_UCS_COATES_MaxY)

	def Get_UCS_COATES_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[5], attributeName)

	def Set_UCS_COATES_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[5], attributeName, str(newValue))

	def Save_UCS_PHIT(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[6], index, float(value))

	def Save_Array_UCS_PHIT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[6], index, float(value), xVal, yVal)

	def Save_UCS_PHIT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[6], index, str(value))

	def Save_Array_UCS_PHIT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[6], index, str(value), xVal, yVal)

	def UCS_PHIT(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[6], index)

	def Array_UCS_PHIT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[6], index, xVal, yVal)

	def UCS_PHIT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[6], index)

	def Array_UCS_PHIT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[6], index, xVal, yVal)

	def get_UCS_PHIT_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 1)

	UCS_PHIT_Name = property(fget=get_UCS_PHIT_Name)

	def get_UCS_PHIT_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 2)

	UCS_PHIT_Units = property(fget=get_UCS_PHIT_Units)

	def get_UCS_PHIT_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 3)

	UCS_PHIT_Comments = property(fget=get_UCS_PHIT_Comments)

	def Save_UCS_PHIT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[6], 3, str(newValue))

	def get_Array_UCS_PHIT_MaxX(self):
		return self._outArrayX[6]

	Array_UCS_PHIT_MaxX = property(fget=get_Array_UCS_PHIT_MaxX)

	def get_Array_UCS_PHIT_MaxY(self):
		return self._outArrayY[6]

	Array_UCS_PHIT_MaxY = property(fget=get_Array_UCS_PHIT_MaxY)

	def Get_UCS_PHIT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[6], attributeName)

	def Set_UCS_PHIT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[6], attributeName, str(newValue))

	def Save_POI_RAT_STA(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[7], index, float(value))

	def Save_Array_POI_RAT_STA(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[7], index, float(value), xVal, yVal)

	def Save_POI_RAT_STA_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[7], index, str(value))

	def Save_Array_POI_RAT_STA_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[7], index, str(value), xVal, yVal)

	def POI_RAT_STA(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[7], index)

	def Array_POI_RAT_STA(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[7], index, xVal, yVal)

	def POI_RAT_STA_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[7], index)

	def Array_POI_RAT_STA_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[7], index, xVal, yVal)

	def get_POI_RAT_STA_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 1)

	POI_RAT_STA_Name = property(fget=get_POI_RAT_STA_Name)

	def get_POI_RAT_STA_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 2)

	POI_RAT_STA_Units = property(fget=get_POI_RAT_STA_Units)

	def get_POI_RAT_STA_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 3)

	POI_RAT_STA_Comments = property(fget=get_POI_RAT_STA_Comments)

	def Save_POI_RAT_STA_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[7], 3, str(newValue))

	def get_Array_POI_RAT_STA_MaxX(self):
		return self._outArrayX[7]

	Array_POI_RAT_STA_MaxX = property(fget=get_Array_POI_RAT_STA_MaxX)

	def get_Array_POI_RAT_STA_MaxY(self):
		return self._outArrayY[7]

	Array_POI_RAT_STA_MaxY = property(fget=get_Array_POI_RAT_STA_MaxY)

	def Get_POI_RAT_STA_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[7], attributeName)

	def Set_POI_RAT_STA_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[7], attributeName, str(newValue))

	def Save_YNG_MOD_STA_WANG(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[8], index, float(value))

	def Save_Array_YNG_MOD_STA_WANG(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[8], index, float(value), xVal, yVal)

	def Save_YNG_MOD_STA_WANG_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[8], index, str(value))

	def Save_Array_YNG_MOD_STA_WANG_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[8], index, str(value), xVal, yVal)

	def YNG_MOD_STA_WANG(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[8], index)

	def Array_YNG_MOD_STA_WANG(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[8], index, xVal, yVal)

	def YNG_MOD_STA_WANG_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[8], index)

	def Array_YNG_MOD_STA_WANG_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[8], index, xVal, yVal)

	def get_YNG_MOD_STA_WANG_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 1)

	YNG_MOD_STA_WANG_Name = property(fget=get_YNG_MOD_STA_WANG_Name)

	def get_YNG_MOD_STA_WANG_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 2)

	YNG_MOD_STA_WANG_Units = property(fget=get_YNG_MOD_STA_WANG_Units)

	def get_YNG_MOD_STA_WANG_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 3)

	YNG_MOD_STA_WANG_Comments = property(fget=get_YNG_MOD_STA_WANG_Comments)

	def Save_YNG_MOD_STA_WANG_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[8], 3, str(newValue))

	def get_Array_YNG_MOD_STA_WANG_MaxX(self):
		return self._outArrayX[8]

	Array_YNG_MOD_STA_WANG_MaxX = property(fget=get_Array_YNG_MOD_STA_WANG_MaxX)

	def get_Array_YNG_MOD_STA_WANG_MaxY(self):
		return self._outArrayY[8]

	Array_YNG_MOD_STA_WANG_MaxY = property(fget=get_Array_YNG_MOD_STA_WANG_MaxY)

	def Get_YNG_MOD_STA_WANG_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[8], attributeName)

	def Set_YNG_MOD_STA_WANG_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[8], attributeName, str(newValue))

	def Save_YNG_MOD_STA_MORALS(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[9], index, float(value))

	def Save_Array_YNG_MOD_STA_MORALS(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[9], index, float(value), xVal, yVal)

	def Save_YNG_MOD_STA_MORALS_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[9], index, str(value))

	def Save_Array_YNG_MOD_STA_MORALS_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[9], index, str(value), xVal, yVal)

	def YNG_MOD_STA_MORALS(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[9], index)

	def Array_YNG_MOD_STA_MORALS(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[9], index, xVal, yVal)

	def YNG_MOD_STA_MORALS_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[9], index)

	def Array_YNG_MOD_STA_MORALS_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[9], index, xVal, yVal)

	def get_YNG_MOD_STA_MORALS_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[9], 1)

	YNG_MOD_STA_MORALS_Name = property(fget=get_YNG_MOD_STA_MORALS_Name)

	def get_YNG_MOD_STA_MORALS_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[9], 2)

	YNG_MOD_STA_MORALS_Units = property(fget=get_YNG_MOD_STA_MORALS_Units)

	def get_YNG_MOD_STA_MORALS_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[9], 3)

	YNG_MOD_STA_MORALS_Comments = property(fget=get_YNG_MOD_STA_MORALS_Comments)

	def Save_YNG_MOD_STA_MORALS_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[9], 3, str(newValue))

	def get_Array_YNG_MOD_STA_MORALS_MaxX(self):
		return self._outArrayX[9]

	Array_YNG_MOD_STA_MORALS_MaxX = property(fget=get_Array_YNG_MOD_STA_MORALS_MaxX)

	def get_Array_YNG_MOD_STA_MORALS_MaxY(self):
		return self._outArrayY[9]

	Array_YNG_MOD_STA_MORALS_MaxY = property(fget=get_Array_YNG_MOD_STA_MORALS_MaxY)

	def Get_YNG_MOD_STA_MORALS_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[9], attributeName)

	def Set_YNG_MOD_STA_MORALS_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[9], attributeName, str(newValue))

	def Save_SHE_MOD_STA_WANG(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[10], index, float(value))

	def Save_Array_SHE_MOD_STA_WANG(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[10], index, float(value), xVal, yVal)

	def Save_SHE_MOD_STA_WANG_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[10], index, str(value))

	def Save_Array_SHE_MOD_STA_WANG_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[10], index, str(value), xVal, yVal)

	def SHE_MOD_STA_WANG(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[10], index)

	def Array_SHE_MOD_STA_WANG(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[10], index, xVal, yVal)

	def SHE_MOD_STA_WANG_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[10], index)

	def Array_SHE_MOD_STA_WANG_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[10], index, xVal, yVal)

	def get_SHE_MOD_STA_WANG_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[10], 1)

	SHE_MOD_STA_WANG_Name = property(fget=get_SHE_MOD_STA_WANG_Name)

	def get_SHE_MOD_STA_WANG_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[10], 2)

	SHE_MOD_STA_WANG_Units = property(fget=get_SHE_MOD_STA_WANG_Units)

	def get_SHE_MOD_STA_WANG_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[10], 3)

	SHE_MOD_STA_WANG_Comments = property(fget=get_SHE_MOD_STA_WANG_Comments)

	def Save_SHE_MOD_STA_WANG_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[10], 3, str(newValue))

	def get_Array_SHE_MOD_STA_WANG_MaxX(self):
		return self._outArrayX[10]

	Array_SHE_MOD_STA_WANG_MaxX = property(fget=get_Array_SHE_MOD_STA_WANG_MaxX)

	def get_Array_SHE_MOD_STA_WANG_MaxY(self):
		return self._outArrayY[10]

	Array_SHE_MOD_STA_WANG_MaxY = property(fget=get_Array_SHE_MOD_STA_WANG_MaxY)

	def Get_SHE_MOD_STA_WANG_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[10], attributeName)

	def Set_SHE_MOD_STA_WANG_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[10], attributeName, str(newValue))

	def Save_SHE_MOD_STA_MORALS(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[11], index, float(value))

	def Save_Array_SHE_MOD_STA_MORALS(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[11], index, float(value), xVal, yVal)

	def Save_SHE_MOD_STA_MORALS_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[11], index, str(value))

	def Save_Array_SHE_MOD_STA_MORALS_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[11], index, str(value), xVal, yVal)

	def SHE_MOD_STA_MORALS(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[11], index)

	def Array_SHE_MOD_STA_MORALS(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[11], index, xVal, yVal)

	def SHE_MOD_STA_MORALS_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[11], index)

	def Array_SHE_MOD_STA_MORALS_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[11], index, xVal, yVal)

	def get_SHE_MOD_STA_MORALS_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[11], 1)

	SHE_MOD_STA_MORALS_Name = property(fget=get_SHE_MOD_STA_MORALS_Name)

	def get_SHE_MOD_STA_MORALS_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[11], 2)

	SHE_MOD_STA_MORALS_Units = property(fget=get_SHE_MOD_STA_MORALS_Units)

	def get_SHE_MOD_STA_MORALS_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[11], 3)

	SHE_MOD_STA_MORALS_Comments = property(fget=get_SHE_MOD_STA_MORALS_Comments)

	def Save_SHE_MOD_STA_MORALS_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[11], 3, str(newValue))

	def get_Array_SHE_MOD_STA_MORALS_MaxX(self):
		return self._outArrayX[11]

	Array_SHE_MOD_STA_MORALS_MaxX = property(fget=get_Array_SHE_MOD_STA_MORALS_MaxX)

	def get_Array_SHE_MOD_STA_MORALS_MaxY(self):
		return self._outArrayY[11]

	Array_SHE_MOD_STA_MORALS_MaxY = property(fget=get_Array_SHE_MOD_STA_MORALS_MaxY)

	def Get_SHE_MOD_STA_MORALS_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[11], attributeName)

	def Set_SHE_MOD_STA_MORALS_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[11], attributeName, str(newValue))

	def Save_BULK_MOD_STA_WANG(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[12], index, float(value))

	def Save_Array_BULK_MOD_STA_WANG(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[12], index, float(value), xVal, yVal)

	def Save_BULK_MOD_STA_WANG_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[12], index, str(value))

	def Save_Array_BULK_MOD_STA_WANG_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[12], index, str(value), xVal, yVal)

	def BULK_MOD_STA_WANG(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[12], index)

	def Array_BULK_MOD_STA_WANG(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[12], index, xVal, yVal)

	def BULK_MOD_STA_WANG_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[12], index)

	def Array_BULK_MOD_STA_WANG_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[12], index, xVal, yVal)

	def get_BULK_MOD_STA_WANG_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[12], 1)

	BULK_MOD_STA_WANG_Name = property(fget=get_BULK_MOD_STA_WANG_Name)

	def get_BULK_MOD_STA_WANG_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[12], 2)

	BULK_MOD_STA_WANG_Units = property(fget=get_BULK_MOD_STA_WANG_Units)

	def get_BULK_MOD_STA_WANG_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[12], 3)

	BULK_MOD_STA_WANG_Comments = property(fget=get_BULK_MOD_STA_WANG_Comments)

	def Save_BULK_MOD_STA_WANG_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[12], 3, str(newValue))

	def get_Array_BULK_MOD_STA_WANG_MaxX(self):
		return self._outArrayX[12]

	Array_BULK_MOD_STA_WANG_MaxX = property(fget=get_Array_BULK_MOD_STA_WANG_MaxX)

	def get_Array_BULK_MOD_STA_WANG_MaxY(self):
		return self._outArrayY[12]

	Array_BULK_MOD_STA_WANG_MaxY = property(fget=get_Array_BULK_MOD_STA_WANG_MaxY)

	def Get_BULK_MOD_STA_WANG_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[12], attributeName)

	def Set_BULK_MOD_STA_WANG_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[12], attributeName, str(newValue))

	def Save_BULK_MOD_STA_MORALS(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[13], index, float(value))

	def Save_Array_BULK_MOD_STA_MORALS(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[13], index, float(value), xVal, yVal)

	def Save_BULK_MOD_STA_MORALS_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[13], index, str(value))

	def Save_Array_BULK_MOD_STA_MORALS_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[13], index, str(value), xVal, yVal)

	def BULK_MOD_STA_MORALS(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[13], index)

	def Array_BULK_MOD_STA_MORALS(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[13], index, xVal, yVal)

	def BULK_MOD_STA_MORALS_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[13], index)

	def Array_BULK_MOD_STA_MORALS_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[13], index, xVal, yVal)

	def get_BULK_MOD_STA_MORALS_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[13], 1)

	BULK_MOD_STA_MORALS_Name = property(fget=get_BULK_MOD_STA_MORALS_Name)

	def get_BULK_MOD_STA_MORALS_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[13], 2)

	BULK_MOD_STA_MORALS_Units = property(fget=get_BULK_MOD_STA_MORALS_Units)

	def get_BULK_MOD_STA_MORALS_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[13], 3)

	BULK_MOD_STA_MORALS_Comments = property(fget=get_BULK_MOD_STA_MORALS_Comments)

	def Save_BULK_MOD_STA_MORALS_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[13], 3, str(newValue))

	def get_Array_BULK_MOD_STA_MORALS_MaxX(self):
		return self._outArrayX[13]

	Array_BULK_MOD_STA_MORALS_MaxX = property(fget=get_Array_BULK_MOD_STA_MORALS_MaxX)

	def get_Array_BULK_MOD_STA_MORALS_MaxY(self):
		return self._outArrayY[13]

	Array_BULK_MOD_STA_MORALS_MaxY = property(fget=get_Array_BULK_MOD_STA_MORALS_MaxY)

	def Get_BULK_MOD_STA_MORALS_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[13], attributeName)

	def Set_BULK_MOD_STA_MORALS_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[13], attributeName, str(newValue))

	def Save_P_IMP(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[14], index, float(value))

	def Save_Array_P_IMP(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[14], index, float(value), xVal, yVal)

	def Save_P_IMP_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[14], index, str(value))

	def Save_Array_P_IMP_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[14], index, str(value), xVal, yVal)

	def P_IMP(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[14], index)

	def Array_P_IMP(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[14], index, xVal, yVal)

	def P_IMP_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[14], index)

	def Array_P_IMP_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[14], index, xVal, yVal)

	def get_P_IMP_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[14], 1)

	P_IMP_Name = property(fget=get_P_IMP_Name)

	def get_P_IMP_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[14], 2)

	P_IMP_Units = property(fget=get_P_IMP_Units)

	def get_P_IMP_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[14], 3)

	P_IMP_Comments = property(fget=get_P_IMP_Comments)

	def Save_P_IMP_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[14], 3, str(newValue))

	def get_Array_P_IMP_MaxX(self):
		return self._outArrayX[14]

	Array_P_IMP_MaxX = property(fget=get_Array_P_IMP_MaxX)

	def get_Array_P_IMP_MaxY(self):
		return self._outArrayY[14]

	Array_P_IMP_MaxY = property(fget=get_Array_P_IMP_MaxY)

	def Get_P_IMP_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[14], attributeName)

	def Set_P_IMP_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[14], attributeName, str(newValue))

	def Save_S_IMP(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[15], index, float(value))

	def Save_Array_S_IMP(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[15], index, float(value), xVal, yVal)

	def Save_S_IMP_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[15], index, str(value))

	def Save_Array_S_IMP_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[15], index, str(value), xVal, yVal)

	def S_IMP(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[15], index)

	def Array_S_IMP(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[15], index, xVal, yVal)

	def S_IMP_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[15], index)

	def Array_S_IMP_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[15], index, xVal, yVal)

	def get_S_IMP_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[15], 1)

	S_IMP_Name = property(fget=get_S_IMP_Name)

	def get_S_IMP_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[15], 2)

	S_IMP_Units = property(fget=get_S_IMP_Units)

	def get_S_IMP_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[15], 3)

	S_IMP_Comments = property(fget=get_S_IMP_Comments)

	def Save_S_IMP_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[15], 3, str(newValue))

	def get_Array_S_IMP_MaxX(self):
		return self._outArrayX[15]

	Array_S_IMP_MaxX = property(fget=get_Array_S_IMP_MaxX)

	def get_Array_S_IMP_MaxY(self):
		return self._outArrayY[15]

	Array_S_IMP_MaxY = property(fget=get_Array_S_IMP_MaxY)

	def Get_S_IMP_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[15], attributeName)

	def Set_S_IMP_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[15], attributeName, str(newValue))

