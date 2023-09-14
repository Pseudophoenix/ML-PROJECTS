from setuptools import find_packages, setup
from typing import List
# finds the packages used in ML application
HYPEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    '''This function will return the list of required list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(
    name="ML Project",
    version='0.0.1',
    author="Alok",
    author_email="wayneroonry0089@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    # ['pandas','seaborn','numpy']
)