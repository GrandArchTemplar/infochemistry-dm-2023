def solution(expr, n):
    expr = expr.strip("()")
    a, terms = expr.split("*", 1)
    x, second_part = terms.split("+", 1)
    b, y = second_part.split("*")

    a = float(a) if '.' in a else int(a)
    b = float(b) if '.' in b else int(b)

    def binomial_coefficient(n, k):
        if k == 0 or k == n:
            return 1
        return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)

    terms = []
    for k in range(n+1):
        coeff = binomial_coefficient(n, k) * (a ** (n-k)) * (b ** k)
        term = f'{coeff:.6g}'
        if n-k > 0:
            term += f"*{x}" if n-k == 1 else f"*{x}**{n-k}"
        if k > 0:
            term += f"*{y}" if k == 1 else f"*{y}**{k}"
        terms.append(term)

    return " + ".join(terms)


 
# Test 1 
# test_input = input()# "(0.5*a + 4*b)" 
# test_n = int(input())# 3 
test_input = "(0.5*a + 4*b)"
test_n = 3
print(solution(test_input, test_n))