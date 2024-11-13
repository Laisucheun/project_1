from setuptools import find_packages, setup
from typing import List

HYPEN_DOT_E = "-e ."

def get_requirement(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Remove newline characters
        
        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)
            
    return requirements

setup(
    name='MLproj',
    version='0.0.1',
    author="scl",
    author_email='laisucheun95@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement('requirements.txt')
)
