def findRoot(x, power, epsilon):
	"""x どepsilon >0 は整数もしくは浮動小数点数、power >=1を整数と仮定
	y**power が x の epsilon 以内になるような浮動小数点数 y を返す
	もし、そのような浮動小数点数が存在しなければNoneを返す"""

	if x < 0 and power%2 == 0: # 負の数は平方根を持たない
		return None

	low = min(-1.0, x)
	high = max(1.0, x)
	ans = (high + low)/2.0
	while abs(ans**power - x) >= epsilon:
		if ans**power < x:
			low = ans
		else:
			high = ans
		ans = (high + low)/2.0
	return ans

def testFindRoot():
	epsilon = 0.0001
	for x in (0.25, -0.25, 2, -2, 8, -8):
		for power in range(1, 4):
			print('Testing x = ', str(x), ' and power =', power)
			result = findRoot(x, power, epsilon)
			if result == None:
				print(' No root')
			else:
				print(' ', result**power, '~=', x)

def factI(n):
	"""
	:param n: n>0 の整数
	:return: n! を返す
	"""
	result = 1
	while n > 1:
		result = result * n
		n -= 1

def factR(n):
	"""
	:param n: n>0 の整数
	:return: n! を返す
	"""
	if n == 1:
		return n
	else:
		return n*factR(n-1)

def fib(n):
	"""
	:param n: 整数
	:return: フィボナッチ数列
	"""
	if n == 0 or n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

def testFib(n):
	for i in range(n):
		res = fib(i)
		print('fib of', i, ' =', res)

def isPalindrome(s):
	"""
	:param s: 文字列
	:return: sが回文ならTrue、そうでなければFalse
	"""

	def toChars(s):
		s = s.lower()
		letters = ''
		for c in s:
			if c in 'abcdefghijklmnopqrstuvwxyz':
				letters = letters + c
		return letters

	def isPal(s):
		if len(s) <= 1:
			return True
		else:
			return s[0] == s[-1] and isPal(s[1:-1])

	return isPal(toChars(s))
