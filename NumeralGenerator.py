class NumeralGenerator:
	def __init__(self, name):
		self.name = name
	
	def get1(self, i, isNoZero=False):
		return ''
	
	def get10(self, ii, i, isNoZero=False):
		return ''
	
	def get100(self, iii, ii, i, isNoZero=False):
		return ''
	
	def get1000(self, iv, iii, ii, i, isNoZero=False):
		return ''

class NumeralGeneratorChineseHanzi(NumeralGenerator):
	def __init__(self):
		NumeralGenerator.__init__(self, 'chinese_hanzi')
		self.ones = [
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
		self.twoAlt = '两'
		self.oneTen = '十'
		self.oneHundred = '百'
		self.oneThousand = '千'

	def get1(self, i, isNoZero=False):
		if isNoZero and i == 0:
			return ''
		return self.ones[i]

	def get10(self, ii, i, isNoZero=False):
		if ii == 0:
			return self.get1(i, isNoZero)
		elif ii == 1:
			return self.oneTen + self.get1(i, True)
		else:
			return self.get1(ii, True) + self.oneTen + self.get1(i, True)

	def get100(self, iii, ii, i, isNoZero=False):
		if iii == 0:
			return self.get10(ii, i, isNoZero)
		elif iii == 2:
			return self.twoAlt + self.oneHundred + self.get10(ii, i, True)
		else:
			return self.get1(iii, True) + self.oneHundred + self.get10(ii, i, True)

	def get1000(self, iv, iii, ii, i, isNoZero=False):
		if iv == 0:
			return self.get100(iii, ii, i, isNoZero)
		elif iv == 2:
			return self.twoAlt + self.oneThousand + self.get100(iii, ii, i, True)
		else:
			return self.get1(iv, True) + self.oneThousand + self.get100(iii, ii, i, True)

class NumeralGeneratorChineseMandarin(NumeralGenerator):
	def __init__(self):
		NumeralGenerator.__init__(self, 'chinese_mandarin')		
		self.ones = [
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
		self.twoAlt = 'liǎng'
		self.oneTen = 'shí'
		self.oneHundred = 'bǎi'
		self.oneThousand = 'qiān'

	def get1(self, i, isNoZero=False):
		if isNoZero and i == 0:
			return ''
		return self.ones[i]

	def get10(self, ii, i, isNoZero=False):
		if ii == 0:
			return self.get1(i, isNoZero)
		elif ii == 1:
			return self.oneTen + ' ' + self.get1(i, True)
		else:
			return self.get1(ii, True) + ' ' + self.oneTen + ' ' + self.get1(i, True)

	def get100(self, iii, ii, i, isNoZero=False):
		if iii == 0:
			return self.get10(ii, i, isNoZero)
		elif iii == 2:
			return self.twoAlt + ' ' + self.oneHundred + ' ' + self.get10(ii, i, True)
		else:
			return self.get1(iii, True) + ' ' + self.oneHundred + ' ' + self.get10(ii, i, True)

	def get1000(self, iv, iii, ii, i, isNoZero=False):
		if iv == 0:
			return self.get100(iii, ii, i, isNoZero)
		elif iv == 2:
			return self.twoAlt + ' ' + self.oneThousand + ' ' + self.get100(iii, ii, i, True)
		else:
			return self.get1(iv, True) + ' ' + self.oneThousand + ' ' + self.get100(iii, ii, i, True)

class NumeralGeneratorFinnish(NumeralGenerator):
	def __init__(self):
		NumeralGenerator.__init__(self, 'finnish')	
		self.ones = [
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
	
	def get1(self, i, isNoZero=False):
		if isNoZero and i == 0:
			return ''
		return self.ones[i]
	
	def get10(self, ii, i, isNoZero=False):
		if ii == 0:
			return self.get1(i, isNoZero)
		elif ii == 1 and i == 0:
			return 'kymmenen'
		elif ii == 1:
			return self.get1(i, True) + 'toista'
		else:
			return self.get1(ii, True) + 'kymmentä' + ' ' + self.get1(i, True)
	
	def get100(self, iii, ii, i, isNoZero=False):
		if iii == 0:
			return self.get10(ii, i, isNoZero)
		elif iii == 1:
			return 'sata' + ' ' + self.get10(ii, i, True)
		else:
			return self.get1(iii, True) + 'sataa' + ' ' + self.get10(ii, i, True)
	
	def get1000(self, iv, iii, ii, i, isNoZero=False):
		if iv == 0:
			return self.get100(iii, ii, i, isNoZero)
		elif iv == 1:
			return 'tuhat' + ' ' + self.get100(iii, ii, i, True)
		else:
			return self.get1(iv, True) + 'tuhatta' + ' ' + self.get100(iii, ii, i, True)

class NumeralGeneratorTurkish(NumeralGenerator):
	def __init__(self):
		NumeralGenerator.__init__(self, 'turkish')
		self.ones = [
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
		self.tens = [
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
		self.oneHundred = 'yüz'
		self.oneThousand = 'bin'

	def get1(self, i, isNoZero=False):
		if isNoZero and i == 0:
			return ''
		return self.ones[i]

	def get10(self, ii, i, isNoZero=False):
		if ii == 0:
			return self.get1(i, isNoZero)
		elif i == 0:
			return self.tens[ii]
		else:
			return self.tens[ii] + ' ' + self.get1(i, True)

	def get100(self, iii, ii, i, isNoZero=False):
		if iii == 0:
			return self.get10(ii, i, isNoZero)
		elif iii == 1:
			return self.oneHundred + ' ' + self.get10(ii, i, True)
		else:
			return self.get1(iii, True) + ' ' + self.oneHundred + ' ' + self.get10(ii, i, True)

	def get1000(self, iv, iii, ii, i, isNoZero=False):
		if iv == 0:
			return self.get100(iii, ii, i, isNoZero)
		elif iv == 1:
			return self.oneThousand + ' ' + self.get100(iii, ii, i, True)
		else:
			return self.get1(iv, True) + ' ' + self.oneThousand + ' ' + self.get100(iii, ii, i, True)

class NumeralGeneratorVietnamese(NumeralGenerator):
	def __init__(self):
		NumeralGenerator.__init__(self, 'vietnamese')
		# 1000 = một nghìn
		# 1001 = một nghìn - không trăm - linh một
		# 1009 = một nghìn - không trăm - linh chín
		# 1010 = một nghìn - không trăm - mười
		# 1020 = một nghìn - không trăm - hai mươi
		# compare with:
		# 1109 = một nghìn - một trăm - linh chín
		# 1110 = một nghìn - một trăm - mười
		# 1120 = một nghìn - một trăm - hai mươi
		self.ones = [
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
		self.zeroAlt = 'linh'
		self.oneAlt = 'mốt' # for 21-91
		self.fiveAlt = 'lăm' # for 15-95, e.g. 35 = ba mươi lăm and 535 = năm trăm ba mươi lăm
		self.oneTen = 'mười'
		self.oneTenAlt = 'mươi' # for 20-90
		self.oneHundred = 'trăm'
		self.oneThousand = 'nghìn'

	def get1(self, i, isNoZero=False, isAltOne=False, isAltFive=False):
		if isNoZero and i == 0:
			return ''
		if isAltOne and i == 1:
			return self.oneAlt
		if isAltFive and i == 5:
			return self.fiveAlt
		return self.ones[i]

	def get10(self, ii, i, isNoZero=False):
		if ii == 0:
			return self.get1(i, isNoZero)
		elif ii == 1:
			return self.oneTen + ' ' + self.get1(i, True, isAltFive=True)
		else:
			return self.get1(ii, True) + ' ' + self.oneTenAlt + ' ' + self.get1(i, True, isAltOne=True, isAltFive=True)

	def get100(self, iii, ii, i, isNoZero=False, hasZeroOrdinal=False):
		if iii == 0 and not hasZeroOrdinal:
			return self.get10(ii, i, isNoZero)
		elif ii == 0 and i != 0:
			return self.get1(iii, not hasZeroOrdinal) + ' ' + self.oneHundred + ' ' + self.zeroAlt + ' ' + self.get10(ii, i, True)
		else:
			return self.get1(iii, not hasZeroOrdinal) + ' ' + self.oneHundred + ' ' + self.get10(ii, i, True)

	def get1000(self, iv, iii, ii, i, isNoZero=False):
		if iv == 0:
			return self.get100(iii, ii, i, isNoZero)
		else:
			isZeroOrdinal = (iii == 0 and not (ii == 0 and i == 0))
			return self.get1(iv, True) + ' ' + self.oneThousand + ' ' + self.get100(iii, ii, i, True, hasZeroOrdinal=isZeroOrdinal)
