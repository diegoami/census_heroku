# Script to train machine learning model.

from sklearn.model_selection import train_test_split

# Add the necessary imports for the starter code.
#!/usr/bin/env python
import argparse
import pandas as pd
import joblib
import os

from ml.data import process_data
from ml.model import inference, compute_model_metrics
from ml.eval import get_tn_fp_fn_tp, list_unique_features, show_performance_on_slices

from sklearn.metrics import confusion_matrix


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Evaluate a model",
        fromfile_prefix_chars="@",
    )

    parser.add_argument(
        "--data_file_name",
        type=str,
        help="Fully-qualified file name location for data",
        required=False,
        default=os.path.join(os.getcwd(), 'data', 'census.csv')
    )


    parser.add_argument(
        "--model_dir_name",
        type=str,
        help="Fully-qualified dir name location for model",
        required=False,
        default=os.path.join(os.getcwd(), 'model', 'latest')
    )



    # Add code to load in the data.
    args = parser.parse_args()
    data = pd.read_csv(args.data_file_name)
    dirname = args.model_dir_name

    # Add code to load in the data.
    model = joblib.load(os.path.join(dirname, 'model'))
    encoder = joblib.load(os.path.join(dirname, 'encoder'))
    lb = joblib.load(os.path.join(dirname, 'lb'))
    cat_features = joblib.load(os.path.join(dirname, 'cat_features'))

    X, y, _, _ =  process_data(
        data, categorical_features=cat_features, label="salary", encoder = encoder, lb = lb, training = False
    )

    idx_pos, idx_neg = y == 0, y == 1

    preds = inference(model, X)
    print(" =============== GENERAL ====================")
    precision, recall, fbeta = compute_model_metrics(y, preds)
    print(f"precision: {precision}, recall: {recall}, fbeta: {fbeta}")
    tn, fp, fn, tp = get_tn_fp_fn_tp(y, preds)
    print(f"TN, FP, FN, TP: {(tn, fp, fn, tp)}")

    print("\n============================================\n")

    list_unique_features(data, cat_features)

    show_performance_on_slices(data, X, y, preds, cat_features)
