from typing import List
from setuptools import setup,find_packages
HYPHEN_E_DOT='-e .'

def get_requirements(file_path):
    
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [i.replace("\n","") for i in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
    return requirements
        
        
    
setup(
    name='Spam_Classifier',
    version='0.0.1',
    author='Het',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages(),
    author_email='hetbhagatji09@gmail.com'
    
    
)