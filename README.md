# ml


## Enabling the python virtual environment

source venv/bin/activate


## Creating a new environment

python3 -m venv <myenvname>

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
