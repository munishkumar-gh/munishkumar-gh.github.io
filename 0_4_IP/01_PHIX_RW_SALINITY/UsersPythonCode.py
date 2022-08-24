"""
Created on Wed Aug 12 08:55:59 2020

@author: Munish Kumar (13/08/20)
PROGRAM: RWA_SP_SALINITY_MK

The main features of this program are

1. Computation of cross-plot porosity (PHIX) from Density-Neutron logs. 
2. Calcuation of hydrocarbon corrected cross-plot porosity (PHIT_HC) if light hydrocarbons such as gas is present
3. Calcuation of apparent matrix density (RHOGM) from Density-Neutron logs
4. Calcuation of apparent formation water resistivity or RWA in ohmm
5. Calculation of apparet formation water conductivity or CWA in mhos-m
6. Determination of apparent formation water salinity (SALINITY) in ppm NaCl equivalent
7. Determination of true formation water resistivity or RW from SP
6. Determination of true formation water salinity (SALINITY_SP) in ppm NaCl equivalent

With respect to porosity the programs handles all circumstances for standard porosity logs present 
and situations where some of these are absent or not selected. These include:

1. RHOB, NPHI, DT, RT are present and selected. Under these circumstance, the program calculates the 
- Neutron cross plot porosity and Sonic porosity (PHIA) by Wyllie's or Hunt-Raymer's equation depending on 
the choice of the analyst. The cross-plot porosity is used to calculate RWA, CWA, formation Salinity and apparent 
grain density (RHOGM). If light hydrocarbons such as gas are present, the program also calculates a hydrocarbon 
corrected cross-plot porosity (PHIT_HC)

2. RHOBI,DT and RT are present but NPHI is absent or not selected. In this case a Density porosity is calculated 
from RHOB and input apparent grain density (RHOGA). A Sonic porosity(PHIA) is also calculated using either Wyllie's 
or Hunt-Raymer's equation depending on the analyst's choice. The Density porosity is used to calculate RWA and 
Salinity. 

3. RHOB is absent but DT and RT are present. Sonic porosity (PHIA) is calculated using Wyllie's or Hunt-Raymer's 
equation depending on the analyst's. The Sonic porosity is used to calculate RWA and Salinity.

4. RHOB, RT present but NPHI and DT are absent or not selected. In this case a Density porosity is calcualted 
from an input apparent grain density(RHOGA) and this in turn used to compute RWA and formation salinity.

It should be noted that the cross-plot porosity from the Density-Neutron porosity is equivalent to PHIT in water 
bearing and low GOR oil bearing sands. If RHOB or NPHI are absent, then RHOGM is treated missing.

The program also checks to see if coal or volcanics flag or both available. If they are, the output logs in the 
intervals where either lithology or both are present,are set to the following values:

PHIX = missing
PHIA = missing
PHIT_HC = missing
RWA = missing
CWA = missing
SALINITY = missing

INPUT
                                        /*
                                        /* INTERVALS ----------------------
                                        /*
       RHOFL                  G/C3      /* Fluid Density
       DTM                    US/FT     /* Clean sand matrix transit time
       DTF                    US/FT     /* Fluid transit time
       RHOBQ                  G/C3      /* Bulk Density of Quartz
       NPHIQ                  V/V       /* Neutron Porosity of Quartz
       RHOBWSH_C              G/C3      /* Bulk Density of wet Shale
       NPHIWSH_C              V/V       /* Neutron Porosity of wet Shale
       CLAY_FRACTION                    /* Clay fraction in Shale
       GRD_CLAY               G/C3      /* Grain Density of Dry Clay
       BHT                              /* Bottom Hole Temperature in deg.C
       RHOGA                  G/C3      /* Apparent Grain Density of Matrix
       TD                               /* Total Depth in TVDSS
       SBT                    DEG       /* Surface Temperature in deg C
       WD                               /* Water Depth
       RTE                              /* Rotary Table Elevation
       M                                /* Cementation Factor
       OPT_SONIC_METHOD       ALPHA*15  /* Choice of Wyllie vs Hunt-Raymer equation
       OPT_SONIC              ALPHA*16  /* Choosing to calculate sonic por vs not calculate
       OPT_TEMPLOG            ALPHA*16  /* Availability of formation temperature log
       OPT_TEMP_UNITS         ALPHA*15  /* Temperature in Celcius or Farenheight
                                        /*
                                        /* LOGS ---------------------------
                                        /*
       RHOB                   G/C3      /* Bulk Density
       DT                     US/FT     /* SLB Delta-T Comp - P & S
       RT                     OHMM      /* Deep Resistivity
       NPHI                   V/V       /* Neutron porosity
       NPHIWSH_L              V/V       /* Neutron Porosity of Wet Shale
       RHOBWSH_L              G/C3      /* Bulk Density of Wet Shale
       DEPTH                  METRES    /* Downhole depth
       FTEMP_L                DEGC      /* Formation temperature log
       FLAG_COAL                        /* Coal Flag
       FLAG_VOLC                        /* Volcanics Flag
       CF                               /* Compaction Factor

LOCAL
       m2                               /* Grad WTR-QTZ lilne
       c2                               /* Intercept WTR-QTZ line
       m3                               /* Grad QTZ-Dry Shale Line
       c3                               /* Intercept QTZ-Dry Shale Line
       m4                               /* Grad WTR-Log Point Line
       c4                               /* Intercept WTR-Log Point Line
       rhobdsh                          /* Bulk Density Dry Shale
       nphidsh                          /* Neutron Porosity Dry Shale
       phidsnd                          /* Density Porosity of Sand
       rhobwsh                          /* 
       nphiwsh                          /* 
       nphisnd                          /* Neutron Porosity of Sand
       gg                               /* Geothermal gradient calculated from BHT
       ft                               /* Formation temperature in deg C
       ftf                              /* Formation temperature in deg F
       aa                               /* Intermediate value in Hunt-Raymern Eq
       bb                               /* Intermediate value in Hunt-Raymern Eq
       cc                               /* Intermediate value in Hunt-Raymern Eq
       b1                               /* Intermediate value for PHIT_HC
       b2                               /* Intermediate value for PHIT_HC
       b3                               /* Intermediate value for PHIT_HC

OUTPUT
                                        /*
                                        /* LOGS ---------------------------
                                        /*
       SALINITY               PPM       /* Apparent Salinity
       RWA                    OHMM      /* Resistivity of Water (Apparent)
       RHOGM                  G/C3      /* Apparent Density of Matrix
       CWA                    MH/M      /* Water Conductivity (Apparent)
       PHIX                   V/V       /* Crossplot Porosity
       PHIT                   V/V       /* Total Porosity (HC Corr + Non HC Bearing)
       PHIT_HC                V/V       /* Total Porosity (Hydrocarbon Corrected)
       PHID                   V/V       /* Density Porosity
       PHIA                   V/V       /* Sonic Porosity

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
        #
        # Loop through the data one level at a time
        # TopDepth and BottomDepth are the index equivalent depths entered on the run window. 
        #
        index = self.TopDepth
        while index <= self.BottomDepth:
            # Enter user code here
            try:
                ##################################################
                ### Code to calculate RW and Salinity from SP  ###
                ##################################################
                # Setting ouput in Coal & Volcanics
                #self.ipprint("Entered Depth " + str( self.Depth(index) ))
                if (self.FLAG_COAL(index) > 0) or (self.FLAG_VOLC(index) > 0):
                    RW_SP, SALINITY_SP, PHIX, PHIA, PHIT_HC, PHIT, PHID, CWA, RWA, SALINITY, RHOGM = self.COAL_VOLC() 
                    #self.ipprint("Entered Depth " + str( self.Depth(index) ))
                else:
                    # GEOTHERMAL GRADIENT & FORMATION TEMPERATURE
                    if (self.OPT_TEMPLOG == 'AVAILABLE'):
                        FT = self.FTEMP_L(index)
                    else:
                        GG = (self.BHT(index) - self.SBT(index))/(self.TD(index) - self.WD(index) - self.RTE(index))
                        FT = ((self.Depth(index) - self.WD(index) - self.RTE(index))*GG) + self.SBT(index)
                        #self.ipprint("Entered FT " + str( FT ))

                    # Conversion of Temperature units
                    if (self.OPT_TEMP_UNITS == 'CELSIUS'):
                        FTF = (FT*9/5)+32
                    else:
                        FTF = FT
                    #self.ipprint("Entered FTF " + str( FTF ))
                    # Calculation of RMF @ 75 deg F and at Formation Temperatutre (deg F)
                    if (self.OPT_TEMP_UNITS == 'CELSIUS'):
                        TRMFF = (self.TRMF(index)*9/5)+32
                    else:
                        TRMFF = self.TRMF(index)
                    
                    RMFA = self.RMF(index)*(TRMFF+6.77)/81.77
                    RMFI = RMFA*(TRMFF+6.77)/(FTF+6.77)
                
                    # Setting the values of SP Baseline either as a constant or as a log
                    if (self.SPB_L(index) != None):
                        SPB = self.SPB_C(index)
                    else:
                        SPB = self.SPB_L(index)
                    # Calculation of RMFE
                    if (RMFA > 0.1):
                        RMFE = 0.75*RMFI
                    else:
                        RMFE = (RMFA + (0.131*10**((1/math.log10(FTF/19.9))-2)))/((10**(0.0426/math.log10(FTF/50.8))) - 0.5*RMFA)
                    
                    # Calculation of RWE
                    if (self.OPT_MUD_TYPE == 'CACL2') or (self.OPT_MUD_TYPE == 'NACL') or (self.OPT_MUD_TYPE == 'GYPSUM'):
                        RWE = RMFE * (10**((self.SP(index) - SPB)/(61+0.133*FTF)) )
                    elif (self.OPT_MUD_TYPE == 'KCL'):
                        RWE = 10**(((self.SP(index)-SPB-22)/(56+0.12*FTF)) + math.log10(RMFE))

                    # Calculation of RW
                    RW_SP = (RWE + (0.131*10**((1/math.log10(FTF/19.9))-2)))/((10**(0.0426/math.log10(FTF/50.8)))-0.5*RWE)
                    #self.ipprint("Entered RW_SP " + str( RW_SP ))

                    # Formation Water Salinity
                    SALINITY_SP = (300000/((max(0.001,RW_SP))*(FTF+6.77)-1))**1.05

                    ##################################################
                    ### Calculation of PHIX, RWA and salinity      ###
                    ##################################################
                    # Setting Value of RHOBWSH as Curve or Constant
                    if (self.RHOB(index) != None) and (self.NPHI(index) != None):
                        if (self.RHOBWSH_L(index) == None):
                            RHOBWSH = self.RHOBWSH_C
                            NPHIWSH = self.NPHIWSH_C
                        else:
                            RHOBWSH = self.RHOBWSH_L(index)
                            NPHIWSH = self.NPHIWSH_L(index)
                    
                    # Calculate apparent grain density dry shale or RHOBDSH         
                    RHOBDSH = (self.CLAY_FRACTION(index)*self.GRD_CLAY(index))+ ((1-self.CLAY_FRACTION(index))*2.65)
                    
                    if (self.DT(index) != None):    
                        DT = self.DT(index)
                        DTM = self.DTM(index)
                        DTF = self.DTF(index)
                        CF = self.CF(index)
                    # PHIX - Density-Neutron Cross-Plot Porosity, Density Porsity or Sonic Porosity           
                    if (self.RHOB(index) == None) and (self.DT(index) != None) and (self.RT(index) != None):
                        PHIA = self.SONIC_POR(DT, DTM, DTF, CF)
                        PHIX = PHIA
                        PHIT = None
                        PHID = None
                        PHIT_HC = None
                        RHOGM = None
                        # self.ipprint("Entered Loop 1 " + str( PHIA ))
                    elif (self.RHOB(index) != None) and (self.NPHI(index) == None) \
                        and (self.DT(index) != None) and (self.RT(index) != None):
                        PHID = min(1,(max(0,((self.RHOGA(index) - self.RHOB(index))/(self.RHOGA(index)-self.RHOFL(index))))))
                        PHIX = PHID
                        RHOGM = None
                        PHIT_HC = None
                        PHIT = None
                        PHIA = self.SONIC_POR(DT, DTM, DTF, CF)
                        # self.ipprint("Entered Loop 2 " + str( PHIA ))
                    elif (self.RHOB(index) != None) and (self.NPHI(index) == None) \
                        and (self.RT(index) != None):
                        PHID = min(1,(max(0,((self.RHOGA(index) - self.RHOB(index))/(self.RHOGA(index)-self.RHOFL(index))))))
                        PHIX = PHID
                        RHOGM = None
                        PHIT = None
                        PHIT_HC = None
                        PHIA = None
                        # self.ipprint("Entered Loop 3 " + str( PHID ))
                    elif (self.RHOB(index) != None) and (self.NPHI(index) != None) \
                        and (self.RT(index) != None):
                        m2 = (1-RHOBWSH)/(1-NPHIWSH)
                        c2 = 1-m2
                        NPHIDSH = (m2-1+RHOBDSH)/m2    
                        m3 = (self.RHOBQ(index) - RHOBDSH)/(self.NPHIQ(index) - NPHIDSH)
                        c3 = RHOBDSH-(m3*NPHIDSH)
                        m4 = (1-self.RHOB(index))/(1-self.NPHI(index))
                        c4 = self.RHOB(index) - (m4*self.NPHI(index))
                        RHOGM = ((c3*m4) - (m3*c4))/(m4 - m3)
                        PHIX = max(0,min(1,((RHOGM - self.RHOB(index))/(RHOGM - self.RHOFL(index)))))
                        PHID = max(0, min(1,(self.RHOGA(index)-self.RHOB(index))/(self.RHOGA(index)-self.RHOFL(index))))
                        PHIA = self.SONIC_POR(DT, DTM, DTF, CF)
                        # self.ipprint("Entered Loop 4 " + str( RHOGM ))

                    # Total Porosity in the presence of light hydrocarbons
                    PHIDSND = (self.RHOBQ(index) - self.RHOB(index))/(self.RHOBQ(index) - self.RHOFL(index))
                    NPHISND = self.NPHI(index) + self.NPHIQ(index)
                    B1 = 7.0- 11*NPHISND
                    B2 = abs(B1**2 + 308*PHIDSND)
                    # self.ipprint("Entered B2 " + str( B2 ))
                    B3 = math.sqrt(B2) - B1

                    # HC corrected Total Porosity
                    PHIT_HC = B3/22                          
                    PHIT_HC = (max(0,min(1,PHIT_HC)))
                    # self.ipprint("Entered PHIT_HC " + str( PHIT_HC ))
                    
                    # Combined Total Porosity - Light hydrocarb corrected + non-hydrocarb bearing Total Porosity
                    if (RHOGM < 2.64):
                        PHIT = PHIT_HC
                    else:
                        PHIT = PHIX     

                    # RWA
                    RWA = self.RT(index) * (PHIX**self.M(index))
                    if RWA == 0:
                        CWA = -999
                        SALINITY = -999
                    else:
                        CWA = 1/RWA
                        # APPARENT SALINITY
                        SALINITY = (300000/(RWA*(FTF+6.77))-1)**1.05
                        # self.ipprint("Entered SALINITY " + str( SALINITY ))            
        
                # Output the curve results
                self.Save_RW_SP(index, RW_SP)
                self.Save_SALINITY_SP(index, SALINITY_SP)
                self.Save_PHIX(index, PHIX)
                self.Save_PHIA(index, PHIA)
                self.Save_PHIT_HC(index, PHIT_HC)
                self.Save_PHIT(index, PHIT)
                self.Save_PHID(index, PHID)
                self.Save_CWA(index, CWA)
                self.Save_RWA(index, RWA)
                self.Save_SALINITY(index, SALINITY)
                self.Save_RHOGM(index, RHOGM)
                index += 1
            except Exception:
                index += 1
                continue                
            # self.ipprint("Entered Loop 7 " + str( PHIT ))

    def COAL_VOLC(self):
        RW_SP = -999
        SALINITY_SP = -999
        PHIX = 0
        PHIA = 0 
        PHIT_HC = 0
        PHIT = 0
        PHID = 0
        CWA = -999
        RWA = -999
        SALINITY = -999
        RHOGM = -999
        return RW_SP, SALINITY_SP, PHIX, PHIA, PHIT_HC, PHIT, PHID, CWA, RWA, SALINITY, RHOGM

    def SONIC_POR(self, DT, DTM, DTF, CF):
        if(self.OPT_SONIC_METHOD == 'WYLLIE'):
            PHIA = ((DT - DTM)/(DTF - DTM))/CF
            PHIA = max(0,min(1,PHIA))
        elif (self.OPT_SONIC_METHOD == 'HUNT-RAYMER'):
            aa = DTF*DT
            bb = DTM*DT-2*DTF*DT
            cc = DTF*(DT-DTM)
            PHIA = ((((-1)*(bb)) - (math.sqrt(bb**2 - 4*aa*cc)))/(2*aa))/CF
            PHIA = max(0,min(1,PHIA))
        return (PHIA)
        
    def ipprint(self, text):
        from PGL.IP.API import IntPetroAPI
        messageBoard = IntPetroAPI().GetService('PGL.IP.Services.IMessageBoard, PGL.IP.Services')
        messageBoard.Add(1, text)