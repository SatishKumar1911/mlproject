from setuptools import setup, find_packages

HYPHEN_E_DOT = "-e ."

def get_requirements(path:str):
    '''
    This function returns a list of package names.
    '''
    with open(path, 'r') as file_obj:
        packages = file_obj.readlines()

    packages = [ package.rstrip('\n') for package in packages]
    if HYPHEN_E_DOT in packages:
        packages.remove(HYPHEN_E_DOT)
    return packages

setup(
    name="ml_project",
    version="0.0.1",
    description="End to End Machine Learning Project",
    author="satish kumar",
    author_email="satish.191199@gmail.com",
    packages=find_packages(), # Provide a list of folder names that contain a file named "init.py".
    python_requires = ">3.8",
    install_requires = get_requirements('./requirements.txt')
)
