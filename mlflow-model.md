# KEY POINTS

1. MLflow provides tools to deploy models locally as a REST API server, generate Docker images, or directly score files. The deployments accept DataFrame, JSON, or CSV data.


2. Models with the python_function flavor can be deployed to Azure ML, SageMaker, Kubernetes, and other environments. Dedicated plugins help package and deploy to these platforms. 


3. MLflow integrates with MLServer to serve models that conform to the V2 inference protocol used by KServe and Seldon Core.


4. The mlflow deployments module and CLI enable deploying models to custom targets via third-party plugins, abstracting away platform specific logic.


5. MLflow Models can be exported as Spark UDFs to score data in a Spark DataFrame through Pandas UDFs, handling DataFrame input and output.


