"""
@author: Munish Kumar (17/08/20)
PROGRAM: Determin_VSH_PHIT_SWT_PERM_BV_PAY_MK
"""

from Methods import Methods
from IpClassicPythonLink import IPLink
import math
import cmath

# Debugging Code
# import ptvsd

class UserApp(Methods, IPLink):

    def UserCode(self):
        # Uncomment the next two lines to enable debgugging
        # ptvsd.enable_attach(address=('127.0.0.1', 5678))
        # ptvsd.wait_for_attach() 
        #
        # Loop through the data one level at a time
        # TopDepth and BottomDepth are the index equivalent depths entered on the run window. 
        #
        index = self.TopDepth
        while index <= self.BottomDepth:
            # Enter user code here
            # Declarations:
            try:
                GR = self.GR(index)
                GRMIN = self.GRMIN_L(index)
                GRMAX = self.GRMAX_L(index)

                SP = self.SP(index)
                SPB = self.SPB_L(index) 

                RT = self.RT(index)
                RSAND = self.RSAND_L(index)
                RSHALE = self.RSHALE_L(index)

                SPSHALE = self.SPSHALE_L(index)
                SPSAND = self.SPSAND_L(index)

                RHOB = self.RHOB(index)
                NPHI = self.NPHI(index)
                RHOFL = self.RHOFL(index)
                RHOHC = self.RHOHC(index)
                RHOBQ = self.RHOBQ(index)
                NPHIQ = self.NPHIQ(index)
                NPHIWSH = self.NPHIWSH(index)
                RHOBWSH = self.RHOBWSH(index)

                RMF = self.RMF(index)
                
                OPT_MUD_TYPE = self.OPT_MUD_TYPE
                OPT_VSH_CORR = self.OPT_VSH_CORR
                FLAG_LITH = self.FLAG_LITH
                
                OPT_SONIC_METHOD = self.OPT_SONIC_METHOD
                CLAY_FRAC = self.CLAY_FRAC(index)
                GRD_CLAY = self.GRD_CLAY(index)
                
                DTCO = self.DTCO(index)
                DTM = self.DTM(index)
                DTF = self.DTF(index)
                DTSH = self.DTSH(index)
                CF = self.CF(index)
                a1 = self.a1(index) # For carbonate, 0.0055
                b1 = self.b1(index) # For carbonate, -0.2925

                A = self.A(index)
                M = self.M(index)
                N = self.N(index)
                RTSH = self.SHRT(index)

                VSHCO = self.VSHCO(index)
                FRAC_NPHI = self.FRAC_NPHI(index)
                RHOGA = self.RHOGA(index)
                OPT_RXO = self.OPT_RXO
                OPT_SW_TECH = self.OPT_SW_TECH

                V_KAO = self.V_KAO(index)
                V_CH = self.V_CH(index)
                V_SMC = self.V_SMC(index)

                Z = self.Z(index)
                RXO = self.RXO(index)

                PHIECO = self.PHIECO(index)
                SWIRR = self.SWIRR(index)
                RHOGL = self.RHOGL(index)
                RHOGU = self.RHOGU(index)

                SAND_FRAC  = self.SAND_FRAC(index)
                OPT_CLAY_SILT = self.OPT_CLAY_SILT
                PHITCO = self.PHITCO(index)
                SWTCO = self.SWTCO(index)

                #global VSH, VSH_GR, VSH_SP, VSH_RES, VSH_ND, PHIX, PHIA, PHIT_HC, PHIT, PHID_A, PHIE, RW_SP, SALINITY_SP, RW, SALINITY, RHOGM, RHOGC, SWT, SWE, SXOT, SXOE, BVW, BVWE, BVSH, BVO
                VSH= VSH_GR= VSH_SP= VSH_RES= VSH_ND= PHIX= PHIA= PHIT_HC= PHIT= PHID_A= PHIE= VCL= -999
                RW_SP= SALINITY_SP= RW= SALINITY= RHOGM= RHOGC= SWT= SWE= SXOT= SXOE= BVW= BVWE= BVSH= BVO= -999
                BVLIM= BVSAND= -999
                
                ##################################################
                ### Code to calculate RW and Salinity from SP  ###
                ##################################################
            
                # GEOTHERMAL GRADIENT & FORMATION TEMPERATURE
                if (self.OPT_TEMPLOG == 'AVAILABLE'):
                    FT = self.FTEMP_L(index)
                elif (self.TVD(index) < (self.WD(index) - self.RTE(index))):
                    FT = self.SBT(index)
                else:
                    GG = (self.BHT(index) - self.SBT(index))/(self.TVD(index) - self.WD(index) - self.RTE(index))
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
                    RMFI = RMF*((TRMFF+6.77)/(FTF+6.77))
                    P = 0.1778*(3/(RMF*(TRMFF+7)-1))**(1.05)
                    RW_SP, SALINITY_SP = self.SAL_FROM_SP(SP, SPB, RMF, RMFI, FTF, OPT_MUD_TYPE)

                # Calculation of RW at Formation Temperature
                if (self.OPT_RW == 'SAL_CONST') or (self.OPT_RW =='SAL_CURV'):
                    SALINITY = self.FMSAL_L(index)
                    RW = self.SAL_RW(SALINITY, FTF)
                elif (self.OPT_RW == 'MEASURED'):
                    RW = self.RWI(index)*((self.T_RWI(index)+21.5)/(FT+21.5))
                
                # Calculate VSH
                if (self.OPT_VSH == 'GR'):
                    if (self.GR(index) == -999):
                        VSH = -999
                        VSH_GR = -999 
                        VSH_SP = -999 
                        VSH_RES = -999 
                        VSH_ND = -999
                    else:
                        VSH_GR = self.VSH_GAPI(GR, GRMIN, GRMAX)
                        VSH_COR = self.VSH_CORR(index, OPT_VSH_CORR, VSH_GR)
                        VSH = VSH_COR
                        VSH_SP = -999 
                        VSH_RES = -999
                        VSH_ND = -999
                elif (self.OPT_VSH == 'ALL'):
                        VSH_ALL, VSH_GR, VSH_SP, VSH_RES, VSH_ND = self.VSH_ALL(GR, GRMIN, GRMAX, 
                        RT, RSAND, RSHALE, 
                        SP, SPSHALE, SPSAND,
                        RHOB, NPHI, RHOHC, RHOBQ, NPHIQ, NPHIWSH, RHOBWSH,
                        FLAG_LITH,
                        )
                        VSH_COR = self.VSH_CORR(index, OPT_VSH_CORR, VSH_ALL)
                        VSH = VSH_COR
                elif (self.OPT_VSH == 'IP'):
                        VSH = self.VSH_IP(index)
                        VSH_GR = -999 
                        VSH_SP = -999 
                        VSH_RES = -999 
                        VSH_ND = -999

                # Calculate apparent grain density of dry shale or RHOBDSH & PHIT of Shale*/
                PHISH = 0
                if (RHOB != -999):
                    RHOBDSH = (CLAY_FRAC*GRD_CLAY)+ ((1-CLAY_FRAC)*2.65)
                    PHISH = (RHOBDSH-RHOBWSH)/(RHOBDSH-RHOFL)
                elif (DTCO != -999):
                    DT=DTSH
                    PHIA = self.SONIC_POR(OPT_SONIC_METHOD, DT, DTM, DTF, CF, a1, b1)
                    PHISH = PHIA
                
                # Calculate RWB from PHISH & Archie
                #RWB = ((RTSH)*(PHISH**M))/A
                RWB = (RTSH*cmath.exp(M*cmath.log(PHISH)).real)/A

                #------------------------------------------------------------------------------------
                # Conditional checks for Porosity-Water Saturation - refer to documentation for help
                #------------------------------------------------------------------------------------
                # No porosity logs are present, or FLAG_LITH = ASH & FLAG_LITH = SALT
                if ((RHOB == -999) and (DTCO == -999) and (NPHI == -999)) or (FLAG_LITH == 'ASH') or (FLAG_LITH == 'SALT'):            
                    VSH, VSH_GR, VSH_SP, VSH_RES, VSH_ND, PHIX, PHIA, PHIT_HC, PHIT, PHID_A, PHIE, RW_SP, SALINITY_SP, RW, SALINITY, RHOGM, RHOGC, SWT, SWE, SXOT, SXOE, BVW, BVWE, BVSH, BVO, BVSAND, BVLIM = self.COAL_VOLC()
                    NPHIH = RHOBH = -999
                # No resistivity logs are present, only interpret PHIT
                elif (RT == -999):
                    #self.ipprint("Entered Loop RESDEEP -999 " + str( RT ))
                    NPHIH = RHOBH = -999     
                    SWT = SWE = SXOT = SXOE = BVW = BVWE = 0.999
                    if (RHOB == -999):
                        # PHIA out - Neutron Porosity is not used
                        if (DTCO != -999): 
                            RHOGM = RHOGC = -999        			    
                            DT = DTCO
                            PHIT = self.SONIC_POR(OPT_SONIC_METHOD, DT, DTM, DTF, CF, a1, b1)
                            VSH = VSH
                            VCL = VSH * CLAY_FRAC
                            PHIE = self.TOTAL_EFFECTIVE_SIM(VSH, VSHCO, PHIT, PHISH)
                        # Neutron Porosity is used
                        elif (NPHI != -999):
                            RHOGM = RHOGC = -999 
                            NPHISND = NPHI - NPHIQ
                            if (GR == -999):
                                PHIT = NPHISND
                                PHIE = -999
                            # Interpreting porosity using a modified 
                            # "old-style" neutron log technique - graphical solution
                            else:
                                PHIT = self.NUET_POR(NPHISND, GRMIN, GRMAX, FRAC_NPHI, GR)
                                VSH = VSH
                                VCL = VSH * CLAY_FRAC
                                PHIE = self.TOTAL_EFFECTIVE_SIM(VSH, VSHCO, PHIT, PHISH)
                        # Density porosity is used; Sonic Porosity as check
                    elif (RHOB != -999) and (NPHI == -999):
                        DT = DTCO
                        RH = RHOHC 
                        PHIT = min(0.9999,(max(0.0001,((RHOGA - RHOB)/(RHOGA-RH)))))
                        if (DT != -999):
                            PHIA = self.SONIC_POR(OPT_SONIC_METHOD, DT, DTM, DTF, CF, a1, b1)                     
                        VSH = VSH
                        VCL = VSH * CLAY_FRAC
                        PHIE = self.TOTAL_EFFECTIVE_SIM(VSH, VSHCO, PHIT, PHISH)
                        RHOGM = RHOGM
                        RHOGC = self.CLEAN_MTRX_DEN(RHOBWSH, NPHIWSH, RHOBDSH, RHOBQ, NPHIQ, RHOB, NPHI)
                        # Density-neutron porosity with Hydrocarbon corrections
                    elif (RHOB != -999) and (NPHI != -999):
                        DT = DTCO
                        if (DT != -999):
                            PHIA = self.SONIC_POR(OPT_SONIC_METHOD, DT, DTM, DTF, CF, a1, b1)
                        PHIT_HC = self.DEN_NEU_HCPOR(RHOBQ, RHOFL, RHOB, NPHI, NPHIQ)
                        RHB = RHOB
                        NPH = NPHI
                        RHOGM, PHIT = self.XPLOT_POR(FLAG_LITH, RHOGA, RHOBQ, RHB, 
                        NPH, RHOHC, RHOBWSH, NPHIWSH, RHOBDSH, NPHIQ)
                        RHOGC = self.CLEAN_MTRX_DEN(RHOBWSH, NPHIWSH, RHOBDSH, RHOBQ, NPHIQ, RHB, NPH)
                # Interpret SWT & PHIT
                else:
                    #self.ipprint("Entered Loop RESDEEP not -999 " + str( RT ))
                    if (RHOB == -999):
                        # PHIA out - Neutron Porosity is not used
                        if (DTCO != -999): 
                            RHOGM = RHOGC = -999        			    
                            DT = DTCO
                            PHIT = self.SONIC_POR(OPT_SONIC_METHOD, DT, DTM, DTF, CF, a1, b1)
                            PHIX = PHIT                   	
                            RES = RT
                            RWC = RW
                            SWB = max(0.0001,(min(0.9999,(VSH*PHISH/PHIX))))
                            # No matter which water saturation technique 
                            # is selected, conditions stated above and here 
                            # always produce an Archie solution
                            SW = self.SW_DW(OPT_SW_TECH, FLAG_LITH, PHIX, A, M, RES, RWC, RT, N, SWB, RWB, 
                            V_KAO, V_CH, V_SMC, RHOGM, RHOB, RHOFL, NPHI, NPHIQ, FTF)
                            SWTU = SW
                            SWT = min(0.9999,(max(0.0001,SWTU)))
                            if (OPT_RXO =='ABSENT') or (OPT_MUD_TYPE == 'OIL'):
                                #SXOT = SWT**Z
                                SXOT = math.pow(SWT, Z)
                            else:
                                RES = RXO
                                RWC = RMFI
                                SW = self.SW_DW(OPT_SW_TECH, FLAG_LITH, PHIX, A, M, RES, RWC, RT, N, SWB, RWB, 
                                V_KAO, V_CH, V_SMC, RHOGM, RHOB, RHOFL, NPHI, NPHIQ, FTF)
                                SXOT = SW
                                SXOT = min(0.9999,(max(0.0001,SXOT,SWT)))
                            RHOGM = RHOGC = -999
                            PHIE, SWT, SWE, SXOT, SXOE, BVW, BVWE, BVSH, BVO, VCL = self.TOTAL_EFFECTIVE(
                                PHIT, VSH, VSHCO, RHOGC, SWIRR, PHISH, SWT, SXOT, PHIECO, CLAY_FRAC
                                )
                        # Neutron Porosity is used
                        elif (NPHI != -999):
                            RHOGM = RHOGC = -999 
                            NPHISND = NPHI - NPHIQ
                            if (GR == -999):
                                PHIT = NPHISND
                                PHIE = -999
                            # Interpreting porosity using a modified 
                            # "old-style" neutron log technique - graphical solution
                            else:
                                PHIT = self.NUET_POR(NPHISND, GRMIN, GRMAX, FRAC_NPHI, GR)
                                PHIX = PHIT
                                # Archie Solution
                                RES = RT
                                #FORM_FACT = A*(PHIT**-M)
                                FORM_FACT = A*cmath.exp(-M*cmath.log(PHIT)).real
                                RO = min(RES,FORM_FACT*RW)
                                #SW = (RO/RT)**(1/N)
                                SW = cmath.exp((1/N)*cmath.log(RO/RT)).real
                                SWTU = SW
                                SWT = min(0.9999, max(0.0001,SWTU))
                            PHIE, SWT, SWE, SXOT, SXOE, BVW, BVWE, BVSH, BVO, VCL = self.TOTAL_EFFECTIVE(
                            PHIT, VSH, VSHCO, RHOGC, SWIRR, PHISH, SWT, SXOT, PHIECO, CLAY_FRAC
                            )
                        # Density porosity is used; Sonic Porosity as check
                    elif (RHOB != -999) and (NPHI == -999):
                        # self.ipprint("Entered Loop RHOB not -999 but NPHI -999" + str( RHOB ) + str( NPHI ))
                        DT = DTCO
                        NPHIH = -999
                        PHIT = min(0.9999,(max(0.0001,((RHOGA - RHOB)/(RHOGA-RHOFL)))))
                        if (DT != -999):
                            PHIA = self.SONIC_POR(OPT_SONIC_METHOD, DT, DTM, DTF, CF, a1, b1)
                        EXPHI = 0
                        RH = 0.9999
                        # Hydrocarbon correction based on Gaymard-Poupon
                        RHOBH = RHOB+1.07*PHIX*(1-SXOT)*((1.11-0.1*P)*RHOFL-1.15*RH)
                        PHID_A = min(0.9999,(max(0.0001,((RHOGA - RHOBH)/(RHOGA-RHOFL)))))
                        PHIXP = PHID_A
                        FLAG_COUNT = True
                        while (FLAG_COUNT == True) and (abs(PHIXP-PHIX) < 0.008):
                            RES = RT
                            RWC = RW
                            PHIX = PHIT
                            SWB = max(0.0001,(min(0.9999,(VSH*PHISH/PHIX))))
                            SW = self.SW_DW(OPT_SW_TECH, FLAG_LITH, PHIX, A, M, RES, RWC, RT, N, SWB, RWB, 
                            V_KAO, V_CH, V_SMC, RHOGM, RHOB, RHOFL, NPHI, NPHIQ, FTF)
                            SWTU = SW
                            SWT = min(0.9999, max(0.0001,SWTU))
                            if (OPT_RXO =='ABSENT') or (OPT_MUD_TYPE == 'OIL'):
                                #SXOT = SWT**Z
                                SXOT = math.pow(SWT, Z)
                            else:
                                RES = RXO
                                RWC = RMFI
                                SW = self.SW_DW(OPT_SW_TECH, FLAG_LITH, PHIX, A, M, RES, RWC, RT, N, SWB, RWB, 
                                V_KAO, V_CH, V_SMC, RHOGM, RHOB, RHOFL, NPHI, NPHIQ, FTF)
                                SXOT = SW
                                SXOT = min(0.9999,(max(0.0001,SXOT,SWT)))
                            RH = RHOHC
                            # Hydrocarbon correction based on Gaymard-Poupon
                            RHOBH = RHOB+1.07*PHIX*(1-SXOT)*((1.11-0.1*P)*RHOFL-1.15*RH)
                            PHID_A = min(0.9999,(max(0.0001,((RHOGA - RHOBH)/(RHOGA-RHOFL)))))
                            PHIXP = PHID_A
                            EXPHI = EXPHI+1
                            if (EXPHI >= 5):
                                FLAG_COUNT = False
                        PHIT = PHID_A
                        RHOGM = RHOGA
                        RHOGC = RHOGA
                        PHIE, SWT, SWE, SXOT, SXOE, BVW, BVWE, BVSH, BVO, VCL = self.TOTAL_EFFECTIVE(
                            PHIT, VSH, VSHCO, RHOGC, SWIRR, PHISH, SWT, SXOT, PHIECO, CLAY_FRAC
                            )
                    # Density-neutron porosity with Hydrocarbon corrections
                    elif (RHOB != -999) and (NPHI != -999):
                        #self.ipprint("Entered Loop RHOB-NPHI not -999 " + str( RHOB ) + str( NPHI )) 
                        DT = DTCO
                        if (DT != -999):
                            PHIA = self.SONIC_POR(OPT_SONIC_METHOD, DT, DTM, DTF, CF, a1, b1)
                            #self.ipprint("PHIA: " + str( PHIA ) + ", index: " + str( index ) + ", stage: " + str( 1 ))
                        PHIT_HC = self.DEN_NEU_HCPOR(RHOBQ, RHOFL, RHOB, NPHI, NPHIQ)
                        RHB = RHOB
                        NPH = NPHI
                        RHOGM, PHIX = self.XPLOT_POR(FLAG_LITH, RHOGA, RHOBQ, RHB, 
                        NPH, RHOFL, RHOBWSH, NPHIWSH, RHOBDSH, NPHIQ)
                        # Determination of corrected D-N logs
                        # 2 loops - inner loop does hydrocarbon correction
                        # Outer loop does Vsh correction
                        EXV=0
                        PHIXP = PHIX
                        FLAG_COUNT = True
                        while (EXV < 11):
                            EXPHI = 0
                            while (FLAG_COUNT == True) and (abs(PHIXP-PHIX) < 0.008):
                                RES = RT
                                RWC = RW
                                SWB = max(0.0001,(min(0.9999,(VSH*PHISH/PHIX))))
                                SW = self.SW_DW(OPT_SW_TECH, FLAG_LITH, PHIX, A, M, RES, RWC, RT, N, SWB, RWB, 
                                V_KAO, V_CH, V_SMC, RHOGM, RHOB, RHOFL, NPHI, NPHIQ, FTF)
                                SWTU = SW
                                SWT = min(0.9999,(max(0.0001,SWTU)))
                                if (OPT_RXO =='ABSENT') or (OPT_MUD_TYPE == 'OIL'):
                                    #SXOT =SWT**Z
                                    SXOT = math.pow(SWT, Z)        
                                else:
                                    RES = RXO
                                    RWC = RMFI
                                    SW = self.SW_DW(OPT_SW_TECH, FLAG_LITH, PHIX, A, M, RES, RWC, RT, N, SWB, RWB, 
                                    V_KAO, V_CH, V_SMC, RHOGM, RHOB, RHOFL, NPHI, NPHIQ, FTF)
                                    SXOT = SW
                                    SXOT = min(0.9999,(max(0.0001,SXOT,SWT)))
                                RH = RHOHC
                                # Hydrocarbon correction based on Gaymard-Poupon
                                RHOBH = RHOB+1.07*PHIX*(1-SXOT)*((1.11-0.1*P)*RHOFL-1.15*RH)
                                NPHIH = NPHI+(1.3*PHIX*(1-SXOT)*(RHOFL*(1-P)-1.5*RH+0.2))/(RHOFL*(1-P))
                                RHB = RHOBH
                                NPH = NPHIH
                                PHIXP=PHIX
                                RHOGM, PHIX = self.XPLOT_POR(FLAG_LITH, RHOGA, RHOBQ, RHB, 
                                NPH, RHOFL, RHOBWSH, NPHIWSH, RHOBDSH, NPHIQ)
                                EXPHI = EXPHI+1
                                if (EXPHI >= 5):
                                    FLAG_COUNT = False
                            # (Density of matrix + fluid + shale) - (shale) 
                            # Divided by volume of the (matrix +fluid) = RHOBC 
                            # i.e. signal from 100% matrix + fluid
                            # In other words, what is the signal assuming you do not have any shale
                            PHIT = PHIX
                            RHOBC = (RHOBH-VSH*RHOBWSH)/(1-VSH) 
                            NPHIC = (NPHIH-VSH*NPHIWSH)/(1-VSH)
                            RHB = RHOBC
                            NPH = NPHIC
                            RHOGC = self.CLEAN_MTRX_DEN(RHOBWSH, NPHIWSH, RHOBDSH, RHOBQ, NPHIQ, RHB, NPH)
                            if (RHOGC >= RHOGL) and (RHOGC <=RHOGU):
                                PHIE, SWT, SWE, SXOT, SXOE, BVW, BVWE, BVSH, BVO, VCL = self.TOTAL_EFFECTIVE(
                                    PHIT, VSH, VSHCO, RHOGC, SWIRR, PHISH, SWT, SXOT, PHIECO, CLAY_FRAC
                                    )
                            elif (RHOGC < RHOGL):
                                VSH = VSH-0.03
                                VSH = min(0.9999,max(0.0001,VSH))
                            else:
                                VSH = VSH+0.03
                                VSH = min(0.9999,max(0.0001,VSH))
                            VSH = max(0.0001,VSH)
                            EXV = EXV+1                            
                        RHOGC = self.CLEAN_MTRX_DEN(RHOBWSH, NPHIWSH, RHOBDSH, RHOBQ, NPHIQ, RHOB, NPHI)
                        #self.ipprint("PHIA: " + str( PHIA ) + ", index: " + str( index ) + ", stage: " + str( 2 ))
                    
                if (VSH >= 0.99):
                    PHIE = 0.001
                    SWT = SWE = SXOT = SXOE = 0.999
                
                #BVSAND = (1-PHIT)*(1-VSH)

                #SUM_TOT, BVSILT, BVLIM, BVCLAY, BVSAND = self.SSC(PHIT, OPT_CLAY_SILT, VSH, CLAY_FRAC, SAND_FRAC, FLAG_LITH, BVSAND)
                SD, RESV, PAY = self.FLAG_PAY(VSH, VSHCO, PHIT, PHITCO, SWT, SWTCO)

                # Setting output in Coal & Volcanics
                if (self.FLAG_COAL == True) or (self.FLAG_VOLC == True) or (self.FLAG_VOLC > 0) or (self.FLAG_COAL > 0):
                    VSH, VSH_GR, VSH_SP, VSH_RES, VSH_ND, PHIX, PHIA, PHIT_HC, PHIT, PHID_A, PHIE, RW_SP, SALINITY_SP, RW, SALINITY, RHOGM, RHOGC, SWT, SWE, SXOT, SXOE, BVW, BVWE, BVSH, BVO, BVSAND, BVLIM = self.COAL_VOLC()
                #self.ipprint("Entered Depth " + str( self.Depth(index) ))
                            
                # Output the curve results
                self.Save_VSH(index, VSH)
                self.Save_VSH_GR(index, VSH_GR)
                self.Save_VSH_SP(index, VSH_SP)
                self.Save_VSH_RES(index, VSH_RES)
                self.Save_VSH_ND(index, VSH_ND)
                self.Save_VCL(index, VCL)

                self.Save_RW_SP(index, RW_SP)
                self.Save_SALINITY_SP(index, SALINITY_SP)
                self.Save_RW(index, RW)
                self.Save_SALINITY(index, SALINITY)

                self.Save_PHIX(index, PHIX)
                self.Save_PHIA(index, PHIA)
                #self.ipprint("PHIA: " + str( PHIA ) + ", index: " + str( index ) + ", stage: " + str( 3 ))
                self.Save_PHIT_HC(index, PHIT_HC)
                self.Save_PHIT(index, PHIT)
                
                self.Save_NPHIH(index, NPHIH)
                self.Save_RHOBH(index, RHOBH)

                self.Save_RHOGM(index, RHOGM)
                self.Save_RHOGC(index, RHOGC)

                self.Save_SWT(index, SWT)
                self.Save_SXOT(index, SXOT)

                self.Save_PHIE(index, PHIE)
                self.Save_SWE(index, SWE)
                self.Save_SXOE(index, SXOE)

                self.Save_BVW(index, BVW)
                self.Save_BVWE(index, BVWE)
                self.Save_BVSH(index, BVSH)
                #self.Save_BVO(index, BVO)
                #self.Save_BVSAND(index, BVSAND)
                #self.Save_BVSILT(index, BVSILT)
                #self.Save_BVLIM(index, BVLIM)
                #self.Save_BVCLAY(index, BVCLAY)
                #self.Save_SUM_TOT(index, SUM_TOT)

                self.Save_SD(index, SD)
                self.Save_RESV(index, RESV)
                self.Save_PAY(index, PAY)

                index += 1
            
            except Exception:
                index += 1
                continue
            #self.ipprint("Entered Depth " + str( self.Depth(index) ))

    ######################################################
    # IP Print Statement
    ######################################################            
    def ipprint(self, text):
        from PGL.IP.API import IntPetroAPI
        messageBoard = IntPetroAPI().GetService('PGL.IP.Services.IMessageBoard, PGL.IP.Services')
        messageBoard.Add(1, text)

    ######################################################
    # Output values in Coal & Volcanics
    ######################################################
    def COAL_VOLC(self):
        VSH = VSH_GR = VSH_SP = VSH_RES = VSH_ND = -999
        PHIX = PHIA = PHIT_HC = PHIT = PHID_A = PHIE = -999
        RW_SP = SALINITY_SP = RW = SALINITY = RHOGM = RHOGC = -999
        SWT = SWE = SXOT = SXOE = -999
        BVW = BVWE = BVSH = BVO = BVSAND = BVLIM = -999
        return VSH, VSH_GR, VSH_SP, VSH_RES, VSH_ND, PHIX, PHIA, PHIT_HC, PHIT, PHID_A, PHIE, RW_SP, SALINITY_SP, RW, SALINITY, RHOGM, RHOGC, SWT, SWE, SXOT, SXOE, BVW, BVWE, BVSH, BVO, BVSAND, BVLIM

    ######################################################
    # Determining salinity and Rw from SP 
    ######################################################    
    def SAL_FROM_SP(self, SP, SPB, RMF, RMFI, FTF, OPT_MUD_TYPE):
        # Setting the values of SP Baseline either as a constant or as a log     
        # Calculation of RMFE
        if (RMF > 0.1):
            RMFE = 0.75*RMFI
        else:
            RMFE = (RMF + (0.131*10**((1/math.log10(FTF/19.9))-2)))/((10**(0.0426/math.log10(FTF/50.8))) - 0.5*RMF)
        
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
    def VSH_GAPI(self, GR, GRMIN, GRMAX):
        VSH_GR = max(0.0001,(min(0.9999,((GR-GRMIN)/(GRMAX-GRMIN)))))
        VSH = VSH_GR
        return VSH
    
    def VSH_ALL(self,
                 GR, GRMIN, GRMAX, 
                 RT, RSAND, RSHALE,
                 SP, SPSHALE, SPSAND,
                 RHOB, NPHI, RHOFL, RHOBQ, NPHIQ,
                 NPHIWSH, RHOBWSH, FLAG_LITH
                ):     
        VSH_GR = self.VSH_GAPI(GR, GRMIN, GRMAX)
        if (FLAG_LITH == 'CARBONATES'):
            VSH = VSH_GR
            VSH_RES = VSH_SP = VSH_ND = -999
        else:
            if (RT != -999) and ((RSHALE > 0) and (RSAND > 0)):
                VSH_RES = max(0.0001,min(0.9999,(RSHALE/RT)*((RSAND-RT)/(RSAND-RSHALE))))
            else:
                VSH_RES = -999
            
            if (SP != -999) and ((SPSAND > 0) and (SPSHALE > 0)):
                VSH_SP = max(0.0001,min(0.9999,((SP-SPSAND)/(SPSHALE-SPSAND))))
            else:
                VSH_SP = -999
            
            # A geometric solution based on the N-D crossplot, and 
            # solving for the distance between the shale point (NPHI, RHOB) to 
            # the 100% Vsh point
            # Vsh = |A*NPHI + B*RHOB + C| / |A*NPHIWSH + B*RHOBWSH + C|
            # A = RHOQ - RHOFL, 
            # B = NPHIFL - NPHIMA
            # C = NPHIMA*RHOFL - RHOMA*NPHIFL            
            if (RHOB != -999) and (NPHI != -999):
                NPHIFL = RHOFL
                #RHOFL = 0.9999
                dd = (RHOBQ - RHOFL)*(NPHIFL-NPHI)
                ee = (RHOB - RHOFL)*(NPHIFL-NPHIQ)
                ff = (RHOBQ - RHOFL)*(NPHIFL - NPHIWSH)
                hh = (RHOBWSH - RHOFL)*(NPHIFL - NPHIQ)
                VSH_ND = max(0.0001,min(0.9999,((dd-ee)/(ff-hh))))
                
                #NPHIFL = 1
                #RHOFL = 1
                #L = ((RHOFL-RHOBQ)/(NPHIFL-NPHIQ))*(-1)
                #B = 1
                #C = -L*NPHIQ + RHOBQ

                #J = (L*NPHIWSH + RHOBWSH - C)/(math.sqrt(L**2 + B**2))
                #I = (L*NPHI + RHOB - C)/(math.sqrt(L**2 + B**2))
              
                #VSH_ND = max(0.0001,min(0.9999,I/J))
            else:
                VSH_ND = -999
              
        VSH = min(abs(VSH_GR), abs(VSH_SP), abs(VSH_RES), abs(VSH_ND))
        return VSH, VSH_GR, VSH_SP, VSH_RES, VSH_ND

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

    ######################################################
    # Sonic
    # 1 - Wyllie
    # 2 - Hunt-Raymer-Gardner
    # 3- Regression
    ######################################################
    def SONIC_POR(self, OPT_SONIC_METHOD, DT, DTM, DTF, CF, a1, b1):
        if(OPT_SONIC_METHOD == 'WYLLIE'):
            PHIA = ((DT - DTM)/(DTF - DTM))/CF
            PHIA = max(0.0001,min(0.9999,PHIA))
        elif (OPT_SONIC_METHOD == 'HUNT-RAYMER'):
            aa = DTF*DT
            bb = DTM*DT-2*DTF*DT
            cc = DTF*(DT-DTM)
            PHIA = ((((-1)*(bb)) - (math.sqrt(bb**2 - 4*aa*cc)))/(2*aa))/CF
            PHIA = max(0.0001,min(0.9999,PHIA))
        elif (OPT_SONIC_METHOD == 'REGRESSION'):
            PHIA = a1*DT + b1
        return PHIA

    ######################################################
    # Old Sytle Gamma Neutron Porosity  
    ######################################################
    def NUET_POR(self, NPHISND, GRMIN, GRMAX, FRAC_NPHI, GR):
        NPHISND_MAX = min(0.35, max(0.2,NPHISND))
        NPHISND_MIN = min(0.01, max(0.05,NPHISND))
        B_SLOPE = (math.log10(NPHISND_MAX/NPHISND_MIN))/(GRMIN - GRMAX)
        A_INT =  NPHISND_MAX/(10**(B_SLOPE*GRMIN))
        PHIGRN = A_INT*10**(B_SLOPE*FRAC_NPHI*GR)
        return PHIGRN

    ######################################################
    # Effective Porosity  
    ######################################################
    def TOTAL_EFFECTIVE_SIM(self, VSH, VSHCO, PHIT, PHISH):
        if (VSH > VSHCO):
            PHIE = 0.001
        else:
            PHIE = max(0.001,(PHIT-(VSH*PHISH)))
        return PHIE

    ######################################################
    # Determining grain density of Shale-free Matrix
    ###################################################### 
    def CLEAN_MTRX_DEN(self, RHOBWSH, NPHIWSH, RHOBDSH, RHOBQ, NPHIQ, RHOB, NPHI):
        m2 = (1-RHOBWSH)/(1-NPHIWSH)
        c2 = 1-m2
        NPHIDSH = (m2-1+RHOBDSH)/m2
        m3 = (RHOBQ - RHOBDSH)/(NPHIQ - NPHIDSH)
        c3 = RHOBDSH-(m3*NPHIDSH)
        m4 = (1-RHOB)/(1-NPHI)
        c4 = RHOB - (m4*NPHI)
        RHOGC = ((c3*m4) - (m3*c4))/(m4 - m3)
        return RHOGC

    ######################################################
    # Determining Xplot Porosity from Density-Neutron 
    # with light hydrocarbons and not using RT
    ###################################################### 
    def DEN_NEU_HCPOR(self, RHOBQ, RHOFL, RHOB, NPHI, NPHIQ):
        PHIDSND = (RHOBQ - RHOB)/(RHOBQ-RHOFL)
        if (PHIDSND < 0):
            PHIT_HC =0.0001
        else:
            NPHISND = NPHI - NPHIQ
            B1 = 7.0 - 11*NPHISND
            B2 = B1**2 + 308*PHIDSND
            B3 = math.sqrt(B2) - B1
            PHIT_HC = B3/22
            PHIT_HC = max(0.0001, min(0.9999,PHIT_HC))
        return PHIT_HC

    ######################################################
    # Determining Xplot Porosity from Density-Neutron 
    ###################################################### 
    def XPLOT_POR(self, FLAG_LITH, RHOGA, RHOBQ, RHOB, NPHI, RHOFL, RHOBWSH, NPHIWSH, RHOBDSH, NPHIQ):
        # Carbonate
        # Warning to check RHOBQ and RHOGA
        RHB = RHOB
        NPH = NPHI
        if (FLAG_LITH == 'CARBONATES'):
            if (RHOGA != RHOBQ):
                self.ipprint("RHOGA = " + str( RHOGA ) + " is not equal to RHOBQ = " 
                + str( RHOBQ ) + ". Please make them equal to one another."
                )
            m2 = RHOGA - RHOB + NPHI*(RHOFL-RHOGA)
            if (m2 < 0):
                RHOGM = RHOGA-0.64*m2
            else:
                RHOGM = RHOGA-0.5*m2
        else:

            m2 = (1-RHOBWSH)/(1-NPHIWSH)
            c2 = 1-m2
            NPHIDSH = (m2-1+RHOBDSH)/m2
            m3 = (RHOBQ - RHOBDSH)/(NPHIQ - NPHIDSH)
            c3 = RHOBDSH-(m3*NPHIDSH)
            m4 = (1-RHB)/(1-NPH)
            c4 = RHB - (m4*NPH)
            RHOGM = ((c3*m4) - (m3*c4))/(m4 - m3)
        PHIX = max(0.0001, min(0.9999,((RHOGM - RHB)/(RHOGM - RHOFL))))
        return RHOGM, PHIX

    ######################################################
    # Dual-Water Sw using Newton's Solution
    ###################################################### 
    def SW_DW(self, OPT_SW_TECH, FLAG_LITH, PHIX, A, M, RES, RWC, RT, N, SWB, RWB,
    V_KAO, V_CH, V_SMC, RHOGM, RHOB, RHOFL, NPHI, NPHIQ, FTF
    ):
        # Carbonate
        if (OPT_SW_TECH =='ARCHIE') or (FLAG_LITH == 'CARBONATES'):
            #FORM_FACT = A*(PHIX**-M)
            FORM_FACT = A*cmath.exp(-M*cmath.log(PHIX)).real
            RO = min(RES,FORM_FACT*RWC)
            # Based on Archie Eqn, assuming 100% Sw & RO = RESD
            CWAFT = FORM_FACT/RT			
            #SW = (RO/RT)**(1/N)
            SW = cmath.exp((1/N)*cmath.log(RO/RT)).real
        elif (OPT_SW_TECH =='DUAL_WATER'):
            exsw =0
            SW = 0.9
            #g1 = ((PHIX**M)/(A*RWC))
            #g2 = ((SWB*(PHIX**M)/A)*((1/RWB)-(1/RWC)))
            g1 = cmath.exp(M*cmath.log(PHIX)).real/(A*RWC)
            g2 = ((SWB*cmath.exp(M*cmath.log(PHIX)).real/A)*((1/RWB)-(1/RWC)))
            while (exsw < 6):
                #fx1 = (g1*(SW**N)) + (g2*(SW**(N-1)))-(1/RES)
                #fx2 = (N*g1*(SW**(N-1))) + ((N-1)*g2*(SW**(N-2)))
                fx1 = (g1*cmath.exp(N*cmath.log(SW)).real) + (g2*cmath.exp((N-1)*cmath.log(SW)).real)-(1/RES)
                fx2 = (N*g1*cmath.exp((N-1)*cmath.log(SW)).real) + ((N-1)*g2*cmath.exp((N-2)*cmath.log(SW)).real)
                SWP = SW
                SW = SWP-(fx1/fx2)
                exsw = exsw + 1
        # Method is based on hybrid Waxman-Smits model - refer to description for details
        # This technique is very stringent. Needs both RHOB and NPHI present  
        # If RHOB is missing this technique cannot be used and defaults to Archies
        # If NPHI is missing this technique defaults to Dual Water
        elif (OPT_SW_TECH =='WS_DRY_CLAY'):
            if (RHOB == -999):         				
                #FORM_FACT = A*(PHIX**-M)
                FORM_FACT = A*cmath.exp(-M*cmath.log(PHIX)).real
                RO = min(RES,FORM_FACT*RWC)
                #SW = min(0.9999, max(0.0001,(RO/RT)**(1/N)))
                SW = min(0.9999, max(0.0001,cmath.exp((1/N)*cmath.log(RO/RT)).real))
            elif (NPHI == -999):    		
                exsw =0
                SW = 0.9
                #g1 = ((PHIX**M)/(A*RWC))
                #g2 = ((SWB*(PHIX**M)/A)*((1/RWB)-(1/RWC)))
                g1 = cmath.exp(M*cmath.log(PHIX)).real/(A*RWC)
                g2 = ((SWB*cmath.exp(M*cmath.log(PHIX)).real/A)*((1/RWB)-(1/RWC)))
                while (exsw < 6):
                    #fx1 = (g1*(SW**N)) + (g2*(SW**(N-1)))-(1/RES)
                    #fx2 = (N*g1*(SW**(N-1))) + ((N-1)*g2*(SW**(N-2)))
                    fx1 = (g1*cmath.exp(N*cmath.log(SW)).real) + (g2*cmath.exp((N-1)*cmath.log(SW)).real)-(1/RES)
                    fx2 = (N*g1*cmath.exp((N-1)*cmath.log(SW)).real) + ((N-1)*g2*cmath.exp((N-2)*cmath.log(SW)).real)
                    SWP = SW
                    SW = SWP-(fx1/fx2)
                    exsw = exsw + 1	
            else:				
                FTTEMP = (FTF-32)*5/9
                exsw =0
                SW = 0.9
                BMAX = (1-0.83*math.exp(-((-2.47+0.229*(math.log(FTTEMP)**2)+1311/(FTTEMP**2))**-1)/RWC))*(-9.2431+2.6146*FTTEMP**0.5)
                # Density of dry kaolinite = 2.62 g/cc, chlorite = 2.7 g/cc, smectite = 2.45 g/cc and illite = 2.68 g/cc
                RHOBDC = V_KAO*2.62 + V_CH*2.7 + V_SMC*2.45 + (1-V_KAO-V_CH-V_SMC)*2.68
                # CEC of dry kaolinite = 0.05 meq/g, chlorite = 0.1 meq/g, smectite = 1 meq/g and illite = 0.25 meq/g
                CECDC = V_KAO*0.05 + V_CH*0.1 + V_SMC*1 + (1-V_KAO-V_CH-V_SMC)*0.25
                # Hydrogen Index (~neutron porosity) of dry kaolinite = 0.37, chlorite = 0.4, smectite = 0.55 and illite = 0.25
                HIDC = V_KAO*0.37 + V_CH*0.4 + V_SMC*0.55 + (1-V_KAO-V_CH-V_SMC)*0.25
                NPHISND = NPHI - NPHIQ
                PHIDCL = (RHOGM - RHOB)/(RHOGM - RHOFL)	
                PHIDDC = (RHOGM - RHOBDC)/(RHOGM - RHOFL)
                QV = ((NPHISND - PHIDCL)/((HIDC - PHIDDC)* PHIX))* RHOBDC* CECDC 
                #g1 = ((PHIX**M)/(A*RWC))
                #g2 = BMAX*QV*((PHIX**M)/A)
                g1 = cmath.exp(M*cmath.log(PHIX)).real/(A*RWC)
                g2 = BMAX*QV*(cmath.exp(M*cmath.log(PHIX)).real/A)
                while (exsw < 6):
                    #fx1 = (g1*(SW**N)) + (g2*(SW**(N-1)))-(1/RES)
                    #fx2 = (N*g1*(SW**(N-1))) + ((N-1)*g2*(SW**(N-2)))
                    fx1 = (g1*cmath.exp(N*cmath.log(SW)).real) + (g2*cmath.exp((N-1)*cmath.log(SW)).real)-(1/RES)
                    fx2 = (N*g1*cmath.exp((N-1)*cmath.log(SW)).real) + ((N-1)*g2*cmath.exp((N-2)*cmath.log(SW)).real)
                    SWP = SW
                    SW = SWP-(fx1/fx2)
                    exsw = exsw + 1		
        return SW

    ######################################################
    # Computes a clean set of product curves, removes 
    # spikes from VSH as well
    ######################################################
    def TOTAL_EFFECTIVE(self, PHIT, VSH, VSHCO, RHOGC, SWIRR, PHISH, SWT, SXOT, PHIECO, CLAY_FRAC): 
        if (VSH > VSHCO):   
            SWT = SWE = SXOT = SXOE = 0.999
            PHIE = 0.001
            if (VSH > 0.95):
                RHOGC = -999
            RHOGC = RHOGC
        else:
            PHIE = max(0.001,(PHIT-(VSH*PHISH)))
            SWE = max(SWIRR,(1-((PHIT/PHIE)*(1-SWT))))
        
        if (SWE > SWT):
            SWE = SWT
        else:
            SWE = SWE

        SXOE = max(SWIRR,(1-((PHIT/PHIE)*(1-SXOT))))
        SXOE = min((max(SXOE,SWE)),1)
        if (SXOE > SXOT):
            SXOE = SXOT
        else:
            SXOE = SXOE

        if (VSH > (VSHCO-0.2)):
            PHIE = max(0.0001, PHIE*((VSHCO-VSH)/0.2))
            SWE = max(SWIRR, 1-((1-SWE)*((VSHCO-VSH)/0.2)))
            SWT = max(SWIRR, 1-((1-SWT)*((VSHCO-VSH)/0.2)))
            SXOE = max(SWIRR, 1-((1-SXOE)*((VSHCO-VSH)/0.2)))

        if (SWE > SWT):
            SWE = SWT
        else:
            SWE = SWE

        if (SXOE > SXOT):
            SXOE = SXOT
        else:
            SXOE = SXOE

        if (PHIE < PHIECO):
            SWT = SWE = SXOT = SXOE = 0.999
        elif (PHIE < (PHIECO+0.02)):
            SWE = max(SWIRR, 1-((1-SWE)*((PHIE-PHIECO)/0.2)))
            SXOE = max(SWIRR, 1-((1-SXOE)*((PHIE-PHIECO)/0.02)))

        if (SWE > SWT):
            SWE = SWT
        else:
            SWE=SWE

        if (SXOE > SXOT):
            SXOE = SXOT
        else:
            SXOE = SXOE

        if (PHIE == -999):
            PHIE = 0.001
        if (SWE == -999):
            SWE = 0.999
        
        #BVW = PHIT * SWT
        #BVO = PHIT - BVW
        #BVWE = PHIE * SWE
        #BVSH = (1-PHIT) * VSH
        # Currently not running well. Use Standalone Module
        BVW = BVO = BVWE = BVSH = -999
        VCL = VSH * CLAY_FRAC
        return PHIE, SWT, SWE, SXOT, SXOE, BVW, BVWE, BVSH, BVO, VCL

    ######################################################
    # Min-Max Clamp
    ######################################################
    def clamp(self, n, minn, maxn):
        return max(min(maxn, n), minn)

    ######################################################
    # Interpreting sand (carbonate) -silt-clay from VSH 
    ######################################################
    def SSC(self, PHIT, OPT_CLAY_SILT, VSH, CLAY_FRAC, SAND_FRAC, FLAG_LITH, BVSAND):
        if (OPT_CLAY_SILT == 'NO'):
            CLAY_FRAC = SAND_FRAC = 1

        MVCL = VSH*CLAY_FRAC

        if (VSH < (CLAY_FRAC + 0.1)):
            MVSD = 1 - VSH
        else:
            MVSD = 0

        BVCLAY = (1-PHIT)*MVCL
        # To fractionate the portion of sand-silt from remaining non-clay portion. 
        # A low sand fraction portions more of the non-clay matrix to silt*/
        if (VSH < 0.1):
            BVSC = self.clamp((1-PHIT)*MVSD, 0, 1)
        else:
            BVSC = self.clamp((1-PHIT)*(SAND_FRAC)*MVSD, 0, 1)

        if (FLAG_LITH == 'CLASTICS'):
            BVSAND = BVSC
            BVLIM = 0
        elif (FLAG_LITH == 'CARBONATES'):
            BVLIM = BVSC
            BVSAND = 0
        else:
            BVLIM = BVSAND = 0
            BVCLAY = 1
        
        BVSILT = 1 - (PHIT + BVSAND + BVLIM + BVCLAY)

        # Checking Condition; sum total must be 1 */
        S = BVSILT + PHIT + BVSAND + BVLIM + BVCLAY

        return S, BVSILT, BVLIM, BVCLAY, BVSAND

    ######################################################
    # Generating Pay Flags
    ######################################################
    def FLAG_PAY(self, VSH, VSHCO, PHIT, PHITCO, SWT, SWTCO):
        # Net Sand
        if (VSH < VSHCO):
            # Net Reservoir
            if (PHIT > PHITCO):
                # Net Pay
                if (SWT < SWTCO):
                    SD = RESV = PAY = 1
                else:
                    SD = RESV = 1
                    PAY = 0
            else:
                SD = 1
                RESV = PAY = 0
        else:
            SD = RESV = PAY = 0
        return SD, RESV, PAY