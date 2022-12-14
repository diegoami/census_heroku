from ml.data import process_data
from ml.model import inference, compute_model_metrics
from sklearn.metrics import confusion_matrix
from values.metric_info import MetricInfo
from ml.model import compute_model_metrics

def get_tn_fp_fn_tp(y, preds):
    """
    Retrieves the confusion matrix values

    Inputs
    ------
    y : np.array
        true values.
    preds : np.array
        predictions
    Returns
    -------
    tn, fp, fn, tp
        a tuple for true negative
    """

    cm = confusion_matrix(y, preds).ravel()
    if cm is not None and len(cm) == 4:
        tn, fp, fn, tp = cm
        return tn, fp, fn, tp
    else:
        return None

def get_metric_info(y, preds):
    """
    Retrieves Metrics information based on true values and predictions

    Inputs
    ------
    y : np.array
        true values.
    preds : np.array
        predictions
    Returns
    -------
    metric_info
        a metric information object containing all metrics for evaluation
    """

    metric_info = MetricInfo()
    precision, recall, fbeta = compute_model_metrics(y=y, preds=preds)
    tn, fp, fn, tp = get_tn_fp_fn_tp(y, preds)

    metric_info.precision = precision
    metric_info.recall = recall
    metric_info.fbeta = fbeta

    metric_info.tn = tn
    metric_info.fp = fp
    metric_info.fn = fn
    metric_info.tp = tp
    return metric_info




def list_unique_features(data, cat_features):
    """
    Lists the unique values of categorical features in a dataframe

    Inputs
    ------
    data : Dataframe
        the data to analyze
    cat_features : list
        the categorical features list

    """
    for slice_feature in cat_features:
        list_unique = data[slice_feature].unique()
        print(f"{slice_feature} : {list_unique}")


def show_performance_on_slices(data, X, y, preds, cat_features):
    """
    Show the model performance on separate slices of data
    Inputs
    -----
    data : Dataframe
        true values.
    X : np.ndarray
        features
    y : np.ndarray
        labels
    preds:
        prediction
    cat_features:
        categorical features names
    """
    for slice_feature in cat_features:
        print(f"==== SLICE FORF FEATURE : {slice_feature}")
        for cls in data[slice_feature].unique():
            print(f"== CLS FOR FEATURE : {cls}")
            idx_slice = data[slice_feature] == cls
            x_slice, y_slice, preds_slice = X[idx_slice], y[idx_slice], preds[idx_slice]

            precision, recall, fbeta = compute_model_metrics(y_slice, preds_slice)
            print(f"precision: {precision}, recall: {recall}, fbeta: {fbeta}")
            if y_slice is not None and preds_slice is not None:
                slice_result = get_tn_fp_fn_tp(y_slice, preds_slice)
                if slice_result:
                    tn, fp, fn, tp = slice_result
                    print(f"TN, FP, FN, TP: {(tn, fp, fn, tp)}")
        print("\n\n\n\n")

