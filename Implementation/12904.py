S=list(input())
T=list(input())

def ab_game(S,T):
    while len(T)!=len(S):
        reverse_T=T[-1::-1]
        if T[-1]=='A':
            T=T[:-1]
        elif reverse_T[0]=='B':
            T=reverse_T[1:]
        else :return 0
    return 1 if S==T else 0

print(ab_game(S,T))


