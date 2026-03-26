# building the project as a package itself

from typing import List
from setuptools import setup, find_packages


def get_requirements(file_path:str) -> List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    packages=find_packages(),
    author="Swaraj",
    description="A machine learning project",
    author_email="kdmswaraj17@gmail.com",
    install_requires=get_requirements('requirements.txt')
)