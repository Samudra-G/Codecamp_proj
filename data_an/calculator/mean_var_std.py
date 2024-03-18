import numpy as np
def calculate(x):
    try:
        #list -> 3*3 array
        arr = np.array(x).reshape(3,3)
        #dictionary to calculate what's needed:
        results = {
        'mean': [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(), arr.mean().tolist()],
        'variance': [arr.var(axis=0).tolist(), arr.var(axis=1).tolist(), arr.var().tolist()],
        'standard deviation': [arr.std(axis=0).tolist(), arr.std(axis=1).tolist(), arr.std().tolist()],
        'max': [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), arr.max().tolist()],
        'min': [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), arr.min().tolist()],
        'sum': [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), arr.sum().tolist()]
        }
        return results
    except ValueError:
        print("Input list should contain 9 elements")
        return None

