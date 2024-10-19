def swap_case(s: str) -> int:
    new_string = ""

    for a in s:
        if a.isupper():
            new_string += a.lower()
        elif a.islower():
            new_string += a.upper()
        else:
            new_string += a

    return new_string