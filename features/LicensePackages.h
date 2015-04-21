#ifndef _LICENSE_PACKAGES__H_
#define _LICENSE_PACKAGES__H_
#pragma once

#include "resource\AppStrings.rh"
#include "AWR_Common\License_Features.h"

/*****************************************************************************\
* Enumerate the different product types
\*****************************************************************************/
enum AWRPRODUCT
{
	awrp_NA =  0,
	awrp_MWO = 1,
	awrp_ANO = 2,
	awrp_VSS = 3,
	awrp_ADE = 4,  // When both ANO/MWO and VSS are used
	awrp_AWR = 5,  // Fake feature names AWR-xxx
};
	
/*****************************************************************************\
* Struct to group product info
\*****************************************************************************/
struct PRODUCTINFO
{
	AWRPRODUCT m_Type;
	int m_ProductNameID;

	bool IsPrimary()
	{
		return m_Type != awrp_NA? true:false;
	}

	int GetProductNameID()
	{
		return m_ProductNameID;
	}
};


/*****************************************************************************\
* Structure to group Feature info
\*****************************************************************************/
struct FEATURESET
{
	LPCTSTR FeatureName;
	unsigned char* FeatureList;
	unsigned int cFeatures;
	PRODUCTINFO& m_ProductInfo;
};



/*****************************************************************************\
* MWO 
\*****************************************************************************/
static PRODUCTINFO piMWO = 
{
	awrp_MWO,
	IDS_L_MICROWAVEOFFICE
};

static unsigned char MWO_100[] = 
{
	LicFeat_Wizards,
	LicFeat_LinearCircuit,
	LicFeat_AplacLinearSim,
	LicFeat_YieldAnalysis,
};

static unsigned char MWO_105[] = 
{
	LicFeat_Wizards,
	LicFeat_LinearCircuit,
	LicFeat_AplacLinearSim,
	LicFeat_YieldAnalysis,

	LicFeat_Layout,
	LicFeat_GDSIIImport, LicFeat_GDSIIExport,
	LicFeat_DXFImport, LicFeat_DXFExport,
	LicFeat_GerberExport,
};

static unsigned char MWO_106[] = 
{
	LicFeat_Wizards,
	LicFeat_LinearCircuit,
	LicFeat_AplacLinearSim,
	LicFeat_YieldAnalysis,

	LicFeat_Layout,
	LicFeat_iNets,
	LicFeat_GDSIIImport, LicFeat_GDSIIExport,
	LicFeat_DXFImport, LicFeat_DXFExport,
	LicFeat_GerberExport,
};

// Not on price list, for EM socket partners
static unsigned char MWO_025[] =
{
	LicFeat_EMSimulator,

	LicFeat_Layout,
	LicFeat_GDSIIImport, LicFeat_GDSIIExport,
	LicFeat_DXFImport, LicFeat_DXFExport,
	LicFeat_GerberExport,

	LicFeat_EmSight,
};

static unsigned char MWO_125[] = 
{
	LicFeat_Wizards,
	LicFeat_LinearCircuit,
	LicFeat_AplacLinearSim,
	LicFeat_EMSimulator,
	LicFeat_YieldAnalysis,

	LicFeat_Layout,
	LicFeat_GDSIIImport, LicFeat_GDSIIExport,
	LicFeat_DXFImport, LicFeat_DXFExport,
	LicFeat_GerberExport,

	LicFeat_EmSight,
};

static unsigned char MWO_126[] = 
{
	LicFeat_Wizards,
	LicFeat_LinearCircuit,
	LicFeat_AplacLinearSim,
	LicFeat_EMSimulator,
	LicFeat_YieldAnalysis,

	LicFeat_Layout,
	LicFeat_iNets,
	LicFeat_GDSIIImport, LicFeat_GDSIIExport,
	LicFeat_DXFImport, LicFeat_DXFExport,
	LicFeat_GerberExport,

	LicFeat_EmSight,
};

static unsigned char MWO_200[] = 
{
	LicFeat_Wizards,

	LicFeat_LinearCircuit,
	LicFeat_HarmonicBalance, 
	LicFeat_AplacImport,
	LicFeat_AplacLinearSim,
	LicFeat_AplacHBSim,
	LicFeat_HspiceImport,
	LicFeat_SpectreImport,

	LicFeat_YieldAnalysis,
	LicFeat_Loadpull,
};

