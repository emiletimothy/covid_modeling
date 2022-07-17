## Group 23 - Variant Track
Goal: 
- Accurately predict future variant distributions
- Explore the relationship between vaccination rates and variant proportion distribution

Results:
- Predictions were not ideal but captured some trends
- There exists a relationship between vaccination rates and variant proportion distribution
- There is a lack of data variety in variant data
  - P.1 and B.1.351 cases were fewer than <5% of the B.1.1.7 cases which is consistently over 40% in our proportion scale
  - B.1.1.7 dominates the proportions. (B.1.427, B.1.429 were even less)
  - Data variety itself can possible be attributed to the nature of the variants in that there are more B.1.1.7 cases.  


Main Model (Located in Ensemble folder and title Final_model):
- Ensemble of LSTM RNN and VAR autoregressive model
- Ensemble1 and Ensemble 2 have different interpretations. Final Model includes all the interpretations made. 
- The final model was trained on data used from Outbreak.info for variants and Our World in Data for vaccinations

Challenges:
- Variant data scarcity
  -  Set minimum threshold of variant proportions a state needed to be considered
  -  Switched to Outbreak.info variant proportion data
  -  Reduced model complexity by reducing input features
    - For final model this was reducing time series data for LSTM to 14 days and VAR to 5-8 days.
  - Increased data by training over all the states together instead of individually by state

Other Models that were explored but less successful: 
- ARIMA
- LSTM
- SIRModels
- RandomForest
- Gaussian Process Regression

Data folder: (Data sourced from Outbreak.info, Our World In Data, CDC, GISAID, and USA today)
- Contains data that cannot be accessed from APIs or GitHub repositories.
- Vaccine Data 
  - Weekly World Data
  - Vaccination rates pulled from OWID. 
- Variant Data
  - Weekly World Data
  - Only examined the five variants of concern chosen by CDC (B.1.1.7, B.1.351, P.1, B.1.427, B.1.429)
  - USA variant proportions contained in Outbreak folder
- Some data parses were created and are in data parser folder
- In addition, crawl.py pulls latest data from outbreak.info.

Running Instructions:
- Code for all models are directly runnable as a jupyter notebook or by uploading to Google Colab, so long as the referenced web links are maintained
- Models in the Ensemble folder require that data/outbreak/outbreak_combined_us_state_data.json and data/outbreak/outbreak_us.json are uploaded to the same folder

## Data Update Commands for cs156b Data

Once you've cloned your version of this repository, run `git submode init` and `git submodule update --recursive` to pull down all of the starter data. To update the starter data, just run `git submodule update --recursive` again.

## Data citations
---------------------------------------------------------------------------
Our World In Data COVID-19 Dataset
---------------------------------------------------------------------------
https://github.com/owid/covid-19-data/tree/master/public/data
This data has been collected, aggregated, and documented by Cameron Appel, Diana Beltekian, Daniel Gavrilov, Charlie Giattino, Joe Hasell, Bobbie Macdonald, Edouard Mathieu, Esteban Ortiz-Ospina, Hannah Ritchie, Lucas Rodés-Guirao, Max Roser.

The mission of Our World in Data is to make data and research on the world's largest problems understandable and accessible. Read more about our mission.

---------------------------------------------------------------------------
outbreak.info
---------------------------------------------------------------------------
Julia L. Mullen, Ginger Tsueng, Alaa Abdel Latif, Manar Alkuzweny, Marco Cano, Emily Haag, Jerry Zhou, Mark Zeller, Nate Matteson, Kristian G. Andersen, Chunlei Wu, Andrew I. Su, Karthik Gangavarapu, Laura D. Hughes, and the Center for Viral Systems Biology outbreak.info. Available online: https://outbreak.info/ (2020)
(Contained Data sourced from GISAID as well as other sources listed in resources further down)

---------------------------------------------------------------------------
GISAID
---------------------------------------------------------------------------
Elbe, S., and Buckland-Merrett, G. (2017) Data, disease and diplomacy: GISAID’s innovative contribution to global health. Global Challenges, 1:33-46. DOI:10.1002/gch2.1018  PMCID: 31565258

