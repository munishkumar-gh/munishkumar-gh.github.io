"""
@author: Munish Kumar (17/08/20)
PROGRAM: Determin_VSH_PHIT_SWT_PERM_BV_PAY_MK
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
            # Declarations:
            GR = self.GR(index)
            GRMIN_L = self.GRMIN_L(index)
            GRMAX_L = self.GRMAX_L(index)
            GRMIN_C = self.GRMIN_C(index)
            GRMAX_C = self.GRMAX_C(index)
            
            SP = self.SP(index)
            SPB_L = self.SPB_L(index) 
            SPB_C = self.SPB_C(index) 
            RMFA = self.RMFA(index)
            RMFI = self.RMFI(index) 
            OPT_MUD_TYPE = self.OPT_MUD_TYPE
            
            RT = self.RT(index)
            RSAND_L = self.RSAND_L(index)
            RSHALE_L = self.RSHALE_L(index)
            RSAND_C = self.RSAND_C(index)
            RSHALE_C = self.RSHALE_C(index)
            
            SPSHALE_C = self.SPSHALE_C(index)
            SPSAND_C = self.SPSAND_C(index)
            SPSHALE_L = self.SPSHALE_L(index)
            SPSAND_L = self.SPSAND_L(index)
            
            RHOB = self.RHOB(index)
            NPHI = self.NPHI(index)
            RHOFL = self.RHOFL(index)
            RHOBQ = self.RHOBQ(index)
            NPHIQ = self.NPHIQ(index)
            NPHIWSH = self.NPHIWSH(index)
            RHOBWSH = self.RHOBWSH(index)
            
            OPT_VSH_CORR = self.OPT_VSH_CORR
            
            
            
            ##################################################
            ### Code to calculate RW and Salinity from SP  ###
            ##################################################
            # Setting ouput in Coal & Volcanics
            if ((self.FLAG_COAL(index) != None) and (self.FLAG_COAL(index) > 0)) \
            or ((self.FLAG_VOLC(index) != None) and (self.FLAG_VOLC(index) > 0)):
                self.COAL_VOLC() 
            self.ipprint("Entered Depth " + str( self.Depth(index) ))
            
            # GEOTHERMAL GRADIENT & FORMATION TEMPERATURE
            if (self.OPT_TEMPLOG == 'AVAILABLE'):
                FT = self.FTEMP_L(index)
            elif (self.TVD(index) < (self.WD(index) - self.RTE(index))):
                FT = self.SBT(index)
            else:
                GG = (self.BHT(index) - self.SBT(index))/(self.TD(index) - self.WD(index) - self.RTE(index))
                FT = ((self.TVD(index) - self.WD(index) - self.RTE(index))*GG) + self.SBT(index)
                #self.ipprint("Entered FT " + str( FT ))

            # Conversion of Temperature units
            if (self.OPT_TEMP_UNITS == 'CELSIUS'):
                FTF = (FT*9/5)+32
                TRMFF = (self.TRMF(index)*9/5)+32
            else:
                TRMFF = self.TRMF
                FTF = FT
            #self.ipprint("Entered FTF " + str( FTF ))
            
            # Conversion of RMF and P at Formation Temperature
            if (OPT_MUD_TYPE == 'OIL'):
                RMFI = -999
                P = 0
            else:
                RMFI = self.RMF(index)*((TRMFF+6.77)/(FTF+6.77))
                P = 0.1778*(3/(self.RMF(index)*(TRMFF+7)-1))**(1.05)
                RW_SP, SALINITY_SP = self.SAL_FROM_SP(SP, SPB_L, SPB_C, RMFA, RMFI, FTF, OPT_MUD_TYPE)

            # Calculation of RW at Formation Temperature
            if (self.OPT_RW == 'SAL_CONST'):
                SALINITY = self.FMSAL_C(index)
                RW = self.SAL_RW(SALINITY, FTF)
            elif (self.OPT_RW =='SAL_CURV'):
                SALINITY = self.FMSAL_L(index)
                RW = self.SAL_RW(SALINITY, FTF)
            elif (self.OPT_RW == 'MEASURED'):
                RW = self.RWI(index)*((self.T_RWI(index)+21.5)/(FT+21.5))
            
            # Calculate VSH
            if (self.OPT_VSH == 'GR'):
                if (self.GR(index) == None):
                    VSH = None
                else:
                    VSH_GR = self.VSH_GAPI(GR, GRMIN_L, GRMAX_L, GRMIN_C, GRMAX_C)
                    VSH_COR = self.VSH_CORR(index, OPT_VSH_CORR, VSH_GR)
                    VSH = VSH_COR
            elif (self.OPT_VSH == 'ALL'):
                    VSH_ALL = self.VSH_ALL(GR, GRMIN_L, GRMAX_L, GRMIN_C, GRMAX_C, 
                                           RT, RSAND_L, RSHALE_L, RSAND_C, RSHALE_C, 
                                           SP, SPSHALE_L, SPSAND_L, SPSHALE_C, SPSAND_C,
                                           RHOB, NPHI, RHOFL, RHOBQ, NPHIQ, NPHIWSH, RHOBWSH,
                                           )
                    VSH_COR = self.VSH_CORR(index, OPT_VSH_CORR, VSH_ALL)
                    VSH = VSH_COR
            elif (self.OPT_VSH == 'IP'):
                    VSH = self.VSH_IP(index)

                
            
            
            
            
            




            # Output the curve results
            # self.Save_RW_SP(index, RW_SP)
            # self.Save_SALINITY_SP(index, SALINITY_SP)
            # self.Save_PHIX(index, PHIX)
            # self.Save_PHIA(index, PHIA)
            # self.Save_PHIT_HC(index, PHIT_HC)
            # self.Save_PHIT(index, PHIT)
            # self.Save_PHID(index, PHID)
            # self.Save_CWA(index, CWA)
            # self.Save_RWA(index, RWA)
            # self.Save_SALINITY(index, SALINITY)
            # self.Save_RHOGM(index, RHOGM)
            index += 1
            # self.ipprint("Entered Loop 7 " + str( PHIT ))

    ######################################################
    # Output values in Coal & Volcanics
    ######################################################
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

    ######################################################
    # Determining salinity and Rw from SP 
    ######################################################    
    def SAL_FROM_SP(self, SP, SPB_L, SPB_C, RMFA, RMFI, FTF, OPT_MUD_TYPE):
        # Setting the values of SP Baseline either as a constant or as a log
        if (SPB_L != None):
            SPB = SPB_C
        else:
            SPB = SPB_L
        
        # Calculation of RMFE
        if (RMFA > 0.1):
            RMFE = 0.75*RMFI
        else:
            RMFE = (RMFA + (0.131*10**((1/math.log10(FTF/19.9))-2)))/((10**(0.0426/math.log10(FTF/50.8))) - 0.5*RMFA)
        
        # Calculation of RWE
        if (OPT_MUD_TYPE == 'CACL2') or (OPT_MUD_TYPE == 'NACL') or (OPT_MUD_TYPE == 'GYPSUM'):
            RWE = RMFE * (10**((SP - SPB)/(61+0.133*FTF)) )
        elif (OPT_MUD_TYPE == 'KCL'):
            RWE = 10**(((SP-SPB-22)/(56+0.12*FTF)) + math.log10(RMFE))
        
        # Calculation of RW
        RW_SP = (RWE + (0.131*10**((1/math.log10(FTF/19.9))-2)))/((10**(0.0426/math.log10(FTF/50.8)))-0.5*RWE)
        #self.ipprint("Entered RW_SP " + str( RW_SP ))
        
        # Formation Water Salinity
        SALINITY_SP = (300000/((max(0.001,RW_SP))*(FTF+6.77)-1))**1.05     
        return RW_SP, SALINITY_SP

    ######################################################
    # Determining salinity and Rw from SP 
    ######################################################      
    def SAL_RW(self, SALINITY, FTF):
        RW =((300000/(SALINITY**0.9524))+1)*(1/(FTF+7))
        return RW

    ######################################################
    # Determining VSH
    # 1 - Based on GR min and max
    # 2 - Uses all possible sources (SP, RES, N-D)
    ######################################################
    def VSH_GAPI (self, GR, GRMIN_L, GRMAX_L, GRMIN_C, GRMAX_C):
        if (GRMIN_L != None) or (GRMAX_L != None):
            GRMIN = GRMIN_L
            GRMAX = GRMAX_L
        else:
            GRMIN = GRMIN_C
            GRMAX = GRMAX_C
        VSH_GR = max(0,(min(1,((GR-GRMIN)/(GRMAX-GRMIN)))))
        VSH = VSH_GR
        return VSH
    
    def VSH_ALL (self,
                 GR, GRMIN_L, GRMAX_L, GRMIN_C, GRMAX_C, 
                 RT, RSAND_L, RSHALE_L, RSAND_C, RSHALE_C,
                 SP, SPSHALE_L, SPSAND_L, SPSHALE_C, SPSAND_C,
                 RHOB, NPHI, RHOFL, RHOBQ, NPHIQ,
                 NPHIWSH, RHOBWSH, FLAG_LITH
                 ):     
        VSH_GR = self.VSH_GAPI(GR, GRMIN_L, GRMAX_L, GRMIN_C, GRMAX_C)
        if (self.FLAG_LITH == 'CARBONATE'):
            VSH = VSH_GR
        else:
            if (RT != None):
                if (RSAND_L == None) or (RSHALE_L == None):
                    RSHALE = RSHALE_C
                    RSAND = RSAND_C
                else:
                    RSHALE = RSHALE_L
                    RSAND = RSAND_L
                VSH_RES = max(0,min(1,(RSHALE/RT)*((RSAND-RT)/(RSAND-RSHALE))))
            else:
                VSH_RES = -999
            
            if (SP != None):
                if (SPSHALE_L != None) or (SPSAND_L != None):
                    SPSHALE = SPSHALE_C
                    SPSAND = SPSAND_C
                else:
                    SPSHALE = SPSHALE_L
                    SPSAND = SPSAND_L
                VSH_SP = max(0,min(1,((SP-SPSAND)/(SPSHALE-SPSAND))))
            else:
                VSH_SP = -999
            
            # A geometric solution based on the N-D crossplot, and 
            # solving for the distance between the shale point (NPHI, RHOB) to 
            # the 100% Vsh point
            # Vsh = |A*NPHI + B*RHOB + C| / |A*NPHIWSH + B*RHOBWSH + C|
            # A = RHOQ - RHOFL, 
            # B = NPHIFL - NPHIMA
            # C = NPHIMA*RHOFL - RHOMA*NPHIFL            
            if (RHOB != None) and (NPHI != None):
                NPHIFL = RHOFL
                dd = (RHOBQ - RHOFL)*(NPHIFL-NPHI)
                ee = (RHOB - RHOFL)*(NPHIFL-NPHIQ)
                ff = (RHOBQ - RHOFL)*(NPHIFL - NPHIWSH)
                hh = (RHOBWSH - RHOFL)*(NPHIFL - NPHIQ)
                
                VSH_ND = max(0,min(1,((dd-ee)/(ff-hh))))
            else:
                VSH_ND = -999
                
        VSH = min(VSH_GR, VSH_SP, VSH_RES, VSH_ND)
        return VSH

    ######################################################
    # Correction to VSH
    # 1 - Steiber
    # 2 - Clavier
    # 3 - Larionov (Tertiary or Older)
    ######################################################
    def VSH_CORR(self, index, OPT_VSH_CORR, VSH):
        if (OPT_VSH_CORR == 'STEIBER'):
            VSH_COR = VSH/(3-2*VSH)
        elif (OPT_VSH_CORR == 'CLAVIER'):
            VSH_COR = 1.7-((3.38-(VSH-0.7)**2)**0.5)
        elif (OPT_VSH_CORR == 'LARIONOV_TER'):
            VSH_COR = 0.083*(2**(3.7*VSH)-1)
        elif (OPT_VSH_CORR == 'LARIONOV'):
            VSH_COR = 0.33*(2**(2*VSH)-1)
        elif (OPT_VSH_CORR == 'NONE'):
            VSH_COR = VSH
        return VSH_COR