def minion_game(s: str) -> str:
<<<<<<< HEAD
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
=======
    kevin_points = 0
    stuart_points = 0
>>>>>>> f374331 (betts_hf4_final)

    for i in range(len(s)):
        if s[i] in 'AEIOU':
                kevin_points += (len(s)-i)
        else:
             stuart_points += (len(s)-i)

    if kevin_points > stuart_points:
        return f"Kevin {kevin_points}"
    elif stuart_points > kevin_points:
        return f"Stuart {stuart_points}"
    else:
        return "Draw" 

<<<<<<< HEAD
    return minion_game

>>>>>>> c733f68 (betts_hf4_2)
=======
    return minion_game
>>>>>>> 372a4cf (betts_valamifura_final)
