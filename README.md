# PixelTrees

Make pixel trees used for testing and calibration of reconstruction.


## Software setup

Prepare your working directory with CMSSW

```
export SCRAM_ARCH=slc7_amd64_gcc820
cmsrel CMSSW_11_1_4
cd CMSSW_11_1_4/src
cmsenv
git clone https://github.com/CMSTrackerDPG/SiPixelTools-PixelTrees.git SiPixelTools/PixelTrees
scram b -j 8
cd SiPixelTools/PixelTrees/test/
```
