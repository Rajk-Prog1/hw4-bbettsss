def swap_case(s: str) -> int:
<<<<<<< HEAD
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
=======
    string = ""
>>>>>>> f374331 (betts_hf4_final)

    for letter in s:
        if letter.isupper():
            string += letter.lower()
            
        elif letter.islower():
            string += letter.upper()

        else:
            string += letter

    return string

>>>>>>> 52c6c02 (betts_hf4_1)
