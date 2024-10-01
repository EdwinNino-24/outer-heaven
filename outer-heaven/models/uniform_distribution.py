import random

class UniformDistribution:
    def __init__(self, min_value, max_value, quantity):
        self.quantity = quantity
        self.min_value = min_value
        self.max_value = max_value
        self.results = []

    def generate(self):
        while self.quantity > 0:
            random_number = random.uniform(self.min_value, self.max_value)
            xi = float(random_number) / 10000.0  
            Ri = float(random_number) / 10000.0  
            Ni = self.min_value + (self.max_value - self.min_value) * xi
            
            self.results.append([round(xi, 5), round(Ri, 5), round(Ni, 5)])
            
            self.quantity -= 1

        return self.results