### Create a new experiment in MLflow with the name "produce metrics"
```mlflow experiments create --experiment-name "produce metrics"```

This command creates a new experiment in MLflow, allowing you to track metrics related to that specific experiment.

### Set the environment variable to specify which experiment ID to use for logging metrics
```export MLFLOW_EXPERIMENT_ID=2```

his command sets an environment variable that tells MLflow which experiment ID to use when logging metrics. This is crucial for organizing and retrieving metrics later.


### Run the Python script to produce and log metrics
```python produce_metrics.py```
