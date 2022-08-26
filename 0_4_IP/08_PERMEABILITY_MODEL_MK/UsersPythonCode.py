"""
Coded by Munish Kumar (07/09/2020)

Petrophysical Deterministic script for quickly interpret
of permeability as well as Capillary Pressure

(a) Permeabilities based on 3 techniques (Timor-Coates, Herron and Damien-Lu)
(b) Supply a non-linear Skelt-Harrison capillary pressure function that has been pre-defined
Note that this module only deals with non-linear Skelt-Harrison functions

"""
from Methods import Methods
from IpClassicPythonLink import IPLink
import math
import numpy as np

# Debugging Code
#import ptvsd

class UserApp(Methods, IPLink):

	def UserCode(self):
		# Uncomment the next two lines to enable debgugging
#		ptvsd.enable_attach(address=('127.0.0.1', 5678))
#		ptvsd.wait_for_attach()
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
				PHIE = self.PHIE(index)
				SWT_RES = self.SWT_RES(index)
				Y = self.Y(index)

				SA_CL = self.SA_CL(index)
				VI = self.VI(index)
				SA_SA = self.SA_SA(index)
				RHOM = self.RHOM(index)
				Z1 = self.Z1(index)
				
				ALPHA = self.ALPHA(index)
				BETA = self.BETA(index)
				GAM = self.GAM(index)
				CHARLIE = self.CHARLIE(index)

				PHISH_COEF = self.PHISH_COEF(index)
				PHISH_INT = self.PHISH_INT(index)
				TVDSS = self.TVDSS(index)
				DEPTH = self.DEPTH(index)

				GSI_SD = self.GSI_SD(index)
				GSI_SI = self.GSI_SI(index)
				E1 = self.E1(index)
				E2 = self.E2(index)
				F1 = self.F1(index)
				F2 = self.F2(index)

				FLAG_SWT_RES = self.FLAG_SWT_RES(index)
				PERM_CO = self.PERM_CO(index)
				PHI_CO = self.PHI_CO(index)

				MC = self.MC(index)
				SR = self.SR(index)
				FWL = self.FWL(index)
				G_GD = self.G_GD(index)
				W_GD = self.W_GD(index)
				O_GD = self.O_GD(index)
				TCosT_AW_L = self.TCOST_AW_L(index)
				TCosT_GW_R = self.TCOST_GW_R(index)
				TCosT_OW_L = self.TCOST_OW_L(index)
				TCosT_OW_R = self.TCOST_OW_R(index)
				GOC = self.GOC(index)
				PERM = self.PERM(index)

				A_C0 = self.A_C0(index)
				A_C1 = self.A_C1(index)
				A_C2 = self.A_C2(index)
				A_C3 = self.A_C3(index)
				A_C4 = self.A_C4(index)

				B_C0 = self.B_C0(index)
				B_C1 = self.B_C1(index)
				B_C2 = self.B_C2(index)
				B_C3 = self.B_C3(index)

				C_C0 = self.C_C0(index)
				C_C1 = self.C_C1(index)
				C_C2 = self.C_C2(index)
				C_C3 = self.C_C3(index)
				C_C4 = self.C_C4(index)

				D_C0 = self.D_C0(index)
				D_C1 = self.D_C1(index)
				D_C2 = self.D_C2(index)
				D_C3 = self.D_C3(index)
				D_C4 = self.D_C4(index)

				FLAG_FLUIDS = self.FLAG_FLUIDS
				OPT_FLUID_SYSTEM = self.OPT_FLUID_SYSTEM
				CORE_REG_USE = self.CORE_REG_USE
				CAP_PRESSURE = self.CAP_PRESSURE

				CLAMP_MIN = 0.001
				CLAMP_MAX = 8000

				#Set to Null
				HAFWL= PCLAB= PCRES= SW_PC= TCPERM= TCPERM_PHISH= KTIM_FREE_FLUID= HPERM= LUPERM= K_RGPZ= -999
				REG_PERM_A1= REG_PERM_A2= PERM_MIN= PERM_MAX= PERM_FINAL= -999

				################################
				# Part A - Permeability
				################################
				if (VSH <= 0) or (PHIT <= 0) or (PHIE <= 0) or (SWT_RES <= 0) or (RHOM <= 0):
					VSH = SWT_RES = 1 - CLAMP_MIN
					PHIT = PHIE = CLAMP_MIN
					RHOM = abs(RHOM)

				BVW = PHIT*SWT_RES
				BVG = PHIT-BVW
				VCL = Y*VSH

				# HERRON PERM - mineralogy-based
				# S0 = Specific Surface Area
				S0 = (VCL*SA_CL*VI) + ((1-VCL)*SA_SA)
				# M* "Measured" m value
				M = 1.653 + 0.0818*((S0*RHOM)**0.5)
				Z2 = 0.37 * (Z1**1.7)
				# HIGH PERM, LOW PERM, COMBINED PERM
				K_A1 = (Z1*(PHIT**(M+2))) / ((RHOM**2)*((1-PHIT)**2)*(S0**2))
				K_A2 = (Z2*(PHIT**(1.7*(M+2)))) / ((RHOM**3.4)*((1-PHIT)**3.4)*(S0**3.4))

				HPERM = min(K_A1,K_A2)
				#self.ipprint("HPERM: " + str( HPERM ) +" @Depth: " + str( DEPTH ) )

				# TIMOR-COATES PERM - saturation-based
				if (BVG != 0) and (BVW != 0):
					TCPERM = ((100*PHIT/ALPHA)**BETA)*(max(0.001,(BVG/BVW))**GAM)
				else:
					TCPERM = CLAMP_MIN
				#self.ipprint("TCPERM: " + str( TCPERM ) +" @Depth: " + str( DEPTH ) )
				
				PHISH = PHISH_INT*(abs(TVDSS)**(PHISH_COEF))
				if PHISH < 0:
					PHISH = CLAMP_MIN
				else:
					PHISH = PHISH

				# TIMOR-COATES PERM USING PHISH - modified Timor-Coates perm using shale porosity
				if (PHIE != 0) and (VSH != 0):
					TCPERM_PHISH = ((100*PHIT/ALPHA)**BETA)*(max(0.001, ((PHIE*(1-VSH))/(PHISH*VSH)))**GAM)
				else:
					TCPERM_PHISH = CLAMP_MIN
				#self.ipprint("TCPERM_PHISH: " + str( TCPERM_PHISH ) +" @Depth: " + str( DEPTH ) )

				# Timor Coates using free fluid model
				if (PHIE != 0) and (BVW != 0):
					KTIM_FREE_FLUID = (((PHIT/CHARLIE)**2)*(max(0.001,(PHIE/BVW))**GAM))
				else:
					KTIM_FREE_FLUID = CLAMP_MIN
				#self.ipprint("KTIM_FREE_FLUID: " + str( KTIM_FREE_FLUID ) +" @Depth: " + str( DEPTH ) )

				# DAMIEN-LU PERM - for use in very high porosity sands only
				GS = (1-VSH)*GSI_SD + VSH*GSI_SI
				#self.ipprint("GS: " + str( GS ) +" @Depth: " + str( DEPTH ) )
				if (PHIT-0.025 > 0):
					Ko = (5 * GS**2)*(PHIT-0.025)**3.05
				else:
					Ko = CLAMP_MIN
				#self.ipprint("Ko: " + str( Ko ) +" @Depth: " + str( DEPTH ) )
				R_CLAY = (PHIT-PHIE)/PHIT
				#self.ipprint("R_CLAY: " + str( R_CLAY ) +" @Depth: " + str( DEPTH ) )
				U = 12.5*(1 - 0.75*R_CLAY)			
				#self.ipprint("U: " + str( U ) +" @Depth: " + str( DEPTH ) )

				LUPERM = Ko * (1-R_CLAY)**U
				#self.ipprint("LUPERM: " + str( LUPERM ) +" @Depth: " + str( DEPTH ) )

				# RGPZ equation - 8/3 used is the constant for the grain packing constant (a)
				# Note that the method follows the relationship that a large grain size means
				# good sorting, and therefore good porosity:permeability. This is not true in PNG
				# where there is poor sorting, low porosities, but where perms are high. Need to use
				# unrealistic grain sizes and calculate for a scenario where the rock is behaving as
				# in a normal environment
				K_RGPZ = (1000*GS**BETA*PHIT**(3*M))/(4*8/3*M**GAM)
				#self.ipprint("K_RGPZ: " + str( K_RGPZ ) +" @Depth: " + str( DEPTH ) )

				# Core Permeability to Log PHIE/PHIT Regression
				REG_PERM_A1 = 10**(E1 + PHIE*F1)
				REG_PERM_A2 = 10**(E2 + PHIT*F2)
				#self.ipprint("REG_PERM_A1: " + str( REG_PERM_A1 ) +" @Depth: " + str( DEPTH ) )
				#self.ipprint("REG_PERM_A2: " + str( REG_PERM_A2 ) +" @Depth: " + str( DEPTH ) )

				# MIN/ MAX PERM - min/ max of all perm methods except Timur Coates free fluid model
				# Flags indicate quality of resistivity based water saturation - 1 is good, 0 is bad
				if (CORE_REG_USE == 'YES'):
					if (FLAG_SWT_RES == 0):
						PERM_MIN = min(HPERM, LUPERM, K_RGPZ, REG_PERM_A1, REG_PERM_A2)
						PERM_MAX = max(HPERM, LUPERM, K_RGPZ)
					else:
						PERM_MIN = min(HPERM, TCPERM, TCPERM_PHISH, LUPERM, K_RGPZ, REG_PERM_A1, REG_PERM_A2)
						PERM_MAX = max(HPERM, TCPERM, TCPERM_PHISH, LUPERM, K_RGPZ)
				else:
					if (FLAG_SWT_RES == 0):
						PERM_MIN = min(HPERM, LUPERM, K_RGPZ)
						PERM_MAX = max(HPERM, LUPERM, K_RGPZ)
					else:
						PERM_MIN = min(HPERM, TCPERM, TCPERM_PHISH, LUPERM, K_RGPZ)
						PERM_MAX = max(HPERM, TCPERM, TCPERM_PHISH, LUPERM, K_RGPZ)

				# Check condition to determine if there is a need to lower the permeability towards a minimum value
				# As all the emperical techniques tend to overestimate the permeabilities in the low quality sands
				# this check condition ensures that the core k to log porosity correlation is applied in such zones
				if (PERM_MIN <= PERM_CO) and (VSH != 0) and (PHIT - PHIE > PHI_CO):
					PERM_FINAL = PERM_MIN
				else:
					PERM_FINAL = PERM_MAX			
				#self.ipprint("PERM_FINAL: " + str( PERM_FINAL ) +" @Depth: " + str( DEPTH ) )

				################################
				# Part B - Capillary Pressure
				################################
				if (CAP_PRESSURE == 'YES'):
					if (FLAG_FLUIDS == 'WATER') or (FLAG_FLUIDS == 'PERCHED_WATER'):
						HAFWL = PCRES = PCLAB = -999
						SW_PC = 1
					elif (FLAG_FLUIDS == 'RELICT_HC') or (FLAG_FLUIDS =='RESIDUAL_HC'):
						HAFWL = PCRES = PCLAB = SW_PC = -999
					elif (FLAG_FLUIDS == 'GAS') or (FLAG_FLUIDS == 'OIL'):
						if (OPT_FLUID_SYSTEM == 'OIL') or (OPT_FLUID_SYSTEM == 'GAS'):
							HAFWL = FWL - TVDSS
							if (FLAG_FLUIDS == 'GAS'):
								PCRES = HAFWL*(W_GD - G_GD)
								PCLAB = PCRES*TCosT_AW_L/TCosT_GW_R
							elif (FLAG_FLUIDS == 'OIL'):
								PCRES = HAFWL*(W_GD - O_GD)
								PCLAB = PCRES*TCosT_AW_L/TCosT_OW_R		
						elif (OPT_FLUID_SYSTEM == 'GAS-OIL-WTR'):
							X = (FWL - GOC)*(G_GD - O_GD)/(G_GD - W_GD)
							PGWC = FWL - X
							if (FLAG_FLUIDS == 'GAS'):
								HAFWL = PGWC - TVDSS
								PCRES = HAFWL*(W_GD - G_GD)
								PCLAB = PCRES*TCosT_AW_L/TCosT_GW_R
							elif (FLAG_FLUIDS == 'OIL'):
								HAFWL = FWL - TVDSS
								PCRES = HAFWL*(W_GD - O_GD)
								PCLAB = PCRES*TCosT_AW_L/TCosT_OW_R

					# Calculations are only applied in gas leg (or oil leg), when coal is not present
					# The 5 constants for each parameter are entered into Loglan as c0, c1, c2, c3, c4
					# c and d will generally be constants (enter as c4 and set c1-3 to 0)
					K = PERM
					if (K > 0):
						a = (A_C0 * (math.log(K)**4)) + (A_C1 * (math.log(K)**3)) + (A_C2 * (math.log(K)**2)) + (A_C3 * math.log(K)) + A_C4
						b = B_C0 * math.exp(((B_C1 -(B_C2* math.log(K)))/(1 + (B_C3 *math.log(K)))))
						c = (C_C0 * (math.log(K)**4)) + (C_C1 * (math.log(K)**3)) + (C_C2 * (math.log(K)**2)) + (C_C3 * math.log(K)) + C_C4
						d = (D_C0 * (math.log(K)**4)) + (D_C1 * (math.log(K)**3)) + (D_C2 * (math.log(K)**2)) + (D_C3 * math.log(K)) + D_C4
						SW_PC = min(0.9999, 1-(a*(math.exp(-((b/(d + PCLAB))**c)))))
					else:
						SW_PC = 1
				else:
					SW_PC = -999

				self.Save_HAFWL(index, HAFWL)
				self.Save_PCLAB(index, PCLAB)
				self.Save_PCRES(index, PCRES)
				self.Save_SW_PC(index, SW_PC)
				self.Save_TCPERM(index, TCPERM)
				self.Save_TCPERM_PHISH(index, TCPERM_PHISH)
				self.Save_KTIM_FREE_FLUID(index, KTIM_FREE_FLUID)
				self.Save_HPERM(index, HPERM)
				self.Save_LUPERM(index, LUPERM)
				self.Save_K_RGPZ(index, K_RGPZ)
				self.Save_REG_PERM_A1(index, REG_PERM_A1)
				self.Save_REG_PERM_A2(index, REG_PERM_A2)

				self.Save_PERM_MIN(index, PERM_MIN)
				self.Save_PERM_MAX(index, PERM_MAX)
				self.Save_PERM_FINAL(index, PERM_FINAL)
				index += 1
			except Exception:
				continue
				index += 1

	def ipprint(self, text):
		from PGL.IP.API import IntPetroAPI
		messageBoard = IntPetroAPI().GetService('PGL.IP.Services.IMessageBoard, PGL.IP.Services')
		messageBoard.Add(1, text)

	def clamp(self, n, minn, maxn):
		return max(min(maxn, n), minn)

	def moving_average(self, a, n=3) :
		ret = np.cumsum(a, dtype=float)
		ret[n:] = ret[n:] - ret[:-n]
		return ret[n - 1:] / n