## LOCAL DEPLOYMENT

### SET UP ENVIRONMENT
To execute the code locally, set up a conda environment with the following command

```
conda create -n [envname] "python=3.8" 
conda activate [envname]
python -m pip install -r requirements_local.txt
```

### MANAGING DATA

The data can be found in the directory `data`. It is managed with DVC by means of `census.csv.dvc`.
It is retrieved from a remote repository, `s3://ud-mlops-3/census`
It can be retrieved wit `dvc pull`

Using this data we can create a model able to predict whether someone earns more or less than 50K based on their census data.
It contains a version of the census data, which has been managed with `DVC` and cleaned up to get better results
The original data is in the file `orig.csv`

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

An evaluation of the model and how it behaves can be found in [notebooks\Analyse Model performance.ipynb](notebooks\Analyse Model performance.ipynb)

### LOCAL API



The API used to call the model and retrieve a result can be found in `api/main.py`.
A web server publishing the model that can be used to return predictions can be started from a command line with `uvicorn api.main:app`, 
which will start tha application on `http://127.0.0.1:8000`
Then with the test `python -m pytest test/test_local_census_api.py` it can be verified that a model is running and giving prediction results

### TESTING

The tests are located in the `test` directory and can be executed with `PYTHONPATH=$(pwd) pytest`.



## DEPLOYING REMOTELY

The project is deployed on github: https://github.com/diegoami/census_heroku

To ensure deployment on Heroku, two workflows have been setup,

* _test_and_deploy_ executes retrieves data, creates a model and deploys it on heroku
* _deploy_ deploys the model to heroku. The model deployed is the one in the directory `model/latest`
 