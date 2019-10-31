import numpy as np

class City:
    def __init__(self):
        self.name = ""


lille = City()
paris = City()
tokyo = City()
arr = np.array([lille, paris, tokyo])
print(arr)