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



---

# Hugging Face CLI (huggingface-cli)

The Hugging Face CLI allows interacting with the Hub from the command line.

### Key Features:
- **Login, logout, and check login status**
- **Create repositories**
- **Upload and download files**
- **Manage local cache**
- **Open pull requests**
- **Schedule periodic syncs**

### Key Points:
- Builds on top of the Hub Python library, providing an interface similar to git commands.
- **Benefits** include automation, scripting capabilities, and reducing manual work.
- The CLI automatically authenticates using your saved token. Additional options exist for explicitly providing a token, revision branch, commit message, etc.
- Outputs can be quieted to only print essential information, enabling seamless integration in scripts. Progress bars and warnings provide detailed visibility by default.
- Complementary commands like `huggingface-cli env` and `huggingface-cli scan-cache` assist in debugging problems or managing disk usage.

Overall, the CLI makes common Hub workflows more streamlined and reproducible. It's a tool both for ad-hoc exploration of repositories and automated, production workflows.


---

##  **Using the Dataset**
   - You can load the dataset in a Jupyter Notebook using:
     ```python
     from datasets import load_dataset
     dataset = load_dataset("your_account/temporary_dataset")
     ```


## Splits
- Splits allow access to subsets of the same data.
- Example splits: 
  - **Training**: Full dataset (e.g., 3000 rows)
  - **Test**: Subset (e.g., 200 rows)
  - **Validation**: Another subset
