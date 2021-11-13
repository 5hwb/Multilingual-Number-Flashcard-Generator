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

tens = [
	'{}', # 0#
	'{}toista', # 1#
	'{}kymmentä{}', # 2#
	'{}kymmentä{}', # 3#
	'{}kymmentä{}', # 4#
	'{}kymmentä{}', # 5#
	'{}kymmentä{}', # 6#
	'{}kymmentä{}', # 7#
	'{}kymmentä{}', # 8#
	'{}kymmentä{}' # 9#
]

hundreds = [
	'{}', # 0##
	'sata{}', # 1##
	'{}sataa{}', # 2##
	'{}sataa{}', # 3##
	'{}sataa{}', # 4##
	'{}sataa{}', # 5##
	'{}sataa{}', # 6##
	'{}sataa{}', # 7##
	'{}sataa{}', # 8##
	'{}sataa{}', # 9##
]

oneTen = 'kymmenen'

def generateTens(xx, x):
	# Edge case for ten
	if (xx == 1 and x == 0):
		return oneTen
	# 1#
	elif (tens[xx].count('{') == 1):
		return tens[xx].format(ones[x])
	# 2# or more
	else:
		one = ones[x] if x != 0 else ''
		return tens[xx].format(ones[xx], one)

def generateHundreds(xxx, xx, x):
	# Edge case for non-hundreds
	if (xxx == 0):
		return generateTens(xx, x)
	# 0## or 1##
	elif (hundreds[xxx].count('{') == 1):
		ten = generateTens(xx, x) if not (xx == 0 and x == 0) else ''
		return hundreds[xxx].format(ten)	
	# 2## or more
	else:
		hundred = ones[xxx] if xxx != 0 else ''
		ten = generateTens(xx, x) if not (xx == 0 and x == 0) else ''
		return hundreds[xxx].format(hundred, ten)

for xxx in range(0, 10):
	for xx in range(0, 10):
		for x in range(0, 10):
			result = generateHundreds(xxx, xx, x)
			print('{}{}{}: {}'.format(xxx, xx, x, result))
