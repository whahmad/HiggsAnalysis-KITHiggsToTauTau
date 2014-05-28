
#pragma once

#include <utility>

#include "Kappa/DataFormats/interface/Kappa.h"
#include "Artus/Utility/interface/ArtusLogging.h"

/**
   \brief Place to collect functions calculating CP quantities
   
   -Phi* : this is a variable, with which one can say, whether the considered boson is a scalar (CP even) or a pseudoscalar (CP odd)
   -Psi*CP : this is a variable, with which one can figure out, whether the have a CP-mixture or not
*/

class CPQuantities {
public:
	static std::pair<float, float> CalculatePhiPsiStar(RMDataLV tau1, RMDataLV tau2, RMDataLV pion1, RMDataLV pion2);
	static float CalculatePhi(RMDataLV boson, RMDataLV tau1, RMDataLV tau2, RMDataLV pion1, RMDataLV pion2);
	static float CalculateChargedProngEnergy(RMDataLV tau, RMDataLV chargedProng);
	static float CalculateChargedProngEnergyApprox(RMDataLV tau, RMDataLV chargedProng);
	static float CalculateThetaNuHadron(RMDataLV tau, RMDataLV nuTau, RMDataLV hadron);
	static float CalculateAlphaTauNeutrinos(RMDataLV tauM, RMDataLV nuTauM, RMDataLV tauP, RMDataLV nuTauP);
};