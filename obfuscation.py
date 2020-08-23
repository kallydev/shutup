def obfuscation(content):
    result = ""
    for index, char in enumerate(content):
        if index != 0:
            result += "\u200B"
        result += char
    return result
