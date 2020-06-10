def lcs(X, Y):
    m = len(X)
    n = len(Y)
    table = [[0 for x in range(n + 1)] for y in range(m + 1)]
    for i in range(1, m + 1):
	for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
		table[i][j] = table[i - 1][j - 1] + 1
	    else:
		table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return table[m][n]

S1=input()
S2=input()
print(lcs(S1,S2))
