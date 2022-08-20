from ml.data import process_data
from ml.model import inference, compute_model_metrics
from sklearn.metrics import confusion_matrix
from values.metric_info import MetricInfo
from ml.model import compute_model_metrics

def get_tn_fp_fn_tp(y, preds):
    cm = confusion_matrix(y, preds).ravel()
    if len(cm) == 4:
        tn, fp, fn, tp = cm
        print(f"TP, FP, FN, TN: {(tn, fp, fn, tp)}")
        return tn, fp, fn, tp

def get_metric_info(y, preds):
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
