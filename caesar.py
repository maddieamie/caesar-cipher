
def encrypt(phrase: str, shift: int) -> str:
    encrypted_text = ""

    number_of_characters = 26
    base_character = "A"
    base_lower = "a"

    for char in phrase:
        base_code = ord(base_character)
        base_lower = ord(base_lower)
        current_code = ord(char)
        # if in range for capital A 65 - 90
        if 65 <= current_code <= 90:
            current_position = current_code - base_code
            shifted_position = (current_position + shift) % number_of_characters
            shifted_char = base_code + shifted_position
            encrypted_text += chr(shifted_char)
        # if in range for lowercase a 97 - 122
        if 97 <= current_code <= 122:
            current_position = current_code - base_lower
            shifted_position = (current_position + shift) % number_of_characters
            shifted_char = base_lower + shifted_position
            encrypted_text += chr(shifted_char)

    return encrypted_text


def decrypt(encrypted: str, shift: int) -> str:
    return encrypt(encrypted, -shift)


def crack(encrypted: str) -> str | int:

    # when filtering, change to lowercase only

    letter_dict = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }
    frequency_decimals = []

    def frequency_decimal_calculator(item):

        frequency_decimals.append((item, [item/length]))
        return item(item - 1)

    # count the frequency of each letter in the text using letter dictionary, ignore all else
    for char in encrypted:
        if char.lower() in letter_dict.keys():
            letter_dict[char] += 1

    # find the amount of letters in the encrypted text
    length = sum(letter_dict.values())

    # find the summation of frequencies of each letter for the index of coincidence
    numerators = [frequency_decimal_calculator(item) for item in letter_dict.values() if item > 0]
    numerator_sum = sum(numerators)

    # find the denominator of the index of coincidence formula
    denominator = length(length - 1)

    # find the index of coincidence
    index_of_coincidence = numerator_sum/denominator

    # if index of coincidence is near 0.070, it's probably english, if low, 0.0385
    # if the shifted char stands for the letter, do we need to find the distance from a to e?
    if index_of_coincidence >= 0.055:
        for letter, decimal in frequency_decimals:
            t = ord(letter)
            c = 0
            b = 97
            # where 'c' is what the shifted character probably is
            if decimal >= 0.095:
                c = ord('e')
            elif 0.083 <= decimal <= 0.094:
                c = ord('t')
            elif 0.076 <= decimal <= 0.082:
                c = ord('a')
            elif 0.071 <= decimal <= 0.075:
                c = ord('o')
            elif 0.068 <= decimal <= 0.070:
                c = ord('i')
            elif 0.064 <= decimal <= 0.067:
                c = ord('n')
            elif 0.06 <= decimal <= 0.063:
                c = ord('s')

            pos = c - b
            shift = t - pos
            return decrypt(encrypted, shift)
    else:
        return ""



    # use character frequency dict
    # if amount / len is greater than a certain amount, that char becomes base
    # subtract from curr char to base, that's the shift
    # do for top 8 letters




