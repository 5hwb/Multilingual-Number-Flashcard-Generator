from file_io import save_str_to_file
from numeral_generator import NumeralGeneratorArmenianRomanised, NumeralGeneratorChineseHanzi, NumeralGeneratorChineseMandarin, \
NumeralGeneratorEnglish, NumeralGeneratorFinnish, NumeralGeneratorFrench, NumeralGeneratorGeorgian, NumeralGeneratorGeorgianRomanised, \
NumeralGeneratorGerman, NumeralGeneratorIndonesian, NumeralGeneratorItalian, NumeralGeneratorTagalog, NumeralGeneratorTurkish, NumeralGeneratorVietnamese

# Generate numbers
num_generators = [
	NumeralGeneratorArmenianRomanised(),
	NumeralGeneratorChineseHanzi(),
	NumeralGeneratorChineseMandarin(),
	NumeralGeneratorEnglish(),
	NumeralGeneratorFinnish(),
	NumeralGeneratorFrench(),
	NumeralGeneratorGeorgian(),
	NumeralGeneratorGeorgianRomanised(),
	NumeralGeneratorGerman(),
	NumeralGeneratorIndonesian(),
	NumeralGeneratorItalian(),
	NumeralGeneratorTagalog(),
	NumeralGeneratorTurkish(),
	NumeralGeneratorVietnamese(),
]
def get_list_of_numerals(num_generator, start, end):
	flashcard_entries = ''
	for x in range(start, end+1):
		xStr = '{:04d}'.format(x)
		result = num_generator.get1000(int(xStr[0]), int(xStr[1]), int(xStr[2]), int(xStr[3]))
		flashcard_entries += '{}\t{}\n'.format(result, x)
	return flashcard_entries

def generate_decks_for_each_language():
	for num_generator in num_generators:
		save_str_to_file('first_10_numerals_{}.txt'.format(num_generator.name), get_list_of_numerals(num_generator, 0, 10))
		save_str_to_file('numerals_11_to_20_{}.txt'.format(num_generator.name), get_list_of_numerals(num_generator, 11, 20))
		save_str_to_file('numerals_21_to_100_{}.txt'.format(num_generator.name), get_list_of_numerals(num_generator, 21, 100))
		save_str_to_file('numerals_to_9999_{}.txt'.format(num_generator.name), get_list_of_numerals(num_generator, 101, 9999))

if __name__ == "__main__":
	generate_decks_for_each_language()