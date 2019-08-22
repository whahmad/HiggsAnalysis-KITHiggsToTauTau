# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import re

import HiggsAnalysis.KITHiggsToTauTau.ArtusConfigs.Run2CPStudies.quantities as Run2CPQuantities

class Quantities(Run2CPQuantities.Quantities):

	def __init__(self):
		Run2CPQuantities.Quantities.__init__(self)
		# self.quantities = set()
		# quantities = {"Quantities" : set()}
		# self.quantities = set()

	def build_quantities(self, nickname, channel):

		#super(Quantities, self).build_quantities(nickname, channel)

		print "build_quantities"
		self.quantities.update(self.recoCPFinalStateQuantities())
		if channel == "GEN":
			pass
		else:
			if re.search('(DY.?JetsToLL).*(?=(Spring16|Summer16|Summer17|Fall17))', nickname):
				self.quantities.update(self.recoCPQuantities(melaQuantities=False))
		# ************ datasets(groups, samples) common across all except mm channels are all the rest
			else:
				if not channel == "MM" and re.search('(HTo.*TauTau|H2JetsToTauTau|Higgs|JJHiggs).*(?=(Spring16|Summer16|Summer17|Fall17))', nickname):
					self.quantities.update(self.recoCPQuantities(melaQuantities=True))

	@classmethod
	def recoCPFinalStateQuantities(klass, melaQuantities=True):

		s = klass.recoCPQuantities(melaQuantities)

		s += [
			"sigmaIP_1",
			"sigmaIP_2",
			"sigmaIPrPV_1",
			"sigmaIPrPV_2",
			"sigmaIPrPVBS_1",
			"sigmaIPrPVBS_2",
			"sigmaIPHel_1",
			"sigmaIPHel_2",
			"sigmaIPHelrPV_1",
			"sigmaIPHelrPV_2",
			"sigmaIPHelrPVBS_1",
			"sigmaIPHelrPVBS_2",

			"recoPhiStarCP",
			"recoPhiStarCPHel",
			"recoPhiStarCPrPV",
			"recoPhiStarCPHelrPV",
			"recoPhiStarCPrPVBS",
			"recoPhiStarCPHelrPVBS",

			"recoPhiStarCPCombrPV",
			"recoPhiStarCPCombrPVBS",
			"recoPhiStarCPCombHel",
			"recoPhiStarCPCombHelrPV",
			"recoPhiStarCPCombHelrPVBS",

			"recoPhiStarCPCombMergedrPV",
			"recoPhiStarCPCombMergedrPVBS",
			"recoPhiStarCPCombMergedHel",
			"recoPhiStarCPCombMergedHelrPV",
			"recoPhiStarCPCombMergedHelrPVBS",

			"RefHelix_1",
			"RefHelix_2",

			"helixQOverP_1",
			"helixLambda_1",
			"helixPhi_1",
			"helixDxy_1",
			"helixDsz_1",

			"helixQOverP_2",
			"helixLambda_2",
			"helixPhi_2",
			"helixDxy_2",
			"helixDsz_2",

			"IPHel_1",
			"IPHel_2",
			"IPrPV_1",
			"IPrPV_2",
			"IPrPVBS_1",
			"IPrPVBS_2",
			"IPHelrPV_1",
			"IPHelrPV_2",
			"IPHelrPVBS_1",
			"IPHelrPVBS_2",


			"helixRadius",
			"recoMagneticField",
			"recoP_SI",
			"recoV_z_SI",
			"recoOmega",
			"recoPhi1",
			"recoOprime",

			"deltaEtaGenRecoIPrPVBS_1",
			"deltaEtaGenRecoIPrPVBS_2",
			"deltaPhiGenRecoIPrPVBS_1",
			"deltaPhiGenRecoIPrPVBS_2",
			"deltaRGenRecoIPrPVBS_1",
			"deltaRGenRecoIPrPVBS_2",
			"deltaGenRecoIPrPVBS_1",
			"deltaGenRecoIPrPVBS_2",

			"deltaEtaGenRecoIPHelrPVBS_1",
			"deltaEtaGenRecoIPHelrPVBS_2",
			"deltaPhiGenRecoIPHelrPVBS_1",
			"deltaPhiGenRecoIPHelrPVBS_2",
			"deltaRGenRecoIPHelrPVBS_1",
			"deltaRGenRecoIPHelrPVBS_2",
			"deltaGenRecoIPHelrPVBS_1",
			"deltaGenRecoIPHelrPVBS_2",

			]
		return s
