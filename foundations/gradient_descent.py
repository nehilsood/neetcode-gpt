class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        minimizer = init

        for _ in range(iterations):
            derivative = 2 * minimizer ## d(f(x)) = 2*x
            minimizer = minimizer - (learning_rate * derivative)
        
        return round(minimizer,5)


        
    