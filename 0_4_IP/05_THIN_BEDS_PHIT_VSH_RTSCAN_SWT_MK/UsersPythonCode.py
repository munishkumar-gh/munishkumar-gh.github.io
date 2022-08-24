"""
Coded by: Munish Kumar (24/08/2020)
“Thin bed” earth model (TBA), comprising Thomas-Stieber (TS) & 
Triaxial Resistivity Approach for determination of petrophysical 
properties of laminated shaly sand.

The algorithm will (mathematically) extract sand resistivity (Rsand), 
volume fractions (VSST) and porosity (PHISST). 

Stage 1 - TS using conventional D-N to interpret PHIT and VSH/VCL; 
next pore space is apported into “facies” . Output are logs representing 
VSST from TS and PHISST.

Stage 2 - RT Scanner used to solve for formation parameters of horizontal 
resistivity (Rh), vertical resistivity (Rv), dip magnitude and azimuth 
in an anisotropic manner. Rh and Rv are then further utilized for 
evaluation of VSST from RT and Rsand.

Compare both VSST; differences could be geologic in origin or incorrect 
assumptions within the earth models, but on average, both logs should be 
similar. Next, using a simple Archie equation (listed in Appendix 2), with 
PHISST and Rsand as inputs, SW for the sands (SWSST) is evaluated. 

The final solution has PHISST and SWSST (clean portion of the “facies” only) 
corrected with VSST to get BULK properties. 

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
		try: 		
			index = self.TopDepth
			while index <= self.BottomDepth:
				# Enter user code here
				VSH = self.VSH(index)
				PHIT = self.PHIT(index)
				SWT = self.SWT(index)

				RV = self.RV(index)
				RH = self.RH(index)
				RSHV = self.RSHV(index)
				RSHH = self.RSHH(index)

				# Must consider compaction
				# PHIT_SH_REF = m*burial + c
				PHIT_SH_REF = self.PHIT_SH_REF(index)
				PHIT_SST_REF = self.PHIT_SST_REF(index)
				VSH_SH_REF = self.VSH_SH_REF(index)
				VSH_SST_REF = self.PHIT_SST_REF(index)

				SALINITY = self.SALINITY(index)

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
				# Saturation from Triaxial Resistivity
				#--------------------------------------------
				if (RH > 0 and RV > 0 and RSHH > 0 and RSHV > 0):
					if (RV <= RH):
						RS1 = (RV+RH)/2
						F1 = 0
					else:
						RS1 = ((RV/RSHH-RSHV/RH)+math.sqrt((RSHV/RH-RV/RSHH)**2-4*(1/RSHH-1/RH)*(RV-RSHV)))/(2*(1/RSHH-1/RH))
						F1 = (RV-RS1)/(RSHV-RS1)
						RS2 = ((RV/RSHH-RSHV/RH)-math.sqrt((RSHV/RH-RV/RSHH)**2-4*(1/RSHH-1/RH)*(RV-RSHV)))/(2*(1/RSHH-1/RH))
						F2 = (RV-RS2)/(RSHV-RS2)

				if (RS2 > 0 and F2 >= 0 and F2<=1):
   					R_SA_RT = RS2
   					F_SH_RT = F2
					   
				if (RS1 > 0 and F1 >= 0 and F1 <= 1):
   					R_SA_RT = RS1
   					F_SH_RT = F1

				VSH_RTSCAN = F_SH_RT
				VCL_RTSCAN = 0.6*VSH_RTSCAN
				VSST_RTSCAN = 1 - VSH_RTSCAN
				if (VSST_RTSCAN > VSH_SST_REF):
					R_SA_RT_FILT = R_SA_RT
				else:
					R_SA_RT_FILT = -999

				if (VSH < VSH_SST_REF):
					PHIT_SST_MOD = PHIT
				else:
					PHIT_SST_MOD = PHIT_SST

				# Use Archie to determine water saturation
				RES = R_SA_RT_FILT
				
				# Conversion of Temperature units
				if (self.OPT_TEMP_UNITS == 'CELSIUS'):
					FTF = (FT*9/5)+32
				else:
					FTF = FT
				
				RW =((300000/(SALINITY**0.9524))+1)*(1/(FTF+7))
				
                # There is an error where FORM_FACT gives a negative number
                # for all values of M not 2 i.e. any decimal number. 
                # This is because the missing value in IP = -999
				# is still mathematically valid for operations.
                # Solution is to use complex numbers cmath
				# where a**b in complex space = e*8(b*ln*a)
                #FORM_FACT = A*(PHIT_SST_MOD**-M)
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
				self.Save_VSH_RTSCAN(index, VSH_RTSCAN)
				self.Save_VSST_RTSCAN(index, VSST_RTSCAN)
				self.Save_R_SA_RT(index, R_SA_RT)
				self.Save_R_SA_RT_FILT(index, R_SA_RT_FILT)
				self.Save_PHIT_SST_MOD(index, PHIT_SST_MOD)
				self.Save_SWT_ARCH(index, SWT_ARCH)
				self.Save_FACIES_TBA(index, FACIES_TBA)
				#self.Save_FACIES_TBA_COLOUR_Text(index, FACIES_TBA_COLOUR)
				self.Save_PHIT_SH_BULK(index, PHIT_SH_BULK)
				self.Save_PHIT_SST_BULK(index, PHIT_SST_BULK)
				self.Save_SWT_BULK(index, SWT_BULK)
				self.Save_VOLHC_SST_BULK(index, VOLHC_SST_BULK)
				self.Save_VOLWAT_SST_BULK(index, VOLWAT_SST_BULK)

				index += 1
		except Exception:
			pass