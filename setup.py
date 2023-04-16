from setuptools import find_packages,setup
from typing import List



HYPEN_E_DOT = '-e .'
def get_reqs(file_path:str)->List[str]:
    '''
    This function will return the list of req.
    '''
    reqe=[]
    with open(file_path) as file_obj:
        reqe = file_obj.readlines()
        reqe=[reqe.replace("\n","")for r in reqe]

        if HYPEN_E_DOT in reqe:
            reqe.remove(HYPEN_E_DOT)

    return reqe




setup(
    name='M.L. Project',
    version='0.0.1',
    author="Darsh_Dave",
    author_email='davedarsh1999@gmail.com',
    packages=find_packages(),
    install_requires=get_reqs(req.txt)
)