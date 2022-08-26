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

				PHIT = self.PHIT(index)
				PHIE = self.PHIE(index)

				#PHI_MAX = self.PHI_MAX(index)

				VSH = self.VSH(index)
				VCL = self.VCL(index)

				SWT = self.SWT(index)
				SWE = self.SWE(index)

				if (PHIT == -999) or (PHIT < 0):
					PHIT = 0.03
				elif (PHIT > PHI_MAX):
					PHIT = PHI_MAX
				else:
					PHIT = PHIT

				if (PHIE == -999) or (PHIE < 0):
					PHIE = 0.03
				elif (PHIE > PHI_MAX):
					PHIE = PHI_MAX
				else:
					PHIE = PHIE

				if (VSH == -999) or (VSH < 0):
					VSH = 0.03
				elif (VSH > 1):
					VSH = 0.97
				else:
					VSH = VSH

				if (VCL == -999) or (VCL < 0):
					VCL = 0.03
				elif (VCL > 1):
					VCL = 0.97
				else:
					VCL = VCL
				
				if (SWT == -999) or (SWT < 0):
					SWT = 0.03
				elif (SWT > 1):
					SWT = 1
				else:
					SWT = SWT

				if (SWE == -999) or (SWE < 0):
					SWE = 0.03
				elif (SWE > 1):
					SWE = 1
				else:
					SWE = SWE

				self.Save_VSH(index, VSH)
				self.Save_VCL(index, VCL)
				self.Save_PHIT(index, PHIT)
				self.Save_PHIE(index, PHIE)
				self.Save_SWT(index, SWT)
				self.Save_SWE(index, SWE)

				index += 1
			except Exception:
				pass