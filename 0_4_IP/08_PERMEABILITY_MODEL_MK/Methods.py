# /***********************************************/
#  * File dynamically created from IP: 08/25/2022 14:55:15
#  * DO NOT MANUALLY EDIT
# /***********************************************/

class Methods:
	def __init__(self):
		self._FIRST_AVAILABLE_LOG_RUN = -1
		self._LAST_AVAILABLE_LOG_RUN = -2

	def Depth(self, index):
		return self._IPProxy.GetCurveData(1, index)

	def TVDSS(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[0],0, index, True)

	def Array_TVDSS(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[0],0, index, xVal, yVal, True)

	def TVDSS_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[0], index)

	def Array_TVDSS_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[0], index, xVal, yVal)

	def get_TVDSS_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 1)

	TVDSS_Name = property(fget=get_TVDSS_Name)

	def get_TVDSS_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 2)

	TVDSS_Units = property(fget=get_TVDSS_Units)

	def get_TVDSS_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[0], 3)

	TVDSS_Comments = property(fget=get_TVDSS_Comments)

	def Save_TVDSS_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[0], 3, str(newValue))

	def Get_TVDSS_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[0], attributeName)

	def Set_TVDSS_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[0], attributeName, str(newValue))

	def Save_TVDSS(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[0], index, float(value))

	def Save_Array_TVDSS(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[0], index, float(value), xVal, yVal)

	def Save_TVDSS_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[0], index, str(value))

	def Save_Array_TVDSS_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[0], index, str(value), xVal, yVal)

	def get_Array_TVDSS_MaxX(self):
		return self._inArrayX[0]

	Array_TVDSS_MaxX = property(fget=get_Array_TVDSS_MaxX)

	def get_Array_TVDSS_MaxY(self):
		return self._inArrayY[0]

	Array_TVDSS_MaxY = property(fget=get_Array_TVDSS_MaxY)

	def DEPTH(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[1],1, index, True)

	def Array_DEPTH(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[1],1, index, xVal, yVal, True)

	def DEPTH_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[1], index)

	def Array_DEPTH_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[1], index, xVal, yVal)

	def get_DEPTH_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 1)

	DEPTH_Name = property(fget=get_DEPTH_Name)

	def get_DEPTH_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 2)

	DEPTH_Units = property(fget=get_DEPTH_Units)

	def get_DEPTH_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[1], 3)

	DEPTH_Comments = property(fget=get_DEPTH_Comments)

	def Save_DEPTH_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[1], 3, str(newValue))

	def Get_DEPTH_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[1], attributeName)

	def Set_DEPTH_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[1], attributeName, str(newValue))

	def Save_DEPTH(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[1], index, float(value))

	def Save_Array_DEPTH(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[1], index, float(value), xVal, yVal)

	def Save_DEPTH_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[1], index, str(value))

	def Save_Array_DEPTH_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[1], index, str(value), xVal, yVal)

	def get_Array_DEPTH_MaxX(self):
		return self._inArrayX[1]

	Array_DEPTH_MaxX = property(fget=get_Array_DEPTH_MaxX)

	def get_Array_DEPTH_MaxY(self):
		return self._inArrayY[1]

	Array_DEPTH_MaxY = property(fget=get_Array_DEPTH_MaxY)

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

	def RHOM(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[3],3, index, True)

	def Array_RHOM(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[3],3, index, xVal, yVal, True)

	def RHOM_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[3], index)

	def Array_RHOM_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[3], index, xVal, yVal)

	def get_RHOM_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 1)

	RHOM_Name = property(fget=get_RHOM_Name)

	def get_RHOM_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 2)

	RHOM_Units = property(fget=get_RHOM_Units)

	def get_RHOM_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[3], 3)

	RHOM_Comments = property(fget=get_RHOM_Comments)

	def Save_RHOM_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[3], 3, str(newValue))

	def Get_RHOM_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[3], attributeName)

	def Set_RHOM_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[3], attributeName, str(newValue))

	def Save_RHOM(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[3], index, float(value))

	def Save_Array_RHOM(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[3], index, float(value), xVal, yVal)

	def Save_RHOM_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[3], index, str(value))

	def Save_Array_RHOM_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[3], index, str(value), xVal, yVal)

	def get_Array_RHOM_MaxX(self):
		return self._inArrayX[3]

	Array_RHOM_MaxX = property(fget=get_Array_RHOM_MaxX)

	def get_Array_RHOM_MaxY(self):
		return self._inArrayY[3]

	Array_RHOM_MaxY = property(fget=get_Array_RHOM_MaxY)

	def PHIT(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[4],4, index, True)

	def Array_PHIT(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[4],4, index, xVal, yVal, True)

	def PHIT_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[4], index)

	def Array_PHIT_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[4], index, xVal, yVal)

	def get_PHIT_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 1)

	PHIT_Name = property(fget=get_PHIT_Name)

	def get_PHIT_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 2)

	PHIT_Units = property(fget=get_PHIT_Units)

	def get_PHIT_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[4], 3)

	PHIT_Comments = property(fget=get_PHIT_Comments)

	def Save_PHIT_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[4], 3, str(newValue))

	def Get_PHIT_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[4], attributeName)

	def Set_PHIT_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[4], attributeName, str(newValue))

	def Save_PHIT(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[4], index, float(value))

	def Save_Array_PHIT(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[4], index, float(value), xVal, yVal)

	def Save_PHIT_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[4], index, str(value))

	def Save_Array_PHIT_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[4], index, str(value), xVal, yVal)

	def get_Array_PHIT_MaxX(self):
		return self._inArrayX[4]

	Array_PHIT_MaxX = property(fget=get_Array_PHIT_MaxX)

	def get_Array_PHIT_MaxY(self):
		return self._inArrayY[4]

	Array_PHIT_MaxY = property(fget=get_Array_PHIT_MaxY)

	def PHIE(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[5],5, index, True)

	def Array_PHIE(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[5],5, index, xVal, yVal, True)

	def PHIE_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[5], index)

	def Array_PHIE_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[5], index, xVal, yVal)

	def get_PHIE_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 1)

	PHIE_Name = property(fget=get_PHIE_Name)

	def get_PHIE_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 2)

	PHIE_Units = property(fget=get_PHIE_Units)

	def get_PHIE_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[5], 3)

	PHIE_Comments = property(fget=get_PHIE_Comments)

	def Save_PHIE_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[5], 3, str(newValue))

	def Get_PHIE_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[5], attributeName)

	def Set_PHIE_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[5], attributeName, str(newValue))

	def Save_PHIE(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[5], index, float(value))

	def Save_Array_PHIE(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[5], index, float(value), xVal, yVal)

	def Save_PHIE_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[5], index, str(value))

	def Save_Array_PHIE_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[5], index, str(value), xVal, yVal)

	def get_Array_PHIE_MaxX(self):
		return self._inArrayX[5]

	Array_PHIE_MaxX = property(fget=get_Array_PHIE_MaxX)

	def get_Array_PHIE_MaxY(self):
		return self._inArrayY[5]

	Array_PHIE_MaxY = property(fget=get_Array_PHIE_MaxY)

	def SWT_RES(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[6],6, index, True)

	def Array_SWT_RES(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[6],6, index, xVal, yVal, True)

	def SWT_RES_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[6], index)

	def Array_SWT_RES_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[6], index, xVal, yVal)

	def get_SWT_RES_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[6], 1)

	SWT_RES_Name = property(fget=get_SWT_RES_Name)

	def get_SWT_RES_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[6], 2)

	SWT_RES_Units = property(fget=get_SWT_RES_Units)

	def get_SWT_RES_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[6], 3)

	SWT_RES_Comments = property(fget=get_SWT_RES_Comments)

	def Save_SWT_RES_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[6], 3, str(newValue))

	def Get_SWT_RES_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[6], attributeName)

	def Set_SWT_RES_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[6], attributeName, str(newValue))

	def Save_SWT_RES(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[6], index, float(value))

	def Save_Array_SWT_RES(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[6], index, float(value), xVal, yVal)

	def Save_SWT_RES_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[6], index, str(value))

	def Save_Array_SWT_RES_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[6], index, str(value), xVal, yVal)

	def get_Array_SWT_RES_MaxX(self):
		return self._inArrayX[6]

	Array_SWT_RES_MaxX = property(fget=get_Array_SWT_RES_MaxX)

	def get_Array_SWT_RES_MaxY(self):
		return self._inArrayY[6]

	Array_SWT_RES_MaxY = property(fget=get_Array_SWT_RES_MaxY)

	def PERM(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[7],7, index, True)

	def Array_PERM(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[7],7, index, xVal, yVal, True)

	def PERM_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[7], index)

	def Array_PERM_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._inputCurves[7], index, xVal, yVal)

	def get_PERM_Name(self):
		return self._IPProxy.GetCurveText(self._inputCurves[7], 1)

	PERM_Name = property(fget=get_PERM_Name)

	def get_PERM_Units(self):
		return self._IPProxy.GetCurveText(self._inputCurves[7], 2)

	PERM_Units = property(fget=get_PERM_Units)

	def get_PERM_Comments(self):
		return self._IPProxy.GetCurveText(self._inputCurves[7], 3)

	PERM_Comments = property(fget=get_PERM_Comments)

	def Save_PERM_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._inputCurves[7], 3, str(newValue))

	def Get_PERM_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[7], attributeName)

	def Set_PERM_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[7], attributeName, str(newValue))

	def Save_PERM(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[7], index, float(value))

	def Save_Array_PERM(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[7], index, float(value), xVal, yVal)

	def Save_PERM_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[7], index, str(value))

	def Save_Array_PERM_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[7], index, str(value), xVal, yVal)

	def get_Array_PERM_MaxX(self):
		return self._inArrayX[7]

	Array_PERM_MaxX = property(fget=get_Array_PERM_MaxX)

	def get_Array_PERM_MaxY(self):
		return self._inArrayY[7]

	Array_PERM_MaxY = property(fget=get_Array_PERM_MaxY)

	def Save_HAFWL(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, float(value))

	def Save_Array_HAFWL(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, float(value), xVal, yVal)

	def Save_HAFWL_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, str(value))

	def Save_Array_HAFWL_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, str(value), xVal, yVal)

	def HAFWL(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[0], index)

	def Array_HAFWL(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[0], index, xVal, yVal)

	def HAFWL_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[0], index)

	def Array_HAFWL_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[0], index, xVal, yVal)

	def get_HAFWL_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 1)

	HAFWL_Name = property(fget=get_HAFWL_Name)

	def get_HAFWL_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 2)

	HAFWL_Units = property(fget=get_HAFWL_Units)

	def get_HAFWL_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[0], 3)

	HAFWL_Comments = property(fget=get_HAFWL_Comments)

	def Save_HAFWL_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[0], 3, str(newValue))

	def get_Array_HAFWL_MaxX(self):
		return self._outArrayX[0]

	Array_HAFWL_MaxX = property(fget=get_Array_HAFWL_MaxX)

	def get_Array_HAFWL_MaxY(self):
		return self._outArrayY[0]

	Array_HAFWL_MaxY = property(fget=get_Array_HAFWL_MaxY)

	def Get_HAFWL_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[0], attributeName)

	def Set_HAFWL_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[0], attributeName, str(newValue))

	def Save_PCLAB(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value))

	def Save_Array_PCLAB(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, float(value), xVal, yVal)

	def Save_PCLAB_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value))

	def Save_Array_PCLAB_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, str(value), xVal, yVal)

	def PCLAB(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[1], index)

	def Array_PCLAB(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[1], index, xVal, yVal)

	def PCLAB_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[1], index)

	def Array_PCLAB_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[1], index, xVal, yVal)

	def get_PCLAB_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 1)

	PCLAB_Name = property(fget=get_PCLAB_Name)

	def get_PCLAB_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 2)

	PCLAB_Units = property(fget=get_PCLAB_Units)

	def get_PCLAB_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[1], 3)

	PCLAB_Comments = property(fget=get_PCLAB_Comments)

	def Save_PCLAB_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[1], 3, str(newValue))

	def get_Array_PCLAB_MaxX(self):
		return self._outArrayX[1]

	Array_PCLAB_MaxX = property(fget=get_Array_PCLAB_MaxX)

	def get_Array_PCLAB_MaxY(self):
		return self._outArrayY[1]

	Array_PCLAB_MaxY = property(fget=get_Array_PCLAB_MaxY)

	def Get_PCLAB_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[1], attributeName)

	def Set_PCLAB_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[1], attributeName, str(newValue))

	def Save_PCRES(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, float(value))

	def Save_Array_PCRES(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, float(value), xVal, yVal)

	def Save_PCRES_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, str(value))

	def Save_Array_PCRES_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, str(value), xVal, yVal)

	def PCRES(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[2], index)

	def Array_PCRES(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[2], index, xVal, yVal)

	def PCRES_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[2], index)

	def Array_PCRES_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[2], index, xVal, yVal)

	def get_PCRES_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 1)

	PCRES_Name = property(fget=get_PCRES_Name)

	def get_PCRES_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 2)

	PCRES_Units = property(fget=get_PCRES_Units)

	def get_PCRES_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[2], 3)

	PCRES_Comments = property(fget=get_PCRES_Comments)

	def Save_PCRES_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[2], 3, str(newValue))

	def get_Array_PCRES_MaxX(self):
		return self._outArrayX[2]

	Array_PCRES_MaxX = property(fget=get_Array_PCRES_MaxX)

	def get_Array_PCRES_MaxY(self):
		return self._outArrayY[2]

	Array_PCRES_MaxY = property(fget=get_Array_PCRES_MaxY)

	def Get_PCRES_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[2], attributeName)

	def Set_PCRES_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[2], attributeName, str(newValue))

	def Save_SW_PC(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, float(value))

	def Save_Array_SW_PC(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, float(value), xVal, yVal)

	def Save_SW_PC_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, str(value))

	def Save_Array_SW_PC_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, str(value), xVal, yVal)

	def SW_PC(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[3], index)

	def Array_SW_PC(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[3], index, xVal, yVal)

	def SW_PC_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[3], index)

	def Array_SW_PC_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[3], index, xVal, yVal)

	def get_SW_PC_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 1)

	SW_PC_Name = property(fget=get_SW_PC_Name)

	def get_SW_PC_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 2)

	SW_PC_Units = property(fget=get_SW_PC_Units)

	def get_SW_PC_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[3], 3)

	SW_PC_Comments = property(fget=get_SW_PC_Comments)

	def Save_SW_PC_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[3], 3, str(newValue))

	def get_Array_SW_PC_MaxX(self):
		return self._outArrayX[3]

	Array_SW_PC_MaxX = property(fget=get_Array_SW_PC_MaxX)

	def get_Array_SW_PC_MaxY(self):
		return self._outArrayY[3]

	Array_SW_PC_MaxY = property(fget=get_Array_SW_PC_MaxY)

	def Get_SW_PC_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[3], attributeName)

	def Set_SW_PC_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[3], attributeName, str(newValue))

	def Save_TCPERM(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, float(value))

	def Save_Array_TCPERM(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, float(value), xVal, yVal)

	def Save_TCPERM_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, str(value))

	def Save_Array_TCPERM_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, str(value), xVal, yVal)

	def TCPERM(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[4], index)

	def Array_TCPERM(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[4], index, xVal, yVal)

	def TCPERM_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[4], index)

	def Array_TCPERM_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[4], index, xVal, yVal)

	def get_TCPERM_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 1)

	TCPERM_Name = property(fget=get_TCPERM_Name)

	def get_TCPERM_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 2)

	TCPERM_Units = property(fget=get_TCPERM_Units)

	def get_TCPERM_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[4], 3)

	TCPERM_Comments = property(fget=get_TCPERM_Comments)

	def Save_TCPERM_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[4], 3, str(newValue))

	def get_Array_TCPERM_MaxX(self):
		return self._outArrayX[4]

	Array_TCPERM_MaxX = property(fget=get_Array_TCPERM_MaxX)

	def get_Array_TCPERM_MaxY(self):
		return self._outArrayY[4]

	Array_TCPERM_MaxY = property(fget=get_Array_TCPERM_MaxY)

	def Get_TCPERM_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[4], attributeName)

	def Set_TCPERM_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[4], attributeName, str(newValue))

	def Save_TCPERM_PHISH(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[5], index, float(value))

	def Save_Array_TCPERM_PHISH(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[5], index, float(value), xVal, yVal)

	def Save_TCPERM_PHISH_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[5], index, str(value))

	def Save_Array_TCPERM_PHISH_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[5], index, str(value), xVal, yVal)

	def TCPERM_PHISH(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[5], index)

	def Array_TCPERM_PHISH(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[5], index, xVal, yVal)

	def TCPERM_PHISH_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[5], index)

	def Array_TCPERM_PHISH_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[5], index, xVal, yVal)

	def get_TCPERM_PHISH_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 1)

	TCPERM_PHISH_Name = property(fget=get_TCPERM_PHISH_Name)

	def get_TCPERM_PHISH_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 2)

	TCPERM_PHISH_Units = property(fget=get_TCPERM_PHISH_Units)

	def get_TCPERM_PHISH_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[5], 3)

	TCPERM_PHISH_Comments = property(fget=get_TCPERM_PHISH_Comments)

	def Save_TCPERM_PHISH_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[5], 3, str(newValue))

	def get_Array_TCPERM_PHISH_MaxX(self):
		return self._outArrayX[5]

	Array_TCPERM_PHISH_MaxX = property(fget=get_Array_TCPERM_PHISH_MaxX)

	def get_Array_TCPERM_PHISH_MaxY(self):
		return self._outArrayY[5]

	Array_TCPERM_PHISH_MaxY = property(fget=get_Array_TCPERM_PHISH_MaxY)

	def Get_TCPERM_PHISH_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[5], attributeName)

	def Set_TCPERM_PHISH_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[5], attributeName, str(newValue))

	def Save_KTIM_FREE_FLUID(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[6], index, float(value))

	def Save_Array_KTIM_FREE_FLUID(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[6], index, float(value), xVal, yVal)

	def Save_KTIM_FREE_FLUID_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[6], index, str(value))

	def Save_Array_KTIM_FREE_FLUID_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[6], index, str(value), xVal, yVal)

	def KTIM_FREE_FLUID(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[6], index)

	def Array_KTIM_FREE_FLUID(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[6], index, xVal, yVal)

	def KTIM_FREE_FLUID_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[6], index)

	def Array_KTIM_FREE_FLUID_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[6], index, xVal, yVal)

	def get_KTIM_FREE_FLUID_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 1)

	KTIM_FREE_FLUID_Name = property(fget=get_KTIM_FREE_FLUID_Name)

	def get_KTIM_FREE_FLUID_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 2)

	KTIM_FREE_FLUID_Units = property(fget=get_KTIM_FREE_FLUID_Units)

	def get_KTIM_FREE_FLUID_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[6], 3)

	KTIM_FREE_FLUID_Comments = property(fget=get_KTIM_FREE_FLUID_Comments)

	def Save_KTIM_FREE_FLUID_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[6], 3, str(newValue))

	def get_Array_KTIM_FREE_FLUID_MaxX(self):
		return self._outArrayX[6]

	Array_KTIM_FREE_FLUID_MaxX = property(fget=get_Array_KTIM_FREE_FLUID_MaxX)

	def get_Array_KTIM_FREE_FLUID_MaxY(self):
		return self._outArrayY[6]

	Array_KTIM_FREE_FLUID_MaxY = property(fget=get_Array_KTIM_FREE_FLUID_MaxY)

	def Get_KTIM_FREE_FLUID_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[6], attributeName)

	def Set_KTIM_FREE_FLUID_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[6], attributeName, str(newValue))

	def Save_HPERM(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[7], index, float(value))

	def Save_Array_HPERM(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[7], index, float(value), xVal, yVal)

	def Save_HPERM_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[7], index, str(value))

	def Save_Array_HPERM_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[7], index, str(value), xVal, yVal)

	def HPERM(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[7], index)

	def Array_HPERM(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[7], index, xVal, yVal)

	def HPERM_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[7], index)

	def Array_HPERM_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[7], index, xVal, yVal)

	def get_HPERM_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 1)

	HPERM_Name = property(fget=get_HPERM_Name)

	def get_HPERM_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 2)

	HPERM_Units = property(fget=get_HPERM_Units)

	def get_HPERM_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[7], 3)

	HPERM_Comments = property(fget=get_HPERM_Comments)

	def Save_HPERM_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[7], 3, str(newValue))

	def get_Array_HPERM_MaxX(self):
		return self._outArrayX[7]

	Array_HPERM_MaxX = property(fget=get_Array_HPERM_MaxX)

	def get_Array_HPERM_MaxY(self):
		return self._outArrayY[7]

	Array_HPERM_MaxY = property(fget=get_Array_HPERM_MaxY)

	def Get_HPERM_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[7], attributeName)

	def Set_HPERM_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[7], attributeName, str(newValue))

	def Save_LUPERM(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[8], index, float(value))

	def Save_Array_LUPERM(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[8], index, float(value), xVal, yVal)

	def Save_LUPERM_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[8], index, str(value))

	def Save_Array_LUPERM_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[8], index, str(value), xVal, yVal)

	def LUPERM(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[8], index)

	def Array_LUPERM(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[8], index, xVal, yVal)

	def LUPERM_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[8], index)

	def Array_LUPERM_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[8], index, xVal, yVal)

	def get_LUPERM_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 1)

	LUPERM_Name = property(fget=get_LUPERM_Name)

	def get_LUPERM_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 2)

	LUPERM_Units = property(fget=get_LUPERM_Units)

	def get_LUPERM_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[8], 3)

	LUPERM_Comments = property(fget=get_LUPERM_Comments)

	def Save_LUPERM_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[8], 3, str(newValue))

	def get_Array_LUPERM_MaxX(self):
		return self._outArrayX[8]

	Array_LUPERM_MaxX = property(fget=get_Array_LUPERM_MaxX)

	def get_Array_LUPERM_MaxY(self):
		return self._outArrayY[8]

	Array_LUPERM_MaxY = property(fget=get_Array_LUPERM_MaxY)

	def Get_LUPERM_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[8], attributeName)

	def Set_LUPERM_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[8], attributeName, str(newValue))

	def Save_K_RGPZ(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[9], index, float(value))

	def Save_Array_K_RGPZ(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[9], index, float(value), xVal, yVal)

	def Save_K_RGPZ_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[9], index, str(value))

	def Save_Array_K_RGPZ_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[9], index, str(value), xVal, yVal)

	def K_RGPZ(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[9], index)

	def Array_K_RGPZ(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[9], index, xVal, yVal)

	def K_RGPZ_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[9], index)

	def Array_K_RGPZ_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[9], index, xVal, yVal)

	def get_K_RGPZ_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[9], 1)

	K_RGPZ_Name = property(fget=get_K_RGPZ_Name)

	def get_K_RGPZ_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[9], 2)

	K_RGPZ_Units = property(fget=get_K_RGPZ_Units)

	def get_K_RGPZ_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[9], 3)

	K_RGPZ_Comments = property(fget=get_K_RGPZ_Comments)

	def Save_K_RGPZ_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[9], 3, str(newValue))

	def get_Array_K_RGPZ_MaxX(self):
		return self._outArrayX[9]

	Array_K_RGPZ_MaxX = property(fget=get_Array_K_RGPZ_MaxX)

	def get_Array_K_RGPZ_MaxY(self):
		return self._outArrayY[9]

	Array_K_RGPZ_MaxY = property(fget=get_Array_K_RGPZ_MaxY)

	def Get_K_RGPZ_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[9], attributeName)

	def Set_K_RGPZ_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[9], attributeName, str(newValue))

	def Save_REG_PERM_A1(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[10], index, float(value))

	def Save_Array_REG_PERM_A1(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[10], index, float(value), xVal, yVal)

	def Save_REG_PERM_A1_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[10], index, str(value))

	def Save_Array_REG_PERM_A1_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[10], index, str(value), xVal, yVal)

	def REG_PERM_A1(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[10], index)

	def Array_REG_PERM_A1(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[10], index, xVal, yVal)

	def REG_PERM_A1_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[10], index)

	def Array_REG_PERM_A1_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[10], index, xVal, yVal)

	def get_REG_PERM_A1_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[10], 1)

	REG_PERM_A1_Name = property(fget=get_REG_PERM_A1_Name)

	def get_REG_PERM_A1_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[10], 2)

	REG_PERM_A1_Units = property(fget=get_REG_PERM_A1_Units)

	def get_REG_PERM_A1_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[10], 3)

	REG_PERM_A1_Comments = property(fget=get_REG_PERM_A1_Comments)

	def Save_REG_PERM_A1_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[10], 3, str(newValue))

	def get_Array_REG_PERM_A1_MaxX(self):
		return self._outArrayX[10]

	Array_REG_PERM_A1_MaxX = property(fget=get_Array_REG_PERM_A1_MaxX)

	def get_Array_REG_PERM_A1_MaxY(self):
		return self._outArrayY[10]

	Array_REG_PERM_A1_MaxY = property(fget=get_Array_REG_PERM_A1_MaxY)

	def Get_REG_PERM_A1_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[10], attributeName)

	def Set_REG_PERM_A1_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[10], attributeName, str(newValue))

	def Save_REG_PERM_A2(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[11], index, float(value))

	def Save_Array_REG_PERM_A2(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[11], index, float(value), xVal, yVal)

	def Save_REG_PERM_A2_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[11], index, str(value))

	def Save_Array_REG_PERM_A2_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[11], index, str(value), xVal, yVal)

	def REG_PERM_A2(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[11], index)

	def Array_REG_PERM_A2(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[11], index, xVal, yVal)

	def REG_PERM_A2_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[11], index)

	def Array_REG_PERM_A2_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[11], index, xVal, yVal)

	def get_REG_PERM_A2_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[11], 1)

	REG_PERM_A2_Name = property(fget=get_REG_PERM_A2_Name)

	def get_REG_PERM_A2_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[11], 2)

	REG_PERM_A2_Units = property(fget=get_REG_PERM_A2_Units)

	def get_REG_PERM_A2_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[11], 3)

	REG_PERM_A2_Comments = property(fget=get_REG_PERM_A2_Comments)

	def Save_REG_PERM_A2_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[11], 3, str(newValue))

	def get_Array_REG_PERM_A2_MaxX(self):
		return self._outArrayX[11]

	Array_REG_PERM_A2_MaxX = property(fget=get_Array_REG_PERM_A2_MaxX)

	def get_Array_REG_PERM_A2_MaxY(self):
		return self._outArrayY[11]

	Array_REG_PERM_A2_MaxY = property(fget=get_Array_REG_PERM_A2_MaxY)

	def Get_REG_PERM_A2_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[11], attributeName)

	def Set_REG_PERM_A2_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[11], attributeName, str(newValue))

	def Save_PERM_MIN(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[12], index, float(value))

	def Save_Array_PERM_MIN(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[12], index, float(value), xVal, yVal)

	def Save_PERM_MIN_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[12], index, str(value))

	def Save_Array_PERM_MIN_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[12], index, str(value), xVal, yVal)

	def PERM_MIN(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[12], index)

	def Array_PERM_MIN(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[12], index, xVal, yVal)

	def PERM_MIN_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[12], index)

	def Array_PERM_MIN_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[12], index, xVal, yVal)

	def get_PERM_MIN_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[12], 1)

	PERM_MIN_Name = property(fget=get_PERM_MIN_Name)

	def get_PERM_MIN_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[12], 2)

	PERM_MIN_Units = property(fget=get_PERM_MIN_Units)

	def get_PERM_MIN_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[12], 3)

	PERM_MIN_Comments = property(fget=get_PERM_MIN_Comments)

	def Save_PERM_MIN_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[12], 3, str(newValue))

	def get_Array_PERM_MIN_MaxX(self):
		return self._outArrayX[12]

	Array_PERM_MIN_MaxX = property(fget=get_Array_PERM_MIN_MaxX)

	def get_Array_PERM_MIN_MaxY(self):
		return self._outArrayY[12]

	Array_PERM_MIN_MaxY = property(fget=get_Array_PERM_MIN_MaxY)

	def Get_PERM_MIN_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[12], attributeName)

	def Set_PERM_MIN_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[12], attributeName, str(newValue))

	def Save_PERM_MAX(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[13], index, float(value))

	def Save_Array_PERM_MAX(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[13], index, float(value), xVal, yVal)

	def Save_PERM_MAX_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[13], index, str(value))

	def Save_Array_PERM_MAX_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[13], index, str(value), xVal, yVal)

	def PERM_MAX(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[13], index)

	def Array_PERM_MAX(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[13], index, xVal, yVal)

	def PERM_MAX_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[13], index)

	def Array_PERM_MAX_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[13], index, xVal, yVal)

	def get_PERM_MAX_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[13], 1)

	PERM_MAX_Name = property(fget=get_PERM_MAX_Name)

	def get_PERM_MAX_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[13], 2)

	PERM_MAX_Units = property(fget=get_PERM_MAX_Units)

	def get_PERM_MAX_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[13], 3)

	PERM_MAX_Comments = property(fget=get_PERM_MAX_Comments)

	def Save_PERM_MAX_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[13], 3, str(newValue))

	def get_Array_PERM_MAX_MaxX(self):
		return self._outArrayX[13]

	Array_PERM_MAX_MaxX = property(fget=get_Array_PERM_MAX_MaxX)

	def get_Array_PERM_MAX_MaxY(self):
		return self._outArrayY[13]

	Array_PERM_MAX_MaxY = property(fget=get_Array_PERM_MAX_MaxY)

	def Get_PERM_MAX_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[13], attributeName)

	def Set_PERM_MAX_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[13], attributeName, str(newValue))

	def Save_PERM_FINAL(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[14], index, float(value))

	def Save_Array_PERM_FINAL(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[14], index, float(value), xVal, yVal)

	def Save_PERM_FINAL_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[14], index, str(value))

	def Save_Array_PERM_FINAL_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[14], index, str(value), xVal, yVal)

	def PERM_FINAL(self, index):
		return self._IPProxy.GetCurveData(self._outputCurves[14], index)

	def Array_PERM_FINAL(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._outputCurves[14], index, xVal, yVal)

	def PERM_FINAL_Text(self, index):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[14], index)

	def Array_PERM_FINAL_Text(self, index, xVal, yVal):
		return self._IPProxy.GetTextCurveValue(self._outputCurves[14], index, xVal, yVal)

	def get_PERM_FINAL_Name(self):
		return self._IPProxy.GetCurveText(self._outputCurves[14], 1)

	PERM_FINAL_Name = property(fget=get_PERM_FINAL_Name)

	def get_PERM_FINAL_Units(self):
		return self._IPProxy.GetCurveText(self._outputCurves[14], 2)

	PERM_FINAL_Units = property(fget=get_PERM_FINAL_Units)

	def get_PERM_FINAL_Comments(self):
		return self._IPProxy.GetCurveText(self._outputCurves[14], 3)

	PERM_FINAL_Comments = property(fget=get_PERM_FINAL_Comments)

	def Save_PERM_FINAL_Comments(self, newValue):
		self._IPProxy.SetCurveText(self._outputCurves[14], 3, str(newValue))

	def get_Array_PERM_FINAL_MaxX(self):
		return self._outArrayX[14]

	Array_PERM_FINAL_MaxX = property(fget=get_Array_PERM_FINAL_MaxX)

	def get_Array_PERM_FINAL_MaxY(self):
		return self._outArrayY[14]

	Array_PERM_FINAL_MaxY = property(fget=get_Array_PERM_FINAL_MaxY)

	def Get_PERM_FINAL_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[14], attributeName)

	def Set_PERM_FINAL_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[14], attributeName, str(newValue))

	def TCOST_AW_L(self, index):
		if self._parCnIn[0] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[0], index)
		else:
			return self._inputParameters[0]

	def Save_TCOST_AW_L(self, index, value):
		if self._parCnIn[0] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[0], index, float(value))
		else:
			self._IPProxy.SetNumericParam(1, float(value))
			self._inputParameters[0] = float(value)

	def get_TCOST_AW_L_Name(self):
		if self._parCnIn[0] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[0], 1)
		else:
			return str(self._inputParameters[0])

	TCOST_AW_L_Name = property(fget=get_TCOST_AW_L_Name)

	def TCOST_GW_R(self, index):
		if self._parCnIn[1] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[1], index)
		else:
			return self._inputParameters[1]

	def Save_TCOST_GW_R(self, index, value):
		if self._parCnIn[1] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[1], index, float(value))
		else:
			self._IPProxy.SetNumericParam(2, float(value))
			self._inputParameters[1] = float(value)

	def get_TCOST_GW_R_Name(self):
		if self._parCnIn[1] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[1], 1)
		else:
			return str(self._inputParameters[1])

	TCOST_GW_R_Name = property(fget=get_TCOST_GW_R_Name)

	def TCOST_OW_L(self, index):
		if self._parCnIn[2] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[2], index)
		else:
			return self._inputParameters[2]

	def Save_TCOST_OW_L(self, index, value):
		if self._parCnIn[2] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[2], index, float(value))
		else:
			self._IPProxy.SetNumericParam(3, float(value))
			self._inputParameters[2] = float(value)

	def get_TCOST_OW_L_Name(self):
		if self._parCnIn[2] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[2], 1)
		else:
			return str(self._inputParameters[2])

	TCOST_OW_L_Name = property(fget=get_TCOST_OW_L_Name)

	def TCOST_OW_R(self, index):
		if self._parCnIn[3] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[3], index)
		else:
			return self._inputParameters[3]

	def Save_TCOST_OW_R(self, index, value):
		if self._parCnIn[3] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[3], index, float(value))
		else:
			self._IPProxy.SetNumericParam(4, float(value))
			self._inputParameters[3] = float(value)

	def get_TCOST_OW_R_Name(self):
		if self._parCnIn[3] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[3], 1)
		else:
			return str(self._inputParameters[3])

	TCOST_OW_R_Name = property(fget=get_TCOST_OW_R_Name)

	def A_C0(self, index):
		if self._parCnIn[4] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[4], index)
		else:
			return self._inputParameters[4]

	def Save_A_C0(self, index, value):
		if self._parCnIn[4] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[4], index, float(value))
		else:
			self._IPProxy.SetNumericParam(5, float(value))
			self._inputParameters[4] = float(value)

	def get_A_C0_Name(self):
		if self._parCnIn[4] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[4], 1)
		else:
			return str(self._inputParameters[4])

	A_C0_Name = property(fget=get_A_C0_Name)

	def A_C1(self, index):
		if self._parCnIn[5] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[5], index)
		else:
			return self._inputParameters[5]

	def Save_A_C1(self, index, value):
		if self._parCnIn[5] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[5], index, float(value))
		else:
			self._IPProxy.SetNumericParam(6, float(value))
			self._inputParameters[5] = float(value)

	def get_A_C1_Name(self):
		if self._parCnIn[5] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[5], 1)
		else:
			return str(self._inputParameters[5])

	A_C1_Name = property(fget=get_A_C1_Name)

	def A_C2(self, index):
		if self._parCnIn[6] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[6], index)
		else:
			return self._inputParameters[6]

	def Save_A_C2(self, index, value):
		if self._parCnIn[6] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[6], index, float(value))
		else:
			self._IPProxy.SetNumericParam(7, float(value))
			self._inputParameters[6] = float(value)

	def get_A_C2_Name(self):
		if self._parCnIn[6] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[6], 1)
		else:
			return str(self._inputParameters[6])

	A_C2_Name = property(fget=get_A_C2_Name)

	def A_C3(self, index):
		if self._parCnIn[7] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[7], index)
		else:
			return self._inputParameters[7]

	def Save_A_C3(self, index, value):
		if self._parCnIn[7] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[7], index, float(value))
		else:
			self._IPProxy.SetNumericParam(8, float(value))
			self._inputParameters[7] = float(value)

	def get_A_C3_Name(self):
		if self._parCnIn[7] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[7], 1)
		else:
			return str(self._inputParameters[7])

	A_C3_Name = property(fget=get_A_C3_Name)

	def A_C4(self, index):
		if self._parCnIn[8] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[8], index)
		else:
			return self._inputParameters[8]

	def Save_A_C4(self, index, value):
		if self._parCnIn[8] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[8], index, float(value))
		else:
			self._IPProxy.SetNumericParam(9, float(value))
			self._inputParameters[8] = float(value)

	def get_A_C4_Name(self):
		if self._parCnIn[8] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[8], 1)
		else:
			return str(self._inputParameters[8])

	A_C4_Name = property(fget=get_A_C4_Name)

	def B_C0(self, index):
		if self._parCnIn[9] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[9], index)
		else:
			return self._inputParameters[9]

	def Save_B_C0(self, index, value):
		if self._parCnIn[9] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[9], index, float(value))
		else:
			self._IPProxy.SetNumericParam(10, float(value))
			self._inputParameters[9] = float(value)

	def get_B_C0_Name(self):
		if self._parCnIn[9] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[9], 1)
		else:
			return str(self._inputParameters[9])

	B_C0_Name = property(fget=get_B_C0_Name)

	def B_C1(self, index):
		if self._parCnIn[10] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[10], index)
		else:
			return self._inputParameters[10]

	def Save_B_C1(self, index, value):
		if self._parCnIn[10] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[10], index, float(value))
		else:
			self._IPProxy.SetNumericParam(11, float(value))
			self._inputParameters[10] = float(value)

	def get_B_C1_Name(self):
		if self._parCnIn[10] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[10], 1)
		else:
			return str(self._inputParameters[10])

	B_C1_Name = property(fget=get_B_C1_Name)

	def B_C2(self, index):
		if self._parCnIn[11] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[11], index)
		else:
			return self._inputParameters[11]

	def Save_B_C2(self, index, value):
		if self._parCnIn[11] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[11], index, float(value))
		else:
			self._IPProxy.SetNumericParam(12, float(value))
			self._inputParameters[11] = float(value)

	def get_B_C2_Name(self):
		if self._parCnIn[11] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[11], 1)
		else:
			return str(self._inputParameters[11])

	B_C2_Name = property(fget=get_B_C2_Name)

	def B_C3(self, index):
		if self._parCnIn[12] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[12], index)
		else:
			return self._inputParameters[12]

	def Save_B_C3(self, index, value):
		if self._parCnIn[12] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[12], index, float(value))
		else:
			self._IPProxy.SetNumericParam(13, float(value))
			self._inputParameters[12] = float(value)

	def get_B_C3_Name(self):
		if self._parCnIn[12] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[12], 1)
		else:
			return str(self._inputParameters[12])

	B_C3_Name = property(fget=get_B_C3_Name)

	def C_C0(self, index):
		if self._parCnIn[13] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[13], index)
		else:
			return self._inputParameters[13]

	def Save_C_C0(self, index, value):
		if self._parCnIn[13] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[13], index, float(value))
		else:
			self._IPProxy.SetNumericParam(14, float(value))
			self._inputParameters[13] = float(value)

	def get_C_C0_Name(self):
		if self._parCnIn[13] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[13], 1)
		else:
			return str(self._inputParameters[13])

	C_C0_Name = property(fget=get_C_C0_Name)

	def C_C1(self, index):
		if self._parCnIn[14] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[14], index)
		else:
			return self._inputParameters[14]

	def Save_C_C1(self, index, value):
		if self._parCnIn[14] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[14], index, float(value))
		else:
			self._IPProxy.SetNumericParam(15, float(value))
			self._inputParameters[14] = float(value)

	def get_C_C1_Name(self):
		if self._parCnIn[14] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[14], 1)
		else:
			return str(self._inputParameters[14])

	C_C1_Name = property(fget=get_C_C1_Name)

	def C_C2(self, index):
		if self._parCnIn[15] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[15], index)
		else:
			return self._inputParameters[15]

	def Save_C_C2(self, index, value):
		if self._parCnIn[15] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[15], index, float(value))
		else:
			self._IPProxy.SetNumericParam(16, float(value))
			self._inputParameters[15] = float(value)

	def get_C_C2_Name(self):
		if self._parCnIn[15] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[15], 1)
		else:
			return str(self._inputParameters[15])

	C_C2_Name = property(fget=get_C_C2_Name)

	def C_C3(self, index):
		if self._parCnIn[16] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[16], index)
		else:
			return self._inputParameters[16]

	def Save_C_C3(self, index, value):
		if self._parCnIn[16] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[16], index, float(value))
		else:
			self._IPProxy.SetNumericParam(17, float(value))
			self._inputParameters[16] = float(value)

	def get_C_C3_Name(self):
		if self._parCnIn[16] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[16], 1)
		else:
			return str(self._inputParameters[16])

	C_C3_Name = property(fget=get_C_C3_Name)

	def C_C4(self, index):
		if self._parCnIn[17] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[17], index)
		else:
			return self._inputParameters[17]

	def Save_C_C4(self, index, value):
		if self._parCnIn[17] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[17], index, float(value))
		else:
			self._IPProxy.SetNumericParam(18, float(value))
			self._inputParameters[17] = float(value)

	def get_C_C4_Name(self):
		if self._parCnIn[17] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[17], 1)
		else:
			return str(self._inputParameters[17])

	C_C4_Name = property(fget=get_C_C4_Name)

	def D_C0(self, index):
		if self._parCnIn[18] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[18], index)
		else:
			return self._inputParameters[18]

	def Save_D_C0(self, index, value):
		if self._parCnIn[18] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[18], index, float(value))
		else:
			self._IPProxy.SetNumericParam(19, float(value))
			self._inputParameters[18] = float(value)

	def get_D_C0_Name(self):
		if self._parCnIn[18] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[18], 1)
		else:
			return str(self._inputParameters[18])

	D_C0_Name = property(fget=get_D_C0_Name)

	def D_C1(self, index):
		if self._parCnIn[19] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[19], index)
		else:
			return self._inputParameters[19]

	def Save_D_C1(self, index, value):
		if self._parCnIn[19] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[19], index, float(value))
		else:
			self._IPProxy.SetNumericParam(20, float(value))
			self._inputParameters[19] = float(value)

	def get_D_C1_Name(self):
		if self._parCnIn[19] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[19], 1)
		else:
			return str(self._inputParameters[19])

	D_C1_Name = property(fget=get_D_C1_Name)

	def D_C2(self, index):
		if self._parCnIn[20] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[20], index)
		else:
			return self._inputParameters[20]

	def Save_D_C2(self, index, value):
		if self._parCnIn[20] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[20], index, float(value))
		else:
			self._IPProxy.SetNumericParam(21, float(value))
			self._inputParameters[20] = float(value)

	def get_D_C2_Name(self):
		if self._parCnIn[20] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[20], 1)
		else:
			return str(self._inputParameters[20])

	D_C2_Name = property(fget=get_D_C2_Name)

	def D_C3(self, index):
		if self._parCnIn[21] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[21], index)
		else:
			return self._inputParameters[21]

	def Save_D_C3(self, index, value):
		if self._parCnIn[21] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[21], index, float(value))
		else:
			self._IPProxy.SetNumericParam(22, float(value))
			self._inputParameters[21] = float(value)

	def get_D_C3_Name(self):
		if self._parCnIn[21] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[21], 1)
		else:
			return str(self._inputParameters[21])

	D_C3_Name = property(fget=get_D_C3_Name)

	def D_C4(self, index):
		if self._parCnIn[22] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[22], index)
		else:
			return self._inputParameters[22]

	def Save_D_C4(self, index, value):
		if self._parCnIn[22] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[22], index, float(value))
		else:
			self._IPProxy.SetNumericParam(23, float(value))
			self._inputParameters[22] = float(value)

	def get_D_C4_Name(self):
		if self._parCnIn[22] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[22], 1)
		else:
			return str(self._inputParameters[22])

	D_C4_Name = property(fget=get_D_C4_Name)

	def E1(self, index):
		if self._parCnIn[23] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[23], index)
		else:
			return self._inputParameters[23]

	def Save_E1(self, index, value):
		if self._parCnIn[23] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[23], index, float(value))
		else:
			self._IPProxy.SetNumericParam(24, float(value))
			self._inputParameters[23] = float(value)

	def get_E1_Name(self):
		if self._parCnIn[23] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[23], 1)
		else:
			return str(self._inputParameters[23])

	E1_Name = property(fget=get_E1_Name)

	def F1(self, index):
		if self._parCnIn[24] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[24], index)
		else:
			return self._inputParameters[24]

	def Save_F1(self, index, value):
		if self._parCnIn[24] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[24], index, float(value))
		else:
			self._IPProxy.SetNumericParam(25, float(value))
			self._inputParameters[24] = float(value)

	def get_F1_Name(self):
		if self._parCnIn[24] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[24], 1)
		else:
			return str(self._inputParameters[24])

	F1_Name = property(fget=get_F1_Name)

	def E2(self, index):
		if self._parCnIn[25] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[25], index)
		else:
			return self._inputParameters[25]

	def Save_E2(self, index, value):
		if self._parCnIn[25] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[25], index, float(value))
		else:
			self._IPProxy.SetNumericParam(26, float(value))
			self._inputParameters[25] = float(value)

	def get_E2_Name(self):
		if self._parCnIn[25] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[25], 1)
		else:
			return str(self._inputParameters[25])

	E2_Name = property(fget=get_E2_Name)

	def F2(self, index):
		if self._parCnIn[26] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[26], index)
		else:
			return self._inputParameters[26]

	def Save_F2(self, index, value):
		if self._parCnIn[26] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[26], index, float(value))
		else:
			self._IPProxy.SetNumericParam(27, float(value))
			self._inputParameters[26] = float(value)

	def get_F2_Name(self):
		if self._parCnIn[26] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[26], 1)
		else:
			return str(self._inputParameters[26])

	F2_Name = property(fget=get_F2_Name)

	def FLAG_SWT_RES(self, index):
		if self._parCnIn[27] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[27], index)
		else:
			return self._inputParameters[27]

	def Save_FLAG_SWT_RES(self, index, value):
		if self._parCnIn[27] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[27], index, float(value))
		else:
			self._IPProxy.SetNumericParam(28, float(value))
			self._inputParameters[27] = float(value)

	def get_FLAG_SWT_RES_Name(self):
		if self._parCnIn[27] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[27], 1)
		else:
			return str(self._inputParameters[27])

	FLAG_SWT_RES_Name = property(fget=get_FLAG_SWT_RES_Name)

	def MC(self, index):
		if self._parCnIn[28] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[28], index)
		else:
			return self._inputParameters[28]

	def Save_MC(self, index, value):
		if self._parCnIn[28] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[28], index, float(value))
		else:
			self._IPProxy.SetNumericParam(29, float(value))
			self._inputParameters[28] = float(value)

	def get_MC_Name(self):
		if self._parCnIn[28] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[28], 1)
		else:
			return str(self._inputParameters[28])

	MC_Name = property(fget=get_MC_Name)

	def SR(self, index):
		if self._parCnIn[29] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[29], index)
		else:
			return self._inputParameters[29]

	def Save_SR(self, index, value):
		if self._parCnIn[29] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[29], index, float(value))
		else:
			self._IPProxy.SetNumericParam(30, float(value))
			self._inputParameters[29] = float(value)

	def get_SR_Name(self):
		if self._parCnIn[29] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[29], 1)
		else:
			return str(self._inputParameters[29])

	SR_Name = property(fget=get_SR_Name)

	def G_GD(self, index):
		if self._parCnIn[30] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[30], index)
		else:
			return self._inputParameters[30]

	def Save_G_GD(self, index, value):
		if self._parCnIn[30] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[30], index, float(value))
		else:
			self._IPProxy.SetNumericParam(31, float(value))
			self._inputParameters[30] = float(value)

	def get_G_GD_Name(self):
		if self._parCnIn[30] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[30], 1)
		else:
			return str(self._inputParameters[30])

	G_GD_Name = property(fget=get_G_GD_Name)

	def O_GD(self, index):
		if self._parCnIn[31] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[31], index)
		else:
			return self._inputParameters[31]

	def Save_O_GD(self, index, value):
		if self._parCnIn[31] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[31], index, float(value))
		else:
			self._IPProxy.SetNumericParam(32, float(value))
			self._inputParameters[31] = float(value)

	def get_O_GD_Name(self):
		if self._parCnIn[31] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[31], 1)
		else:
			return str(self._inputParameters[31])

	O_GD_Name = property(fget=get_O_GD_Name)

	def W_GD(self, index):
		if self._parCnIn[32] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[32], index)
		else:
			return self._inputParameters[32]

	def Save_W_GD(self, index, value):
		if self._parCnIn[32] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[32], index, float(value))
		else:
			self._IPProxy.SetNumericParam(33, float(value))
			self._inputParameters[32] = float(value)

	def get_W_GD_Name(self):
		if self._parCnIn[32] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[32], 1)
		else:
			return str(self._inputParameters[32])

	W_GD_Name = property(fget=get_W_GD_Name)

	def GOC(self, index):
		if self._parCnIn[33] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[33], index)
		else:
			return self._inputParameters[33]

	def Save_GOC(self, index, value):
		if self._parCnIn[33] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[33], index, float(value))
		else:
			self._IPProxy.SetNumericParam(34, float(value))
			self._inputParameters[33] = float(value)

	def get_GOC_Name(self):
		if self._parCnIn[33] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[33], 1)
		else:
			return str(self._inputParameters[33])

	GOC_Name = property(fget=get_GOC_Name)

	def FWL(self, index):
		if self._parCnIn[34] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[34], index)
		else:
			return self._inputParameters[34]

	def Save_FWL(self, index, value):
		if self._parCnIn[34] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[34], index, float(value))
		else:
			self._IPProxy.SetNumericParam(35, float(value))
			self._inputParameters[34] = float(value)

	def get_FWL_Name(self):
		if self._parCnIn[34] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[34], 1)
		else:
			return str(self._inputParameters[34])

	FWL_Name = property(fget=get_FWL_Name)

	def Y(self, index):
		if self._parCnIn[35] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[35], index)
		else:
			return self._inputParameters[35]

	def Save_Y(self, index, value):
		if self._parCnIn[35] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[35], index, float(value))
		else:
			self._IPProxy.SetNumericParam(36, float(value))
			self._inputParameters[35] = float(value)

	def get_Y_Name(self):
		if self._parCnIn[35] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[35], 1)
		else:
			return str(self._inputParameters[35])

	Y_Name = property(fget=get_Y_Name)

	def Z1(self, index):
		if self._parCnIn[36] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[36], index)
		else:
			return self._inputParameters[36]

	def Save_Z1(self, index, value):
		if self._parCnIn[36] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[36], index, float(value))
		else:
			self._IPProxy.SetNumericParam(37, float(value))
			self._inputParameters[36] = float(value)

	def get_Z1_Name(self):
		if self._parCnIn[36] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[36], 1)
		else:
			return str(self._inputParameters[36])

	Z1_Name = property(fget=get_Z1_Name)

	def SA_CL(self, index):
		if self._parCnIn[37] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[37], index)
		else:
			return self._inputParameters[37]

	def Save_SA_CL(self, index, value):
		if self._parCnIn[37] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[37], index, float(value))
		else:
			self._IPProxy.SetNumericParam(38, float(value))
			self._inputParameters[37] = float(value)

	def get_SA_CL_Name(self):
		if self._parCnIn[37] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[37], 1)
		else:
			return str(self._inputParameters[37])

	SA_CL_Name = property(fget=get_SA_CL_Name)

	def SA_SA(self, index):
		if self._parCnIn[38] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[38], index)
		else:
			return self._inputParameters[38]

	def Save_SA_SA(self, index, value):
		if self._parCnIn[38] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[38], index, float(value))
		else:
			self._IPProxy.SetNumericParam(39, float(value))
			self._inputParameters[38] = float(value)

	def get_SA_SA_Name(self):
		if self._parCnIn[38] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[38], 1)
		else:
			return str(self._inputParameters[38])

	SA_SA_Name = property(fget=get_SA_SA_Name)

	def VI(self, index):
		if self._parCnIn[39] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[39], index)
		else:
			return self._inputParameters[39]

	def Save_VI(self, index, value):
		if self._parCnIn[39] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[39], index, float(value))
		else:
			self._IPProxy.SetNumericParam(40, float(value))
			self._inputParameters[39] = float(value)

	def get_VI_Name(self):
		if self._parCnIn[39] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[39], 1)
		else:
			return str(self._inputParameters[39])

	VI_Name = property(fget=get_VI_Name)

	def ALPHA(self, index):
		if self._parCnIn[40] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[40], index)
		else:
			return self._inputParameters[40]

	def Save_ALPHA(self, index, value):
		if self._parCnIn[40] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[40], index, float(value))
		else:
			self._IPProxy.SetNumericParam(41, float(value))
			self._inputParameters[40] = float(value)

	def get_ALPHA_Name(self):
		if self._parCnIn[40] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[40], 1)
		else:
			return str(self._inputParameters[40])

	ALPHA_Name = property(fget=get_ALPHA_Name)

	def BETA(self, index):
		if self._parCnIn[41] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[41], index)
		else:
			return self._inputParameters[41]

	def Save_BETA(self, index, value):
		if self._parCnIn[41] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[41], index, float(value))
		else:
			self._IPProxy.SetNumericParam(42, float(value))
			self._inputParameters[41] = float(value)

	def get_BETA_Name(self):
		if self._parCnIn[41] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[41], 1)
		else:
			return str(self._inputParameters[41])

	BETA_Name = property(fget=get_BETA_Name)

	def GAM(self, index):
		if self._parCnIn[42] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[42], index)
		else:
			return self._inputParameters[42]

	def Save_GAM(self, index, value):
		if self._parCnIn[42] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[42], index, float(value))
		else:
			self._IPProxy.SetNumericParam(43, float(value))
			self._inputParameters[42] = float(value)

	def get_GAM_Name(self):
		if self._parCnIn[42] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[42], 1)
		else:
			return str(self._inputParameters[42])

	GAM_Name = property(fget=get_GAM_Name)

	def CHARLIE(self, index):
		if self._parCnIn[43] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[43], index)
		else:
			return self._inputParameters[43]

	def Save_CHARLIE(self, index, value):
		if self._parCnIn[43] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[43], index, float(value))
		else:
			self._IPProxy.SetNumericParam(44, float(value))
			self._inputParameters[43] = float(value)

	def get_CHARLIE_Name(self):
		if self._parCnIn[43] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[43], 1)
		else:
			return str(self._inputParameters[43])

	CHARLIE_Name = property(fget=get_CHARLIE_Name)

	def GSI_SD(self, index):
		if self._parCnIn[44] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[44], index)
		else:
			return self._inputParameters[44]

	def Save_GSI_SD(self, index, value):
		if self._parCnIn[44] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[44], index, float(value))
		else:
			self._IPProxy.SetNumericParam(45, float(value))
			self._inputParameters[44] = float(value)

	def get_GSI_SD_Name(self):
		if self._parCnIn[44] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[44], 1)
		else:
			return str(self._inputParameters[44])

	GSI_SD_Name = property(fget=get_GSI_SD_Name)

	def GSI_SI(self, index):
		if self._parCnIn[45] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[45], index)
		else:
			return self._inputParameters[45]

	def Save_GSI_SI(self, index, value):
		if self._parCnIn[45] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[45], index, float(value))
		else:
			self._IPProxy.SetNumericParam(46, float(value))
			self._inputParameters[45] = float(value)

	def get_GSI_SI_Name(self):
		if self._parCnIn[45] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[45], 1)
		else:
			return str(self._inputParameters[45])

	GSI_SI_Name = property(fget=get_GSI_SI_Name)

	def PHI_CO(self, index):
		if self._parCnIn[46] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[46], index)
		else:
			return self._inputParameters[46]

	def Save_PHI_CO(self, index, value):
		if self._parCnIn[46] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[46], index, float(value))
		else:
			self._IPProxy.SetNumericParam(47, float(value))
			self._inputParameters[46] = float(value)

	def get_PHI_CO_Name(self):
		if self._parCnIn[46] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[46], 1)
		else:
			return str(self._inputParameters[46])

	PHI_CO_Name = property(fget=get_PHI_CO_Name)

	def PERM_CO(self, index):
		if self._parCnIn[47] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[47], index)
		else:
			return self._inputParameters[47]

	def Save_PERM_CO(self, index, value):
		if self._parCnIn[47] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[47], index, float(value))
		else:
			self._IPProxy.SetNumericParam(48, float(value))
			self._inputParameters[47] = float(value)

	def get_PERM_CO_Name(self):
		if self._parCnIn[47] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[47], 1)
		else:
			return str(self._inputParameters[47])

	PERM_CO_Name = property(fget=get_PERM_CO_Name)

	def PHISH_COEF(self, index):
		if self._parCnIn[48] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[48], index)
		else:
			return self._inputParameters[48]

	def Save_PHISH_COEF(self, index, value):
		if self._parCnIn[48] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[48], index, float(value))
		else:
			self._IPProxy.SetNumericParam(49, float(value))
			self._inputParameters[48] = float(value)

	def get_PHISH_COEF_Name(self):
		if self._parCnIn[48] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[48], 1)
		else:
			return str(self._inputParameters[48])

	PHISH_COEF_Name = property(fget=get_PHISH_COEF_Name)

	def PHISH_INT(self, index):
		if self._parCnIn[49] > 0:
			return self._IPProxy.GetCurveData(self._parCnIn[49], index)
		else:
			return self._inputParameters[49]

	def Save_PHISH_INT(self, index, value):
		if self._parCnIn[49] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[49], index, float(value))
		else:
			self._IPProxy.SetNumericParam(50, float(value))
			self._inputParameters[49] = float(value)

	def get_PHISH_INT_Name(self):
		if self._parCnIn[49] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[49], 1)
		else:
			return str(self._inputParameters[49])

	PHISH_INT_Name = property(fget=get_PHISH_INT_Name)

	def get_FLAG_FLUIDS(self):
		return self._textInputParameters[0]

	FLAG_FLUIDS = property(fget=get_FLAG_FLUIDS)

	def get_OPT_FLUID_SYSTEM(self):
		return self._textInputParameters[1]

	OPT_FLUID_SYSTEM = property(fget=get_OPT_FLUID_SYSTEM)

	def get_CORE_REG_USE(self):
		return self._textInputParameters[2]

	CORE_REG_USE = property(fget=get_CORE_REG_USE)

	def get_CAP_PRESSURE(self):
		return self._textInputParameters[3]

	CAP_PRESSURE = property(fget=get_CAP_PRESSURE)

