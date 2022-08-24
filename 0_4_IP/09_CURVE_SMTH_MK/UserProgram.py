"""
Coded by Munish Kumar (17/09/2020)

Calculates (a) average (b) geometric (c) harmonic mean of log curves
Used for Curve smoothing

Original Code written by Andy McDonald - 29/10/2019 (IP) 
"""

from System import *
from System.Collections.Generic import *
import math

# Debugging Code
#import ptvsd

class IPLink:

	def UserCode(self):
		#
		# Loop through the data one level at a time
		# TopDepth and BottomDepth are the index equivalent depths entered on the run window. 
		#
		# Uncomment the next two lines to enable debgugging
		#ptvsd.enable_attach(address=('127.0.0.1', 5678))
		#ptvsd.wait_for_attach()  		
		
		index = self.TopDepth
		# Enter user code here
			# Compute depth step by subtracting the depth from the next depth
			wellStep = self.Depth(index +1) - self.Depth(index)

			# Convert the user entered depths into depth levels
			depthAbove = self.depthAbove(index) / wellStep
			depthBelow = self.depthBelow(index) / wellStep
			
			valsAbove = 0
			valsBelow = 0

			while index <= self.BottomDepth:
				try:
					# Default values reset at each depth level
					depthAboveCount = depthAbove
					depthBelowCount = depthBelow
					sumAbove = prodAbove = harmAbove = sumBelow = prodBelow = harmBelow = valsAbove = valsBelow = 0

					# Checks if the depthAboveCount is between 0 and the user defined depth. If it is sum the value.
					while depthAboveCount <= depthAbove and depthAboveCount > 0: 
						if self.input(index - depthAboveCount) != -999: 
							sumAbove += self.input(index - depthAboveCount)
							prodAbove += math.log(self.input(index - depthAboveCount))
							harmAbove += 1/self.input(index - depthAboveCount)
							valsAbove += 1
						depthAboveCount -= 1
					
					# Sum up the values below
					while depthBelowCount <= depthBelow and depthBelowCount > 0:
						if self.input(index + depthBelowCount) != -999:
							sumBelow += self.input(index + depthBelowCount)
							prodBelow += math.log(self.input(index + depthBelowCount))
							harmBelow += 1/self.input(index - depthAboveCount)
							valsBelow += 1
						depthBelowCount -= 1

					# Compute the average by summing values above, below and at current depth level
					# As current depth level is not accounted for in the while loops above, 1 needs to be added
					# to the denominator
					# If the current depth level is a null, only use the data above and below
					if (self.OPT_MEAN_MTD == "ARITHMETIC"):
						if self.input(index) != -999:
							finalAverage = (sumAbove + sumBelow + self.input(index)) / (valsAbove + valsBelow + 1)
						else:
							finalAverage = (sumAbove + sumBelow) / (valsAbove + valsBelow)
					elif (self.OPT_MEAN_MTD == "GEOMETRIC"):
						if self.input(index) != -999:
							finalAverage = math.exp((prodAbove + prodBelow + math.log(self.input(index)))/(valsAbove + valsBelow + 1))
						else:
							finalAverage = math.exp((prodAbove + prodBelow )/(valsAbove + valsBelow))
					elif (self.OPT_MEAN_MTD == "HARMONIC"):
						if self.input(index) != -999:
							finalAverage = ((harmAbove + harmBelow + 1/self.input(index)) / (valsAbove + valsBelow + 1))**(-1)
						else:
							finalAverage = ((harmAbove + harmBelow) / (valsAbove + valsBelow))**(-1)
					else:
						finalAverage = self.input	

					# This section computes the difference between the values below and above to the depth levels below and above
					# There is the added option to check for nulls within the values above or values below
					# If a null is detected the current depth level is set to null
					
					x = self.input(index + depthBelow) - self.input(index - depthAbove)
					
					if self.input(index - depthAbove) != -999 and self.input(index + depthBelow) != -999:
						self.Save_DiffBelowAbove(index, x)
					else:
						self.Save_DiffBelowAbove(index, -999)		

					if self.nullCheck is True:
						if valsAbove != depthAbove or valsBelow != depthBelow:
							self.Save_SumDiffBelowAbove(index, -999) #Save back a null value
						else:
							# Calculated Difference between the summation of data below and above current depth level
							self.Save_SumDiffBelowAbove(index, sumBelow-sumAbove)
					else:
						self.Save_SumDiffBelowAbove(index, sumBelow-sumAbove)

					# Save the Average curves back to IP			
					if (index - depthAbove) < self.TopDepth:
						# At the start of the well, null the output when index-depthAbove is above the start of the well
						self.Save_OutCurve(index, -999)
					
					elif (index + depthBelow) > self.BottomDepth:
						# At the end of the well, null the output when index+depthBelow is below the end of the well
						self.Save_OutCurve(index, -999)
					else:
						# Else save the result back to IP
						self.Save_OutCurve(index, finalAverage)

					#Additional output curves used for QC
					self.Save_SumAbove(index, sumAbove)
					self.Save_SumBelow(index, sumBelow)			
					self.Save_ProdAbove(index, prodAbove)			
					self.Save_ProdBelow(index, prodBelow)
					self.Save_HarmAbove(index, harmAbove)			
					self.Save_HarmBelow(index, harmBelow)

					index += 1
				except Exception:
					index += 1
					continue

	def __init__(self):
		self._FIRST_AVAILABLE_LOG_RUN = -1
		self._LAST_AVAILABLE_LOG_RUN = -2

	def Depth(self, index):
		return self._IPProxy.GetCurveData(1, index)

	def input(self, index):
		return self._IPProxy.GetCurveData(self._inputCurves[0],0, index)

	def Array_input(self, index, xVal, yVal):
		return self._IPProxy.GetCurveData(self._inputCurves[0],0, index, xVal, yVal)

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
		self._IPProxy.SetCurveText(self._inputCurves[0], 3, newValue)

	def Get_input_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._inputCurves[0], attributeName)

	def Set_input_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._inputCurves[0], attributeName, newValue)

	def Save_input(self, index, value):
		self._IPProxy.SetCurveData(self._inputCurves[0], index, value)

	def Save_Array_input(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._inputCurves[0], index, value, xVal, yVal)

	def Save_input_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[0], index, value)

	def Save_Array_input_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._inputCurves[0], index, value, xVal, yVal)

	def get_Array_input_MaxX(self):
		return self._inArrayX[0]

	Array_input_MaxX = property(fget=get_Array_input_MaxX)

	def get_Array_input_MaxY(self):
		return self._inArrayY[0]

	Array_input_MaxY = property(fget=get_Array_input_MaxY)

	def Save_OutCurve(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, value)

	def Save_Array_OutCurve(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[0], index, value, xVal, yVal)

	def Save_OutCurve_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, value)

	def Save_Array_OutCurve_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[0], index, value, xVal, yVal)

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
		self._IPProxy.SetCurveText(self._outputCurves[0], 3, newValue)

	def get_Array_OutCurve_MaxX(self):
		return self._outArrayX[0]

	Array_OutCurve_MaxX = property(fget=get_Array_OutCurve_MaxX)

	def get_Array_OutCurve_MaxY(self):
		return self._outArrayY[0]

	Array_OutCurve_MaxY = property(fget=get_Array_OutCurve_MaxY)

	def Get_OutCurve_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[0], attributeName)

	def Set_OutCurve_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[0], attributeName, newValue)

	def Save_SumAbove(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, value)

	def Save_Array_SumAbove(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[1], index, value, xVal, yVal)

	def Save_SumAbove_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, value)

	def Save_Array_SumAbove_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[1], index, value, xVal, yVal)

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
		self._IPProxy.SetCurveText(self._outputCurves[1], 3, newValue)

	def get_Array_SumAbove_MaxX(self):
		return self._outArrayX[1]

	Array_SumAbove_MaxX = property(fget=get_Array_SumAbove_MaxX)

	def get_Array_SumAbove_MaxY(self):
		return self._outArrayY[1]

	Array_SumAbove_MaxY = property(fget=get_Array_SumAbove_MaxY)

	def Get_SumAbove_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[1], attributeName)

	def Set_SumAbove_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[1], attributeName, newValue)

	def Save_SumBelow(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, value)

	def Save_Array_SumBelow(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[2], index, value, xVal, yVal)

	def Save_SumBelow_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, value)

	def Save_Array_SumBelow_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[2], index, value, xVal, yVal)

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
		self._IPProxy.SetCurveText(self._outputCurves[2], 3, newValue)

	def get_Array_SumBelow_MaxX(self):
		return self._outArrayX[2]

	Array_SumBelow_MaxX = property(fget=get_Array_SumBelow_MaxX)

	def get_Array_SumBelow_MaxY(self):
		return self._outArrayY[2]

	Array_SumBelow_MaxY = property(fget=get_Array_SumBelow_MaxY)

	def Get_SumBelow_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[2], attributeName)

	def Set_SumBelow_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[2], attributeName, newValue)

	def Save_SumDiffBelowAbove(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, value)

	def Save_Array_SumDiffBelowAbove(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[3], index, value, xVal, yVal)

	def Save_SumDiffBelowAbove_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, value)

	def Save_Array_SumDiffBelowAbove_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[3], index, value, xVal, yVal)

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
		self._IPProxy.SetCurveText(self._outputCurves[3], 3, newValue)

	def get_Array_SumDiffBelowAbove_MaxX(self):
		return self._outArrayX[3]

	Array_SumDiffBelowAbove_MaxX = property(fget=get_Array_SumDiffBelowAbove_MaxX)

	def get_Array_SumDiffBelowAbove_MaxY(self):
		return self._outArrayY[3]

	Array_SumDiffBelowAbove_MaxY = property(fget=get_Array_SumDiffBelowAbove_MaxY)

	def Get_SumDiffBelowAbove_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[3], attributeName)

	def Set_SumDiffBelowAbove_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[3], attributeName, newValue)

	def Save_DiffBelowAbove(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, value)

	def Save_Array_DiffBelowAbove(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[4], index, value, xVal, yVal)

	def Save_DiffBelowAbove_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, value)

	def Save_Array_DiffBelowAbove_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[4], index, value, xVal, yVal)

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
		self._IPProxy.SetCurveText(self._outputCurves[4], 3, newValue)

	def get_Array_DiffBelowAbove_MaxX(self):
		return self._outArrayX[4]

	Array_DiffBelowAbove_MaxX = property(fget=get_Array_DiffBelowAbove_MaxX)

	def get_Array_DiffBelowAbove_MaxY(self):
		return self._outArrayY[4]

	Array_DiffBelowAbove_MaxY = property(fget=get_Array_DiffBelowAbove_MaxY)

	def Get_DiffBelowAbove_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[4], attributeName)

	def Set_DiffBelowAbove_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[4], attributeName, newValue)

	def Save_ProdAbove(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[5], index, value)

	def Save_Array_ProdAbove(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[5], index, value, xVal, yVal)

	def Save_ProdAbove_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[5], index, value)

	def Save_Array_ProdAbove_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[5], index, value, xVal, yVal)

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
		self._IPProxy.SetCurveText(self._outputCurves[5], 3, newValue)

	def get_Array_ProdAbove_MaxX(self):
		return self._outArrayX[5]

	Array_ProdAbove_MaxX = property(fget=get_Array_ProdAbove_MaxX)

	def get_Array_ProdAbove_MaxY(self):
		return self._outArrayY[5]

	Array_ProdAbove_MaxY = property(fget=get_Array_ProdAbove_MaxY)

	def Get_ProdAbove_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[5], attributeName)

	def Set_ProdAbove_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[5], attributeName, newValue)

	def Save_ProdBelow(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[6], index, value)

	def Save_Array_ProdBelow(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[6], index, value, xVal, yVal)

	def Save_ProdBelow_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[6], index, value)

	def Save_Array_ProdBelow_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[6], index, value, xVal, yVal)

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
		self._IPProxy.SetCurveText(self._outputCurves[6], 3, newValue)

	def get_Array_ProdBelow_MaxX(self):
		return self._outArrayX[6]

	Array_ProdBelow_MaxX = property(fget=get_Array_ProdBelow_MaxX)

	def get_Array_ProdBelow_MaxY(self):
		return self._outArrayY[6]

	Array_ProdBelow_MaxY = property(fget=get_Array_ProdBelow_MaxY)

	def Get_ProdBelow_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[6], attributeName)

	def Set_ProdBelow_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[6], attributeName, newValue)

	def Save_HarmAbove(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[7], index, value)

	def Save_Array_HarmAbove(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[7], index, value, xVal, yVal)

	def Save_HarmAbove_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[7], index, value)

	def Save_Array_HarmAbove_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[7], index, value, xVal, yVal)

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
		self._IPProxy.SetCurveText(self._outputCurves[7], 3, newValue)

	def get_Array_HarmAbove_MaxX(self):
		return self._outArrayX[7]

	Array_HarmAbove_MaxX = property(fget=get_Array_HarmAbove_MaxX)

	def get_Array_HarmAbove_MaxY(self):
		return self._outArrayY[7]

	Array_HarmAbove_MaxY = property(fget=get_Array_HarmAbove_MaxY)

	def Get_HarmAbove_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[7], attributeName)

	def Set_HarmAbove_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[7], attributeName, newValue)

	def Save_HarmBelow(self, index, value):
		self._IPProxy.SetCurveData(self._outputCurves[8], index, value)

	def Save_Array_HarmBelow(self, index, xVal, yVal, value):
		self._IPProxy.SetCurveData(self._outputCurves[8], index, value, xVal, yVal)

	def Save_HarmBelow_Text(self, index, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[8], index, value)

	def Save_Array_HarmBelow_Text(self, index, xVal, yVal, value):
		self._IPProxy.SetTextCurveValue(self._outputCurves[8], index, value, xVal, yVal)

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
		self._IPProxy.SetCurveText(self._outputCurves[8], 3, newValue)

	def get_Array_HarmBelow_MaxX(self):
		return self._outArrayX[8]

	Array_HarmBelow_MaxX = property(fget=get_Array_HarmBelow_MaxX)

	def get_Array_HarmBelow_MaxY(self):
		return self._outArrayY[8]

	Array_HarmBelow_MaxY = property(fget=get_Array_HarmBelow_MaxY)

	def Get_HarmBelow_Attribute(self, attributeName):
		return self._IPProxy.GetText(2, self._outputCurves[8], attributeName)

	def Set_HarmBelow_Attribute(self, attributeName, newValue):
		self._IPProxy.SetText(2, self._outputCurves[8], attributeName, newValue)

	def depthAbove(self, index):
		if ((self._parCnIn[0] > 0) or (self._parCnIn[0] < -100)):
			return self._IPProxy.GetCurveData(self._parCnIn[0], index)
		else:
			return self._inputParameters[0]

	def Save_depthAbove(self, index, value):
		if self._parCnIn[0] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[0], index, Convert.ToSingle(value))
		else:
			self._IPProxy.SetNumericParam(1, Convert.ToSingle(value))
			self._inputParameters[0] = Convert.ToSingle(value)

	def get_depthAbove_Name(self):
		if self._parCnIn[0] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[0], 1)
		else:
			return Convert.ToString(self._inputParameters[0])

	depthAbove_Name = property(fget=get_depthAbove_Name)

	def depthBelow(self, index):
		if ((self._parCnIn[1] > 0) or (self._parCnIn[1] < -100)):
			return self._IPProxy.GetCurveData(self._parCnIn[1], index)
		else:
			return self._inputParameters[1]

	def Save_depthBelow(self, index, value):
		if self._parCnIn[1] > 0:
			self._IPProxy.SetCurveData(self._parCnIn[1], index, Convert.ToSingle(value))
		else:
			self._IPProxy.SetNumericParam(2, Convert.ToSingle(value))
			self._inputParameters[1] = Convert.ToSingle(value)

	def get_depthBelow_Name(self):
		if self._parCnIn[1] > 0:
			return self._IPProxy.GetCurveText(self._parCnIn[1], 1)
		else:
			return Convert.ToString(self._inputParameters[1])

	depthBelow_Name = property(fget=get_depthBelow_Name)

	def get_OPT_MEAN_MTD(self):
		return self._textInputParameters[0]

	OPT_MEAN_MTD = property(fget=get_OPT_MEAN_MTD)

	def get_nullCheck(self):
		return self._flagInputParameters[0]

	nullCheck = property(fget=get_nullCheck)

	def SetupParameters(self, CnIn, CnOut, ParIn, TxtParIn, FlagIn, StIndex, SpIndex, ZoneNum, TotZones, AXIn, AYIn, AXOut, AYOut, ParamCrvIn):
		self._inputCurves = List[int](CnIn)
		self._outputCurves = List[int](CnOut)
		self._inputParameters = List[Single](ParIn)
		self._textInputParameters = List[str](TxtParIn)
		self._flagInputParameters = List[Boolean](FlagIn)
		self._topIndex = StIndex
		self._bottomIndex = SpIndex
		self._totalZones = TotZones
		self._zoneNumber = ZoneNum
		self._inArrayX = List[int](AXIn)
		self._inArrayY = List[int](AYIn)
		self._outArrayX = List[int](AXOut)
		self._outArrayY = List[int](AYOut)
		self._parCnIn = List[int](ParamCrvIn)

	def ResetZoneParameters(self, ParIn, TxtParIn, FlagIn, ParamCrvIn, StIndex, SpIndex, ZoneNum):
		self._inputParameters = List[Single](ParIn)
		self._textInputParameters = List[str](TxtParIn)
		self._flagInputParameters = List[Boolean](FlagIn)
		self._parCnIn = List[int](ParamCrvIn)
		self._topIndex = StIndex
		self._bottomIndex = SpIndex
		self._zoneNumber = ZoneNum

	def SetupIPProxy(self, ip):
		self._IPProxy = ip

	def Run(self):
		self.UserCode()

	def get_TopDepth(self):
		return self._topIndex

	TopDepth = property(fget=get_TopDepth)

	def get_BottomDepth(self):
		return self._bottomIndex

	BottomDepth = property(fget=get_BottomDepth)

	def get_TotalZones(self):
		return self._totalZones

	TotalZones = property(fget=get_TotalZones)

	def get_ZoneNumber(self):
		return self._zoneNumber

	ZoneNumber = property(fget=get_ZoneNumber)

	def SetZone(self, zoneNum):
		self._IPProxy.SetZone(zoneNum)

	def get_Well_Name(self):
		return self.Read_Well_Attribute("WellName")

	Well_Name = property(fget=get_Well_Name)

	def get_Well_Company(self):
		return self.Read_Well_Attribute("Company")

	Well_Company = property(fget=get_Well_Company)

	def get_Well_Field(self):
		return self.Read_Well_Attribute("Field")

	Well_Field = property(fget=get_Well_Field)

	def Read_Well_Attribute(self, attributeName):
		return self._IPProxy.GetWellText(attributeName)

	def Write_Well_Attribute(self, attributeName, value):
		self._IPProxy.SetWellText(attributeName, value)

	def Read_Log_Attribute(self, attributeName, logRunNum):
		return self._IPProxy.GetLogText(attributeName, logRunNum)

	def Write_Log_Attribute(self, attributeName, value, logRunNum):
		self._IPProxy.SetLogText(attributeName, value, logRunNum)

	def Read_Curve_Attribute(self, curveNumber, attributeName):
		return self._IPProxy.GetText(2, curveNumber, attributeName)

	def Write_Curve_Attribute(self, curveNumber, attributeName, value):
		self._IPProxy.SetText(2, curveNumber, attributeName, value)

	# flags: 0 = Well, 1 = Log, 2 = Curve...
	def Read_Text(self, flags, index, attributeName):
		return self._IPProxy.GetText(flags, index, attributeName)

	def Write_Text(self, flags, index, attributeName, value):
		self._IPProxy.SetText(flags, index, attributeName, value)