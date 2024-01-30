card_number = '6791-4311-3874-3894'
card_translation = str.maketrans({'-' : '', ' ' : ''})
translated_card_number = card_number.translate(card_translation)
reversed_card_number = translated_card_number[::-1]
print(translated_card_number)
print(reversed_card_number)
