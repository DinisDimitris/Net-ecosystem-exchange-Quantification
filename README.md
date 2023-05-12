# Co2-crop-quantification

To run webapp, install dependencies in the requirements.txt , pip install -r demo/requirements.txt
Launch the app by navigating in demo and running the app.py script: python app.py

In an agroecosystem, carbon net ecosystem exchange (NEE) represents the carbon net prime productivity (NPP) (gross carbon capture minus losses resulting from plant respiration) reduced by heterotrophic respiration (carbon released from soil to atmosphere from the decomposition of soil microbes and fauna organic matter).

This project tries to quantify the net ecosystem exchange of crops under different environments (maize-soybean in cool, warm, irrigated, dryland environments).XGboost is benchmarked against the Deep Learning Gated Recurrent Unit (inspired from: https://gmd.copernicus.org/articles/15/2839/2022/gmd-15-2839-2022.html). Both models have shown to perform well when temporal data about the state of the weather as well as the planting dates. This is because Co2 fluxes are homogeneous in nature, meaning microbial processes vary over time and space. 


<p align="center">
  <img src="https://github.com/DinisDimitris/Net-ecosystem-exchange-Quantification/blob/main/kgml-results/trainlossGRUopt.png" alt="First Image" width="500px">
  <br>
  Optimizers trialled for GRU RNN.
</p>

<p align="center">
  <img src="https://github.com/DinisDimitris/Net-ecosystem-exchange-Quantification/blob/main/results/rmspropgru_pred.png" alt="Second Image" width="500px">
  <br>
  GRU model with rmsPROP opt, pre-trained on simulated data and fine-tuned on field measurements
</p>

<p align="center">
  <img src="https://github.com/DinisDimitris/Net-ecosystem-exchange-Quantification/blob/main/results/bayesian_pretrained_gridsearchfinetuned_xgbmodel.png?" alt="Second Image" width="500px">
  <br>
  Bayesian optimized XGBoost model, trained on simulated data and fine tuned with observed test performance
</p>

