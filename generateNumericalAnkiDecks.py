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
oneHundred = 'sata'
oneThousand = 'tuhat'

def generateTens(xx, x):
	# Edge case for ten
	if (xx == 1 and x == 0):
		return oneTen
	# 2# or more
	elif (tens[xx].count('{') == 2):
		one = ones[x] if x != 0 else ''
		return tens[xx].format(ones[xx], one)
	# 1#
	else:
		return tens[xx].format(ones[x])

def generateHundreds(xxx, xx, x):
	# Edge case for non-hundreds
	if (xxx == 0):
		return generateTens(xx, x)
	# Edge case for hundred
	elif (xxx == 1 and xx == 0 and x == 0):
		return oneHundred
	# 1##
	elif (xxx == 1):
		return oneHundred + generateTens(xx, x)
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


