"""
@author: Munish Kumar (17/08/20)
PROGRAM: 13_GEOMECH_GEOPHY

Code was developed to evalaute a series of geomechanical and geophysical
propoerties from logs

Geomechanical properties calculated from well logs are called dynamic
properties, and dont always correlate well with statical properties 
measured on lab physical core plug samples. 
However, they yield whole zone continuous curves (instead of a collection of 
sampled points at core depths) and provide useful insights to study 
a reservoir without using destructive rock sampling tests (in the best 
case, the core may not be destroyed, but it is severely altered, thus not 
really representing the in-situ reservoir conditions). 

Some common equations to estimate gemechanical properties from well logs are:
Poisson ratio (v) from shear and compressional sonic logs
Shear modulus (G) from shear travel time and bulk density logs
Young modulus (E) from G and Poisson ratio ν
Bulk modulus (K) from shear & compressional sonic logs, and bulk density log
Sand Production Index (SPI) from G, and shear & compressional sonic logs
Unconfined Compressive Strength (UCS) from E, K, and VSH empirical correlation
UCS Unconfined Compressive Strength from empirical porosity correlation

Using correlations, the dynamic values can be converetd to static values but 
these have to be tuend to the basin in consideration

References:
Wang H.F., Theory of Linear Poroelasticity, Princeton University Press, Princeton, 2000. 

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
			DTC = self.DTC(index)
			DTS = self.DTS(index)
			RHOB = self.RHOB(index)
			PHIT = self.PHIT(index)
			VSH = self.VSH(index)

			# Impedence -----------------
			P_IMP = RHOB * pow(10, 6)/DTC
			S_IMP = RHOB * pow(10, 6)/DTS
			
			# Dynamic Properties -------------------
			# Poisson's ratio (unitless) from shear and compressional sonic
			POI_RAT_DYN = (0.5*(DTS/DTC)**2 - 1)/((DTS/DTC)**2 - 1)

			# Shear Modulus in Mpsi (1 Mpsi = 6894.75729 MPa)
			SHE_MOD_DYN = 1.34*pow(10,4)*RHOB/(DTS**2)

			# Axial Compressional Youngs Stiffness Modulus in Mpsi
			YNG_MOD_DYN = 2*SHE_MOD_DYN*(1+POI_RAT_DYN)
			
			# Volumetric Compressional Bulk Modulus in Mpsi
			BULK_MOD_DYN = 1.34*pow(10,4)*RHOB*(1/(DTC**2)	- 4/(3*DTS**2))

			# Sand Production Index in x10^12 psi^2
			# SPI < 0.8x10^12 suggest stable formation
			SPI = SHE_MOD_DYN*2*((DTS/DTC)**2-4/3)/pow(10, 12)

			# Unconfined Compressive Strength in psi
			UCS_COATES = 0.087*pow(10, -6)*YNG_MOD_DYN*BULK_MOD_DYN*(0.008*VSH+0.0054*(1-VSH))*pow(10, 12)
			UCS_PHIT = 258*math.exp(-9*PHIT)
			# -----------------------------------------------------

			# Static Properties -------------------
			# Poisson's ratio assumes static and dynamic are equal
			POI_RAT_STA	= POI_RAT_DYN

			# Youngs Modulus
			# Subscript Wang and Morals are authors who have created emperical
			# correlations as one moves from dynamic to static	
			YNG_MOD_STA_WANG = 0.4145*YNG_MOD_DYN-1.0593
			YNG_MOD_STA_MORALS = YNG_MOD_DYN*(-2.21*PHIT+0.963)

			SHE_MOD_STA_WANG = YNG_MOD_STA_WANG/ (2*(1+POI_RAT_STA))
			SHE_MOD_STA_MORALS = YNG_MOD_STA_MORALS/ (2*(1+POI_RAT_STA))

			BULK_MOD_STA_WANG = YNG_MOD_STA_WANG/ (3*(1-2*POI_RAT_STA))
			BULK_MOD_STA_MORALS = YNG_MOD_STA_MORALS/ (3*(1-2*POI_RAT_STA))
			# -----------------------------------------------------

			#Convert to MPa
			YNG_MOD_DYN = YNG_MOD_DYN*6894.75729
			SHE_MOD_DYN = SHE_MOD_DYN*6894.75729
			BULK_MOD_DYN = BULK_MOD_DYN*6894.75729
			YNG_MOD_STA_WANG = YNG_MOD_STA_WANG*6894.75729
			YNG_MOD_STA_MORALS = YNG_MOD_STA_MORALS*6894.75729
			SHE_MOD_STA_WANG = SHE_MOD_STA_WANG*6894.75729
			SHE_MOD_STA_MORALS = SHE_MOD_STA_MORALS*6894.75729
			BULK_MOD_STA_WANG = BULK_MOD_STA_WANG*6894.75729
			BULK_MOD_STA_MORALS = BULK_MOD_STA_MORALS*6894.75729
			
			self.Save_POI_RAT_DYN(index, POI_RAT_DYN)
			self.Save_SHE_MOD_DYN(index, SHE_MOD_DYN)
			self.Save_YNG_MOD_DYN(index, YNG_MOD_DYN)
			self.Save_BULK_MOD_DYN(index, BULK_MOD_DYN)
			self.Save_SPI(index, SPI)
			self.Save_UCS_COATES(index, UCS_COATES)
			self.Save_UCS_PHIT(index, UCS_PHIT)

			self.Save_POI_RAT_STA(index, POI_RAT_STA)
			self.Save_YNG_MOD_STA_WANG(index, YNG_MOD_STA_WANG)
			self.Save_YNG_MOD_STA_MORALS(index, YNG_MOD_STA_MORALS)			
			self.Save_SHE_MOD_STA_WANG(index, SHE_MOD_STA_WANG)
			self.Save_SHE_MOD_STA_MORALS(index, SHE_MOD_STA_MORALS)
			self.Save_BULK_MOD_STA_WANG(index, BULK_MOD_STA_WANG)
			self.Save_BULK_MOD_STA_MORALS(index, BULK_MOD_STA_MORALS)

			self.Save_P_IMP(index, P_IMP)
			self.Save_S_IMP(index, S_IMP)

			index += 1