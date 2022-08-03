from System import *
from System.Collections.Generic import *

class IPLink:

	def UserCode(self):
		index = self.TopDepth + 1
		while index <= self.BottomDepth:
			# Enter user code here
			# Check for curve equal to zero
			if self.numCrv(index) - self.numCrv(index - 1) == 0.0:
				self.Save_DiffCrv(index, -999)
			elif self.denCrv(index) - self.denCrv(index - 1) == 0.0:
				self.Save_DiffCrv(index, -999)
			else:
				# Calculate the first derivative
				self.Save_DiffCrv(index, (self.numCrv(index) - self.numCrv(index - 1)) / (self.denCrv(index) - self.denCrv(index - 1)))
			index += 1
		self.Save_DiffCrv_Comments("Curve Written by User Program")