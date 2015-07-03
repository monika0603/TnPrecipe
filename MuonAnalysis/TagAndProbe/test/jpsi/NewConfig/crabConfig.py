from CRABClient.UserUtilities import config
config = config()

config.section_('General')
config.General.requestName = 'TagAndProbe'
config.General.workArea = 'TnP'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'tp_from_aod_simple_MC.py'
config.JobType.outputFiles = ['tnpJpsi_MC.root']

config.section_('Data')
config.Data.inputDataset = '/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v1/AODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 1
config.Data.ignoreLocality = True
#config.Data.lumiMask = 'Cert_181530-183126_HI7TeV_PromptReco_Collisions11_JSON.txt'
config.Data.publication = False

config.section_('Site')
config.Site.storageSite = 'T2_US_Vanderbilt'