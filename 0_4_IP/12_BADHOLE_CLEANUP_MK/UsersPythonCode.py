"""
@author: Munish Kumar (17/08/20)
PROGRAM: 12_BADHOLE_CLUEANUP

Clean up product logs

"""
from Methods import Methods
from IpClassicPythonLink import IPLink

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
				BADHOLE = self.BADHOLE(index)

				VSH = self.VSH(index)
				VSH_GR = self.VSH_GR(index)
				VSH_SP = self.VSH_SP(index)
				VSH_RES = self.VSH_RES(index)
				VSH_ND = self.VSH_ND(index)

				PHIX = self.PHIX(index)
				PHIA = self.PHIA(index)
				PHIT_HC = self.PHIT_HC(index)
				PHIT = self.PHIT(index)
				PHID_A = self.PHID_A(index)
				PHIE = self.PHIE(index)

				RW_SP = self.RW_SP(index)
				SALINITY_SP = self.SALINITY_SP(index)
				RW = self.RW(index)
				SALINITY = self.SALINITY(index)

				RHOGM = self.RHOGM(index)
				RHOGC = self.RHOGC(index)

				SWT = self.SWT(index)
				SWE = self.SWE(index)
				SXOT = self.SXOT(index) 
				SXOE = self.SXOE(index)

				BVW = self.BVW(index)
				BVWE = self.BVWE(index)
				BVSH = self.BVSH(index) 
				BVHC = self.BVHC(index)
				BVSAND = self.BVSAND(index)
				BVLIM = self.BVLIM(index)
				BVSILT = self.BVSILT(index)
				BVCLAY = self.BVCLAY(index)

				SD = self.SD(index)
				RESV = self.RESV(index)
				PAY = self.PAY(index)

				if (BADHOLE > 0):
					VSH = VSH_GR = VSH_SP = VSH_RES = VSH_ND = -999 
					PHIX = PHIA = PHIT_HC = PHIT = PHID_A = PHIE = -999 
					RW_SP = SALINITY_SP = RW = SALINITY = -999 
					RHOGM = RHOGC = -999 
					SWT = SWE = SXOT = SXOE =-999 
					BVW = BVWE = BVSH = BVHC = BVSAND = BVLIM = BVSILT = BVCLAY = -999 
					SD = RESV = PAY = -999

				# Output the curve results
				self.Save_VSH(index, VSH)
				self.Save_VSH_GR(index, VSH_GR)
				self.Save_VSH_SP(index, VSH_SP)
				self.Save_VSH_RES(index, VSH_RES)
				self.Save_VSH_ND(index, VSH_ND)

				self.Save_PHIX(index, PHIX)
				self.Save_PHIA(index, PHIA)
				self.Save_PHIT_HC(index, PHIT_HC)
				self.Save_PHIT(index, PHIT)
				self.Save_PHID_A(index, PHID_A)
				self.Save_PHIE(index, PHIE)

				self.Save_RW_SP(index, RW_SP)
				self.Save_SALINITY_SP(index, SALINITY_SP)
				self.Save_RW(index, RW)
				self.Save_SALINITY(index, SALINITY)

				self.Save_RHOGM(index, RHOGM)
				self.Save_RHOGC(index, RHOGC)

				self.Save_SWT(index, SWT)
				self.Save_SXOT(index, SXOT)
				self.Save_SWE(index, SWE)
				self.Save_SXOE(index, SXOE)

				self.Save_BVW(index, BVW)
				self.Save_BVWE(index, BVWE)
				self.Save_BVSH(index, BVSH)
				self.Save_BVHC(index, BVHC)
				self.Save_BVSAND(index, BVSAND)
				self.Save_BVSILT(index, BVSILT)
				self.Save_BVLIM(index, BVLIM)
				self.Save_BVCLAY(index, BVCLAY)

				self.Save_SD(index, SD)
				self.Save_RESV(index, RESV)
				self.Save_PAY(index, PAY)

				index += 1
			except Exception:
				pass