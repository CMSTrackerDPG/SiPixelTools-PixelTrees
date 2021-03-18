import os                                                                                                              
import glob                                                                                                            

from WMCore.Configuration import Configuration
config = Configuration()

# To submit crab jobs:
# crab submit -c <config_file>

# To check crab write permissions: 
# crab checkwrite --site <site>

# Documentation:
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile

config.section_('General')
config.General.transferOutputs = True
config.General.transferLogs = True
config.General.requestName = 'PixelTree_SingleMuon_2018C_Part1_RAW_v3'

config.section_('JobType')
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '4pixelTree-RAW-2018.py'
config.JobType.outputFiles = ['PixelTree.root']
config.JobType.disableAutomaticOutputCollection = True
config.JobType.maxJobRuntimeMin = 3000
config.JobType.maxMemoryMB = 4000

# Run2 2018C: Run 319337 to 320191
# Diff. in run num: 320191 - 319337 = 854
# Split into groups with range of 100 runs each
# Part1: Run 319337 to 319436

config.section_('Data')
config.Data.inputDataset = '/SingleMuon/Run2018C-v1/RAW'
config.Data.runRange = '319337-319436' # 2018C Part1

# slash required after <CERN-username> if <output-directory> is not provided
#config.Data.outLFNDirBase = '/store/user/<CERN-username>/<output-directory>'
config.Data.outLFNDirBase = '/store/user/caleb/PixelTrees'
#config.Data.splitting = 'FileBased'
config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.ignoreLocality = True

# Storage sites: T2_US_Nebraska, T3_US_FNALLPC
# whitelist: don't include 'T3_US_*' as many of them are not up to speed 
# T1_US_FNAL: Fermilab
# T3_US_FNALLPC is up to speed, but you have to have a cmslpc account to run jobs there
config.section_('Site')
config.Site.storageSite = 'T2_US_Nebraska' # make sure you have write access here
config.Site.whitelist = ['T1_IT_*','T1_US_*','T2_DE_DESY','T2_FR_IPHC','T2_CH_CERN','T2_IT_Bari','T2_US_*','T3_US_FNALLPC']
config.Site.ignoreGlobalBlacklist = False

