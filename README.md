# Co2-crop-quantification


In an agroecosystem, carbon net ecosystem exchange (NEE) represents the carbon net prime productivity (NPP) (gross carbon capture minus losses resulting from plant respiration) reduced by heterotrophic respiration (carbon released from soil to atmosphere from the decomposition of soil microbes and fauna organic matter).

This project tries to quantify the net ecosystem exchange of crops under different environments (maize-soybean in cool, warm, irrigated, dryland environments). The project compares the performance of two models that have been shown in literature to perform well. Specifically, the tree-based model XGboost is benchmarked against the Deep Learning Gated Recurrent Unit (inspired from: https://gmd.copernicus.org/articles/15/2839/2022/gmd-15-2839-2022.html). Both models have shown to perform well when temporal data about the state of the weather as well as the planting dates. This is because Co2 fluxes are homogeneous in nature, meaning microbial processes vary over time and space. Both models have succesfully learned to predict the NEE of these agroecosystems with great accuracy: 

Bayesian optimized XGBoost model, trained on simulated data and fine tuned with observed test performance: 
![alt text](https://github.com/DinisDimitris/Net-ecosystem-exchange-Quantification/blob/main/results/HyperParamXGBNEEwith_planting_details.png?raw=true)

GRU model with 64 hidden states and 20% dropout rate pre-trained on simulated data and fine-tuned on observed data: 

![alt text](https://github.com/DinisDimitris/Net-ecosystem-exchange-Quantification/blob/main/kgml-results/fine_tune_results.png?raw=true)


Feature scores based on XGB gini-index: 

![alt text](https://github.com/DinisDimitris/Net-ecosystem-exchange-Quantification/blob/main/results/featureImpBayesianpretrainedgridsearchfinetunedxgbmodelNEEwith_planting_details.png?raw=true)





