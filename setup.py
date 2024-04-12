from setuptools import setup, find_packages  

setup(
    name='nisqaTTS_scriptable', 
    version='1.0.0', 
    description='based on the original nisqaTTS but modified so that it can be pip installed and used in script', 
    author='Mikhailangelo Panzo',
    author_email='mbpanzo@outlook.com',
    packages=find_packages()
)