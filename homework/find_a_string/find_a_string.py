def find_a_string(original_str: str, substr: str) -> int:
<<<<<<< HEAD
    count = original_str.count(substr)
    return count
<<<<<<< HEAD
=======
=======
    count = 0
>>>>>>> f374331 (betts_hf4_final)

    if original_str == "" and substr == "":
     return 0

<<<<<<< HEAD
>>>>>>> 52c6c02 (betts_hf4_1)
=======
    if substr == "":
        return 0

    for i in range(len(original_str) - len(substr) + 1):
        if original_str[i:i + len(substr)] == substr:
            count += 1
        
    return count
>>>>>>> f374331 (betts_hf4_final)
