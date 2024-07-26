from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = '-e .'

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


__version__ = "0.0.1"

REPO_NAME = "end-to-end-NLP"
AUTHOR_USER_NAME = "Rakesh"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "rakeshjv2000@gmail.com"


setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python web app for text summarization",
    package_dir={"": "src"},
    packages=find_packages(where="src")
)