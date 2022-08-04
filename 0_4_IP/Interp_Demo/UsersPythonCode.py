from Methods import Methods
from IpClassicPythonLink import IPLink
import sys
import math
import os

class UserApp(Methods, IPLink):

	def UserCode(self):
		writer = None
		try:
			#   calculate the Pickett plot end point parameters
			self.CalculatePickett()
			#
			#   Intitalize zonal averages
			PayNet = 0.0
			ResNet = 0.0
			PhiPay = 0.0
			PhiRes = 0.0
			SwPay = 0.0
			SwRes = 0.0
			VclPay = 0.0
			VclRes = 0.0
			BVWPay = 0.0
			BVWRes = 0.0
			PayCount = 0.0
			ResCount = 0.0
			#
			# Loop through the data one level at a time
			# TopDepth and BottomDepth are the index equivalent depths entered on the run window. 
			# 
			index = self.TopDepth
			while index <= self.BottomDepth:
				#
				#
				#     Calculate porosity depending om method 
				if self.PorEq == "Sonic":
					S = self.Son(index)
					if S > 0.0:
						Por = (S - self.SonMat(index)) * self.SonCp(index) / (self.SonFluid(index) - self.SonMat(index))
					else:
						Por = -999.0
					#      Calculate clay porosity              
					PorClay = (self.SonClay(index) - self.SonMat(index)) * self.SonCp(index) / (self.SonFluid(index) - self.SonMat(index))
				else:
					D = self.Den(index)
					if D > 0.0:
						Por = (D - self.DenMat(index)) / (self.DenFluid(index) - self.DenMat(index))
					else:
						Por = -999.0
					#      Calculate clay porosity              
					PorClay = (self.DenClay(index) - self.DenMat(index)) / (self.DenFluid(index) - self.DenMat(index))
				#     Calculate Clay volume 
				G = self.Gr(index)
				if G != -999.0:
					VClay = (G - self.GrClean(index)) / (self.GrClay(index) - self.GrClean(index))
					if VClay > 1.0:
						VClay = 1.0
					elif VClay < 0.0:
						VClay = 0.0
					#     Correct Porosity for clay 
					Por = Por - VClay * PorClay
					if Por < 0.0001:
						Por = 0.0001
				else:
					VClay = -999.0
					Por = -999.0
				#     Calculate Water Saturation
				Res = self.Rt(index)
				if (Por < 0.0) | (Res <= 0.0):
					WatSat = -999.0
					Rwa = -999.0
					BVW = -999.0
				else:
					#     Check for Shell m
					if self.Shellm:
						XX = 1.87 + 0.019 / Por
					else:
						#     set m to input parameter 
						XX = self.xm(index)
					#     Check for Archie equation  
					if self.SwEq == "Archie":
						#        calculate F
						F = self.xa(index) / math.pow(Por, XX)
						#        calculate Sw
						WatSat = math.pow(F * self.Rw(index) / Res, 1.0 / self.xn(index))
					else:
						#        calculate Sw Indonesian 
						WatSat = math.pow(math.pow(Res, 0.5) * (math.pow(VClay, (1.0 - VClay / 2.0)) / math.pow(self.Rclay(index), 0.5) + math.pow(Por, (XX / 2.0)) / math.pow(self.xa(index) * self.Rw(index), 0.5)), -2.0 / self.xn(index))
					# Limit Sw            
					if WatSat > 1.2:
						WatSat = 1.2
					# calculate Rw apparent
					Rwa = Res * math.pow(Por, XX) / self.xa(index)
					# calculate BVW
					if WatSat < 1.0:
						BVW = WatSat * Por
					else:
						BVW = Por
				#  calculate the Net pay and net reservoir
				#     Limit Sw to 1.0
				if WatSat > 1.0:
					WS = 1.0
				else:
					WS = WatSat
				if (Por >= self.PhiCut(index)) and (VClay <= self.VclCut(index)):
					ResFlg = 1.0
					if WS <= self.SwCut(index):
						PayFlg = 1.0
					else:
						PayFlg = 0.0
				else:
					ResFlg = 0.0
					PayFlg = 0.0
				#  add results to zone averages 
				if ResFlg == 1.0:
					ResCount = ResCount + 1.0
					PhiRes = PhiRes + Por
					BVWRes = BVWRes + Por * WS
					VclRes = VclRes + VClay
				if PayFlg == 1.0:
					PayCount = PayCount + 1.0
					PhiPay = PhiPay + Por
					BVWPay = BVWPay + Por * WS
					VclPay = VclPay + VClay
				# output the curve results
				self.Save_Phi(index, Por)
				self.Save_Vcl(index, VClay)
				self.Save_Sw(index, WatSat)
				self.Save_Rwapp(index, Rwa)
				self.Save_BVW(index, BVW)
				self.Save_NetResFlg(index, ResFlg)
				self.Save_NetPayFlg(index, PayFlg)
				index += 1
			#
			#
			#  Calculate Well Step from first 2 depths
			Step = self.Depth(self.TopDepth + 1) - self.Depth(self.TopDepth)
			#  Calculate the zonal averages
			ResNet = ResCount * Step
			if ResCount == 0.0:
				PhiRes = 0.0
				VclRes = 0.0
				BVWRes = 0.0
				SwRes = 0.0
			else:
				PhiRes = PhiRes / ResCount
				VclRes = VclRes / ResCount
				BVWRes = BVWRes / ResCount
				SwRes = BVWRes / PhiRes
			PayNet = PayCount * Step
			if PayCount == 0.0:
				PhiPay = 0.0
				VclPay = 0.0
				BVWPay = 0.0
				SwPay = 0.0
			else:
				PhiPay = PhiPay / PayCount
				VclPay = VclPay / PayCount
				BVWPay = BVWPay / PayCount
				SwPay = BVWPay / PhiRes
			#
			#  Output results back to parameters
			#  We loop through all the data because it is possible that the result parameters are set as curves !
			index = self.TopDepth
			while index < self.BottomDepth:
				self.Save_NetRes(index, ResNet)
				self.Save_AvPhiRes(index, PhiRes)
				self.Save_AvVclRes(index, VclRes)
				self.Save_AvSwRes(index, SwRes)
				self.Save_NetPay(index, PayNet)
				self.Save_AvPhiPay(index, PhiPay)
				self.Save_AvVclPay(index, VclPay)
				self.Save_AvSwPay(index, SwPay)
				index += 1
			#    
			#
			# Create a report to a file if this is the last zone
			if self.ZoneNumber == self.TotalZones:
				title = "Interp Demo python Report.TXT"
				writer = open(title, "w")
				writer.write(" USER PROGRAM INTERP PARAMETERS" + os.linesep)
				writer.write(os.linesep)
				writer.write(" Well    : " + self.Well_Name + os.linesep)
				# Write well attributes using attribute name         
				writer.write(" Company : " + self.Read_Well_Attribute("Company") + os.linesep)
				writer.write(" Field   : " + self.Read_Well_Attribute("Field") + os.linesep)
				writer.write(" KB Elev : " + self.Read_Well_Attribute("KBElev") + os.linesep)
				writer.write(os.linesep)
				writer.write(" Input Curves " + os.linesep)
				writer.write("    Rt     = " + self.Rt_Name + " (" + self.Rt_Units + ")" + os.linesep)
				writer.write("    Gr     = " + self.Gr_Name + " (" + self.Gr_Units + ")" + os.linesep)
				writer.write("    Den    = " + self.Den_Name + " (" + self.Den_Units + ")" + os.linesep)
				writer.write("    Son    = " + self.Son_Name + " (" + self.Son_Units + ")" + os.linesep)
				writer.write(" Output Curve " + os.linesep)
				writer.write("    Phi    = " + self.Phi_Name + " (" + self.Phi_Units + ")" + os.linesep)
				writer.write("    Vcl    = " + self.Vcl_Name + " (" + self.Vcl_Units + ")" + os.linesep)
				writer.write("    Sw     = " + self.Sw_Name + " (" + self.Sw_Units + ")" + os.linesep)
				writer.write("    Rwapp  = " + self.Rwapp_Name + " (" + self.Rwapp_Units + ")" + os.linesep)
				writer.write("    BVW    = " + self.BVW_Name + " (" + self.BVW_Units + ")" + os.linesep)
				writer.write("    NetPay = " + self.NetPayFlg_Name + os.linesep)
				writer.write("    NetRes = " + self.NetResFlg_Name + os.linesep)
				i = 1
				
				while i <= self.TotalZones:
					# Set the zone number so we can get the parameters for each zone        
					self.SetZone(i)
					writer.write(os.linesep)
					writer.write(" Input Parameters " + os.linesep)
					writer.write("    a          = " + str(self.xa(1)) + os.linesep)
					writer.write("    m          = " + str(self.xm(1)) + os.linesep)
					writer.write("    n          = " + str(self.xn(1)) + os.linesep)
					writer.write("    Rw         = " + str(self.Rw(1)) + os.linesep)
					writer.write("    Sw Eq      = " + str(self.SwEq) + os.linesep)
					writer.write("    Son Matrix = " + str(self.SonMat(1)) + os.linesep)
					writer.write("    Son Fluid  = " + str(self.SonFluid(1)) + os.linesep)
					writer.write("    Son CP     = " + str(self.SonCp(1)) + os.linesep)
					writer.write("    Son Clay   = " + str(self.SonClay(1)) + os.linesep)
					writer.write("    Den Matrix = " + str(self.DenMat(1)) + os.linesep)
					writer.write("    Den Fluid  = " + str(self.DenFluid(1)) + os.linesep)
					writer.write("    Por Eq     = " + str(self.PorEq) + os.linesep)
					writer.write("    Den Clay   = " + str(self.DenClay(1)) + os.linesep)
					writer.write("    Gr Clean   = " + str(self.GrClean(1)) + os.linesep)
					writer.write("    Gr Clay    = " + str(self.GrClay(1)) + os.linesep)
					writer.write("    Depth Interval" + os.linesep)
					writer.write("    Top = " + str(self.Depth(self.TopDepth)) + "    Bottom = " + str(self.Depth(self.BottomDepth)) + os.linesep)
					i += 1
				writer.close()
			#
			#  Write to database who created these curves
			self.Save_Sw_Comments("Curve written by Interp Demo user program")
			self.Save_Rwapp_Comments("Curve written by Interp Demo user program")
			self.Save_Phi_Comments("Curve written by Interp Demo user program")
			self.Save_Vcl_Comments("Curve written by Interp Demo user program")
			self.Save_BVW_Comments("Curve written by Interp Demo user program")
			self.Save_NetResFlg_Comments("Curve written by Interp Demo user program")
			self.Save_NetPayFlg_Comments("Curve written by Interp Demo user program")
		except Exception:
			#Write_Well_Attribute("Location", "IP Test Location");
			#string RwString = Read_Log_Attribute("Rw", 1);
			#Write_Log_Attribute("Rw", RwString, 2);
			# show any errors
			#MessageBox.Show("Error occurred: " + e.ToString())
			raise
		finally:
			# close the report file 
			if writer != None:
				writer.close()

	#
	# 
	# Calculate the Pickett plot line end points
	#
	def CalculatePickett(self):
		#    
		#    
		# Calculate m amd Rw from end point lines
		Phi1 = self.PPphi1(-1)
		Phi2 = self.PPphi2(-1)
		Ro1 = self.PPres1(-1)
		Ro2 = self.PPres2(-1)
		if Phi1 != Phi2:
			xmc = (math.log(max(Ro1, 0.01), 10) - math.log(max(Ro2, 0.01), 10)) / (math.log(max(Phi2, 0.001), 10) - math.log(max(Phi1, 0.001), 10))
		else:
			xmc = self.xm(-1)
		Rwc = Ro1 * pow(Phi1, xmc) / self.xa(-1)
		Rwc = max(0.0001, min(Rwc, 100.0))
		#    
		#  Check to see if the values calculated are the default values
		#  If they are then assume that the pickett plot is not open and in use
		#  and therefore assume that the values to use for m and Rw are the input normal parameters
		#
		if (abs(Rwc - self.Rwpick(-1)) < 0.001) and (abs(xmc - self.Mpick(-1)) < 0.01):
			Rwc = self.Rw(-1)
			self.Save_Rwpick(-1, Rwc)
			xmc = self.xm(-1)
			self.Save_Mpick(-1, xmc)
			#   Recalculate the line using the parameter values of m and Rw and save
			Ro1 = self.xa(-1) * Rwc * pow(Phi1, -xmc)
			Ro2 = self.xa(-1) * Rwc * pow(Phi2, -xmc)
			self.Save_PPres1(-1, Ro1)
			self.Save_PPres2(-1, Ro2)
		else:
			#   New values of m and Rw save these and also the pickett defaults
			self.Save_Rw(-1, Rwc)
			self.Save_xm(-1, xmc)
			self.Save_Rwpick(-1, Rwc)
			self.Save_Mpick(-1, xmc)
