from setuptools import find_packages, setup
from typing import List

TRIGGER = "-e ."
def get_requirements(file_path:str) -> List[str]:
    '''
    This functiono returns the list of requirements from the requirements.txt file. This is used for scalability.

    There is a line -e . at the end of that .txt file which triggers setup.py while installing the dependencies. 
    But we have to modify such the this is not read in this function.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [rep.replace("\n", "") for rep in requirements]

        if TRIGGER in requirements:
            requirements.remove(TRIGGER)
    return requirements



setup(
    name = 'ML-Project',
    version= '0.0.1',
    author='Anindya',
    author_email='joyanindya99@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)