# ml

## Creating a new environment

python3 -m venv <myenvname>

## Enabling the python virtual environment

source <myenvname>/bin/activate

Remember to install all the libraries inside your virtual environment:

python3 -m pip install -r requirements.txt

## Starting Jupyter Notebook

Once inside the virtual environment:

jupyter notebook


## Connecting the jupyter notebook to your virtual environment

Enter inside your virtual env
python3 -m pip install ipykernel 
ipython kernel install --user --name=mlenv
When creating a new project, select the right kernel


## Development Setup

Remeber to install vim ALE for asynchronous linting, alongside with autopep and pylint


## Linting

Remember pylint has to be installed inside the virtual environment!
