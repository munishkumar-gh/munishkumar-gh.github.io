"""
Coded by Munish Kumar (25/8/2020)

Post-processing after Deterministic Module:
- manage very low SwE in low porosity intervals of HC-bearing reservoirs where saturation is pessimistic.
- Boost SwE at low PhiE and high Vcl. 
- Applied in certain places like Indonesia if Dual Water saturation equation.
Case: Oil-based Mud

"""

from Methods import Methods
from IpClassicPythonLink import IPLink
import math

class UserApp(Methods, IPLink):

	def UserCode(self):
		#
		# Loop through the data one level at a time
		# TopDepth and BottomDepth are the index equivalent depths entered on the run window. 
		# 		
		index = self.TopDepth
		while index <= self.BottomDepth:
			# Enter user code here
			try:
				# Boost water saturation at low porosity and high shaliness
				VCL_OLD = self.VCL_OLD(index)
				VCL_EDIT = self.VCL_EDIT(index)
				PHIE_OLD = self.PHIE_OLD(index)
				PHIE_EDIT = self.PHIE_EDIT(index)			
				BVHC_OLD = self.BVHC_OLD(index)
				SWE_OLD = self.SWE_OLD(index)
				FLAG_LOW_SWE_PHIE = self.FLAG_LOW_SWE_PHIE(index)
				MOD_EXPONENT = self.MOD_EXPONENT(index)

				if (PHIE_OLD <= PHIE_EDIT):
					MOD_PHIE = (1 - 0.5 * (1 + math.cos(math.radians(180 * PHIE_OLD/PHIE_EDIT))))**MOD_EXPONENT
				else:
					MOD_PHIE = 1

				if (VCL_OLD >= VCL_EDIT):
					MOD_VCL = (0.5 * ( 1 + math.cos(math.radians(( 180 * (VCL_OLD - VCL_EDIT)/(1 - VCL_EDIT))))))**MOD_EXPONENT
				else:
					MOD_VCL = 1

				MOD = MOD_PHIE * MOD_VCL

				if MOD < 1:
					BVHC_NEW = BVHC_OLD * MOD
					BVW_NEW = PHIE_OLD - BVHC_NEW
					SWE_NEW1 = BVW_NEW / PHIE_OLD
			
				SWE_NEW = 0
				if (FLAG_LOW_SWE_PHIE == 1):
					SWE_NEW = SWE_NEW1
				else:
					SWE_NEW1 = SWE_OLD			
				
				# output the curve results
				self.Save_BVHC_NEW(index, BVHC_NEW)
				self.Save_BVW_NEW(index, BVW_NEW)
				self.Save_SWE_NEW(index, SWE_NEW)
				
				index += 1
			except Exception:
				index += 1
				continue