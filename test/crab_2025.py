import os
import glob

from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.transferOutputs = True
config.General.requestName = '2025_PixelTree_Run393071_v2'

config.section_('JobType')
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '4pixelTree-FEVT-2025.py'
config.JobType.outputFiles = ['PixelTree.root']
config.JobType.disableAutomaticOutputCollection = True
config.JobType.maxMemoryMB = 4000
# config.JobType.numCores = 8

config.section_('Data')
#config.Data.inputDBS = 'phys03'
config.Data.inputDataset = '/ExpressPhysics/Run2025C-Express-v1/FEVT'
#config.Data.lumiMask = 'goodLumis_run379530.json'
config.Data.runRange = '393071'
config.Data.outLFNDirBase = '/store/group/dpg_tracker_pixel/comm_pixel/PixelTree/2025/'
#config.Data.splitting = 'Automatic'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 5
#config.Data.publication = True

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
