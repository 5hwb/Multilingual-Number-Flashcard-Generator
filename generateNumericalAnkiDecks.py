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

oneTen = 'kymmenen'
oneHundred = 'sata'

for xx in range(0, 10):
	for x in range(0, 10):
		# Edge case for ten
		if (xx == 1 and x == 0):
			result = oneTen
			print('{}{}: {}'.format(xx, x, result))
		elif (tens[xx].count('{') == 2):
			one = ones[x] if x != 0 else ''
			result = tens[xx].format(ones[xx], one)
			print('{}{}: {}'.format(xx, x, result))
		else:
			result = tens[xx].format(ones[x])
			print('{}{}: {}'.format(xx, x, result))

