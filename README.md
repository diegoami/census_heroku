## LOCAL DEPLOYMENT

### SET UP ENVIRONMENT
To execute the code locally, set up a conda environment with the following command

```
conda create -n [envname] "python=3.8" 
conda activate [envname]
python -m pip install -r requirements_local.txt
```

### MANAGING DATA

The data can be found in the directory `data`, in the file `census.csv`.
The idea is to create a model able to predict whether someone earns more or less than 50K based on their census data.
It contains a version of the census data, which has been managed with `DVC` and cleaned up to get better results

### DATA ANALYSIS

The data analysis can be found in `notebooks`.
Analysis of data can be started with the command
```
jupyter notebook --NotebookApp.iopub_msg_rate_limit=1e10 --NotebookApp.rate_limit_window=30.0 "notebooks/Analyze Census Data.ipynb"
```

### MODEL CREATION

An AI Model can be created using the `train_model.py` script. It can be called with following parameters

```
python train_model.py --model_dir_name <model directory destination> --data_file_name <the data file name to  use>
```

The expected output of the training job is something like that:

```
Reading training data from file /home/diego/projects/ud_mlops/census_heroku/data/census.csv
Starting to train model....
Found best params: {'scoring': 'loss', 'min_samples_leaf': 15, 'max_leaf_nodes': 30, 'max_iter': 750, 'max_depth': 25, 'learning_rate': 0.01, 'l2_regularization': 0.6}
Saving model artifacts to /home/diego/projects/ud_mlops/census_heroku/model/latest
Evaluating performance on test data...
precision: 0.7987567987567987, recall: 0.6556122448979592, fbeta: 0.7201401050788092
Evaluating overall performance...
precision: 0.8031866464339908, recall: 0.6750414487947966, fbeta: 0.7335596978726352
```

By default the model is saved under `model\latest`

### EVALUATE MODEL

To evaluate your model, execute

```
python evaluate_model.py --model_dir_name <model directory destination> --data_file_name <the data file name to  use>
```

At first an overall breakdown of metrics is shown

```
precision: 0.8031866464339908, recall: 0.6750414487947966, fbeta: 0.7335596978726352
TN, FP, FN, TP: (23423, 1297, 2548, 5293)
```

And then a breakdown over all features, and how every split fares in terms of metrics

### EVALUATION ANALYSIS

#### OVERALL BIAS


The model sees the value `<=50K` as negative and `>50K` as positive
There are in the database 24720 that earn `<=50k` (negative) and 7841 that earn `>50K`.
There are more False Negatives than False Positives, and precision is better then recall.



Taking into account that
* a True Negative is when we correctly recognize that someone earns less than 50k, 
* a False Positive when someone earns less than 50k, but we predict that it earns more than 50k
* a False Negative when someone earns more than 50k, but we predict that they earn less than 50k
* a True Positive when we correctly recognize that someone earns more than 50k


We have a relatively high number of False Negatives overall, which means that we often predict that someone is making less money than the case is,
rather than the other case.
That is the reason we have a low recall : TP/(TP+FN) and a higher precision TP/(TP+FP)

#### BIAS IN SLICES

An example how the model can be biased in some categories cam be seen by the marriage status.

```
==== SLICE FORF FEATURE : marital-status
== CLS FOR FEATURE : Never-married
precision: 0.9513274336283186, recall: 0.4378818737270876, fbeta: 0.599721059972106
TN, FP, FN, TP: (10181, 11, 276, 215)
== CLS FOR FEATURE : Married-civ-spouse
precision: 0.792938459000165, recall: 0.7181709503885236, fbeta: 0.7537050105857446
TN, FP, FN, TP: (7029, 1255, 1886, 4806)
== CLS FOR FEATURE : Divorced
precision: 0.8744186046511628, recall: 0.4060475161987041, fbeta: 0.5545722713864307
TN, FP, FN, TP: (3953, 27, 275, 188)
```

People who are never married get very few False Positives, but even more False Negatives than True Positives. That is, the model tend to assume that never-married people
earn less than they actually do. That can be seen in a higher precision and lower recall than the overall values.
The model is accurate when it recognizes when never-married people make more than 50k, but flags incorrectly many never-married people as low-income, when they in reality make more money. That's obviously because most never-married people in the database make little money, and the model may see this as an indication of low income. We see the same phenomen for divorced.

For Married-civ-spouse entries, on the other hand, we do not see this effect. We have even a False Negative rate than the overall average, and a much better recall. The model is more accurate than on the full data-set when it flags a family as low-income, but is not.
It has a comparable precision as recorded in the full dataset, which means that the model is not as eager as in never-married entries to flag someone as low-income, but may treate this situation as neutral.

```
==== SLICE FORF FEATURE : sex
== CLS FOR FEATURE : Male
precision: 0.8010186160871092, recall: 0.6846292404683278, fbeta: 0.738264810618323
TN, FP, FN, TP: (13995, 1133, 2101, 4561)
== CLS FOR FEATURE : Female
precision: 0.8169642857142857, recall: 0.6208651399491094, fbeta: 0.7055421686746988
TN, FP, FN, TP: (9428, 164, 447, 732)
```

```
== CLS FOR FEATURE : White
precision: 0.8037880046519356, recall: 0.6797808065196009, fbeta: 0.7366017052375152
TN, FP, FN, TP: (19518, 1181, 2279, 4838)
== CLS FOR FEATURE : Black
precision: 0.823943661971831, recall: 0.6046511627906976, fbeta: 0.6974664679582713
TN, FP, FN, TP: (2687, 50, 153, 234)
```

As expected we see the same phenomenon in other splits, although it is not as dramatic as one might fear. We see that female have lower recall and are more often incorrectly flagged as low-income than males. So is the case for black people compared to white people.

### LOCAL TEST

The API used to call the model and retrieve a result can be found in `main.py`.
A web server publishing the model that can be used to return predictions can be started with `uvicorn main:app`
Then with the test `test_local_census_api.py` it can be started.




