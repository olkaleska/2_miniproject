# Вирішує тільки 1 пробний тест
def duplicate_encode(string):
    char_count = {}
    result = ''
    for char in string:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
            result += ')'
        else:
            char_count[char] = 1
            result += '('
    return result
