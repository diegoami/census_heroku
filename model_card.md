# Model Card

Model card speicification on https://arxiv.org/pdf/1810.03993.pdf

## Model Details

Developed by: Diego Amicabile
On: 18th of October 2022
Version: 5
Model Type: Histogram Gradient Boosting Classification Tree from the Scikit-Learn library.
Hyperparameters: It has been trained using a grid search, the best hyperparameters resulted to be the following ones:  
```
{'scoring': 'loss', 'min_samples_leaf': 20, 'max_leaf_nodes': 40, 'max_iter': 1000, 'max_depth': 20, 'learning_rate': 0.1, 'l2_regularization': 1}  
```

Result: The model returns a binary value meaning to represent whether income exceeds $50K/yr based on census data .
Preprocessing: The model assumes a preprocessing to conveted categorical features to one hot encoding

## Intended Use

The intended use of the model is to execute a prediction based on provided features of a family, to guess whether the family is expected to make more or less than 50k. 
It is used as the basis of a REST web service, wich given the expected features will return a result of '<=50k' or '>50k' 


## Training Data

As Traning data we use census information from https://archive.ics.uci.edu/ml/datasets/census+income.
Some preprocessing has been done for a better formatting.  Extraction was done by Barry Becker from the 1994 Census database. 
There are 35261 records in the database, of which 24720 are negative and 7841 positive. Therefore the data is somewhat skewed to income lesser than 50k.
 

## Evaluation Data

As Evaluation Data we use a subset from the full dataset, which we do not user for training, containing about 20% of the data.

## Metrics

To evaluate the model (which is binary) we use precision, recall and F-Measure, as an harmonic average of precision and recall.

As the model sees the value <=50K as negative and >50K as positive, precision measure when the model is correct in predicting
that income is higher than 50k, while recall measures how often it identifies families making more than 50k.
As expected from the data being somewhat skewed towards lower income, precision is higher than recall. For the model I used,
precision ends up being 0.80, recall 0.66 and fbeta 0.73.


## Ethical Considerations

As many features are used that can be potentially used for discrimination, a model created when using this data is bound to show some bias when evaluating categories.
As a matter as fact, the model we created, when evaluated on specific slices, shows that it tends to overevaluate features such as sex, race and marriage status as indicative of lower income.

## Caveats and Recommendations

Shis model can be used over a pretty big, diverse sample size to make an estimate of an average of salaries. It cannot be used to predict reliably the expected income of a single sample.

