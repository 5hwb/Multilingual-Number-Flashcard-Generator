# NOTE: WIP. need to figure out how to deal with 1001 = 'một nghìn không trăm linh một' (expected) instead of 'một nghìn một' (actual).
ones = [
	'không', # 0
	'một', # 1
	'hai', # 2
	'ba', # 3
	'bốn', # 4
	'năm', # 5
	'sáu', # 6
	'bảy', # 7
	'tám', # 8
	'chín' # 9
]

zeroAlt = 'linh'
oneAlt = 'mốt' # for 21-91
fiveAlt = 'lăm' # for 15-95, e.g. 35 = ba mươi lăm and 535 = năm trăm ba mươi lăm

oneTen = 'mười'
oneTenAlt = 'mươi' # for 20-90

oneHundred = 'trăm'

oneThousand = 'nghìn'

def get1(i, isNoZero=False, isAltOne=False, isAltFive=False):
	if isNoZero and i == 0:
		return ''
	if isAltOne and i == 1:
		return oneAlt
	if isAltFive and i == 5:
		return fiveAlt
	return ones[i]

def get10(ii, i, isNoZero=False):
	if ii == 0:
		return get1(i, isNoZero)
	elif ii == 1:
		return oneTen + ' ' + get1(i, True, isAltFive=True)
	else:
		return get1(ii, True) + ' ' + oneTenAlt + ' ' + get1(i, True, isAltOne=True, isAltFive=True)

def get100(iii, ii, i, isNoZero=False):
	if iii == 0:
		return get10(ii, i, isNoZero)
	elif ii == 0 and i != 0:
		return get1(iii, True) + ' ' + oneHundred + ' ' + zeroAlt + ' ' + get10(ii, i, True)
	else:
		return get1(iii, True) + ' ' + oneHundred + ' ' + get10(ii, i, True)

def get1000(iv, iii, ii, i, isNoZero=False):
	if iv == 0:
		return get100(iii, ii, i, isNoZero)
	else:
		return get1(iv, True) + ' ' + oneThousand + ' ' + get100(iii, ii, i, True)

# Generate numbers up to 9999
for x in range(10000):
	xStr = '{:04d}'.format(x)
	result = get1000(int(xStr[0]), int(xStr[1]), int(xStr[2]), int(xStr[3]))
	print('{}\t{}'.format(result, x))
