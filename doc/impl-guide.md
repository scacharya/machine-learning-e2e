# Applied Machine Learning 
## Steps for end to end machine learning project automation best practices and automation 
This document is a consolidated guide for executing machine learning projects with a focus on automation best practices learned from varying sources listed in Appendix 1. 


A Python based sample implementation of end to end machine learning project with focus on the automation and best practices is available here. The steps are based on CRISP-DM methodology(process framework)  
# Business Understanding 
*Goal is to understand the business context and get business sign off of the deliverables. By the end of business understanding phase following should be clearly documented:* 
## The business problem 
* description 
* objectives
* current solution and its shortcomings
* what are the questions that need answered? 
* assumptions and constraints 
## The solution
Assuming enough data is available, the type of solution should be identified:
* Type of data available in the batches then the analysis is of batch else online
   * if data is labeled and need to predict category -> supervised classification 
   * if data is unlabeled and need to predict category -> unsupervised clustering
   * if qty is available and predicting a value ->supervised regression
   * if qty is unavailable and predicting a value ->further processing(dimensionality reduction)
* What are the performance requirements? 
* How will the results be used 
## The data 
* data source (how to get?), authorizations 
* reliability of the source
* legal obligations
* data formats, data definition, is expertise available? 
* size: how much available vs needed?  
# Data Understanding
*Goal is a high level data understanding*
 * Plot E-R diagram and identify the level of analysis 
 * Read the data with appropriate library: pandas.read_csv or fread. 
 * Summarize the data at the level of analysis and create a single data source(file) 
 * Review data: df.info(), df.col.value_counts(), df.describe(), df.hist(), 
 * Create random train and test holdouts and set test holdout aside; use train data for modeling
      - sklearn.train_test_split(df, test_size, random_state) 
      - sklearn.model_selection.StratifiedSufflerSplit if stratification is needed
 * Summarize train holdout to learn data structure and distribution
 * Plot correlation coefficient matrix 
      - with df.corr(), review the values.
      - with pandas.plotting.scatter_matrix of only important attributes.
      - zoom in important attributes 
 * Experiment with attribute combination
 * Visualize attributes a) histogram and b)pairwise scatterplots
# Data Preparation
*goal is to prepare TIDY data set on train holdout only* 
* Start with a fresh copy of train data set 
* For supervised, separate predictor attributes and label attribute(s)
* Selection: 
      - exclude columns with high cardinality(e.g. names) and correlation(>.9), if using parametric algorithms. 
      - for non-parametric algorithms, this is not needed as they can handle complex attribute interactions. 
* Pre-processing
      - Formatting: text to number
      - Cleaning--handle following
         1. nulls
            1. get rid of null columns (drop) OR
            2. get rid of null rows (dromna)  OR
            3. impute (fill with 0, mean or median or forecast based on algorithm) (fillna(..))
            4. imputer=sklearn.impute.SimpleImputer(strategy=”median”) ; imputer.fit(df), imputer.transform(any_df)
         2. special values such as 9999999 c)missing values d) outliers that are >3x of SD. 
      - Sampling(?)
   * Transformation
      * Encoding: Text and categorical attributes needs following encoding: 
         1. sklearn.OrdinalEncoder- ok for attributes like bad, average, good, excellent
         2. sklearn.OneHotEncoder - binary attribute per category, but will create a large sparse matrix, not good for a lot of binary attributes e.g. country_code which will create attributes like country_code_us…
         3. Custom transformers 
      * Estimator
      * Feature Scaling: ML algorithms don’t perform well if the scale is different  
         1. min-max scaling (aka normalization) rescale the values between 0 and 1, sklearn.MinMaxScaler
      * Standardization: substract mean and divide bu std dev. sklearn.StandardScaler transformer for standardization 
      * Decomposition
      * Aggregation
      * Transformer 
      * Transformation pipeline: sklearn.Pipeline allows to add the imputation, scaling, standardization
         1.    15. Feature engineering
