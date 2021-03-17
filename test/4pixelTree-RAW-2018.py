import os
import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

process = cms.Process("PIXEL",Run2_2018)

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.cerr.FwkReport.reportEvery = 100
#process.MessageLogger.categories.append('HLTrigReport')
#process.MessageLogger.categories.append('L1GtTrigReport')
process.options = cms.untracked.PSet( 
    SkipEvent = cms.untracked.vstring('ProductNotFound'), wantSummary = cms.untracked.bool(True) 
)


process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '112X_dataRun2_v7', '')

# -- Conditions
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load("RecoVertex.BeamSpotProducer.BeamSpot_cfi")
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')

# -- Input files
process.source = cms.Source("PoolSource",
    #fileNames = cms.untracked.vstring("root://cms-xrd-global.cern.ch//store/data/Run2018A/SingleMuon/ALCARECO/SiPixelCalSingleMuon-ForPixelALCARECO_UL2018-v1/50000/FD38563C-89C4-FE4E-AD40-20780C903467.root")
    fileNames = cms.untracked.vstring("root://cms-xrd-global.cern.ch//store/data/Run2018C/SingleMuon/RAW/v1/000/320/065/00000/8C070B38-338E-E811-A4D1-FA163E781D28.root")
)
# -- number of events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )

#---------------------- Refitter -----------------------
process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")
process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
process.load("RecoTracker.MeasurementDet.MeasurementTrackerEventProducer_cfi") 

#process.MeasurementTrackerEvent.pixelClusterProducer = 'ALCARECOSiPixelCalSingleMuon'
#process.MeasurementTrackerEvent.stripClusterProducer = 'ALCARECOSiPixelCalSingleMuon'
#process.MeasurementTrackerEvent.inactivePixelDetectorLabels = cms.VInputTag()
#process.MeasurementTrackerEvent.inactiveStripDetectorLabels = cms.VInputTag()

#process.TrackRefitter.src = 'ALCARECOSiPixelCalSingleMuon'
#process.TrackRefitter.TrajectoryInEvent = True

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)

#-------------------------------------------------------
process.PixelTree = cms.EDAnalyzer(
    "PixelTree",
    verbose                      = cms.untracked.int32(0),
    rootFileName                 = cms.untracked.string("PixelTree.root"),
    associateRecoTracks = cms.bool(False),
    associateStrip = cms.bool(False),
    associatePixel = cms.bool(True),
    #RecHitProducer = cms.string('siStripMatchedRecHits'),
    pixelSimLinkSrc = cms.InputTag("simSiPixelDigis"),
    stripSimLinkSrc = cms.InputTag("simSiStripDigis"),
    ROUList = cms.vstring(
        'TrackerHitsPixelBarrelLowTof', 
        'TrackerHitsPixelBarrelHighTof', 
        'TrackerHitsPixelEndcapLowTof', 
        'TrackerHitsPixelEndcapHighTof'),
    #type                         = cms.untracked.string(getDataset(process.source.fileNames[0])),
    globalTag                    = process.GlobalTag.globaltag,
    dumpAllEvents                = cms.untracked.int32(0),
    PrimaryVertexCollectionLabel = cms.untracked.InputTag('offlinePrimaryVertices'),
    muonCollectionLabel          = cms.untracked.InputTag('muons'),
    trajectoryInputLabel         = cms.untracked.InputTag('TrackRefitter::PIXEL'),
    trackCollectionLabel         = cms.untracked.InputTag('generalTracks'),
    #pixelClusterLabel            = cms.untracked.InputTag('siPixelClusters'),
    pixelRecHitLabel             = cms.untracked.InputTag('siPixelRecHits'),
    HLTProcessName               = cms.untracked.string('HLT'),
    L1GTReadoutRecordLabel       = cms.untracked.InputTag('gtDigis'),
    hltL1GtObjectMap             = cms.untracked.InputTag('hltL1GtObjectMap'),
    accessSimHitInfo             = cms.untracked.bool(False),
    )

# -- Path
process.TrackRefitter_step = cms.Path(
  process.offlineBeamSpot*
  process.MeasurementTrackerEvent*
  process.TrackRefitter
)

process.PixelTree_step = cms.Path(
  process.PixelTree
)

process.schedule = cms.Schedule(
  process.raw2digi_step,
  process.L1Reco_step,
  process.reconstruction_step,
  process.TrackRefitter_step,
  process.PixelTree_step
)

