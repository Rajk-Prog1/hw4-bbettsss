def minion_game(s: str) -> str:
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