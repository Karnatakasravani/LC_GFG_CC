count = 0
        sqrt_N = int(N ** 0.5)
        for i in range(1, sqrt_N + 1):
            if N % i == 0:
                if i % 3 == 0:
                    count += 1
                divisor = N // i
                if divisor != i and divisor % 3 == 0:
                    count += 1
        return count
