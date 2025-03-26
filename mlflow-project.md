## Project Names: 
Each project should have a unique name.
## Conda Environment: 
Specify the Conda environment to manage dependencies.
## YAML File: 
Use a YAML file to define project configurations. Note that it should not have a dotted extension for proper recognition.
## Entry Points: 
At least one entry point is required to run scripts with different parameters.
## Python or Shell Script: 
It's recommended to use Python scripts for consistency with data science libraries.

# MLflow Project Creation Notes

- **Dataset**: Using `wine-ratings.csv` for the project.
- **Key Issues**: The dataset has problems with some columns, including missing values and carriage returns.

## Steps to Create an MLflow Project

1. **Set Up**
    Create a Conda environment named `exploratory` using Python 3.8.
   Activate the environment.

2. **Creating `conda_env.yml`**
   Export the environment to create a `conda_env.yml` file.
   Specify channels and dependencies, including:
     - Base dependencies
     - Additional dependencies using pip (e.g., Pandas, MLflow).

3. **Updating the Environment**
    Use the command to update the environment:
     ```bash
     conda env update --file conda_env.yml --prune
     ```

4. **Running the MLflow Project**
   Activate the environment:
     ```bash
     conda activate exploratory
     ```
    Run the MLflow project with:
     ```bash
     mlflow run . -P filename=carriage.csv
     ```

5. **Parameters**
   - Required parameters: `filename`.
   - Optional parameters: `log` (default: true), `max_errors` (default: 1).
  
# KEY POINTS :

- The conda.yaml file defines dependencies needed to recreate the environment

- Entry points specify which scripts can be executed in the workflow

- MLflow projects can run workflows from local files or remote Git repos

- The mlflow run command executes projects with parameters locally or remotely

- Standardized projects enable portability across different platforms

7. **Error Handling**
   - If a non-existent file is specified (e.g., `fake.csv`), an error will occur.
   - If no parameters are passed, an error will indicate missing parameters.

