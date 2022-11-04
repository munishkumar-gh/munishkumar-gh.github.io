"""
Coded by: Munish Kumar (24/08/2020)

Algorithm to interpret HC shows using Light (C1-C5) Hydrocarbon gases from Mud-log Data
1) Hydrocarbon Wetness, Wh (or gas wetness ratio, GWR)
2) Balance Ratio, Bh (or light to heavy ratio, LHR)
3) Character Ratio, Ch (or oil character qualifier, OCQ)
Generates a flag to indicate potential HC show type

Flag = 1 - Very dry gas
Flag = 2 - Medium Density Gas
Flag = 3 - Gas/Oil Zone
Flag = 4 - Medium Gavity Oil 
Flag = 5 - Residual or transition zone

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
				C1 = self.C1(index)
				C2 = self.C2(index)
				C3 = self.C3(index)
				IC4 = self.IC4(index)
				IC5 = self.IC5(index)
				NC4 = self.NC4(index)
				NC5 = self.NC5(index)
				GASUNITS = self.GASUNITS

				# Converts to PPM
				if (GASUNITS == '%'):
					C1_A = C1*10000
					C2_A = C2*10000
					C3_A = C3*10000
					IC4_A = IC4*10000
					NC4_A = NC4*10000
					IC5_A = IC5*10000
					NC5_A = NC5*10000
					C1 = C1_A
					C2 = C2_A
					C3 = C3_A
					IC4 = IC4_A
					NC4 = NC4_A
					IC5 = IC5_A
					NC5 = NC5_A

				C4 = IC4 + NC4
				C5 = IC5 + NC5

				if (C1< 0):
					C1 = 0
				if (C2< 0):
					C2 = 0
				if (C3< 0):
					C3 = 0
				if (IC4< 0):
					IC4 = 0
				if (IC5< 0):
					IC5 = 0
				if (NC4< 0):
					NC4 = 0
				if (NC5< 0):
					NC5 = 0

				try:
					Wh = ((C2+C3+C4+C5)/(C1+C2+C3+C4+C5))*100
					Bh = ((C1+C2)/(C3+C4+C5))*100	
					Ch = ((C4+C5)/(C3))*100
				except Exception:
					Wh = Bh = Ch = -1
					pass

				if (Wh < 0.5 and Bh > 100):
					FLAG_HC = 1
					FLAG = "Very dry gas"
				elif (Wh > 0.5 and Wh < 17.5 and Bh > Wh):
					if (Ch < 0.5):
						FLAG_HC = 2
						FLAG = "Medium Density Gas"
					else:
						FLAG_HC = 3
						FLAG = "Gas/Oil Zone"
				elif (Wh > 17.5 and Wh < 40 and Bh < Wh):
					FLAG_HC = 4
					FLAG = "Medium Gavity Oil"
				elif (Wh > 40 and Bh < Wh):
					FLAG_HC = 5
					FLAG = "Residual/transition zone"
				else:
					FLAG_HC = 0
					FLAG = "Undefined"

				self.Save_FLAG_HC(index, FLAG_HC)
				self.Save_Wh(index, Wh)
				self.Save_Bh(index, Bh)
				self.Save_Ch(index, Ch)
				self.Save_FLAG_Text(index, FLAG)
				index += 1
			except Exception:
				index += 1
				continue