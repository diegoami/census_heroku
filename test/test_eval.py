import unittest
from ml.eval import get_tn_fp_fn_tp, get_metric_info
import numpy as np

class EvalTestCase(unittest.TestCase):
    def test_get_tn_fp_fn_tp(self):
        y = np.array([1,1,1,1,0,0,0,0])
        preds = np.array([1,1,1,0,0,0,1,1])
        tn, fp, fn, tp = get_tn_fp_fn_tp(y=y, preds=preds)
        assert ((tn, fp, fn, tp) == (2, 2, 1, 3))

    def test_get_metric_info(self):
        y = np.array([1, 1, 1, 1, 0, 0, 0, 0])
        preds = np.array([1, 1, 1, 0, 0, 0, 1, 1])
        metric_info = get_metric_info(y=y, preds=preds)
        assert ((metric_info.tn, metric_info.fp, metric_info.fn, metric_info.tp) == (2, 2, 1, 3))
        assert ((metric_info.precision, metric_info.recall, round(metric_info.fbeta, 2)) == (0.6, 0.75, 0.67))