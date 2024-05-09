import os
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3
process = cms.Process("PIXEL", Run3)

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10

process.options = cms.untracked.PSet( 
    wantSummary = cms.untracked.bool(True) 
)

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '140X_dataRun3_Express_v3', '')

# -- Conditions
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")


# -- Input files
process.source = cms.Source("PoolSource",
    # replace with your files
    fileNames = cms.untracked.vstring(
        #dasgoclient -query="file dataset=/ExpressPhysics/Run2024C-Express-v1/FEVT run=379530 lumi=60"
        "/store/express/Run2024C/ExpressPhysics/FEVT/Express-v1/000/379/530/00000/3e8286ed-515e-4981-ab84-1c20a665b965.root"
    )
)
# -- number of events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(50)
)

# -- RecHit production
process.load("RecoLocalTracker.SiPixelRecHits.SiPixelRecHits_cfi")
# -- Trajectory producer
process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
process.TrackRefitter.src = 'generalTracks'
process.TrackRefitter.NavigationSchool = ""


process.PixelTree = cms.EDAnalyzer("PixelTree",
    verbose                      = cms.untracked.int32(0),
    rootFileName                 = cms.untracked.string("PixelTree.root"),
    associateRecoTracks = cms.bool(False),
    associateStrip = cms.bool(False),
    associatePixel = cms.bool(True),
    pixelSimLinkSrc = cms.InputTag("simSiPixelDigis"),
    stripSimLinkSrc = cms.InputTag("simSiStripDigis"),
    ROUList = cms.vstring(
        'TrackerHitsPixelBarrelLowTof', 
        'TrackerHitsPixelBarrelHighTof', 
        'TrackerHitsPixelEndcapLowTof', 
        'TrackerHitsPixelEndcapHighTof'
    ),
    globalTag                    = process.GlobalTag.globaltag,
    dumpAllEvents                = cms.untracked.int32(0),
    PrimaryVertexCollectionLabel = cms.untracked.InputTag('offlinePrimaryVertices'),
    muonCollectionLabel          = cms.untracked.InputTag('muons'),
    trajectoryInputLabel         = cms.untracked.InputTag('TrackRefitter::PIXEL'),
    trackCollectionLabel         = cms.untracked.InputTag('generalTracks'),
    pixelClusterLabel            = cms.untracked.InputTag('siPixelClusters'),
    pixelRecHitLabel             = cms.untracked.InputTag('siPixelRecHits'),
    HLTProcessName               = cms.untracked.string('HLT'),
    HLTResultsLabel              = cms.untracked.InputTag('TriggerResults::HLT'),
    L1GTReadoutRecordLabel       = cms.untracked.InputTag('gtDigis'),
    hltL1GtObjectMap             = cms.untracked.InputTag('hltL1GtObjectMap'),
    accessSimHitInfo             = cms.untracked.bool(False)
)

# -- Path
process.p = cms.Path(
    process.siPixelRecHits*
    process.TrackRefitter*
    process.PixelTree
)
