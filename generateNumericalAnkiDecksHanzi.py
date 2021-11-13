ones = [
	'零', # 0
	'一', # 1
	'二', # 2
	'三', # 3
	'四', # 4
	'五', # 5
	'六', # 6
	'七', # 7
	'八', # 8
	'九' # 9
]

twoAlt = '两'

oneTen = '十'

oneHundred = '百'

oneThousand = '千'

def get1(i, isNoZero=False):
	if isNoZero and i == 0:
		return ''
	return ones[i]

def get10(ii, i, isNoZero=False):
	if ii == 0:
		return get1(i, isNoZero)
	elif ii == 1:
		return oneTen + get1(i, True)
	else:
		return get1(ii, True) + oneTen + get1(i, True)

def get100(iii, ii, i, isNoZero=False):
	if iii == 0:
		return get10(ii, i, isNoZero)
	elif iii == 2:
		return twoAlt + oneHundred + get10(ii, i, True)
	else:
		return get1(iii, True) + oneHundred + get10(ii, i, True)

def get1000(iv, iii, ii, i, isNoZero=False):
	if iv == 0:
		return get100(iii, ii, i, isNoZero)
	elif iv == 2:
		return twoAlt + oneThousand + get100(iii, ii, i, True)
	else:
		return get1(iv, True) + oneThousand + get100(iii, ii, i, True)

# Generate numbers up to 9999
for x in range(10000):
	xStr = '{:04d}'.format(x)
	result = get1000(int(xStr[0]), int(xStr[1]), int(xStr[2]), int(xStr[3]))
	print('{}\t{}'.format(result, x))
