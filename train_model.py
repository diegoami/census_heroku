# Script to train machine learning model.

from sklearn.model_selection import train_test_split

# Add the necessary imports for the starter code.
#!/usr/bin/env python
import argparse
import pandas as pd
import joblib
import os


from ml.data import process_data
from ml.model import train_model, compute_model_metrics, inference

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Train a model",
        fromfile_prefix_chars="@",
    )

    parser.add_argument(
        "--data_file_name",
        type=str,
        help="Fully-qualified file name location for data",
        default=os.path.join(os.getcwd(), 'data', 'census.csv')
    )

    parser.add_argument(
        "--model_dir_name",
        type=str,
        help="Fully-qualified dir name location for model",
        default=os.path.join(os.getcwd(), 'model', 'latest')
    )


    # Add code to load in the data.
    args = parser.parse_args()
    data = pd.read_csv(args.data_file_name)
    # Optional enhancement, use K-fold cross validation instead of a train-test split.
    train, test = train_test_split(data, test_size=0.20, shuffle=True, stratify=data["salary"])

    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]
    X_train, y_train, encoder, lb = process_data(
        train, categorical_features=cat_features, label="salary", training=True
    )

    # Proces the test data with the process_data function.
    X_test, y_test, _, _ = process_data(
        test, categorical_features=cat_features, label="salary", encoder = encoder, lb = lb, training = False
    )

    model = train_model(X_train, y_train)
    dirname = args.model_dir_name
    os.makedirs(dirname, exist_ok=True)
    joblib.dump(model, os.path.join(dirname, 'model'))
    joblib.dump(encoder, os.path.join(dirname, 'encoder'))
    joblib.dump(lb, os.path.join(dirname, 'lb'))
    joblib.dump(cat_features, os.path.join(dirname, 'cat_features'))

    preds = inference(model, X_test)
    precision, recall, fbeta = compute_model_metrics(y_test, preds)
    # Train and save a model.
    print(f"precision: {precision}, recall: {recall}, fbeta: {fbeta}")



