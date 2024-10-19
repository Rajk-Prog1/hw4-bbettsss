def minion_game(s: str) -> str:
<<<<<<< HEAD
    kevin_points = 0
    stuart_points = 0
     
    for i in range(len(s)):
        if s[i] in 'AEIOU':
           kevin_points += ((len(s))-i)
        else:
           stuart_points += ((len(s))-i)
                
    if kevin_points < stuart_points:
        print('Stuart ' + str(stuart_points))
    elif kevin_points > stuart_points:
        print('Kevin ' + str(kevin_points))
    else:
        print('Draw')
=======
    length = len(s)
    vowel = 0
    consonant = 0

    for i in range(length):
        if s[i] in 'AEIOU':
                vowel += (length-i)
        else:
             consonant += (length-i)

    if vowel > consonant:
        return f"Kevin {vowel}"
    elif consonant > vowel:
        return f"Stuart {consonant}"
    else:
        return "Draw" 

    return minion_game

>>>>>>> c733f68 (betts_hf4_2)
