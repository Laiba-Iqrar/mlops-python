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

## Question 1: why logging paramters important?
Logging parameters is important because it helps track the settings used during training, allowing for reproducibility and better understanding of model behavior.

## Question 2 : What is the difference between parameters and metrics?
parameters are about the settings for training, while metrics are about evaluating the model's performance.

## Question 3 : Why do we connect Mlflow to databricks or Azure MAchine learning?
Databricks is a cloud-based platform designed for big data processing and machine learning. It provides a collaborative environment for data scientists and engineers to work together on data projects.
Azure Machine Learning is a cloud-based service provided by Microsoft that enables developers and data scientists to build, train, and deploy machine learning models.

MAin reasons: 
Big Data processing , Integration is easier , collaboartion
