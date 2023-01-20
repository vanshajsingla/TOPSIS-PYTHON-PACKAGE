import numpy as np
from .topsis import normalize_matrix, calculate_relative_closeness, determine_final_ranking
__version__ = '0.1'

from setuptools import setup, find_packages

setup(
    name='topsis',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/vanshajsingla/TOPSIS-PYTHON-PACKAGE/blob/main/102003346.py',
    author='Vanshaj Singla',
    author_email='vanshajrnv2002@gmail.com',
    description='A python package for implementing the TOPSIS method',
    install_requires=[
        'numpy'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)


def normalize_matrix(matrix, impact):
    """
    Normalize the decision matrix by dividing each element by the
    square root of the sum of squares of the elements in the corresponding column
    """
    for i in range(matrix.shape[1]):
        if impact[i] == "max":
            matrix[:, i] = matrix[:, i] / np.sqrt(np.sum(np.square(matrix[:, i])))
        else:
            matrix[:, i] = -1 * matrix[:, i] / np.sqrt(np.sum(np.square(matrix[:, i])))
    return matrix

def calculate_relative_closeness(matrix, weights):
    """
    Calculate the relative closeness values for each alternative
    """
    weighted_matrix = np.multiply(matrix, weights)
    relative_closeness = np.sum(weighted_matrix, axis=1)
    return relative_closeness

def determine_final_ranking(matrix, weights, impact):
    """
    Determine the final ranking of the alternatives based on their relative closeness values
    """
    normalized_matrix = normalize_matrix(matrix, impact)
    relative_closeness = calculate_relative_closeness(normalized_matrix, weights)
    ranking = np.argsort(relative_closeness)
    return ranking
