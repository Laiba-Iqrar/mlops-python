### Create a new experiment in MLflow with the name "produce metrics"
```mlflow experiments create --experiment-name "produce metrics"```

This command creates a new experiment in MLflow, allowing you to track metrics related to that specific experiment.

### Set the environment variable to specify which experiment ID to use for logging metrics
```export MLFLOW_EXPERIMENT_ID=2```

his command sets an environment variable that tells MLflow which experiment ID to use when logging metrics. This is crucial for organizing and retrieving metrics later.


### Run the Python script to produce and log metrics
```python produce_metrics.py```

#### tree of Ml runs

in linux install tree 
```tree mlruns/```

```mlruns/
├── 0
│   ├── 05e3e29ec764433f83078d59b9a55462
│   │   ├── artifacts
│   │   ├── meta.yaml
│   │   ├── metrics
│   │   │   └── time_to_complete
│   │   ├── params
│   │   │   ├── threshold
│   │   │   └── verbosity
│   │   └── tags
│   │       ├── mlflow.runName
│   │       ├── mlflow.source.git.commit
│   │       ├── mlflow.source.name
│   │       ├── mlflow.source.type
│   │       └── mlflow.user
│   ├── 6c52c101108841ddb432edff0c281bef
│   │   ├── artifacts
│   │   ├── meta.yaml
│   │   ├── metrics
│   │   │   ├── cpu
│   │   │   ├── disk
│   │   │   └── ram
│   │   ├── params
│   │   └── tags
│   │       ├── mlflow.runName
│   │       ├── mlflow.source.git.commit
│   │       ├── mlflow.source.name
│   │       ├── mlflow.source.type
│   │       └── mlflow.user
│   ├── f090319ad9a04c03acbd2b4c7689fc91
│   │   ├── artifacts
│   │   │   └── produced-dataset.csv
│   │   ├── meta.yaml
│   │   ├── metrics
│   │   │   └── time_to_complete
│   │   ├── params
│   │   │   ├── threshold
│   │   │   └── verbosity
│   │   └── tags
│   │       ├── mlflow.runName
│   │       ├── mlflow.source.git.commit
│   │       ├── mlflow.source.name
│   │       ├── mlflow.source.type
│   │       └── mlflow.user
│   └── meta.yaml
├── 914799642224550823
│   └── meta.yaml
└── models```
