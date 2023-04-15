# Co2-crop-quantification


In an agroecosystem, carbon net ecosystem exchange (NEE) represents the carbon net prime pro-
ductivity (NPP) (gross carbon capture minus losses resulting from plant respiration) reduced by
heterotrophic respiration (carbon released from soil to atmosphere from the decomposition of soil
microbes and fauna organic matter) (30). 

If NEE is positive, that is a strong indication that the
carbon gross primary production (GPP) is greater than the ecosystem respiration (Reco), and it
can be concluded the agroecosystem is a carbon sink. 

On the other side, if NEE is negative, Reco
is stronger than GPP, meaning the agroecosystem is a carbon source.
If NEE can be estimated using information such as weather and planting data that can be mea-
sured with ease, farmers can have access to their carbon balance and check whether their farming
practices are improving or not. Companies undergoing the
environmental land management scheme shared by the UK government desire this capability,
which they can use to quantify their carbon balance so they can easily view the effects of their
land practices.

This project tries to qunatify the net ecosystem exchange of crops under different environments (maize-soybean in cool, warm, irrigated, dryland environments). The project compares the performance of two models that have been shown in literature to perform well. Specifically, the tree-based model XGboost is benchmarked against the Deep Learning Gated Recurrent Unit. Both models have shown to perform well when temporal data about the state of the weather as well as the planting dates. This is because Co2 fluxes are homogeneous in nature, meaning microbial processes vary over time and space. Both models have succesfully learned to predict the NEE of these agroecosystems with great accuracy: 


Bayesian optimized XGBoost model, trained on simulated data and fine tuned with observed test performance: 
![alt text](https://github.com/DinisDimitris/Net-ecosystem-exchange-Quantification/results/HyperParam XGBNEEwith_planting_details.png?raw=true)

GRU model with 64 hidden states and 20% dropout rate pre-trained on simulated data and fine-tuned on observed data: 

![alt text](https://github.com/DinisDimitris/Net-ecosystem-exchange-Quantification/kgml-results/fine_tune_results.png?raw=true)
