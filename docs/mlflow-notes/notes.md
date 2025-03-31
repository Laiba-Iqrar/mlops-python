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

## Question 4: How do MLflow Projects differ from simply version controlling and sharing code? What additional value do they provide?
- MLflow Projects package not just code, but also dependencies and metadata (like parameters and entry points) in a structured format.
- They provide reproducibility and reusability, allowing for easy execution of the project in different environments, which is not guaranteed by simple version control.

## Question 5: What kinds of challenges could arise when trying to break up a machine learning pipeline into separate reusable steps? How might MLflow help address some of these?

Challenges in Breaking Up Pipelines:
- Complexity: Identifying clear boundaries between steps can be difficult.
- Dependency Management: Ensuring that each step has the necessary inputs and outputs can be challenging.
  
MLflow Solutions: 
- It helps by providing a framework to define and manage these steps, allowing for modularization and tracking of each component, making it easier to manage dependencies.

## Question 6: What are some examples of workflows or use cases that would benefit from being implemented as MLflow Projects?

Examples of Workflows:
- Hyperparameter Tuning: Running multiple experiments with different parameters can be organized as MLflow Projects.
- Cross-Validation: Implementing a workflow that splits data, trains models, and evaluates them can benefit from the structured approach of MLflow Projects.

## Question 7: How feasible would it be to convert an existing machine learning codebase into an MLflow Project? What would be involved?

Feasibility of Conversion:
- Moderate to High Feasibility: Converting an existing codebase involves creating an MLproject file, defining dependencies in conda.yaml, and structuring the code to fit the MLflow format.
  
Steps Involved: 
- Identify entry points, specify parameters, and ensure that the code can run in the MLflow environment, which may require refactoring.
