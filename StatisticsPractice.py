import numpy as np
import collections as c
import matplotlib.pyplot as plt

def mean(x):
    return sum(x) / len(x)

def median(v):
    """ finds the 'middle most' value of v """
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        # if odd, return the middle value
        return sorted_v[midpoint]
    else:
        # if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

def quantile(x, p):
    """ returns the pth - percentile in x """
    p_index = int(p * len(x))
    return sorted(x)[p_index]

def mode(x):
    """ returns a list, might be more than one mode """
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems()
            if count == max_count]

def data_range(x):
    return max(x) - min(x)

def de_mean(x):
    """ translate x by subtracting its mean """
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    """ assume sx has atleast two elements """
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n-1)

def covariance(x, y):
    n = len(x)
    return dot(de_mean(a), de_mean(y)) / (n - 1)
