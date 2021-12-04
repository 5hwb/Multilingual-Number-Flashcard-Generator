class NumeralGenerator:
	'''
	Base class for all NumeralGenerators for each language
	'''
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
	'''
	Numeral generator for Chinese (hanzi)
	'''
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
	'''
	Numeral generator for Chinese (Mandarin)
	'''
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

class NumeralGeneratorEnglish(NumeralGenerator):
	'''
	Numeral generator for English
	'''
	def __init__(self):
		NumeralGenerator.__init__(self, 'english')	
		self.ones = [
			'zero', # 0
			'one', # 1
			'two', # 2
			'three', # 3
			'four', # 4
			'five', # 5
			'six', # 6
			'seven', # 7
			'eight', # 8
			'nine' # 9
		]
		self.teens = [
			'', # 10
			'eleven', # 11
			'twelve', # 12
			'thirteen', # 13
			'fourteen', # 14
			'fifteen', # 15
			'sixteen', # 16
			'seventeen', # 17
			'eighteen', # 18
			'nineteen' # 19
		]
		self.tens = [
			'', # 0
			'ten', # 10
			'twenty', # 20
			'thirty', # 30
			'forty', # 40
			'fifty', # 50
			'sixty', # 60
			'seventy', # 70
			'eighty', # 80
			'ninety' # 90
		]
		self.hundred = 'hundred'
		self.thousand = 'thousand'
	
	def get1(self, i, isNoZero=False):
		if isNoZero and i == 0:
			return ''
		return self.ones[i]
	
	def get10(self, ii, i, isNoZero=False):
		if ii == 0: # < 10
			return self.get1(i, isNoZero)
		elif ii == 1 and i == 0: # 10
			return self.tens[ii]
		elif ii == 1: # 11-19 
			return self.teens[i]
		elif i == 0: # 20, 30, 40...
			return self.tens[ii]
		else: # >= 21
			return self.tens[ii] + '-' + self.get1(i, True)
	
	def get100(self, iii, ii, i, isNoZero=False):
		if iii == 0: # < 100
			return self.get10(ii, i, isNoZero)
		elif ii == 0 and i == 0: # 100, 200...
			return self.get1(iii, True) + ' ' + self.hundred
		else: # 101-199, 201-299...
			return self.get1(iii, True) + ' ' + self.hundred + ' and ' + self.get10(ii, i, True)
	
	def get1000(self, iv, iii, ii, i, isNoZero=False):
		if iv == 0: # < 1000
			return self.get100(iii, ii, i, isNoZero)
		elif iii == 0 and not (ii == 0 and i == 0): # 1001-1099, 2001-2099...
			return self.get1(iv, True) + ' ' + self.thousand + ' and ' + self.get100(iii, ii, i, True)
		else: # >= 1100
			return self.get1(iv, True) + ' ' + self.thousand + ' ' + self.get100(iii, ii, i, True)

class NumeralGeneratorFinnish(NumeralGenerator):
	'''
	Numeral generator for Finnish
	'''
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
		self.oneTen = 'kymmenen'
		self.teens = 'toista'
		self.twoOrMoreTens = 'kymmentä'
		self.oneHundred = 'sata'
		self.twoOrMoreHundreds = 'sataa'
		self.oneThousand = 'tuhat'
		self.twoOrMoreThousands = 'tuhatta'
	
	def get1(self, i, isNoZero=False):
		if isNoZero and i == 0:
			return ''
		return self.ones[i]
	
	def get10(self, ii, i, isNoZero=False):
		if ii == 0:
			return self.get1(i, isNoZero)
		elif ii == 1 and i == 0:
			return self.oneTen
		elif ii == 1:
			return self.get1(i, True) + self.teens
		else:
			return self.get1(ii, True) + self.twoOrMoreTens + ' ' + self.get1(i, True)
	
	def get100(self, iii, ii, i, isNoZero=False):
		if iii == 0:
			return self.get10(ii, i, isNoZero)
		elif iii == 1:
			return self.oneHundred + ' ' + self.get10(ii, i, True)
		else:
			return self.get1(iii, True) + self.twoOrMoreHundreds + ' ' + self.get10(ii, i, True)
	
	def get1000(self, iv, iii, ii, i, isNoZero=False):
		if iv == 0:
			return self.get100(iii, ii, i, isNoZero)
		elif iv == 1:
			return self.oneThousand + ' ' + self.get100(iii, ii, i, True)
		else:
			return self.get1(iv, True) + self.twoOrMoreThousands + ' ' + self.get100(iii, ii, i, True)

