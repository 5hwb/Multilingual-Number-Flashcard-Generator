from file_io import load_file_to_str, save_str_to_file

ones = [
	'líng', # 0
	'yī', # 1
	'èr', # 2
	'sān', # 3
	'sì', # 4
	'wǔ', # 5
	'liù', # 6
	'qī', # 7
	'bā', # 8
	'jiǔ' # 9
]

twoAlt = 'liǎng'

oneTen = 'shí'

oneHundred = 'bǎi'

oneThousand = 'qiān'

def get1(i, isNoZero=False):
	if isNoZero and i == 0:
		return ''
	return ones[i]

def get10(ii, i, isNoZero=False):
	if ii == 0:
		return get1(i, isNoZero)
	elif ii == 1:
		return oneTen + ' ' + get1(i, True)
	else:
		return get1(ii, True) + ' ' + oneTen + ' ' + get1(i, True)

def get100(iii, ii, i, isNoZero=False):
	if iii == 0:
		return get10(ii, i, isNoZero)
	elif iii == 2:
		return twoAlt + ' ' + oneHundred + ' ' + get10(ii, i, True)
	else:
		return get1(iii, True) + ' ' + oneHundred + ' ' + get10(ii, i, True)

def get1000(iv, iii, ii, i, isNoZero=False):
	if iv == 0:
		return get100(iii, ii, i, isNoZero)
	elif iv == 2:
		return twoAlt + ' ' + oneThousand + ' ' + get100(iii, ii, i, True)
	else:
		return get1(iv, True) + ' ' + oneThousand + ' ' + get100(iii, ii, i, True)

# Generate numbers
def getListOfNumerals(start, end):
	daList = ''
	for x in range(start, end+1):
		xStr = '{:04d}'.format(x)
		result = get1000(int(xStr[0]), int(xStr[1]), int(xStr[2]), int(xStr[3]))
		daList += '{}\t{}\n'.format(result, x)
	return daList

save_str_to_file('first_20_numerals_mandarin_chinese.txt', getListOfNumerals(0, 20))
save_str_to_file('numerals_to_9999_mandarin_chinese.txt', getListOfNumerals(21, 9999))
