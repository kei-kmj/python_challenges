
def remove_vowels_replace(text):
    """ Remove vowels from the string using replace(). """
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        text = text.replace(vowel, "")
    return text


def remove_vowels_split(text):
    """ Remove vowels using split() and join(). """
    vowels = "aeiouAEIOU"
    return "".join(char for char in text if char not in vowels)


def transform_hire(text):
    """ Transform the given text based on predefined character replacements. """
    return text.replace("H", "h").replace("i", "1").replace("r", "R").replace("e", "3")

# Example usage
text = "Hire me!"
print(transform_hire(text))

translation_table = str.maketrans({"H": "h", "i": "1", "r": "R", "e": "3"})

def transform_hire(text):
    """ Transform the given text using str.maketrans(). """

    return text.translate(translation_table)

# Example usage
text = "Hire me!"
print(transform_hire(text))