class NumeralGeneratorFrench(NumeralGenerator):
	'''
	Numeral generator for French
	'''
	def __init__(self):
		NumeralGenerator.__init__(self, 'french')	
		self.ones = [
			'zéro', # 0
			'un', # 1
			'deux', # 2
			'trois', # 3
			'quatre', # 4
			'cinq', # 5
			'six', # 6
			'sept', # 7
			'huit', # 8
			'neuf' # 9
		]
		self.teens = [
			'', # 10
			'onze', # 11
			'douze', # 12
			'treize', # 13
			'quatorze', # 14
			'quinze', # 15
			'seize', # 16
			'dix-sept', # 17
			'dix-huit', # 18
			'dix-neuf' # 19
		]
		self.tens = [
			'', # 0
			'dix', # 10
			'vingt', # 20
			'trente', # 30
			'quarante', # 40
			'cinquante', # 50
			'soixante', # 60
			'soixante', # 70
			'quatre-vingt', # 80
			'quatre-vingt' # 90
		]
		self.altOne = 'et-un'
		self.altEleven = 'et-onze'
		self.eighty = 'quatre-vingts'
		self.hundred = 'cent'
		self.thousand = 'thousand'
	
	def get1(self, i, isNoZero=False, useAltOne=False):
		if isNoZero and i == 0:
			return ''
		if useAltOne and i == 1:
			return self.altOne
		return self.ones[i]

	def getTeens(self, i, isNoZero=False, useAltEleven=False):
		if isNoZero and i == 0:
			return ''
		if useAltEleven and i == 1:
			return self.altEleven
		return self.teens[i]

	def get10(self, ii, i, isNoZero=False):
		if ii == 0: # < 10
			return self.get1(i, isNoZero)
		elif ii == 1 and i == 0: # 10
			return self.tens[ii]
		elif ii == 1: # 11-19 
			return self.getTeens(i)
		elif (ii == 7 or ii == 9) and i == 0: # 70, 90 
			return self.tens[ii-1] + '-' + self.tens[1]
		elif ii == 8 and i == 0: # 80 
			return self.eighty
		elif i == 0: # 20, 30, 40...
			return self.tens[ii]
		elif i == 1 and ii != 8: # == 21, 31, 41... special case for 81
			theAltOne = self.getTeens(i, True, ii == 7) if (ii == 7 or ii == 9) else self.altOne
			return self.tens[ii] + '-' + theAltOne
		else: # 22, 45, etc
			theOne = self.getTeens(i, True, ii == 7) if (ii == 7 or ii == 9) else self.get1(i, True)
			return self.tens[ii] + '-' + theOne
		# TODO: 70 (60 + 10??), 90 (80 + 10!!)
	
	def get100(self, iii, ii, i, isNoZero=False):
		if iii == 0: # < 100
			return self.get10(ii, i, isNoZero)
		elif ii == 0 and i == 0: # 100, 200...
			return self.get1(iii, True) + ' ' + self.hundred
		else: # 101-199, 201-299...
			return self.get1(iii, True) + ' ' + self.hundred + ' and ' + self.get10(ii, i, True)
	
	def get1000(self, iv, iii, ii, i, isNoZero=False):
		if iv == 0: # < 1000
			return self.get100(iii, ii, i, isNoZero)
		elif iii == 0 and not (ii == 0 and i == 0): # 1001-1099, 2001-2099...
			return self.get1(iv, True) + ' ' + self.thousand + ' and ' + self.get100(iii, ii, i, True)
		else: # >= 1100
			return self.get1(iv, True) + ' ' + self.thousand + ' ' + self.get100(iii, ii, i, True)

class NumeralGeneratorGerman(NumeralGenerator):
	'''
	Numeral generator for German
	'''
	def __init__(self):
		NumeralGenerator.__init__(self, 'german')	
		self.ones = [
			'null', # 0
			'eins', # 1
			'zwei', # 2
			'drei', # 3
			'vier', # 4
			'fünf', # 5
			'sechs', # 6
			'sieben', # 7
			'acht', # 8
			'neun' # 9
		]
		self.teens = [
			'', # 10
			'elf', # 11
			'zwölf', # 12
			'dreizehn', # 13
			'vierzehn', # 14
			'fünfzehn', # 15
			'sechzehn', # 16
			'siebzehn', # 17
			'achtzehn', # 18
			'neunzehn' # 19
		]
		self.tens = [
			'', # 0
			'zehn', # 10
			'zwanzig', # 20
			'dreißig', # 30
			'vierzig', # 40
			'fünfzig', # 50
			'sechzig', # 60
			'siebzig', # 70
			'achtzig', # 80
			'neunzig' # 90
		]
		self.altOne = 'ein'
		self.hundred = 'hundert'
		self.thousand = 'tausend'
	
	def get1(self, i, isNoZero=False, useAltOne=False):
		if isNoZero and i == 0:
			return ''
		if useAltOne and i == 1:
			return self.altOne
		return self.ones[i]
	
	def get10(self, ii, i, isNoZero=False):
		if ii == 0: # < 10
			return self.get1(i, isNoZero)
		elif ii == 1 and i == 0: # 10
			return self.tens[ii]
		elif ii == 1: # 11-19 
			return self.teens[i]
		elif i == 0: # 20, 30, 40...
			return self.tens[ii]
		else: # >= 21
			return self.get1(i, True, useAltOne=True) + 'und' + self.tens[ii]
	
	def get100(self, iii, ii, i, isNoZero=False):
		if iii == 0: # < 100
			return self.get10(ii, i, isNoZero)
		elif ii == 0 and i == 0: # 100, 200...
			return self.get1(iii, True, useAltOne=True) + self.hundred
		else: # 101-199, 201-299...
			return self.get1(iii, True, useAltOne=True) + self.hundred + ' ' + self.get10(ii, i, True)
	
	def get1000(self, iv, iii, ii, i, isNoZero=False):
		if iv == 0: # < 1000
			return self.get100(iii, ii, i, isNoZero)
		else: # >= 1001
			return self.get1(iv, True, useAltOne=True) + self.thousand + ' ' + self.get100(iii, ii, i, True)

class NumeralGeneratorTurkish(NumeralGenerator):
	'''
	Numeral generator for Turkish
	'''
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
	'''
	Numeral generator for Vietnamese
	'''
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
