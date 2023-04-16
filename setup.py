from setuptools import find_packages,setup
from typing import List



HYPEN_E_DOT = '-e .'
def get_reqs(file_path:str)->List[str]:
    '''
    This function will return the list of req.
    '''
    req=[]
    with open(file_path) as file_obj:
        req = file_obj.readlines()
        req=[req.replace("\n","")for r in req]

        if HYPEN_E_DOT in req:
            req.remove(HYPEN_E_DOT)

    return req




setup(
    name='M.L. Project',
    version='0.0.1',
    author="Darsh_Dave",
    author_email='davedarsh1999@gmail.com',
    packages=find_packages(),
    install_requires=get_reqs(req.txt)
)