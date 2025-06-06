def count_words(text):
    word_count = 0

    for word in str.split(text):
        word_count += 1

    return word_count


def count_characters(text):
    characters = {}

    for character in str.lower(text):
        if (character not in characters):
            characters[character] = 1
        else:
            characters[character] = characters[character] + 1
    
    return characters


def sorted_character_count(dict):
    list_of_char_dicts = []

    for key in dict:
        list_of_char_dicts.append({
            "char": key,
            "num": dict[key]
        })
    
    list_of_char_dicts.sort(reverse=True, key=sort_on)

    return list_of_char_dicts


def sort_on(dict):
    return dict["num"]


