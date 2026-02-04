def mean(x):
    return sum(x)/len(x)

def std(x):
    m = mean(x)
    return (sum((xi-m)**2 for xi in x)/len(x))**0.5

__all__ = ['mean','std']