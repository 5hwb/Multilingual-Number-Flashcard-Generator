from file_io import load_file_to_str, save_str_to_file
from NumeralGenerator import NumeralGeneratorTurkish

# Generate numbers
numGenerator = NumeralGeneratorTurkish()
def getListOfNumerals(start, end):
	daList = ''
	for x in range(start, end+1):
		xStr = '{:04d}'.format(x)
		result = numGenerator.get1000(int(xStr[0]), int(xStr[1]), int(xStr[2]), int(xStr[3]))
		daList += '{}\t{}\n'.format(result, x)
	return daList

save_str_to_file('first_20_numerals_{}.txt'.format(numGenerator.name), getListOfNumerals(0, 20))
save_str_to_file('numerals_to_9999_{}.txt'.format(numGenerator.name), getListOfNumerals(21, 9999))
