"""
Coded by: Munish Kumar (16/10/2020)

Interpretaiton and evaluation of old style neutron logs.

Old style gamma ray neutron (GRN) logs are un-scaled neutron logs 
recorded in counts per second or API units. They are common in 
ancient wells. The log carries a gamma ray curve (GR) in the 
left hand track and a neutron curve (NEUT) in the right hand 
track. No borehole or casing corrections have been applied to 
these logs. 

Neutron log deflections to the left (lower count rate) represent higher porosity.

Method will be use the "High porosity- Low porosity" method. A logarithmic scale 
can be applied algebraically with the following formulae using the high 
porosity/low porosity method.

Code will calculate VSH and Archie baed Saturation as well
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
				DEPTH_TVDSS = self.DEPTH_TVDSS(index)
				TEMPERATUREOF =  self.TEMPERATUREOF(index)
				TEMPERATUREOC =  self.TEMPERATUREOC(index)
				SALINITY =  self.SALINITY(index)
				WD =  self.WD(index)
				RTE = self.RTE(index)
				SBT = self.SBT(index)
				BHT = self.BHT(index)

				M = self.M(index)
				N = self.N(index)
				
				PHIHI = self.PHIHI(index)
				PHILO = self.PHILO(index)
				CPSHI = self.CPSHI(index)
				CPSLO = self.CPSLO(index)
				MULT = self.MULT(index)

				shale_intcp = self.shale_intcp(index)
				shale_coeff = self.shale_coeff(index)

				NEUT = self.NEUT(index)
				GR = self.GR(index)
				RT = self.RT(index)
				GRmin = self.GRmin(index)
				GRmax = self.GRmax(index)

				# Calc VSH from GR
				VSH = (GR - GRmin)/ (GRmax-GRmin)
				VCL = VSH*0.6

				# Calculate Shale Porosity
				if shale_coeff == -999 or shale_intcp == -999:
					shale_coeff = 0.000810012798
					shale_intcp = 0.360390235
				PHISH = (shale_intcp  +  shale_coeff * VSH)

				CPSH = CPSHI*MULT
				CPSL = CPSLO*MULT			

				SLOPE = (math.log10(PHIHI / PHILO)) / (CPSH - CPSL)
				INTCPT  = PHIHI/ 10**(CPSH * SLOPE)

				PHIn = INTCPT * 10 ** (SLOPE * NEUT)
				PHIE = PHIn - (VSH * PHISH)

				if (TEMPERATUREOF != -999):
					TEMPERATURE = TEMPERATUREOF
				elif (TEMPERATUREOC != -999):
					TEMPERATURE = (TEMPERATUREOC*9/5) + 32
				elif (DEPTH_TVDSS < (WD+RTE)):
					TEMPERATURE = SBT*9/5 + 32
				else:
					GG = (BHT-SBT)/(max(DEPTH_TVDSS)-WD-RTE)
					TEMPERATURE = (((DEPTH_TVDSS-WD-RTE)*GG) + SBT)*9/5 + 32

				#FT = TEMPERATURE

				# RW - If salinity has been zoned use these zones with temperature to make a Rw curve.
				# If a salinity parameter has been given, use this with temperature to make a Rw curve
				# Otherwise use the given Rw parameter (constant)
				if ((SALINITY != -999) and (TEMPERATURE != -999)):
					RW = ((300000/(SALINITY**0.9524))+1) * (1/(TEMPERATURE + 7))
				else:
					RW = 0.25 # Random number

				############### SWT Method ###############
				# RO - this is the resistivity value that should be measured 
				# if the reservoir is water-wet, based on Rw and PHIT
				#  For QC purposes

				PHIT = PHIn  
				#RO = (RW/PHIT**M)

				# SWT - Archie SWT
				if RT != -999:
					SWT = max(0.0001, min(1,((1/PHIT**M) * (RW / RT))**(1/N)))
				else:
					SWT = 1

				# SWE - Archie SWE limited by an irreducible water saturation (SWIRR)
				SWIRR = 0.03
				SWE = max(SWIRR, (1-((PHIT/PHIE)*(1-SWT))))

				# Apply cut-offs and a "ramp" to tidy up your SWT and SWE*/
				VSHCO = 0.8
				if (VSH > VSHCO) or (PHIT < 0.02):
					SWT = 1
					SWE = 1
				elif (VSH>(VSHCO-0.2)):
					SWE = 1-((1-SWE)*((VSHCO-VSH)/0.2))
					SWT = 1-((1-SWT)*((VSHCO-VSH)/0.2))

				if VSH > 1 or VSH < 0:
					VSH = VCL = -999

				if PHIE > 1 or PHIE < 0:
					PHIn = PHIE = -999

				if SWT > 1 or SWT < 0:
					SWT = SWE = -999

				self.Save_VSH(index, VSH)
				self.Save_VCL(index, VCL)
				self.Save_SLOPE(index, SLOPE)
				self.Save_INTCPT(index, INTCPT)
				self.Save_PHIn(index, PHIn)
				self.Save_PHIE(index, PHIE)
				self.Save_SWT(index, SWT)
				self.Save_SWE(index, SWE)
				index += 1
			except Exception:
				index += 1
				continue