ones = [
	'sıfır', # 0
	'bir', # 1
	'iki', # 2
	'üç', # 3
	'dört', # 4
	'beş', # 5
	'altı', # 6
	'yedi', # 7
	'sekiz', # 8
	'dokuz' # 9
]

tens = [
	'', # 0
	'on', # 1
	'yirmi', # 2
	'otuz', # 3
	'kırk', # 4
	'elli', # 5
	'altmış', # 6
	'yetmiş', # 7
	'seksen', # 8
	'doksan' # 9
]

oneHundred = 'yüz'

oneThousand = 'bin'

def get1(i, isNoZero=False):
	if isNoZero and i == 0:
		return ''
	return ones[i]

def get10(ii, i, isNoZero=False):
	if ii == 0:
		return get1(i, isNoZero)
	elif i == 0:
		return tens[ii]
	else:
		return tens[ii] + ' ' + get1(i, True)

def get100(iii, ii, i, isNoZero=False):
	if iii == 0:
		return get10(ii, i, isNoZero)
	elif iii == 1:
		return oneHundred + ' ' + get10(ii, i, True)
	else:
		return get1(iii, True) + ' ' + oneHundred + ' ' + get10(ii, i, True)

def get1000(iv, iii, ii, i, isNoZero=False):
	if iv == 0:
		return get100(iii, ii, i, isNoZero)
	elif iv == 1:
		return oneThousand + ' ' + get100(iii, ii, i, True)
	else:
		return get1(iv, True) + ' ' + oneThousand + ' ' + get100(iii, ii, i, True)

# Generate numbers up to 9999
for x in range(10000):
	xStr = '{:04d}'.format(x)
	result = get1000(int(xStr[0]), int(xStr[1]), int(xStr[2]), int(xStr[3]))
	print('{}\t{:04d}'.format(result, x))
