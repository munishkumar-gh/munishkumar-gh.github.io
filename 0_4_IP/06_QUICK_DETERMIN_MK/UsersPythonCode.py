"""
Coded by Munish Kumar (02/09/2020)

Petrophysical Deterministic scrip for quickly interpret
Useful for wells with poor data quality or for wells
that require fast turnaround

a) VSH - either from GR, DELTA ND or min of the 2
b) PHIT - either from N-D, Sonic (Whyllie) or Sonic (RHG)
c) SWT - From Archie

VCL is x% of VSH
PHIE and SWE are evaluated from VSH

"""

from Methods import Methods
from IpClassicPythonLink import IPLink
import math
#from sklearn.linear_model import LinearRegression

# Debugging Code
#import ptvsd

class UserApp(Methods, IPLink):

	def UserCode(self):
        # Uncomment the next two lines to enable debgugging
		#ptvsd.enable_attach(address=('127.0.0.1', 5678))
		#ptvsd.wait_for_attach()
		#
		# Loop through the data one level at a time
		# TopDepth and BottomDepth are the index equivalent depths entered on the run window. 
		# 		
		index = self.TopDepth
		while index <= self.BottomDepth:
			# Enter user code here
			try:
				BHT = self.BHT(index)
				SBT = self.SBT(index)
				WD = self.WD(index)
				RTE = self.RTE(index)

				RW_PARM = self.RW_PARM(index)
				SWIRR = self.SWIRR(index)
				RHOCL = self.RHOCL(index)
				RHOSA = self.RHOSA(index)
				PHISH_COEF = self.PHISH_COEF(index)
				PHISH_INT = self.PHISH_INT(index)

				X = self.X
				SS_LITH_CORR = self.SS_LITH_CORR(index)
				B = self.B(index)
				VSHCO = self.VSHCO(index)

				CLAY = self.CLAY(index)
				GRMIN = self.GRMIN(index)
				GRMAX = self.GRMAX(index)
				DELTA_MIN_IN = self.DELTA_MIN_IN(index)
				DELTA_MAX_IN = self.DELTA_MAX_IN(index)
				DT_MASD = self.DT_MASD(index)
				#DT_SH = self.DT_SH(index)
				DT_F = self.DT_F(index)
				M = self.M(index)
				N = self.N(index)

				VSH_METHOD = self.VSH_METHOD
				PHIT_METHOD = self.PHIT_METHOD

				BADHOLE = self.BADHOLE(index)
				COAL = self.COAL(index)
				VOLC = self.VOLC(index)
				#DEPTH = self.DEPTH(index)
				DEPTH_TVDSS = self.DEPTH_TVDSS(index)

				TEMPERATUREOF =  self.TEMPERATUREOF(index)
				TEMPERATUREOC =  self.TEMPERATUREOC(index)
				SALINITY =  self.SALINITY(index)
				RHOFL = self.RHOFL(index)
				PHISH_LOG = self.PHISH_LOG(index)
				GR = self.GR(index)
				NPHI = self.NPHI(index)
				RHOB = self.RHOB(index)
				DT = self.DT(index)
				RT = self.RT(index)

				if (TEMPERATUREOF != -999):
					TEMPERATURE = TEMPERATUREOF
				elif (TEMPERATUREOC != -999):
					TEMPERATURE = (TEMPERATUREOC*9/5) + 32
				elif (DEPTH_TVDSS < (WD+RTE)):
					TEMPERATURE = SBT*9/5 + 32
				else:
					GG = (BHT-SBT)/(max(DEPTH_TVDSS)-WD-RTE)
					TEMPERATURE = (((DEPTH_TVDSS-WD-RTE)*GG) + SBT)*9/5 + 32

				FT = TEMPERATURE

				# RW - If salinity has been zoned use these zones with temperature to make a Rw curve.
				# If a salinity parameter has been given, use this with temperature to make a Rw curve
				# Otherwise use the given Rw parameter (constant)
				if ((SALINITY != -999) and (TEMPERATURE != -999)):
					RW = ((300000/(SALINITY**0.9524))+1) * (1/(TEMPERATURE + 7))
				else:
					RW = RW_PARM

				############### VSH Method ###############
				# VSHALE GR
				VSHI  = (GR-GRMIN)/(GRMAX-GRMIN)
				VSH_GR = max(0.0001,min(1,VSHI))

				# VCLAY INITIAL - estimate based on GR
				VCL_GR = CLAY * VSH_GR

				# VSHALE N-D
				RHOMA = (RHOCL * VCL_GR) + ((1-VCL_GR) * RHOSA)
				PHID = max(0.0001,min(1,((RHOMA-RHOB)/(RHOMA-RHOFL))))  
				DELTA_ND = (NPHI+SS_LITH_CORR) - PHID
				
				if (DELTA_MIN_IN != -999) and (DELTA_MAX_IN != -999):
					DELTA_MIN = DELTA_MIN_IN
					DELTA_MAX = DELTA_MAX_IN
				else:
					DELTA_MIN = 0
					DELTA_MAX = 0.3
				
				VSH_NDi = (DELTA_ND - DELTA_MIN)/(DELTA_MAX - DELTA_MIN)
				VSH_ND = max(0.0001,min(1,(VSH_NDi)))

				#self.ipprint("Entered VSH_ND " + str( VSH_ND ))
				
				# Choose a VSH method (GR or N-D or the 
				# minimum of the two) to use for final VCL 
				# and in future calculations
				if (VSH_METHOD == 'GR'):
					VSH = VSH_GR
				elif (VSH_METHOD == 'ND'):
					VSH = VSH_ND
				elif (VSH_METHOD == 'MIN'):
					VSH = min(VSH_GR, VSH_ND)
				else:
					VSH = -999
				
				# VCL FINAL - based on your VSH selection
				VCL = CLAY * VSH

				############### PHIT Method ###############
				# PHIT based on N-D using the 1/3 - 2/3 rule to correct for hydrocarbons
				RHOF = 0.95
				PHI_DHC = max(0.0001,min(1,((RHOMA-RHOB)/(RHOMA-RHOF))))
				PHI_NPIHC = NPHI+SS_LITH_CORR

				# Arithmetic Average Method
				PHIT_HC_AAM = max(0.0001, min(1,((PHI_DHC + PHI_NPIHC)*0.5)))

				# Weighted Average Method
				if X == 'GAS':
					XA = 0.67
				elif X == 'OIL':
					XA = 0.79
				elif X == 'WATER':
					XA = 0.95
				else:
					XA = float(X)
				PHIT_HC_WAM = max(0.0001,min(1,(XA*(PHI_DHC) + (1-XA)*PHI_NPIHC)))

				# Gaymard’s Equation (Root Mean Square Method)
				PHIT_HC_RMS = max(0.0001, min(1, math.sqrt((PHI_DHC**2+PHI_NPIHC**2)/2)))

				PHIT_HC = (PHIT_HC_WAM + PHIT_HC_RMS + PHIT_HC_AAM)/3
				PHIT_ND = PHIT_HC

				# PHIT based on Raymer Hunt Gardner
				if DT !=-999:
					aa = DT_F*DT
					bb = DT_MASD*DT-2*DT_F*DT
					cc = DT_F*(DT-DT_MASD)
					PHIA = ((((-1)*(bb)) -(math.sqrt(bb**2 - 4*aa*cc)))/(2*aa))/B
					PHIT_DT_RHG = max(0.0001,min(1,PHIA))
				else:
					PHIT_DT_RHG = -999

					# PHIT based on Wyllie
				if DT !=-999:
					PHIT_DT_W = ((DT - DT_MASD)/(DT_F - DT_MASD))/B
				else:
					PHIT_DT_W = -999

				# Final PHIT either from Density, N-D or Sonic
				PHIT = PHID
				if (X != 'WATER'):
					if (PHIT_METHOD == 'ND'):
						PHIT = PHIT_ND
					elif (PHIT_METHOD == 'RHG'):
						PHIT = PHIT_DT_RHG
					elif (PHIT_METHOD == 'WY'):
						PHIT = PHIT_DT_W

				# If a shale porosity (PHISH) log/parameter is 
				# present use it! Otherwise build regression.*/
				if (PHISH_LOG != -999):
					PHISH = PHISH_LOG
				else:
					#BURIAL = DEPTH_TVDSS-WD-RTE
					#reg = LinearRegression()
					
					#if (VSH > VSHCO):
					#	y_train = PHIT.reshape(-1,1)
					#	x_train = BURIAL.reshape(-1,1)
					#reg.fit(x_train, y_train)
						
					#PHISH = BURIAL*reg.coef_ + reg.intercept_
					PHISH = (abs(DEPTH_TVDSS)**(PHISH_COEF))*PHISH_INT

				# PHIE from PHIT*/
				PHIE = max(0.0001,(PHIT - (VSH*PHISH)))

				# Apply a VSH cut-off to PHIE and apply 
				# "ramping down" to avoid sharp edge effects
				if (VSH > VSHCO + 0.2):
					PHIE = 0.001
				elif (VSH > (VSHCO-0.2)):
					PHIE = max(0.0001, PHIE*((VSHCO-VSH)/0.2))
				else:
					PHIE = max(0.0001, PHIE)

				############### SWT Method ###############
				# RO - this is the resistivity value that should be measured 
				# if the reservoir is water-wet, based on Rw and PHIT
				#  For QC purposes  
				RO = (RW/PHIT**M)

				# SWT - Archie SWT
				if RT != -999:
					SWT = max(0.0001, min(1,((1/PHIT**M) * (RW / RT))**(1/N)))
				else:
					SWT = 1

				# SWE - Archie SWE limited by an irreducible water saturation (SWIRR)
				SWE = max(SWIRR, (1-((PHIT/PHIE)*(1-SWT))))

				# Apply cut-offs and a "ramp" to tidy up your SWT and SWE*/
				if (VSH>VSHCO) or (PHIT<0.02):
					SWT = 1
					SWE = 1
				elif (VSH>(VSHCO-0.2)):
					SWE = 1-((1-SWE)*((VSHCO-VSH)/0.2))
					SWT = 1-((1-SWT)*((VSHCO-VSH)/0.2))
				
				# BVW & BVG: bulk volume of water and gas
				BVW = PHIT * SWT
				BVG = PHIT - BVW

				# COAL & VOLCANICS: If flags have been created, 
				# PHIT will be set to 0 and saturations to 1
				if (COAL > 0) or (VOLC > 0) or (BADHOLE > 0):
					SWT  = SWE  = 1
					PHIT = PHIE = BVW = BVG = 0
					VSH = VSH_ND = VCL = VSH_GR = 0

				self.Save_FT(index, FT)
				self.Save_RW(index, RW)
				self.Save_VSH_GR(index, VSH_GR)
				self.Save_VCL_GR(index, VCL_GR)
				self.Save_DELTA_ND(index, DELTA_ND)
				self.Save_VSH_ND(index, VSH_ND)
				self.Save_VSH(index, VSH)
				self.Save_VCL(index, VCL)
				self.Save_RHOMA(index, RHOMA)
				self.Save_PHID(index, PHID)
				self.Save_PHIT_ND(index, PHIT_HC)
				self.Save_PHIT_DT_RHG(index, PHIT_DT_RHG)
				self.Save_PHIT_DT_W(index, PHIT_DT_W)
				self.Save_PHIT(index, PHIT)
				self.Save_SWT(index, SWT)
				self.Save_PHIE(index, PHIE)
				self.Save_SWE(index, SWE)
				self.Save_RO(index, RO)
				self.Save_BVW(index, BVW)
				self.Save_BVG(index, BVG)
				index += 1
				# self.ipprint("Entered PHIT_HC " + str( PHIT_HC ))
			except Exception:
				index += 1
				continue

	def ipprint(self, text):
		from PGL.IP.API import IntPetroAPI
		messageBoard = IntPetroAPI().GetService('PGL.IP.Services.IMessageBoard, PGL.IP.Services')
		messageBoard.Add(1, text)
