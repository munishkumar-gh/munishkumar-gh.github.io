"""
Coded by: Munish Kumar (06/10/2020)

Calculation of quick NMR properties

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
				CBP1 = self.CBP1(index)
				CBP2 = self.CBP2(index)
				CBP3 = self.CBP3(index)
				CBP4 = self.CBP4(index)
				CBP5 = self.CBP5(index)
				CBP6 = self.CBP6(index)
				CBP7 = self.CBP7(index)
				CBP8 = self.CBP8(index)

				PHI_DEN = self.PHI_DEN(index)
				BFI_SHALE = self.BFI_SHALE(index)
				PHIT_C = self.PHIT_C(index)
				SWIRR_C = self.SWIRR_C(index)
				PHIT_CL = self.PHIT_CL(index)
				BFVMIN = self.BFVMIN(index)
				BFVMAX = self.BFVMAX(index)

				CK = self.CK(index)
				KK = self.KK(index)

				#Irreducible Sw = Clay bound Water 
				# up to 3 ms
				BFI = CBP1 + CBP2

				#Capillary Bound Water 
				# Up to 33 ms
				BFVC = CBP3 + CBP4
				# Up to 10 ms
				# BFVC = CBP3

				#Free Fluid Volume 
				# From 33 ms to 3000 ms
				CMFF = CBP5 + CBP6 + CBP7 + CBP8
				# From 10 ms to 3000 ms 
				# CMFF = CBP4 + CBP5 + CBP6 + CBP7 + CBP8

				#Bound Fluid Volume
				BFV = BFI + BFVC

				#Total CMR Porosity 
				TCMR = CBP1 + CBP2 + CBP3 + CBP4 + CBP5 + CBP6 + CBP7 + CBP8

				#Density Magnetic Resonance Porosity 
				DMRP = 0.4 * TCMR + 0.6 * PHI_DEN

				#Effective CMR Porosity 
				ECMR = CMFF + BFVC

				#Water Saturation 
				SW_NMR = BFV / TCMR

				#Bound Volume Hydrocarbons 
				BVHC = TCMR * (1 - SW_NMR)

				#Volume of Clay; for denominator, BFI  is from 100% shale 
				VCL = (BFI) / (BFI_SHALE) 

				#Gross Interval Evaluation  
				#Multiplier ck was added to convert VSH to VCL 
				#Note also that PHIT and SWIRR must be from core/sand properties, and not from logs
				VCL_GIE = (1 - CMFF / (PHIT_C * (1 - SWIRR_C))) * CK

				#Volume of Clay from Irreducible Sw 
				#multiplier k was added to account for broadness of the NMR peak. 
				#In most cases, this multiplier is 1. 
				VCL_BFI = BFI / (TCMR) * KK

				#Volume of Clay using CBW and Clay Porosity 
				VCL_NMR_PL = BFI / PHIT_CL

				#Volume of Shale 
				VSH = BFV / CMFF

				#Volume of Shale (Ratio Method - For Thin Sands Analysis) 
				VSH_CMR = (BFV - BFVMIN) / (BFVMAX - BFVMIN)

				self.Save_BFI(index, BFI)
				self.Save_BFVC(index, BFVC)
				self.Save_CMFF(index, CMFF)
				self.Save_BFV(index, BFV)
				self.Save_TCMR(index, TCMR)
				self.Save_DMRP(index, DMRP)
				self.Save_ECMR(index, ECMR)
				self.Save_SW_NMR(index, SW_NMR)
				self.Save_BVHC(index, BVHC)
				self.Save_VCL(index, VCL)
				self.Save_VCL_GIE(index, VCL_GIE)
				self.Save_VCL_BFI(index, VCL_BFI)
				self.Save_VCL_NMR_PL(index, VCL_NMR_PL)
				self.Save_VSH(index, VSH)
				self.Save_VSH_CMR(index, VSH_CMR)
				index += 1
			except Exception:
				index += 1
				continue