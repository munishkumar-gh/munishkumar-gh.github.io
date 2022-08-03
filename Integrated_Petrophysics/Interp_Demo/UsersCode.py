import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.IO")

from System import *
from System.Collections.Generic import *
from System.Windows.Forms import *
from System.IO import *

class IPLink:

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
						F = self.xa(index) / Math.Pow(Por, XX)
						#        calculate Sw
						WatSat = Math.Pow(F * self.Rw(index) / Res, 1.0 / self.xn(index))
					else:
						#        calculate Sw Indonesian 
						WatSat = Math.Pow(Math.Pow(Res, 0.5) * (Math.Pow(VClay, (1.0 - VClay / 2.0)) / Math.Pow(self.Rclay(index), 0.5) + Math.Pow(Por, (XX / 2.0)) / Math.Pow(self.xa(index) * self.Rw(index), 0.5)), -2.0 / self.xn(index))
					# Limit Sw            
					if WatSat > 1.2:
						WatSat = 1.2
					# calculate Rw apparent
					Rwa = Res * Math.Pow(Por, XX) / self.xa(index)
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
				writer = StreamWriter("Interp Demo c# Report.TXT")
				writer.WriteLine(" USER PROGRAM INTERP PARAMETERS")
				writer.WriteLine()
				writer.WriteLine(" Well    : " + self.Well_Name)
				# Write well attributes using attribute name         
				writer.WriteLine(" Company : " + self.Read_Well_Attribute("Company"))
				writer.WriteLine(" Field   : " + self.Read_Well_Attribute("Field"))
				writer.WriteLine(" KB Elev : " + self.Read_Well_Attribute("KBElev"))
				writer.WriteLine()
				writer.WriteLine(" Input Curves ")
				writer.WriteLine("    Rt     = " + self.Rt_Name + " (" + self.Rt_Units + ")")
				writer.WriteLine("    Gr     = " + self.Gr_Name + " (" + self.Gr_Units + ")")
				writer.WriteLine("    Den    = " + self.Den_Name + " (" + self.Den_Units + ")")
				writer.WriteLine("    Son    = " + self.Son_Name + " (" + self.Son_Units + ")")
				writer.WriteLine(" Output Curve ")
				writer.WriteLine("    Phi    = " + self.Phi_Name + " (" + self.Phi_Units + ")")
				writer.WriteLine("    Vcl    = " + self.Vcl_Name + " (" + self.Vcl_Units + ")")
				writer.WriteLine("    Sw     = " + self.Sw_Name + " (" + self.Sw_Units + ")")
				writer.WriteLine("    Rwapp  = " + self.Rwapp_Name + " (" + self.Rwapp_Units + ")")
				writer.WriteLine("    BVW    = " + self.BVW_Name + " (" + self.BVW_Units + ")")
				writer.WriteLine("    NetPay = " + self.NetPayFlg_Name)
				writer.WriteLine("    NetRes = " + self.NetResFlg_Name)
				i = 1
				
				while i <= self.TotalZones:
					# Set the zone number so we can get the parameters for each zone        
					self.SetZone(i)
					writer.WriteLine()
					writer.WriteLine(" Input Parameters ")
					writer.WriteLine("    a          = " + str(self.xa(1)))
					writer.WriteLine("    m          = " + str(self.xm(1)))
					writer.WriteLine("    n          = " + str(self.xn(1)))
					writer.WriteLine("    Rw         = " + str(self.Rw(1)))
					writer.WriteLine("    Sw Eq      = " + str(self.SwEq))
					writer.WriteLine("    Son Matrix = " + str(self.SonMat(1)))
					writer.WriteLine("    Son Fluid  = " + str(self.SonFluid(1)))
					writer.WriteLine("    Son CP     = " + str(self.SonCp(1)))
					writer.WriteLine("    Son Clay   = " + str(self.SonClay(1)))
					writer.WriteLine("    Den Matrix = " + str(self.DenMat(1)))
					writer.WriteLine("    Den Fluid  = " + str(self.DenFluid(1)))
					writer.WriteLine("    Por Eq     = " + str(self.PorEq))
					writer.WriteLine("    Den Clay   = " + str(self.DenClay(1)))
					writer.WriteLine("    Gr Clean   = " + str(self.GrClean(1)))
					writer.WriteLine("    Gr Clay    = " + str(self.GrClay(1)))
					writer.WriteLine("    Depth Interval")
					writer.WriteLine("    Top = " + str(self.Depth(self.TopDepth)) + "    Bottom = " + str(self.Depth(self.BottomDepth)))
					i += 1
			#
			#  Write to database who created these curves
			self.Save_Sw_Comments("Curve written by Interp Demo user program")
			self.Save_Rwapp_Comments("Curve written by Interp Demo user program")
			self.Save_Phi_Comments("Curve written by Interp Demo user program")
			self.Save_Vcl_Comments("Curve written by Interp Demo user program")
			self.Save_BVW_Comments("Curve written by Interp Demo user program")
			self.Save_NetResFlg_Comments("Curve written by Interp Demo user program")
			self.Save_NetPayFlg_Comments("Curve written by Interp Demo user program")
		except Exception, e:
			#Write_Well_Attribute("Location", "IP Test Location");
			#string RwString = Read_Log_Attribute("Rw", 1);
			#Write_Log_Attribute("Rw", RwString, 2);
			# show any errors
			MessageBox.Show("Error occurred: " + e.ToString())
		finally:
			# close the report file 
			if writer != None:
				writer.Flush()
				writer.Close()

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
			xmc = (Math.Log10(Math.Max(Ro1, 0.01)) - Math.Log10(Math.Max(Ro2, 0.01))) / (Math.Log10(Math.Max(Phi2, 0.001)) - Math.Log10(Math.Max(Phi1, 0.001)))
		else:
			xmc = self.xm(-1)
		Rwc = Ro1 * Math.Pow(Phi1, xmc) / self.xa(-1)
		Rwc = Math.Max(0.0001, Math.Min(Rwc, 100.0))
		#    
		#  Check to see if the values calculated are the default values
		#  If they are then assume that the pickett plot is not open and in use
		#  and therefore assume that the values to use for m and Rw are the input normal parameters
		#
		if (Math.Abs(Rwc - self.Rwpick(-1)) < 0.001) and (Math.Abs(xmc - self.Mpick(-1)) < 0.01):
			Rwc = self.Rw(-1)
			self.Save_Rwpick(-1, Rwc)
			xmc = self.xm(-1)
			self.Save_Mpick(-1, xmc)
			#   Recalculate the line using the parameter values of m and Rw and save
			Ro1 = self.xa(-1) * Rwc * Math.Pow(Phi1, -xmc)
			Ro2 = self.xa(-1) * Rwc * Math.Pow(Phi2, -xmc)
			self.Save_PPres1(-1, Ro1)
			self.Save_PPres2(-1, Ro2)
		else:
			#   New values of m and Rw save these and also the pickett defaults
			self.Save_Rw(-1, Rwc)
			self.Save_xm(-1, xmc)
			self.Save_Rwpick(-1, Rwc)
			self.Save_Mpick(-1, xmc)
