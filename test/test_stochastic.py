import unittest
import joblib
import os

from ml.model import train_model, compute_model_metrics, inference
from common.fixtures import first_census_entry, second_census_entry, wrong_category_entry, generate_entry

import numpy as np
rng = np.random.default_rng(seed=42)


class StochasticModelTestCase(unittest.TestCase):
    def setUp(self):
        # Add code to load in the data.
        self.dirname = "model/latest"
        self.model = joblib.load(os.path.join(self.dirname, 'model'))
        self.encoder = joblib.load(os.path.join(self.dirname, 'encoder'))
        self.lb = joblib.load(os.path.join(self.dirname, 'lb'))
        self.cat_features = joblib.load(os.path.join(self.dirname, 'cat_features'))


if __name__ == '__main__':
    unittest.main()
