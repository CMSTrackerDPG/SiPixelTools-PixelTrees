import os                                                                                                              
import glob                                                                                                            

from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.transferOutputs = True
config.General.transferLogs = True
config.General.requestName = 'ALCARECO_2018A_PixelTrees_2021Febr_v1-NoMT'

config.section_('JobType')
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '4pixelTree-ALCARECO-NoMT.py'
config.JobType.outputFiles = ['PixelTree.root']
config.JobType.disableAutomaticOutputCollection = True
config.JobType.maxJobRuntimeMin = 3000
config.JobType.maxMemoryMB = 4000
#config.JobType.numCores = 8

config.section_('Data')
#config.Data.inputDBS = 'phys03'
config.Data.inputDataset = '/SingleMuon/Run2018A-SiPixelCalSingleMuon-ForPixelALCARECO_UL2018-v1/ALCARECO'
#config.Data.runRange = '315257-316995'
config.Data.outLFNDirBase = '/store/user/tvami/PixelTrees/'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.ignoreLocality = True


config.section_('Site')
#config.Site.storageSite = 'T3_US_FNALLPC'
config.Site.storageSite = 'T2_HU_Budapest'
config.Site.whitelist = ['T2_DE_DESY','T2_FR_IPHC','T2_CH_CERN','T2_IT_Bari','T1_IT_*','T2_US_*']

