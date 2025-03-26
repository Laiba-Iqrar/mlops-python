# MLFlow Project Setup with Conda
- Conda installed 
- Terminal/shell access



 **Create Conda environment**
   ```bash
   conda create --name exploratory python=3.8
   ```

 **Initialize conda **
   ```bash
   conda init <your_shell>  # bash/zsh/powershell/cmd.exe
   ```
   Restart terminal after running this.

 **Activate environment**
   ```bash
   conda activate exploratory
   ```

 **Export environment config**
   ```bash
   conda env export --name exploratory > conda_env.yml
   ```

 **Edit `conda_env.yml`**  
   Add these lines under `dependencies:`:
   ```yaml
     - pip:
       - pandas==1.5.0
       - mlflow==1.29.0
   ```

 **Update environment**
   ```bash
   conda env update --file conda_env.yml --prune
   ```

 **Verify installation**
   ```bash
   conda list
   ```

 **Initialize MLFlow project**
   ```bash
   echo "name: wine_ratings
   conda_env: conda_env.yml" > MLproject
   ```


