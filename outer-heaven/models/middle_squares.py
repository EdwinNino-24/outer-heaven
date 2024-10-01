class MiddleSquares:
    def __init__(self, seed, num_iterations, n_digits, a, b):
        self.seed = seed
        self.num_iterations = num_iterations
        self.n_digits = n_digits
        self.a = a
        self.b = b

    def generate(self):
        result = []

        for _ in range(self.num_iterations):
            seed_squared = str(self.seed ** 2).zfill(2 * self.n_digits)

            start = (len(seed_squared) - self.n_digits) // 2
            new_seed = int(seed_squared[start:start + self.n_digits])

            random_num = new_seed / (10 ** self.n_digits)

            mapped_value = self.a + (self.b - self.a) * random_num

            result.append([round(self.seed, 5), round(random_num, 5), round(mapped_value, 5)])

            self.seed = new_seed

        return result