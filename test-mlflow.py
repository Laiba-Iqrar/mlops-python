from mlflow import log_metric, log_param, log_artifact

if __name__ == "__main__":
    log_param("threshold", 3)
    log_param("verbosity", "DEBUG")

    log_metric("time_to_complete", 33)

    log_artifact("produced-dataset.csv")


    #pip install ml-flow
    #for UI write python3 -m mlflow UI