#x**2 - 24 = 0 で誤差がepsilon以下になるxを求める
epsilon = 0.01
k = 24.0
guess = k/2.0
times = 0
while abs(guess**2 - k) >= epsilon:
	times += 1
	guess = guess - (((guess**2) - k)/(2*guess))
	print('[', times, ']guess =', guess)
print('Square root of', k, 'is about', guess)