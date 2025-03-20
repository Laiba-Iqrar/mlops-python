# Key Terms:

## MLflow Tracking 
Logs key metrics, parameters, models, and other artifacts when running ML code to monitor experiments

## MLflow Projects 
Configurable standard format for organizing ML code to ensure consistency and reproducibility

## MLflow Models 
Package ML model files with their dependencies so they can be deployed on diverse platforms


# MLflow Tracking:

## Data Tracking:
MLflow allows you to track various components during machine learning operations.

## Parameters: 

## Defined as key-value pairs (e.g., regularization = 0.1).
Used to log values that are important during model training.
## Metrics: 

Also key-value pairs but focus on performance indicators (e.g., accuracy = 0.1).
Capture essential information about the model's performance.
## Artifacts: 

Refers to files generated during the model training process (e.g., model.pkl).
These files can be stored and accessed later, often pushed to a remote server.
Projects: 


## Models:
Involves tracking different ways of creating and managing models.
Includes instructions on how to load and work with models using specific libraries (e.g., Scikit-learn).
