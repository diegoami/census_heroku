from sklearn.metrics import fbeta_score, precision_score, recall_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import HistGradientBoostingClassifier
import warnings


# Optional: implement hyperparameter tuning.
def rtf_train_model(X_train, y_train):
    """
    Trains a machine learning model and returns it.

    Inputs
    ------
    X_train : np.array
        Training data.
    y_train : np.array
        Labels.
    Returns
    -------
    model
        Trained machine learning model.
    """

    param_grid = {
        'n_estimators': [200, 500],
        'max_features': ['auto', 'sqrt', 'log2'],
        'max_depth': [4, 5, 6, 7, 8],
        'criterion': ['gini', 'entropy']
    }
    with warnings.catch_warnings():
        # ignore all caught warnings
        warnings.filterwarnings("ignore")
        rfc = RandomForestClassifier(random_state=42)
        CV_rfc = GridSearchCV(estimator=rfc, param_grid=param_grid, cv=5)
        CV_rfc.fit(X_train, y_train)
        best_params = CV_rfc.best_params_
        print(f"Found best params: {best_params}")
        rfc_cv = RandomForestClassifier(random_state=42, **best_params )
        model = rfc_cv.fit(X_train, y_train)
        return model

def train_model(X_train, y_train):
    return xgb_train_model(X_train, y_train)

# Optional: implement hyperparameter tuning.
def xgb_train_model(X_train, y_train):
    """
    Trains a machine learning model and returns it.

    Inputs
    ------
    X_train : np.array
        Training data.
    y_train : np.array
        Labels.
    Returns
    -------
    model
        Trained machine learning model.
    """

    seed = 42
    param_grid = {
        'max_iter': [750, 1000, 1200, 1500],
        'learning_rate': [0.01, 0.1, 1],
        'max_depth': [20, 25, 30],
        'max_leaf_nodes': [10, 30, 50],
        'l2_regularization': [0, 0.5, 1, 1.5, 2],
        'scoring': ['f1_micro', 'loss'],
        'min_samples_leaf': [10, 15, 20]
    }

    with warnings.catch_warnings():
        # ignore all caught warnings
        warnings.filterwarnings("ignore")
        hgbc = HistGradientBoostingClassifier(random_state=seed)
        CV_hgbc = RandomizedSearchCV(estimator=hgbc, param_grid=param_grid, cv=5)
        CV_hgbc.fit(X_train, y_train)
        best_params = CV_hgbc.best_params_
        print(f"Found best params: {best_params}")
        hgbc_cv = HistGradientBoostingClassifier(random_state=42, **best_params )
        model = hgbc_cv.fit(X_train, y_train)
        return model


def compute_model_metrics(y, preds):
    """
    Validates the trained machine learning model using precision, recall, and F1.

    Inputs
    ------
    y : np.array
        Known labels, binarized.
    preds : np.array
        Predicted labels, binarized.
    Returns
    -------
    precision : float
    recall : float
    fbeta : float
    """
    fbeta = fbeta_score(y, preds, beta=1, zero_division=1)
    precision = precision_score(y, preds, zero_division=1)
    recall = recall_score(y, preds, zero_division=1)
    return precision, recall, fbeta



def inference(model, X):
    """ Run model inferences and return the predictions.

    Inputs
    ------
    model : ???
        Trained machine learning model.
    X : np.array
        Data used for prediction.
    Returns
    -------
    preds : np.array
        Predictions from the model.
    """

    preds = model.predict(X)
    return preds
