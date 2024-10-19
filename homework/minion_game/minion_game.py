def minion_game(s: str) -> str:
    length = len(s)
    vowel = 0
    consonant = 0
     
    for i in range(s):
        if s[i] in 'AEIOU':
           vowel += (length-i)
        else:
           consonant += (length-i)
                
    if vowel < consonant:
        print('Stuart ' + str(consonant))
    elif vowel > consonant:
        print('Kevin ' + str(vowel))
    else:
        print('Draw')