---------------------------------------------------------------------------
CDC
---------------------------------------------------------------------------
Variant Proportions 
- https://covid.cdc.gov/covid-data-tracker/#variant-proportions
- https://www.cdc.gov/coronavirus/2019-ncov/variants/variant-cases.html?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fcoronavirus%2F2019-ncov%2Ftransmission%2Fvariant-cases.html (Information from second link was deprecated in April)

---------------------------------------------------------------------------
USA Today
---------------------------------------------------------------------------
- COVID variant tracking that pulled data from CDC
- In April became deprecated due to changes in CDC covid variant data release.
https://github.com/USATODAY/covid-variants

---------------------------------------------------------------------------
epidemiology
---------------------------------------------------------------------------
non-U.S. data: Center for Systems Science and Engineering (CSSE) at Johns Hopkins University. <i>COVID-19 Data Repository</i>. Available online: <a href="https://github.com/CSSEGISandData/COVID-19" target="_blank">https://github.com/CSSEGISandData/COVID-19</a> (2020)

U.S. data: The New York Times. <i>Coronavirus (Covid-19) Data in the United States</i>. Available online: <a href="https://github.com/nytimes/covid-19-data" target="_blank">https://github.com/nytimes/covid-19-data</a> (2020)

testing data: The Atlantic. <i>The COVID Tracking Project</i>. Available online: <a href="https://covidtracking.com/" target="_blank">https://covidtracking.com/</a> (2020)


---------------------------------------------------------------------------
resources
---------------------------------------------------------------------------
LitCovid / PubMed: Chen Q, Allot A, Lu Z. <i>Keep up with the latest coronavirus research</i>. Nature. 2020;579(7798):193.

bioRxiv: <a href="https://www.biorxiv.org/about-biorxiv target="_blank"">How to cite a bioRxiv preprint</a>

medRxiv: <a href="https://www.medrxiv.org/about/FAQ" target="_blank">How to cite a medRxiv preprint</a>

MRC Centre for Global Infectious Disease Analysis: Imperial College London. <i>MRC Centre for Global Infectious Disease Analysis COVID-19</i>. Available online: <a href="https://www.imperial.ac.uk/mrc-global-infectious-disease-analysis/covid-19/" target="_blank">https://www.imperial.ac.uk/mrc-global-infectious-disease-analysis/covid-19/</a> (2020)

COVID-19 Literature Surveillance Team: COVID-19 Literature Surveillance Team. <i>Daily COVID-19 LST Reports</i>. Available online: <a href="https://www.covid19lst.org/reports" target="_blank">https://www.covid19lst.org/reports</a> (2020)

ClinicalTrials.gov: ClinicalTrials.gov. <i>Clinical studies related to the coronavirus disease (COVID-19)</i>. Available online: <a href="https://clinicaltrials.gov/ct2/results?cond=COVID-19" target="_blank">https://clinicaltrials.gov/ct2/results?cond=COVID-19</a> (2020)

WHO International Clinical Trials Registry Platform: <a href="https://www.who.int/ictrp/How_to_cite.pdf?ua=1" target="_blank">WHO Citation Policy</a>

Data Discovery Engine: Data Discovery Engine. <i>Data Discovery Engine Data Registry</i>. Available online: <a href="https://discovery.biothings.io/dataset" target="_blank">https://discovery.biothings.io/dataset</a> (2020)

Figshare: Figshare. <i>COVID-19 Open Research Data</i>. Available online: <a href="https://covid19.figshare.com/" target="_blank">https://covid19.figshare.com/</a> (2020)

Harvard Dataverse: <a href="https://dataverse.org/best-practices/data-citation target="_blank"">Dataverse Citation Policies</a>

ImmPort: <a href="https://www.immport.org/cite target="_blank"">Citing ImmPort</a>

The Protein Data Bank: <a href="https://www.rcsb.org/pages/policies#References target="_blank"">PDB Citation Policies</a>

Zenodo: Zenodo. <i>Coronavirus Disease Research Community - COVID-19</i>. Available online: <a href="https://zenodo.org/communities/covid-19/" target="_blank">https://zenodo.org/communities/covid-19/</a> (2020)

protocols.io: protocols.io. <i>Coronavirus Method Development Community</i>. Available online: <a href="https://www.protocols.io/groups/coronavirus-method-development-community" target="_blank">https://www.protocols.io/groups/coronavirus-method-development-community</a> (2020)


---------------------------------------------------------------------------