static unsigned char MWO_205[] = 
{
	LicFeat_Wizards,

	LicFeat_LinearCircuit,
	LicFeat_HarmonicBalance, 
	LicFeat_AplacImport,
	LicFeat_AplacLinearSim,
	LicFeat_AplacHBSim,
	LicFeat_HspiceImport,
	LicFeat_SpectreImport,

	LicFeat_YieldAnalysis,
	LicFeat_Loadpull,

	LicFeat_Layout,
	LicFeat_GDSIIImport, LicFeat_GDSIIExport,
	LicFeat_DXFImport, LicFeat_DXFExport,
	LicFeat_GerberExport,
};

static unsigned char MWO_225[] = 
{
	LicFeat_Wizards,

	LicFeat_LinearCircuit,
	LicFeat_HarmonicBalance, 
	LicFeat_AplacImport,
	LicFeat_AplacLinearSim,
	LicFeat_AplacHBSim,
	LicFeat_HspiceImport,
	LicFeat_SpectreImport,
	LicFeat_EMSimulator,

	LicFeat_YieldAnalysis,
	LicFeat_Loadpull,

	LicFeat_Layout,
	LicFeat_GDSIIImport, LicFeat_GDSIIExport,
	LicFeat_DXFImport, LicFeat_DXFExport,
	LicFeat_GerberExport,

	LicFeat_EmSight,
};

static unsigned char MWO_226[] = 
{
	LicFeat_Wizards,

	LicFeat_LinearCircuit,
	LicFeat_HarmonicBalance, 
	LicFeat_AplacImport,
	LicFeat_AplacLinearSim,
	LicFeat_AplacHBSim,
	LicFeat_HspiceImport,
	LicFeat_SpectreImport,
	LicFeat_EMSimulator,

	LicFeat_YieldAnalysis,
	LicFeat_Loadpull,

	LicFeat_Layout,
	LicFeat_iNets, 
	LicFeat_GDSIIImport, LicFeat_GDSIIExport,
	LicFeat_DXFImport, LicFeat_DXFExport,
	LicFeat_GerberExport,

	LicFeat_EmSight,
};

static unsigned char MWO_228[] = 
{
	LicFeat_Wizards,

	LicFeat_LinearCircuit,
	LicFeat_HarmonicBalance, 
	LicFeat_AplacImport,
	LicFeat_AplacLinearSim,
	LicFeat_AplacHBSim,
	LicFeat_HspiceImport,
	LicFeat_SpectreImport,
	LicFeat_EMSimulator,
	
	LicFeat_YieldAnalysis,
	LicFeat_Loadpull,

	LicFeat_Layout,
	LicFeat_iNets,
	LicFeat_DRC,
	LicFeat_LVS,
	LicFeat_GDSIIImport, LicFeat_GDSIIExport,
	LicFeat_DXFImport, LicFeat_DXFExport,
	LicFeat_GerberExport,

	LicFeat_EmSight,
};

/*****************************************************************************\
* VSS 
\*****************************************************************************/
static PRODUCTINFO piVSS = 
{
	awrp_VSS,
	IDS_L_VISUALSYSTEMSIMULATOR
};

static unsigned char VSS_150[] = 
{
	LicFeat_Vss,
	LicFeat_YieldAnalysis,
	LicFeat_BdgtAnalysisToneInsp,
	LicFeat_Wizards,
};

static unsigned char VSS_250[] = 
{
	LicFeat_Vss,
	LicFeat_YieldAnalysis,
	LicFeat_BdgtAnalysisToneInsp,
	LicFeat_DataFlowSysSim,			// Complex Envelope
	LicFeat_Wizards,
};

static unsigned char VSS_350[] = 
{
	LicFeat_Vss,
	LicFeat_YieldAnalysis,
	LicFeat_BdgtAnalysisToneInsp,
	LicFeat_DataFlowSysSim,			// Complex Envelope
	LicFeat_CommsLibraries,
	LicFeat_Wizards,
};


/*****************************************************************************\
* ANO
\*****************************************************************************/
static PRODUCTINFO piANO = 
{
	awrp_ANO,
	IDS_L_ANALOGOFFICE
};

static unsigned char ANO_200[] = 
{
	LicFeat_ANO_Product,
	LicFeat_Wizards,

	LicFeat_LinearCircuit,
	LicFeat_HarmonicBalance, 
	LicFeat_AplacImport,
	LicFeat_AplacLinearSim,
	LicFeat_AplacHBSim,
	LicFeat_HspiceImport,
	LicFeat_SpectreImport,

	LicFeat_YieldAnalysis,
	LicFeat_Loadpull,
};

