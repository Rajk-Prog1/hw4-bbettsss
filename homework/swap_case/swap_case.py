def swap_case(s: str) -> int:
<<<<<<< HEAD
    string = ""

    for letters in s:
        if letters.isupper():
            string += letters.lower()
        elif letters.islower():
            string += letters.upper()
        else:
            string += letters

    return string
=======
    new_string = ""

    for a in s:
        if a.isupper():
            new_string += a.lower()
            
        elif a.islower():
            new_string += a.upper()

        else:
            new_string += a

    return new_string

>>>>>>> 52c6c02 (betts_hf4_1)
