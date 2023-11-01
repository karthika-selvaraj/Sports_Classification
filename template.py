import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]: %(message)s:')

project_name = "sports_classifier"

## I'm just defining paths here, but to create these paths in local machine you should write the below logic [for loop]

list_of_files = [
    ".github/workflows/.gitkeep",  ## CI/CD command in yaml file
    f"src/{project_name}/__init__.py", ## Basically this src folder will have our project. this src folder, will contain local package so that's why we initiate constructer __init__.py
    f"src/{project_name}/components/__init__.py", ## this components is going to be an another loacl package
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",  ## mlops tool
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
]


## To initiate the above paths in local machine, you should run below logic
for path in list_of_files:
    filePath = Path(path)
    fileDir, fileName = os.path.split(filePath)

    if fileDir !="":  ## this is only to create the paths
        os.makedirs(fileDir, exist_ok=True) ## exist_ok - if file already exist, don't recreate it
        logging.info(f"creating file directory {fileDir} for the file: {fileName}")

    if (not os.path.exists(filePath)) or (os.path.getsize(filePath) == 0): ## if path is not existing or size of the file in that path is 0, then create empty file
        with open(filePath, "w") as f:
            pass
            logging.info(f"creating empty file : {filePath}") 
    else:
        logging.info(f"{filePath} already exists ")