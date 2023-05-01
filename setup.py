from setuptools import find_packages,setup
def get_requirements(file_name):
    with open(file_name) as f:
        R=f.read().splitlines()
        if '-e .' in R:
            R.remove('-e .')
        
        print(R)
        return R
    

setup(
name='ML_Project',
version='0.1',
author='Ahmed Khorshid',
author_email='baheeg@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),

)