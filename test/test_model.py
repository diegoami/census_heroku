import unittest

import pytest
from ml.model import train_model, compute_model_metrics, inference
import numpy as np
rng = np.random.default_rng(seed=42 )


class ModelTestCase(unittest.TestCase):
    def test_create_model(self):
        X = rng.random((100, 10))
        y = np.concatenate((np.repeat(0, 50), np.repeat(1,50)))
        model = train_model(X, y)
        self.assertIsNotNone(model)

    def test_compute_model_metrics(self):
        y = np.array([0,0,0,1])
        preds = np.array([0,0,0,1])
        precision, recall, fbeta = compute_model_metrics(y, preds)
        self.assertEqual(precision, 1)
        self.assertEqual(recall, 1)
        self.assertEqual(fbeta, 1)

    def test_inference(self):
        class model_mock:
            def predict(X):
                return np.array([1, 1, 1])
        X = np.array([0, 0, 0])
        y = inference(model_mock, X)
        self.assertIsNotNone(y)

if __name__ == '__main__':
    unittest.main()
