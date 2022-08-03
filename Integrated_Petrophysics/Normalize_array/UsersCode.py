from System import *
from System.Collections.Generic import *

class IPLink:

	def UserCode(self):
		# Enter user code here
		# Find max and min values in array data
		valMax = -0.0000001
		valMin = 9999999999999.9
		index = self.TopDepth
		while index <= self.BottomDepth:
			ix = 1
			while ix <= self.Array_InCrv_MaxX:
				iy = 1
				while iy <= self.Array_InCrv_MaxY:
					R = self.Array_InCrv(index, ix, iy)
					if (R < valMin) and (R != -999.0):
						valMin = R
					if (R > valMax) and (R != -999.0):
						valMax = R
					iy += 1
				ix += 1
			index += 1
		# Calculate the gain and shift to normalize
		gain = 1.0 / (valMax - valMin)
		shift = -gain * valMin
		# Output new array with normalized values
		index = self.TopDepth
		while index <= self.BottomDepth:
			ix = 1
			while ix <= self.Array_InCrv_MaxX:
				iy = 1
				while iy <= self.Array_InCrv_MaxY:
					R = self.Array_InCrv(index, ix, iy) * gain + shift
					self.Save_Array_OutCrv(index, ix, iy, R)
					iy += 1
				ix += 1
			index += 1
		self.Save_OutCrv_Comments("Updated by Normalize Array User Prog")