ones = [
	'tyhjä', # 0
	'yksi', # 1
	'kaksi', # 2
	'kolme', # 3
	'neljä', # 4
	'viisi', # 5
	'kuusi', # 6
	'seitsemän', # 7
	'kahdeksan', # 8
	'yhdeksän' # 9
]

def get1(x, isNoZero=False):
	if isNoZero and x == 0:
		return ''
	return ones[x]

def get10(xx, x, isNoZero=False):
	if xx == 0:
		return get1(x, isNoZero)
	elif xx == 1 and x == 0:
		return 'kymmenen'
	elif xx == 1:
		return get1(x, True) + 'toista'
	else:
		return get1(xx, True) + 'kymmentä' + get1(x, True)

def get100(xxx, xx, x, isNoZero=False):
	if xxx == 0:
		return get10(xx, x, isNoZero)
	elif xxx == 1:
		return 'sata' + get10(xx, x, True)
	else:
		return get1(xxx, True) + 'sataa' + get10(xx, x, True)

def get1000(iv, xxx, xx, x, isNoZero=False):
	if iv == 0:
		return get100(xxx, xx, x, isNoZero)
	elif iv == 1:
		return 'tuhat' + get100(xxx, xx, x, True)
	else:
		return get1(iv, True) + 'tuhatta' + get100(xxx, xx, x, True)

# Generate numbers up to 9999
for iv in range(10):
	for xxx in range(10):
		for xx in range(10):
			for x in range(10):
				result = get1000(iv, xxx, xx, x)
				print('{}\t{}{}{}{}'.format(result, iv, xxx, xx, x))
