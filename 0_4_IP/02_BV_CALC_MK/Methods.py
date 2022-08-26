# /***********************************************/
#  * File dynamically created from IP: 08/24/2022 15:12:36
#  * DO NOT MANUALLY EDIT
# /***********************************************/

class Methods:
	def __init__(self):
		self._FIRST_AVAILABLE_LOG_RUN = -1
		self._LAST_AVAILABLE_LOG_RUN = -2

	def Depth(self, index):
		return self._IPProxy.GetCurveData(1, index)

	def RESD(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[0],0, index, True)

	def Array_RESD(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[0],0, index, xVal, yVal, True)

	def RESD_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[0], index)

	def Array_RESD_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[0], index, xVal, yVal)

	def get_RESD_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 1)

	RESD_Name = property(fget=get_RESD_Name)

	def get_RESD_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 2)

	RESD_Units = property(fget=get_RESD_Units)

	def get_RESD_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 3)

	RESD_Comments = property(fget=get_RESD_Comments)

	def Save_RESD_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[0], 3, str(newValue))

	def Get_RESD_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[0], attributeName)

	def Set_RESD_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[0], attributeName, str(newValue))

	def Save_RESD(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[0], index, float(value))

	def Save_Array_RESD(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[0], index, float(value), xVal, yVal)

	def Save_RESD_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[0], index, str(value))

	def Save_Array_RESD_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[0], index, str(value), xVal, yVal)

	def get_Array_RESD_MaxX(self):
		return self._inArrayX[0]

	Array_RESD_MaxX = property(fget=get_Array_RESD_MaxX)

	def get_Array_RESD_MaxY(self):
		return self._inArrayY[0]

	Array_RESD_MaxY = property(fget=get_Array_RESD_MaxY)

	def RW(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[1],1, index, True)

	def Array_RW(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[1],1, index, xVal, yVal, True)

	def RW_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[1], index)

	def Array_RW_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[1], index, xVal, yVal)

	def get_RW_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 1)

	RW_Name = property(fget=get_RW_Name)

	def get_RW_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 2)

	RW_Units = property(fget=get_RW_Units)

	def get_RW_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 3)

	RW_Comments = property(fget=get_RW_Comments)

	def Save_RW_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[1], 3, str(newValue))

	def Get_RW_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[1], attributeName)

	def Set_RW_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[1], attributeName, str(newValue))

	def Save_RW(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[1], index, float(value))

	def Save_Array_RW(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[1], index, float(value), xVal, yVal)

	def Save_RW_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[1], index, str(value))

	def Save_Array_RW_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[1], index, str(value), xVal, yVal)

	def get_Array_RW_MaxX(self):
		return self._inArrayX[1]

	Array_RW_MaxX = property(fget=get_Array_RW_MaxX)

	def get_Array_RW_MaxY(self):
		return self._inArrayY[1]

	Array_RW_MaxY = property(fget=get_Array_RW_MaxY)

	def VSH(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[2],2, index, True)

	def Array_VSH(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[2],2, index, xVal, yVal, True)

	def VSH_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[2], index)

	def Array_VSH_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[2], index, xVal, yVal)

	def get_VSH_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 1)

	VSH_Name = property(fget=get_VSH_Name)

	def get_VSH_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 2)

	VSH_Units = property(fget=get_VSH_Units)

	def get_VSH_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[2], 3)

	VSH_Comments = property(fget=get_VSH_Comments)

	def Save_VSH_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[2], 3, str(newValue))

	def Get_VSH_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[2], attributeName)

	def Set_VSH_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[2], attributeName, str(newValue))

	def Save_VSH(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[2], index, float(value))

	def Save_Array_VSH(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[2], index, float(value), xVal, yVal)

	def Save_VSH_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[2], index, str(value))

	def Save_Array_VSH_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[2], index, str(value), xVal, yVal)

	def get_Array_VSH_MaxX(self):
		return self._inArrayX[2]

	Array_VSH_MaxX = property(fget=get_Array_VSH_MaxX)

	def get_Array_VSH_MaxY(self):
		return self._inArrayY[2]

	Array_VSH_MaxY = property(fget=get_Array_VSH_MaxY)

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

	def SWT(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[4],4, index, True)

	def Array_SWT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[4],4, index, xVal, yVal, True)

	def SWT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[4], index)

	def Array_SWT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[4], index, xVal, yVal)

	def get_SWT_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 1)

	SWT_Name = property(fget=get_SWT_Name)

	def get_SWT_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 2)

	SWT_Units = property(fget=get_SWT_Units)

	def get_SWT_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 3)

	SWT_Comments = property(fget=get_SWT_Comments)

	def Save_SWT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[4], 3, str(newValue))

	def Get_SWT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[4], attributeName)

	def Set_SWT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[4], attributeName, str(newValue))

	def Save_SWT(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[4], index, float(value))

	def Save_Array_SWT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[4], index, float(value), xVal, yVal)

	def Save_SWT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[4], index, str(value))

	def Save_Array_SWT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[4], index, str(value), xVal, yVal)

	def get_Array_SWT_MaxX(self):
		return self._inArrayX[4]

	Array_SWT_MaxX = property(fget=get_Array_SWT_MaxX)

	def get_Array_SWT_MaxY(self):
		return self._inArrayY[4]

	Array_SWT_MaxY = property(fget=get_Array_SWT_MaxY)

	def Save_BVW(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, float(value))

	def Save_Array_BVW(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, float(value), xVal, yVal)

	def Save_BVW_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, str(value))

	def Save_Array_BVW_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, str(value), xVal, yVal)

	def BVW(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[0], index)

	def Array_BVW(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[0], index, xVal, yVal)

	def BVW_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[0], index)

	def Array_BVW_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[0], index, xVal, yVal)

	def get_BVW_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 1)

	BVW_Name = property(fget=get_BVW_Name)

	def get_BVW_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 2)

	BVW_Units = property(fget=get_BVW_Units)

	def get_BVW_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 3)

	BVW_Comments = property(fget=get_BVW_Comments)

	def Save_BVW_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[0], 3, str(newValue))

	def get_Array_BVW_MaxX(self):
		return self._outArrayX[0]

	Array_BVW_MaxX = property(fget=get_Array_BVW_MaxX)

	def get_Array_BVW_MaxY(self):
		return self._outArrayY[0]

	Array_BVW_MaxY = property(fget=get_Array_BVW_MaxY)

	def Get_BVW_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[0], attributeName)

	def Set_BVW_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[0], attributeName, str(newValue))

	def Save_BVHC(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value))

	def Save_Array_BVHC(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value), xVal, yVal)

	def Save_BVHC_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value))

	def Save_Array_BVHC_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value), xVal, yVal)

	def BVHC(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[1], index)

	def Array_BVHC(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[1], index, xVal, yVal)

	def BVHC_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[1], index)

	def Array_BVHC_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[1], index, xVal, yVal)

	def get_BVHC_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 1)

	BVHC_Name = property(fget=get_BVHC_Name)

	def get_BVHC_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 2)

	BVHC_Units = property(fget=get_BVHC_Units)

	def get_BVHC_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 3)

	BVHC_Comments = property(fget=get_BVHC_Comments)

	def Save_BVHC_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[1], 3, str(newValue))

	def get_Array_BVHC_MaxX(self):
		return self._outArrayX[1]

	Array_BVHC_MaxX = property(fget=get_Array_BVHC_MaxX)

	def get_Array_BVHC_MaxY(self):
		return self._outArrayY[1]

	Array_BVHC_MaxY = property(fget=get_Array_BVHC_MaxY)

	def Get_BVHC_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[1], attributeName)

	def Set_BVHC_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[1], attributeName, str(newValue))

	def Save_BVSH(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, float(value))

	def Save_Array_BVSH(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, float(value), xVal, yVal)

	def Save_BVSH_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, str(value))

	def Save_Array_BVSH_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, str(value), xVal, yVal)

	def BVSH(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[2], index)

	def Array_BVSH(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[2], index, xVal, yVal)

	def BVSH_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[2], index)

	def Array_BVSH_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[2], index, xVal, yVal)

	def get_BVSH_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 1)

	BVSH_Name = property(fget=get_BVSH_Name)

	def get_BVSH_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 2)

	BVSH_Units = property(fget=get_BVSH_Units)

	def get_BVSH_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 3)

	BVSH_Comments = property(fget=get_BVSH_Comments)

	def Save_BVSH_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[2], 3, str(newValue))

	def get_Array_BVSH_MaxX(self):
		return self._outArrayX[2]

	Array_BVSH_MaxX = property(fget=get_Array_BVSH_MaxX)

	def get_Array_BVSH_MaxY(self):
		return self._outArrayY[2]

	Array_BVSH_MaxY = property(fget=get_Array_BVSH_MaxY)

	def Get_BVSH_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[2], attributeName)

	def Set_BVSH_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[2], attributeName, str(newValue))

	def Save_BVSAND(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, float(value))

	def Save_Array_BVSAND(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, float(value), xVal, yVal)

	def Save_BVSAND_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, str(value))

	def Save_Array_BVSAND_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, str(value), xVal, yVal)

	def BVSAND(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[3], index)

	def Array_BVSAND(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[3], index, xVal, yVal)

	def BVSAND_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[3], index)

	def Array_BVSAND_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[3], index, xVal, yVal)

	def get_BVSAND_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 1)

	BVSAND_Name = property(fget=get_BVSAND_Name)

	def get_BVSAND_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 2)

	BVSAND_Units = property(fget=get_BVSAND_Units)

	def get_BVSAND_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 3)

	BVSAND_Comments = property(fget=get_BVSAND_Comments)

	def Save_BVSAND_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[3], 3, str(newValue))

	def get_Array_BVSAND_MaxX(self):
		return self._outArrayX[3]

	Array_BVSAND_MaxX = property(fget=get_Array_BVSAND_MaxX)

	def get_Array_BVSAND_MaxY(self):
		return self._outArrayY[3]

	Array_BVSAND_MaxY = property(fget=get_Array_BVSAND_MaxY)

	def Get_BVSAND_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[3], attributeName)

	def Set_BVSAND_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[3], attributeName, str(newValue))

	def Save_BVCLAY(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, float(value))

	def Save_Array_BVCLAY(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, float(value), xVal, yVal)

	def Save_BVCLAY_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, str(value))

	def Save_Array_BVCLAY_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, str(value), xVal, yVal)

	def BVCLAY(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[4], index)

	def Array_BVCLAY(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[4], index, xVal, yVal)

	def BVCLAY_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[4], index)

	def Array_BVCLAY_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[4], index, xVal, yVal)

	def get_BVCLAY_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 1)

	BVCLAY_Name = property(fget=get_BVCLAY_Name)

	def get_BVCLAY_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 2)

	BVCLAY_Units = property(fget=get_BVCLAY_Units)

	def get_BVCLAY_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 3)

	BVCLAY_Comments = property(fget=get_BVCLAY_Comments)

	def Save_BVCLAY_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[4], 3, str(newValue))

	def get_Array_BVCLAY_MaxX(self):
		return self._outArrayX[4]

	Array_BVCLAY_MaxX = property(fget=get_Array_BVCLAY_MaxX)

	def get_Array_BVCLAY_MaxY(self):
		return self._outArrayY[4]

	Array_BVCLAY_MaxY = property(fget=get_Array_BVCLAY_MaxY)

	def Get_BVCLAY_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[4], attributeName)

	def Set_BVCLAY_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[4], attributeName, str(newValue))

	def Save_BVSILT(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[5], index, float(value))

	def Save_Array_BVSILT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[5], index, float(value), xVal, yVal)

	def Save_BVSILT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[5], index, str(value))

	def Save_Array_BVSILT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[5], index, str(value), xVal, yVal)

	def BVSILT(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[5], index)

	def Array_BVSILT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[5], index, xVal, yVal)

	def BVSILT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[5], index)

	def Array_BVSILT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[5], index, xVal, yVal)

	def get_BVSILT_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 1)

	BVSILT_Name = property(fget=get_BVSILT_Name)

	def get_BVSILT_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 2)

	BVSILT_Units = property(fget=get_BVSILT_Units)

	def get_BVSILT_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 3)

	BVSILT_Comments = property(fget=get_BVSILT_Comments)

	def Save_BVSILT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[5], 3, str(newValue))

	def get_Array_BVSILT_MaxX(self):
		return self._outArrayX[5]

	Array_BVSILT_MaxX = property(fget=get_Array_BVSILT_MaxX)

	def get_Array_BVSILT_MaxY(self):
		return self._outArrayY[5]

	Array_BVSILT_MaxY = property(fget=get_Array_BVSILT_MaxY)

	def Get_BVSILT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[5], attributeName)

	def Set_BVSILT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[5], attributeName, str(newValue))

	def Save_BVLIM(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[6], index, float(value))

	def Save_Array_BVLIM(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[6], index, float(value), xVal, yVal)

	def Save_BVLIM_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[6], index, str(value))

	def Save_Array_BVLIM_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[6], index, str(value), xVal, yVal)

	def BVLIM(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[6], index)

	def Array_BVLIM(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[6], index, xVal, yVal)

	def BVLIM_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[6], index)

	def Array_BVLIM_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[6], index, xVal, yVal)

	def get_BVLIM_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 1)

	BVLIM_Name = property(fget=get_BVLIM_Name)

	def get_BVLIM_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 2)

	BVLIM_Units = property(fget=get_BVLIM_Units)

	def get_BVLIM_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 3)

	BVLIM_Comments = property(fget=get_BVLIM_Comments)

	def Save_BVLIM_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[6], 3, str(newValue))

	def get_Array_BVLIM_MaxX(self):
		return self._outArrayX[6]

	Array_BVLIM_MaxX = property(fget=get_Array_BVLIM_MaxX)

	def get_Array_BVLIM_MaxY(self):
		return self._outArrayY[6]

	Array_BVLIM_MaxY = property(fget=get_Array_BVLIM_MaxY)

	def Get_BVLIM_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[6], attributeName)

	def Set_BVLIM_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[6], attributeName, str(newValue))

	def Save_SUM_TOT(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[7], index, float(value))

	def Save_Array_SUM_TOT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[7], index, float(value), xVal, yVal)

	def Save_SUM_TOT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[7], index, str(value))

	def Save_Array_SUM_TOT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[7], index, str(value), xVal, yVal)

	def SUM_TOT(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[7], index)

	def Array_SUM_TOT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[7], index, xVal, yVal)

	def SUM_TOT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[7], index)

	def Array_SUM_TOT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[7], index, xVal, yVal)

	def get_SUM_TOT_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 1)

	SUM_TOT_Name = property(fget=get_SUM_TOT_Name)

	def get_SUM_TOT_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 2)

	SUM_TOT_Units = property(fget=get_SUM_TOT_Units)

	def get_SUM_TOT_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 3)

	SUM_TOT_Comments = property(fget=get_SUM_TOT_Comments)

	def Save_SUM_TOT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[7], 3, str(newValue))

	def get_Array_SUM_TOT_MaxX(self):
		return self._outArrayX[7]

	Array_SUM_TOT_MaxX = property(fget=get_Array_SUM_TOT_MaxX)

	def get_Array_SUM_TOT_MaxY(self):
		return self._outArrayY[7]

	Array_SUM_TOT_MaxY = property(fget=get_Array_SUM_TOT_MaxY)

	def Get_SUM_TOT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[7], attributeName)

	def Set_SUM_TOT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[7], attributeName, str(newValue))

	def Save_SD(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[8], index, float(value))

	def Save_Array_SD(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[8], index, float(value), xVal, yVal)

	def Save_SD_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[8], index, str(value))

	def Save_Array_SD_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[8], index, str(value), xVal, yVal)

	def SD(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[8], index)

	def Array_SD(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[8], index, xVal, yVal)

	def SD_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[8], index)

	def Array_SD_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[8], index, xVal, yVal)

	def get_SD_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 1)

	SD_Name = property(fget=get_SD_Name)

	def get_SD_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 2)

	SD_Units = property(fget=get_SD_Units)

	def get_SD_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 3)

	SD_Comments = property(fget=get_SD_Comments)

	def Save_SD_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[8], 3, str(newValue))

	def get_Array_SD_MaxX(self):
		return self._outArrayX[8]

	Array_SD_MaxX = property(fget=get_Array_SD_MaxX)

	def get_Array_SD_MaxY(self):
		return self._outArrayY[8]

	Array_SD_MaxY = property(fget=get_Array_SD_MaxY)

	def Get_SD_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[8], attributeName)

	def Set_SD_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[8], attributeName, str(newValue))

	def Save_RESV(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[9], index, float(value))

	def Save_Array_RESV(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[9], index, float(value), xVal, yVal)

	def Save_RESV_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[9], index, str(value))

	def Save_Array_RESV_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[9], index, str(value), xVal, yVal)

	def RESV(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[9], index)

	def Array_RESV(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[9], index, xVal, yVal)

	def RESV_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[9], index)

	def Array_RESV_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[9], index, xVal, yVal)

	def get_RESV_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[9], 1)

	RESV_Name = property(fget=get_RESV_Name)

	def get_RESV_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[9], 2)

	RESV_Units = property(fget=get_RESV_Units)

	def get_RESV_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[9], 3)

	RESV_Comments = property(fget=get_RESV_Comments)

	def Save_RESV_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[9], 3, str(newValue))

	def get_Array_RESV_MaxX(self):
		return self._outArrayX[9]

	Array_RESV_MaxX = property(fget=get_Array_RESV_MaxX)

	def get_Array_RESV_MaxY(self):
		return self._outArrayY[9]

	Array_RESV_MaxY = property(fget=get_Array_RESV_MaxY)

	def Get_RESV_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[9], attributeName)

	def Set_RESV_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[9], attributeName, str(newValue))

	def Save_PAY(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[10], index, float(value))

	def Save_Array_PAY(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[10], index, float(value), xVal, yVal)

	def Save_PAY_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[10], index, str(value))

	def Save_Array_PAY_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[10], index, str(value), xVal, yVal)

	def PAY(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[10], index)

	def Array_PAY(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[10], index, xVal, yVal)

	def PAY_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[10], index)

	def Array_PAY_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[10], index, xVal, yVal)

	def get_PAY_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[10], 1)

	PAY_Name = property(fget=get_PAY_Name)

	def get_PAY_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[10], 2)

	PAY_Units = property(fget=get_PAY_Units)

	def get_PAY_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[10], 3)

	PAY_Comments = property(fget=get_PAY_Comments)

	def Save_PAY_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[10], 3, str(newValue))

	def get_Array_PAY_MaxX(self):
		return self._outArrayX[10]

	Array_PAY_MaxX = property(fget=get_Array_PAY_MaxX)

	def get_Array_PAY_MaxY(self):
		return self._outArrayY[10]

	Array_PAY_MaxY = property(fget=get_Array_PAY_MaxY)

	def Get_PAY_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[10], attributeName)

	def Set_PAY_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[10], attributeName, str(newValue))

	def Save_BVSALT(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[11], index, float(value))

	def Save_Array_BVSALT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[11], index, float(value), xVal, yVal)

	def Save_BVSALT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[11], index, str(value))

	def Save_Array_BVSALT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[11], index, str(value), xVal, yVal)

	def BVSALT(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[11], index)

	def Array_BVSALT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[11], index, xVal, yVal)

	def BVSALT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[11], index)

	def Array_BVSALT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[11], index, xVal, yVal)

	def get_BVSALT_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[11], 1)

	BVSALT_Name = property(fget=get_BVSALT_Name)

	def get_BVSALT_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[11], 2)

	BVSALT_Units = property(fget=get_BVSALT_Units)

	def get_BVSALT_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[11], 3)

	BVSALT_Comments = property(fget=get_BVSALT_Comments)

	def Save_BVSALT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[11], 3, str(newValue))

	def get_Array_BVSALT_MaxX(self):
		return self._outArrayX[11]

	Array_BVSALT_MaxX = property(fget=get_Array_BVSALT_MaxX)

	def get_Array_BVSALT_MaxY(self):
		return self._outArrayY[11]

	Array_BVSALT_MaxY = property(fget=get_Array_BVSALT_MaxY)

	def Get_BVSALT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[11], attributeName)

	def Set_BVSALT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[11], attributeName, str(newValue))

	def Save_BVASH(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[12], index, float(value))

	def Save_Array_BVASH(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[12], index, float(value), xVal, yVal)

	def Save_BVASH_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[12], index, str(value))

	def Save_Array_BVASH_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[12], index, str(value), xVal, yVal)

	def BVASH(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[12], index)

	def Array_BVASH(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[12], index, xVal, yVal)

	def BVASH_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[12], index)

	def Array_BVASH_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[12], index, xVal, yVal)

	def get_BVASH_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[12], 1)

	BVASH_Name = property(fget=get_BVASH_Name)

	def get_BVASH_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[12], 2)

	BVASH_Units = property(fget=get_BVASH_Units)

	def get_BVASH_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[12], 3)

	BVASH_Comments = property(fget=get_BVASH_Comments)

	def Save_BVASH_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[12], 3, str(newValue))

	def get_Array_BVASH_MaxX(self):
		return self._outArrayX[12]

	Array_BVASH_MaxX = property(fget=get_Array_BVASH_MaxX)

	def get_Array_BVASH_MaxY(self):
		return self._outArrayY[12]

	Array_BVASH_MaxY = property(fget=get_Array_BVASH_MaxY)

	def Get_BVASH_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[12], attributeName)

	def Set_BVASH_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[12], attributeName, str(newValue))

	def m(self, index):
		if self._parCnIn[0] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[0], index)
		else:
			return self._inputParameters[0]

	def Save_m(self, index, value):
		if self._parCnIn[0] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[0], index, float(value))
		else:
			self._IPProxy.SetNumericParam(1, float(value))
			self._inputParameters[0] = float(value)

	def get_m_Name(self):
		if self._parCnIn[0] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[0], 1)
		else:
			return str(self._inputParameters[0])

	m_Name = property(fget=get_m_Name)

	def VSHCO(self, index):
		if self._parCnIn[1] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[1], index)
		else:
			return self._inputParameters[1]

	def Save_VSHCO(self, index, value):
		if self._parCnIn[1] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[1], index, float(value))
		else:
			self._IPProxy.SetNumericParam(2, float(value))
			self._inputParameters[1] = float(value)

	def get_VSHCO_Name(self):
		if self._parCnIn[1] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[1], 1)
		else:
			return str(self._inputParameters[1])

	VSHCO_Name = property(fget=get_VSHCO_Name)

	def PHITCO(self, index):
		if self._parCnIn[2] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[2], index)
		else:
			return self._inputParameters[2]

	def Save_PHITCO(self, index, value):
		if self._parCnIn[2] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[2], index, float(value))
		else:
			self._IPProxy.SetNumericParam(3, float(value))
			self._inputParameters[2] = float(value)

	def get_PHITCO_Name(self):
		if self._parCnIn[2] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[2], 1)
		else:
			return str(self._inputParameters[2])

	PHITCO_Name = property(fget=get_PHITCO_Name)

	def SWTCO(self, index):
		if self._parCnIn[3] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[3], index)
		else:
			return self._inputParameters[3]

	def Save_SWTCO(self, index, value):
		if self._parCnIn[3] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[3], index, float(value))
		else:
			self._IPProxy.SetNumericParam(4, float(value))
			self._inputParameters[3] = float(value)

	def get_SWTCO_Name(self):
		if self._parCnIn[3] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[3], 1)
		else:
			return str(self._inputParameters[3])

	SWTCO_Name = property(fget=get_SWTCO_Name)

	def CLAY_FRAC(self, index):
		if self._parCnIn[4] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[4], index)
		else:
			return self._inputParameters[4]

	def Save_CLAY_FRAC(self, index, value):
		if self._parCnIn[4] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[4], index, float(value))
		else:
			self._IPProxy.SetNumericParam(5, float(value))
			self._inputParameters[4] = float(value)

	def get_CLAY_FRAC_Name(self):
		if self._parCnIn[4] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[4], 1)
		else:
			return str(self._inputParameters[4])

	CLAY_FRAC_Name = property(fget=get_CLAY_FRAC_Name)

	def SAND_FRAC(self, index):
		if self._parCnIn[5] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[5], index)
		else:
			return self._inputParameters[5]

	def Save_SAND_FRAC(self, index, value):
		if self._parCnIn[5] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[5], index, float(value))
		else:
			self._IPProxy.SetNumericParam(6, float(value))
			self._inputParameters[5] = float(value)

	def get_SAND_FRAC_Name(self):
		if self._parCnIn[5] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[5], 1)
		else:
			return str(self._inputParameters[5])

	SAND_FRAC_Name = property(fget=get_SAND_FRAC_Name)

	def get_OPT_CLAY_SILT(self):
		return self._textInputParameters[0]

	OPT_CLAY_SILT = property(fget=get_OPT_CLAY_SILT)

	def get_FLAG_LITH(self):
		return self._textInputParameters[1]

	FLAG_LITH = property(fget=get_FLAG_LITH)

