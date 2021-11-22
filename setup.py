from setuptools import setup, find_packages
import codecs
import os

with open("README.md") as f:
    long_description = f.read()

VERSION = '1.0'
DESCRIPTION = 'Important Packages for Machine Learning. \n Installed in a \'One Click\' '

# Setting up
setup(
    name="CEAI_005",
    version=VERSION,
    author="karrtik159",
    author_email="karrtikbaheti19@gnu.ac.in",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pandas', 'numpy', 'scipy', 'matplotlib', 'seaborn', 
                      'scikit-learn', 'statsmodels', 'pyforest', 'pycaret', 'Flask', 'fastapi',
                      'jupyter', 'xgboost', 'imbalanced-learn', 'bokeh', 'kat',
                      'Boruta', 'spyder', 'mlxtend', 'lightgbm', 'catboost',
                      'tensorflow-cpu==2.6.0', 'tensorflow-gpu==2.6.0'],
    keywords=['CEAI_005', 'Machine Learning in a single file', 'AI', 'ML', 'Machine Learning'],
    url='http://github.com/karrtik159',
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    platforms=["any"],
    zip_safe=True,
)