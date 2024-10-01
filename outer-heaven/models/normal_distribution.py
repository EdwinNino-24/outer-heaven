import random
import math

class NormalDistribution:
    def __init__(self, mu, sigma, quantity):
        self.mu = mu
        self.sigma = sigma
        self.quantity = quantity
        self.results = []

    def generate(self):
        while self.quantity > 0:
            u1 = random.random()
            u2 = random.random()
            z0 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
            random_number = self.mu + z0 * self.sigma

            xi = random.uniform(self.mu - 3 * self.sigma, self.mu + 3 * self.sigma)
            Ri = (random_number - self.mu) / self.sigma
            Ni = self.mu + xi * self.sigma
            
            self.results.append([round(xi, 5), round(Ri, 5), round(Ni, 5)])

            self.quantity -= 1
        
        return self.results