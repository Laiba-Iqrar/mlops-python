import argparse
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import mlflow
import mlflow.sklearn

def train_model(data_path, learning_rate, max_depth):
    # Load data
    data = pd.read_csv(data_path)
    X = data.drop("target", axis=1)
    y = data["target"]
    
    # Train model
    model = RandomForestClassifier(max_depth=max_depth)
    model.fit(X, y)
    
    # Log parameters and model
    mlflow.log_param("learning_rate", learning_rate)
    mlflow.log_param("max_depth", max_depth)
    mlflow.sklearn.log_model(model, "model")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_file")
    parser.add_argument("--learning_rate", type=float)
    parser.add_argument("--max_depth", type=int)
    args = parser.parse_args()
    
    train_model(args.data_file, args.learning_rate, args.max_depth)