g, h, q = [int(i) for i in input().split()]

def discrete_log(g, h, q):
    N = int(q**0.5) + 1
    giant_step = pow(g, N, q)

    baby_steps = {}
    for i in range(N):
        baby_steps[pow(g, i, q)] = i

    inverse_giant_step = pow(giant_step, q - 2, q)
    for j in range(N):
        y = (h * pow(inverse_giant_step, j, q)) % q
        if y in baby_steps:
            return j * N + baby_steps[y]

result = discrete_log(g, h, q)
print(result)
