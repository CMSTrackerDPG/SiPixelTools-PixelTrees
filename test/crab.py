import os                                                                                                              
import glob                                                                                                            

from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.transferOutputs = True
config.General.transferLogs = True
#config.General.requestName = 'PixelTree_SingleMuon_2018C_Part1_RAW_v1'
config.General.requestName = 'PixelTree_SingleMuon_2018C_Part2_RAW_v1'

config.section_('JobType')
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '4pixelTree-RAW-2018.py'
config.JobType.outputFiles = ['PixelTree.root']
config.JobType.disableAutomaticOutputCollection = True
config.JobType.maxJobRuntimeMin = 3000
config.JobType.maxMemoryMB = 4000

config.section_('Data')
config.Data.inputDataset = '/SingleMuon/Run2018C-v1/RAW'
# Run2 2018C: Run 319337 to 320191
# Diff. in run num: 320191 - 319337 = 854, 854/2 = 427
# Middle run: 319337 + 427 = 319764
#config.Data.runRange = '319337-319764' # 2018C Part1
config.Data.runRange = '319765-320191' # 2018C Part2
#config.Data.runRange = '315257-316995' # only process these runs
# put slash at end of path!
#config.Data.outLFNDirBase = '/store/user/<your-location>'
#config.Data.outLFNDirBase = '/store/user/calebsmith/PixelTrees/'
config.Data.outLFNDirBase = '/store/user/caleb/PixelTrees/'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.ignoreLocality = True

# T3_US_Kansas, T2_US_Nebraska, T3_US_FNALLPC
config.section_('Site')
config.Site.storageSite = 'T3_US_FNALLPC' # or anything where you have access to
config.Site.whitelist = ['T2_DE_DESY','T2_FR_IPHC','T2_CH_CERN','T2_IT_Bari','T1_IT_*','T2_US_*']
