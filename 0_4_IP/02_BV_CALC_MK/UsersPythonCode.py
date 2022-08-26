"""
Coded by Munish Kumar (24/8/2020)

Bulk volume Calculator

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
				RESD = self.RESD(index)
				RW = self.RW(index)
				VSH = self.VSH(index)
				VSHCO = self.VSHCO(index)
				PHIT = self.PHIT(index)
				PHITCO = self.PHITCO(index)
				SWT = self.SWT(index)
				SWTCO = self.SWTCO(index)

				m = self.m(index)
				CLAY_FRAC = self.CLAY_FRAC(index)
				SAND_FRAC = self.SAND_FRAC(index)

				OPT_CLAY_SILT = self.OPT_CLAY_SILT
				FLAG_LITH = self.FLAG_LITH

				if (PHIT == None):
					PHIT_R = 10**((math.log10(RESD)-math.log10(RW))/-m)
					PHIT = PHIT_R
					SWT = 1

				BVW = PHIT*SWT
				BVHC = PHIT-BVW
				BVSH = (1-PHIT)*VSH
				BVSAND = (1-PHIT)*(1-VSH)
				
				SUM_TOT, BVSILT, BVLIM, BVCLAY, BVSAND, BVSALT, BVASH = self.SSC(PHIT, OPT_CLAY_SILT, VSH, CLAY_FRAC, SAND_FRAC, FLAG_LITH, BVSAND)
				SD, RESV, PAY = self.FLAG_PAY(VSH, VSHCO, PHIT, PHITCO, SWT, SWTCO)

				# output the curve results
				self.Save_BVW(index, BVW)
				self.Save_BVHC(index, BVHC)
				self.Save_BVSH(index, BVSH)
				self.Save_BVSAND(index, BVSAND)
				
				self.Save_BVSILT(index, BVSILT)
				self.Save_BVLIM(index, BVLIM)
				self.Save_BVCLAY(index, BVCLAY)
				self.Save_BVSALT(index, BVSALT)
				self.Save_BVASH(index, BVASH)
				self.Save_SUM_TOT(index, SUM_TOT)

				self.Save_SD(index, SD)
				self.Save_RESV(index, RESV)
				self.Save_PAY(index, PAY)
				index += 1
			except Exception:
				index += 1
				continue

	#*****************************************************************
	# Min-Max Clamp
	#*****************************************************************
	def clamp(self, n, minn, maxn):
		return max(min(maxn, n), minn)

	#*****************************************************************
	# Interpreting sand (carbonate) -silt-clay from VSH 
	#*****************************************************************
	def SSC(self, PHIT, OPT_CLAY_SILT, VSH, CLAY_FRAC, SAND_FRAC, FLAG_LITH, BVSAND):
		if (OPT_CLAY_SILT == 'NO'):
			CLAY_FRAC = SAND_FRAC = 1

		MVCL = VSH*CLAY_FRAC

		if (VSH < (CLAY_FRAC + 0.1)):
			MVSD = 1 - VSH
		else:
			MVSD = 0

		BVCLAY = (1-PHIT)*MVCL
		# To fractionate the portion of sand-silt from remaining non-clay portion. 
		# A low sand fraction portions more of the non-clay matrix to silt*/
		if (VSH < 0.1):
			BVSC = self.clamp((1-PHIT)*MVSD, 0, 1)
		else:
			BVSC = self.clamp((1-PHIT)*(SAND_FRAC)*MVSD, 0, 1)

		if (FLAG_LITH == 'SAND'):
			BVSAND = BVSC
			BVLIM = 0
			BVSALT = BVASH = 0
			BVSILT = 1 - (PHIT + BVSAND + BVLIM + BVCLAY)
		elif (FLAG_LITH == 'CARBONATE'):
			BVLIM = BVSC
			BVSAND = 0
			BVSALT = BVASH = 0
			BVSILT = 1 - (PHIT + BVSAND + BVLIM + BVCLAY)
		elif (FLAG_LITH == 'SALT'):
			BVSILT = BVSAND = BVLIM = BVCLAY = PHIT = BVASH = 0
			BVSALT = 1
		elif (FLAG_LITH == 'ASH'):
			BVSILT = BVSAND = BVLIM = BVCLAY = PHIT = BVSALT = 0
			BVASH = 1

		# Checking Condition; sum total must be 1 */
		S = BVSILT + PHIT + BVSAND + BVLIM + BVCLAY + BVSALT + BVASH

		return S, BVSILT, BVLIM, BVCLAY, BVSAND, BVSALT, BVASH

	#***************************************************************************
	# Generating Pay Flags
	#***************************************************************************
	def FLAG_PAY(self, VSH, VSHCO, PHIT, PHITCO, SWT, SWTCO):
		# Net Sand
		if (VSH < VSHCO):
			# Net Reservoir
			if (PHIT > PHITCO):
				# Net Pay
				if (SWT < SWTCO):
					SD = RESV = PAY = 1
				else:
					SD = RESV = 1
					PAY = 0
			else:
				SD = 1
				RESV = PAY = 0
		else:
			SD = RESV = PAY = 0
		return SD, RESV, PAY