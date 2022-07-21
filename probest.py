from math import e as eConstant
from functools import reduce

sum = lambda k, n, expr = lambda z : z : 0 if n < k else reduce(lambda a, b : a + b, list(map(expr, list(range(k, n + 1)))))
prod = lambda k, n, expr = lambda z : z : 0 if n < k else reduce(lambda a, b : a * b, list(map(expr, list(range(k, n + 1)))))

factorial = lambda n : 1 if n <= 1 else reduce(lambda x, y: x * y, list(range(1, n + 1)))
choose = lambda n, p : factorial(n) / (factorial(p) * (factorial(n - p)))

# Modelo Binomial
dbinom = lambda x, n, p : choose(n, x) * p ** x * (1 - p) ** (n - x)
pbinom = lambda x, n, p : sum(0, x, lambda i : dbinom(i, n, p))

# Modelo de Poisson
dpois = lambda x, λ : (λ ** x * eConstant ** -λ) / factorial(x)
ppois = lambda x, λ : sum(0, x, lambda i : dpois(i, λ))
