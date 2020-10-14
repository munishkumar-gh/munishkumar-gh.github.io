"""
Coded by Munish Kumar (17/09/2020)

Calculates (a) average (b) geometric (c) harmonic mean of log curves
Used for Curve smoothing

Original COde written by Andy McDonald - 29/10/2019 (IP) 
"""

from System import *
from System.Collections.Generic import *

class IPLink:

	def UserCode(self):
		#
		# Loop through the data one level at a time
		# TopDepth and BottomDepth are the index equivalent depths entered on the run window. 
		# 		
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

			# Default values reset at each depth level
			depthAboveCount = depthAbove
			depthBelowCount = depthBelow
			sumAbove = prodAbove = harmAbove = sumBelow = prodBelow = harmBelow = valsAbove = valsBelow = 0

			# Checks if the depthAboveCount is between 0 and the user defined depth. If it is sum the value.
			while depthAboveCount <= depthAbove and depthAboveCount > 0: 
				if self.input(index - depthAboveCount) != -999: 
					sumAbove += self.input(index - depthAboveCount)
					prodAbove *= self.input(index - depthAboveCount)
					harmAbove += 1/self.input(index - depthAboveCount)
					valsAbove += 1
				depthAboveCount -= 1
			
			# Sum up the values below
			while depthBelowCount <= depthBelow and depthBelowCount > 0:
				if self.input(index + depthBelowCount) != -999:
					sumBelow += self.input(index + depthBelowCount)
					prodBelow *= self.input(index + depthBelowCount)
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
					finalAverage = (prodAbove*prodBelow*self.input(index))**(1/(valsAbove + valsBelow + 1))
				else:
					finalAverage = (prodAbove*prodBelow*self.input(index))**(1/(valsAbove + valsBelow))
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
			#self.Save_valsAbove(index, valsAbove)			

			index += 1