"""
Coded by: Munish Kumar (03/09/2020)
Effective Porosity, Saturation Calculator

"""

from Methods import Methods
from IpClassicPythonLink import IPLink
import math

# Debugging Code
#import ptvsd

class UserApp(Methods, IPLink):

	def UserCode(self):
		# Uncomment the next two lines to enable debgugging
		#ptvsd.enable_attach(address=('127.0.0.1', 5678))
		#ptvsd.wait_for_attach()
		# Loop through the data one level at a time
		# TopDepth and BottomDepth are the index equivalent depths entered on the run window. 
		# 		
		index = self.TopDepth
		while index <= self.BottomDepth:
			# Enter user code here
			try:
				VSHCO = self.VSHCO(index)
				SWIRR = self.SWIRR(index)
				PHIECO = self.PHIECO(index)

				VSH = self.VSH(index)
				PHIT = self.PHIT(index)
				SWT = self.PHIT(index)

				PHISH_COEF = self.PHISH_COEF(index)
				PHISH_INT = self.PHISH_INT(index)
				TVDSS = self.TVDSS(index)

				PHISH = PHISH_INT*(abs(TVDSS)**(PHISH_COEF))
				#self.ipprint("PHISH: " + str( PHISH ))
				if PHISH < 0:
					PHISH = 0
				else:
					PHIE = max(0.001,(PHIT - (VSH*PHISH)))

				if (VSH > VSHCO):
					SWT = SWE = 1
				else:
					SWE = max(SWIRR,(1-((PHIT/PHIE)*(1-SWT))))

				if (SWE > SWT):
					SWE = SWT
				else:
					SWE = SWE

				if (VSH > (VSHCO-0.2)):
					SWE = 1-((1-SWE)*((VSHCO-VSH)/0.2))

				if (SWE > SWT):
					SWE = SWT
				else:
					SWE=SWE

				if (PHIE < PHIECO) or (PHIE < 0):
					SWT = SWE = 1
				elif (PHIE < (PHIECO+0.02)):
					SWE = 1-((1-SWE)*((PHIE-PHIECO)/0.2))

				if (SWE > SWT):
					SWE = SWT
				else:
					SWE = SWE

				self.Save_SWE(index, SWE)
				self.Save_PHIE(index, PHIE)

				index += 1
			except Exception:
				pass

	def ipprint(self, text):
		from PGL.IP.API import IntPetroAPI
		messageBoard = IntPetroAPI().GetService('PGL.IP.Services.IMessageBoard, PGL.IP.Services')
		messageBoard.Add(1, text)