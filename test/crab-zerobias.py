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

# Automatic splitting: config.Data.splitting = 'Automatic'
# The 'maxJobRuntimeMin' parameter is not compatible with the 'Automatic' splitting mode (default).
# In case of Automatic splitting, the Data.unitsPerJob parameter must be in the [180, 2700] minutes range.
# When Data.splitting = 'Automatic', Data.unitsPerJob represents the jobs target runtime in minutes,
# and its minimum allowed value is 180 (i.e. 3 hours).

config.section_('General')
config.General.transferOutputs = True
config.General.transferLogs = True
config.General.requestName = 'PixelTree_ZeroBias_2018C_RAW_Run319313_v1'

config.section_('JobType')
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '4pixelTree-RAW-2018.py'
config.JobType.outputFiles = ['PixelTree.root']
config.JobType.disableAutomaticOutputCollection = True
config.JobType.maxJobRuntimeMin = 3000
config.JobType.maxMemoryMB = 4000

# /ZeroBias/Run2018C-v1/RAW: Run 319313 to 320393
# Diff. in run num: 320393 - 319313 = 1080

config.section_('Data')
config.Data.inputDataset = '/ZeroBias/Run2018C-v1/RAW'
#config.Data.runRange = 'XXX-YYY' # only process runs XXX to YYY inclusive
config.Data.runRange = '319313'

# Note: slash required after <CERN-username> if <output-directory> is not provided
#config.Data.outLFNDirBase = '/store/user/<CERN-username>/<output-directory>'
config.Data.outLFNDirBase = '/store/user/caleb/PixelTrees/'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.ignoreLocality = True

# Storage sites: T2_US_Nebraska, T3_US_FNALLPC
# Fermilab: T1_US_FNAL: Fermilab
# FNAL CMS LPC: T3_US_FNALLPC is up to speed, but you have to have a cmslpc account to run jobs there
# Whitelist: don't include 'T3_US_*' as many of them are not up to speed 
config.section_('Site')

# Make sure you have write access to the config.Site.storageSite that you specify 
# voms-proxy-init --valid 192:00 -voms cms
# crab checkwrite --site T2_US_Nebraska
config.Site.storageSite = 'T2_US_Nebraska'
config.Site.whitelist = ['T1_IT_*','T1_US_*','T2_DE_DESY','T2_FR_IPHC','T2_CH_CERN','T2_IT_Bari','T2_US_*']


