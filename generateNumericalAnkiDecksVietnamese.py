from file_io import load_file_to_str, save_str_to_file

# NOTE: WIP. need to figure out how to deal with 1001 = 'một nghìn không trăm linh một' (expected) instead of 'một nghìn một' (actual).
# 1000 = một nghìn
# 1001 = một nghìn - không trăm - linh một
# 1009 = một nghìn - không trăm - linh chín
# 1010 = một nghìn - không trăm - mười
# 1020 = một nghìn - không trăm - hai mươi
# compare with:
# 1109 = một nghìn - một trăm - linh chín
# 1110 = một nghìn - một trăm - mười
# 1120 = một nghìn - một trăm - hai mươi
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

def get100(iii, ii, i, isNoZero=False, hasZeroOrdinal=False):
	if iii == 0 and not hasZeroOrdinal:
		return get10(ii, i, isNoZero)
	elif ii == 0 and i != 0:
		return get1(iii, not hasZeroOrdinal) + ' ' + oneHundred + ' ' + zeroAlt + ' ' + get10(ii, i, True)
	else:
		return get1(iii, not hasZeroOrdinal) + ' ' + oneHundred + ' ' + get10(ii, i, True)

def get1000(iv, iii, ii, i, isNoZero=False):
	if iv == 0:
		return get100(iii, ii, i, isNoZero)
	else:
		isZeroOrdinal = (iii == 0 and not (ii == 0 and i == 0))
		return get1(iv, True) + ' ' + oneThousand + ' ' + get100(iii, ii, i, True, hasZeroOrdinal=isZeroOrdinal)

# Generate numbers
def getListOfNumerals(start, end):
	daList = ''
	for x in range(start, end+1):
		xStr = '{:04d}'.format(x)
		result = get1000(int(xStr[0]), int(xStr[1]), int(xStr[2]), int(xStr[3]))
		daList += '{}\t{}\n'.format(result, x)
	return daList

save_str_to_file('first_20_numerals_vietnamese.txt', getListOfNumerals(0, 20))
save_str_to_file('numerals_to_9999_vietnamese.txt', getListOfNumerals(21, 9999))
