import numpy as np
from .topsis import normalize_matrix, calculate_relative_closeness, determine_final_ranking
__version__ = '0.1'

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