# Modeling
*goal is to pick the best performing algorithm and tune it*
* Type of problem
      * Learning types: Supervised, Unsupervised, Reinforcement learning ?
      * classification: binary, multiclass
      * regression: univariate, multivariate
      * poisson
      * learning frequency: batch or online learning?
* Tool/framework: SAS JMP , R Studio, or Python(Sagemaker, Tenserflow, Keras) 
* Pick candidate regression analysis models: 
      * Parametric- sample data is from population with a fixed set of parameters and can be modeled using probability distribution-> regression model (estimate using the method of least square) : Linear or polynomial regression, Bayesian methods. Suitable for small set of data with well defined structure and feature relationships. 
      * Non-parametric-the predictor does not take a predetermined form but constructed according to the information derived from the data. Non parametric regression requires large sample of data because the data must supply model structure and estimation. such as ensemble(Bagging, Boosting, Blending) model usually performs better, but not always so test with both ensemble and individual methods. 
* Machine learning
  * Supervised ML
  * Ensemble learning methods: used in Fraud Detection and Financial Decision Making, among others
   1. Decision Tree-Split based on some condition (hiring manager interviewing candidate based on his criteria)
   2. Bagging - Bootstrap aggregation decision based on multiple DTs through a majority voting (multiple interviewers, decision taken based on democratic voting)
   3. Random Forest - Bagging algorithm, only a subset of feature selected at random to create a collection of DTs(forest) (multiple interviewers but access only one area) 
   4. Boosting- Sequential modeling by minimizing errors from previous models while increasing (boosting) influence of high performing models (changing interview based on previous interviewer)
   5. Gradient Boosting- employ gradient descent algorithm to minimize errors (case interview to weed out less qualified candidate)
   6. XGBoost- Optimized gradient boosting algorithm. through parallel processing, tree-pruning, handling missing values and regularization to avoid overfitting/bias  
* Train multiple models on reduced (train-validation holdout) data with varying hyperparameters, save results. 
* Compare performances based on following criteria the validation holdout set and pick best performing model: 
  * AUC, F1, RMSE, Cut-off, Accuracy, precision, recall
* Test the performance again on the test holdout data set, observe if performance gets better or stays comparable. If not, repeat c d and e with different model) 
* Fine-tune hyper parameters
# Evaluation
*goal is to document the results, summarize it and provide recommendations*
* Executive summary
* Problem -what problem was solved  
* Solution- details of the solution including data, preparation, algorithms and comparisons
* Findings - list all the relevant findings, that must include answers to the question at the problem section
* Recommendations - list the recommendations that can be backed up by data and findings, list all incomplete tasks for future work
* Limitations- List all the limitations, including assumptions constraints and shortcomings, including data and models 
* Appendices- provide relevant drawings, data, references, articles etc used for the analysis project
# Deployment
*goal is to deploy into producti* on environment and make predictions on production data*
* Operationalize in produc*   31. Monitor-> 
      * biggest concern is degr* data quality which will impact accuracy -> need constant monitoring
      * availability of new/better attributes; ability to turn off and rollback
* Alert->create suitable alert for anomalous behaviors such as degrade accuracy, response, high error  
* Ability to quickly rollback to a stage of know good data or altogether turn off the algorithm. 
* Retrain->Constantly check and retrain for 
      * new attributes 
      * same attributes but different data, say a different age group becomes prevalent buyers
      * answer more specific/pointed questions 


# Appendix 1 Bibliography
1. Aurellien Geron, Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow, Concepts, Tools, and Techniques to Build Intelligent Systems, O’Reilley, 2019.
2. Lars Buitinck, et. al, API design for machine learning software: experiences from the scikit-learn project https://dtai.cs.kuleuven.be/events/lml2013/papers/lml2013_api_sklearn.pdf
3. Cross-industry standhttps://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_miningard process for data mining 
4. https://www.datanami.com/2020/01/27/an-open-source-alternative-to-aws-sagemaker/
5. https://www.featuretools.com/
