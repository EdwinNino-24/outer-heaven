class LinearCongruence:
    def __init__(self, xo, n, k, c, g, min_val, max_val):
        self.xo = xo
        self.n = n
        self.k = k
        self.c = c
        self.g = g
        self.min_val = min_val
        self.max_val = max_val
        
    def generate(self):
        a = 1 + 2 * self.k
        m = 2 ** self.g
        results = []
        xi = self.xo

        for _ in range(self.n):
            xi = (a * xi + self.c) % m
            Ri = xi / (m - 1)
            Ni = self.min_val + Ri * (self.max_val - self.min_val)
            results.append([round(xi, 5), round(Ri, 5), round(Ni, 5)])

        return results