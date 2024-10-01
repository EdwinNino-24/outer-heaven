class MultiplicativeCongruence:
    def __init__(self, xo, n, t, g, min_val, max_val):
        self.xo = xo
        self.n = n
        self.t = t
        self.g = g
        self.min_val = min_val
        self.max_val = max_val
        
    def generate(self):
        a = 8 * self.t + 3
        m = 2 ** self.g
        
        results = []
        
        for _ in range(self.n):
            xi = (a * self.xo) % m
            Ri = xi / (m - 1)
            Ni = self.min_val + Ri * (self.max_val - self.min_val)
            
            results.append([round(xi, 5), round(Ri, 5), round(Ni, 5)])
            
            self.xo = xi
        
        return results