static unsigned char ANO_226[] = 
{
	LicFeat_ANO_Product,
	LicFeat_Wizards,

	LicFeat_LinearCircuit,
	LicFeat_HarmonicBalance, 
	LicFeat_AplacImport,
	LicFeat_AplacLinearSim,
	LicFeat_AplacHBSim,
	LicFeat_HspiceImport,
	LicFeat_SpectreImport,
	LicFeat_EMSimulator,

	LicFeat_YieldAnalysis,
	LicFeat_Loadpull,

	LicFeat_Layout,
	LicFeat_iNets, 
	LicFeat_GDSIIImport, LicFeat_GDSIIExport,
	LicFeat_DXFImport, LicFeat_DXFExport,
	LicFeat_GerberExport,

	LicFeat_ACE,
	LicFeat_EmSight,
};

// ANO_229 - Helic
static unsigned char ANO_228[] = 
{
	LicFeat_ANO_Product,
	LicFeat_Wizards,

	LicFeat_LinearCircuit,
	LicFeat_HarmonicBalance, 
	LicFeat_AplacImport,
	LicFeat_AplacLinearSim,
	LicFeat_AplacHBSim,
	LicFeat_HspiceImport,
	LicFeat_SpectreImport,
	LicFeat_EMSimulator,

	LicFeat_YieldAnalysis,
	LicFeat_Loadpull,

	LicFeat_Layout,
	LicFeat_iNets, 
	LicFeat_Route,	// (old placement?)
	LicFeat_DRC,
	LicFeat_LVS,
	LicFeat_CadenceFlow,
	LicFeat_GDSIIImport, LicFeat_GDSIIExport,
	LicFeat_DXFImport, LicFeat_DXFExport,
	LicFeat_GerberExport,

	LicFeat_ACE,	// Awr Circuit-based extraction
	LicFeat_EmSight,
};

static unsigned char ANO_229[] = 
{
	LicFeat_ANO_Product,
	LicFeat_Wizards,

	LicFeat_LinearCircuit,
	LicFeat_HarmonicBalance, 
	LicFeat_AplacImport,
	LicFeat_AplacLinearSim,
	LicFeat_AplacHBSim,
	LicFeat_HspiceImport,
	LicFeat_SpectreImport,
	LicFeat_EMSimulator,

	LicFeat_YieldAnalysis,
	LicFeat_Loadpull,

	LicFeat_Layout,
	LicFeat_iNets, 
	LicFeat_Route,	// (old placement?)
	LicFeat_DRC,
	LicFeat_LVS,
	LicFeat_CadenceFlow,
	LicFeat_GDSIIImport, LicFeat_GDSIIExport,
	LicFeat_DXFImport, LicFeat_DXFExport,
	LicFeat_GerberExport,
	
	LicFeat_ACE,	// Awr Circuit-based extraction
	LicFeat_EmSight,
	LicFeat_HelicVeloceRF,
};

/*****************************************************************************\
* Options
\*****************************************************************************/
static PRODUCTINFO notaproduct = 
{
	awrp_NA,
	IDS_L_AWRDESIGNENVIORNMENT
};

static unsigned char HSP_100[] = 
{
	LicFeat_HspiceImport,
	LicFeat_HspiceSim,
};

static unsigned char SPC_100[] = 
{
	LicFeat_SpectreImport,
	LicFeat_SpectreSim,
};

static unsigned char ADS_300[] = 
{
	LicFeat_AdsSim,
};

static unsigned char APL_050[] = 
{
	// mwo-200 bits:
	LicFeat_Wizards,
	LicFeat_LinearCircuit,
	LicFeat_HarmonicBalance, 
	LicFeat_YieldAnalysis,
	LicFeat_Loadpull,

	LicFeat_AplacImport,
	LicFeat_AplacLinearSim,
	LicFeat_AplacHBSim,
};

static unsigned char APL_100[] = 
{
	// mwo-200 bits:
	LicFeat_Wizards,
	LicFeat_LinearCircuit,
	LicFeat_HarmonicBalance, 
	LicFeat_YieldAnalysis,
	LicFeat_Loadpull,

	LicFeat_AplacImport,
	LicFeat_AplacLinearSim,
	LicFeat_AplacTransSim,

	LicFeat_APL_100,
};

