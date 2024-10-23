def find_a_string(original_str: str, substr: str) -> int:
    count = 0

    if original_str == "" and substr == "":
     return 0

    if substr == "":
        return 0

    for i in range(len(original_str) - len(substr) + 1):
        if original_str[i:i + len(substr)] == substr:
            count += 1
        
    return count

