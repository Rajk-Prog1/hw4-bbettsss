def swap_case(s: str) -> int:
    string = ""

    for letters in s:
        if letters.isupper():
            string += letters.lower()
        elif letters.islower():
            string += letters.upper()
        else:
            string += letters

    return string