static unsigned char APL_150[] = 
{
	// mwo-200 bits:
	LicFeat_Wizards,
	LicFeat_LinearCircuit,
	LicFeat_HarmonicBalance, 
	LicFeat_YieldAnalysis,
	LicFeat_Loadpull,

	LicFeat_AplacImport,
	LicFeat_AplacLinearSim,

	LicFeat_APL_150,
};

static unsigned char APL_200[] = 
{
	// mwo-200 bits:
	LicFeat_Wizards,
	LicFeat_LinearCircuit,
	LicFeat_HarmonicBalance, 
	LicFeat_YieldAnalysis,
	LicFeat_Loadpull,

	LicFeat_AplacImport,
	LicFeat_AplacLinearSim,
	LicFeat_AplacTransSim,
	LicFeat_AplacHBSim,

	LicFeat_APL_200,
};

static unsigned char APL_110[] = 
{
	LicFeat_AplacTrCoSim,
	LicFeat_AplacEnvCoSim,
};

static unsigned char OEA_100[] = 
{
	LicFeat_OeaNetAn,
};

static unsigned char CAL_100[] = 
{
	LicFeat_DRC,
	LicFeat_Calibre,
};

static unsigned char ASR_100[] = 
{
	LicFeat_DRC,
	LicFeat_Assura,
};

static unsigned char PRC_100[] = 
{
	LicFeat_DRC,
	LicFeat_PrecisionDrc,
};

static unsigned char PTD_100[] = 
{
	LicFeat_DRC,
	LicFeat_PolytedaDrc,
};

static unsigned char OPA_100[] = 
{
	LicFeat_OpenAccessIO,
};

static unsigned char RDR_100[] = 
{
	LicFeat_RadarLib,
};

static unsigned char VIP_100[] = 
{
	LicFeat_80211acLib,
};

static unsigned char VER_100[] = 
{
	LicFeat_DRC,
	LicFeat_LVS,
};

// Axiem 'front end' license that allows
// problem setup (set options, view mesh)
static unsigned char XEM_001[] = 
{
	LicFeat_EMSimulator,  // Provides the editor, extraction, etc
	LicFeat_AxiemEditor,
};

static unsigned char ANA_001[] = 
{
	LicFeat_EMSimulator,  // Provides the editor, extraction, etc
	LicFeat_EMSimulator3D,
	LicFeat_AnalystEditor,
};

static unsigned char XEM_050[] = 
{
	LicFeat_EMSimulator,  // Provides the editor, extraction, etc
	LicFeat_Axiem,
};

static unsigned char XEM_100[] = 
{
	LicFeat_EMSimulator,  // Provides the editor, extraction, etc
	LicFeat_Axiem,
	LicFeat_Axiem64,
	LicFeat_AxiemFastSlvr,
	LicFeat_AxiemMultiCore
};

static unsigned char TOK_100[] = 
{
	LicFeat_EMSimulator,  // Provides the editor, extraction, etc
	LicFeat_EMSimulator3D,
	LicFeat_Axiem,
	LicFeat_Axiem64,
	LicFeat_AxiemFastSlvr,
	LicFeat_AxiemMultiCore,
	LicFeat_Analyst
};

static unsigned char ACE_100[] = 
{
	LicFeat_ACE,
};

static unsigned char ANA_300[] = 
{
	LicFeat_EMSimulator,  // Provides the editor, extraction, etc
	LicFeat_EMSimulator3D,
	LicFeat_Analyst,
};

static unsigned char ANA_100[] = 
{
	LicFeat_EMSimulator,  // Provides the editor, extraction, etc
	LicFeat_EMSimulator3D,
	LicFeat_Analyst,
};

static unsigned char ANA_003[] = 
{
	LicFeat_EMSimulator,  // Provides the editor, extraction, etc
	LicFeat_EMSimulator3D,
	LicFeat_Analyst
};


/*****************************************************************************\
* Used for fake feature names
\*****************************************************************************/
static PRODUCTINFO piAWR = 
{
	awrp_NA,
	IDS_L_AWRCIRCUITANALYZER
};

static unsigned char AWR_000[] = 
{
	LicFeat_MaxFeature
};

/*****************************************************************************\
* For ANO/MWO and VSS combo
\*****************************************************************************/
static PRODUCTINFO piADE = 
{
	awrp_NA,
	IDS_L_AWRDESIGNENVIORNMENT
};

static unsigned char ADE_100[] = 
{
	LicFeat_MaxFeature
};


#endif // _LICENSE_PACKAGES__H_
