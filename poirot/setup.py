from setuptools import setup, find_packages
from os import path

# Get the absolute path to the directory where setup.py is located
working_directory = path.abspath(path.dirname(__file__))

# Read the contents of the README.md file to use as the long description
with open(path.join(working_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Define the setup configuration
setup(
    name='poirot',  # The name of your package
    version='0.0.1',  # The version of your package
    url='https://github.com/CodingLife1024/Poirot',  # URL to the project’s repository
    author='Riddhidipta Pal',  # The author's name
    author_email='riddhidipta.iitd@gmail.com',  # The author's email
    description='Poirot',  # Short description of your package
    long_description=long_description,  # Long description (from README.md)
    long_description_content_type='text/markdown',  # Type of the long description (Markdown)
    packages=find_packages(),  # Automatically find all packages in the project directory
    install_requires=[],  # List of dependencies, if any
)
