## Create HF Repo and model from terminal

### Create a new virtual environment
``` python -m venv VM ```

### Activate the virtual environment
``` source VM/bin/activate  # For Linux/Mac ```


### Install the huggingface_hub library
``` pip install huggingface_hub```

### Log in to Hugging Face
```huggingface-cli login```

### Create a new token (this is done in the web interface, not a command)

### Create a repository
```huggingface-cli repo create demo-onnx --type model```

### Push a model to the repository
```git push```

### Upload new files to the repository (this is done in the web interface)
