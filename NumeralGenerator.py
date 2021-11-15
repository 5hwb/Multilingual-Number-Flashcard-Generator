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
