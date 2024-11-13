from setuptools import find_packages, setup
from typing import List
import os


def get_requirement(file_path:str) -> List[str]:
    HYPEN_DOT_E = "-e ."
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]  # Remove newline characters
        
        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)
    
    print("Requirements to install:", requirements)  # Debug line
    return requirements

setup(
    name='MLproj',
    version='0.0.1',
    author="scl",
    author_email='laisucheun95@gmail.com',
    packages=find_packages(),
    install_requires =get_requirement('requirements.txt'),
    
)

