def mcs_length(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])
            else:
                dp[i][j] = 0
    print("print table c: \n")
    for row in dp:
        print(row)
    

    return max_length

# Example usage:
X = "algorithm"
Y = "logarithm"
print(mcs_length(X, Y))  # Output: 6