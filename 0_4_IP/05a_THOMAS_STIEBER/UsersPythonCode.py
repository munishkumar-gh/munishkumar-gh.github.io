"""
Coded by: Munish Kumar (24/08/2020)
Thomas-Stieber (TS) earth model

Stage 1 & 2 - TS using conventional D-N to interpret PHIT and VSH followed by Archie

Stage 3 - Facies Mapping

Stage 4 - Bulk Volumes

"""

from Methods import Methods
from IpClassicPythonLink import IPLink
import math
import cmath

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
				VSH = self.VSH(index)
				PHIT = self.PHIT(index)
				SWT = self.SWT(index)

				# Must consider compaction
				# PHIT_SH_REF = m*burial + c
				PHIT_SH_REF = self.PHIT_SH_REF(index)
				PHIT_SST_REF = self.PHIT_SST_REF(index)
				VSH_SH_REF = self.VSH_SH_REF(index)
				VSH_SST_REF = self.PHIT_SST_REF(index)

				SALINITY = self.SALINITY(index)
				RESDEEP = self.RESDEEP(index)

				FT = self.FT(index)
				M = self.M(index) 
				N = self.N(index)
				A = self.A(index)

				SHALE_CUTOFF = self.SHALE_CUTOFF(index)
				SHALY_LAM = self.SHALY_LAM(index)
				SANDY_LAM = self.SANDY_LAM(index)

				#--------------------------------------------
				# Thomas-Stieber
				#--------------------------------------------
				slope = (PHIT_SH_REF - PHIT_SST_REF)/(VSH_SH_REF - VSH_SST_REF)

				PHIT_SH = (PHIT - VSH*slope)/(1 - VSH_SH_REF/PHIT_SH_REF*slope)
				VSH_SH = PHIT_SH * VSH_SH_REF/PHIT_SH_REF

				PHIT_SST = VSH_SST_REF*slope + PHIT - VSH*slope
				VSH_SST = VSH_SST_REF

				VSST=1-(VSH-VSH_SST_REF)/(VSH_SH-VSH_SST_REF)

				if (VSST > 1):
					VSST = 1
					PHIT_SST = PHIT
					VSH_SST = VSH

				if (VSST <= 0):
					VSST = 0
					PHIT_SST = PHIT_SST_REF
					VSH_SH = VSH
					PHIT_SH = PHIT
					SWT_SST = 1
				else:
					SWT_SST = 1 - (PHIT*(1 - SWT))/(PHIT_SST*VSST)

				if (SWT_SST < 0):
					SWT_SST = 0

				#--------------------------------------------
				# Saturation 
				#--------------------------------------------
				# Use Archie to determine water saturation
				RES = RESDEEP

				# Conversion of Temperature units
				if (self.OPT_TEMP_UNITS == 'CELSIUS'):
					FTF = (FT*9/5)+32
				else:
					FTF = FT

				if (VSH <= VSH_SST_REF):
					PHIT_SST_MOD = PHIT
				elif (VSH >= VSH_SH_REF):
					PHIT_SST_MOD = PHIT
				else:
					PHIT_SST_MOD = PHIT_SST

				RW =((300000/(SALINITY**0.9524))+1)*(1/(FTF+7))
				
				# There is an error where FORM_FACT gives a negative number
				# for all values of M not 2 i.e. any decimal number. 
				# Need to use complex numbers to correct for this
				# In complex numbers a**b = exp**(b*ln*a)
				
				# FORM_FACT = float(A)/(PHIT_SST_MOD**float(M))
				FORM_FACT = A*cmath.exp(-M*cmath.log(PHIT_SST_MOD)).real
				
				if (RES > 0):
					RO = min(RES,FORM_FACT*RW)
					# Alternative solution
					#RO = min(RES,FORM_FACT.real*RW)
					
					# Original
					#SW = (RO/RES)**(1/float(N))
					SW = cmath.exp(1/float(N)*cmath.log(RO/RES)).real

					SWTU = SW
					SWT_ARCH = min(1, max(0.03,SWTU))
				else:
					SWT_ARCH = SWT

				#--------------------------------------------
				# Facies
				# 0 - Shale, 1 - Shaly Laminations
				# 2 - Sandy Laminations, 3 - Blocky Sand
				#--------------------------------------------
				if (VSST < SHALE_CUTOFF):
					FACIES_TBA = 0
					#FACIES_TBA_COLOUR = COLOR00
				elif (VSST >= SHALE_CUTOFF and VSST < SHALY_LAM):
					FACIES_TBA = 1
					#FACIES_TBA_COLOUR = COLOR01
				elif (VSST >= SHALY_LAM and VSST < SANDY_LAM):
					FACIES_TBA = 2
					#FACIES_TBA_COLOUR = COLOR02
				else:
					FACIES_TBA = 3
					#FACIES_TBA_COLOUR = COLOR03

				#--------------------------------------------
				# Bulk Volumes
				#--------------------------------------------	
				PHIT_SH_BULK = PHIT_SH*(1-VSST)
				PHIT_SST_BULK = PHIT_SST_MOD*VSST

				# Compare to Deterministic SWT
				SWT_BULK = (PHIT - PHIT_SST_BULK*(1-SWT_ARCH))/PHIT

				# Compare directly to bulk volumes from
				# detemerministic processes
				VOLHC_SST_BULK = PHIT_SST_MOD*VSST*(1-SWT_BULK)
				VOLWAT_SST_BULK = PHIT_SST_MOD*VSST*SWT_BULK

				self.Save_VSH_SH(index, VSH_SH)
				self.Save_PHIT_SH(index, PHIT_SH)
				self.Save_VSH_SST(index, VSH_SST)
				self.Save_PHIT_SST(index, PHIT_SST)
				self.Save_VSST(index, VSST)
				self.Save_SWT_SST(index, SWT_SST)

				self.Save_PHIT_SST_MOD(index, PHIT_SST_MOD)
				self.Save_SWT_ARCH(index, SWT_ARCH)
				self.Save_FACIES_TBA(index, FACIES_TBA)

				self.Save_PHIT_SH_BULK(index, PHIT_SH_BULK)
				self.Save_PHIT_SST_BULK(index, PHIT_SST_BULK)
				self.Save_SWT_BULK(index, SWT_BULK)
				self.Save_VOLHC_SST_BULK(index, VOLHC_SST_BULK)
				self.Save_VOLWAT_SST_BULK(index, VOLWAT_SST_BULK)

				index += 1
			except Exception:
				pass