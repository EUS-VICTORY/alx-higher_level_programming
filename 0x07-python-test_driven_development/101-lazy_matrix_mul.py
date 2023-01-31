#!/usr/bin/python3
"""
Module made up of a function that multiplies two matrices
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Function that multiplies two matrices 
    Args:
        m_a: matix a
        m_b: matrix b

    Returns:
        result of teh multiplication
    """

    return (np.matmul(m_a, m_b))
