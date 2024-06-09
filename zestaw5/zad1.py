def evaluate(S, m):
    if len(S) == 1:
        return m[S]
    else:
        op = S[1]
        if op == '¬':
            return not evaluate(S[2:], m)
        elif op == '∧':
            return evaluate(S[0], m) and evaluate(S[2:], m)
        elif op == '∨':
            return evaluate(S[0], m) or evaluate(S[2:], m)

# Przykładowe zdanie
S = "(p ∧ q) ∨ (¬p)"
# Przykładowe przypisanie
m = {'p': True, 'q': False}

# Sprawdzenie wartości zdania w przypisaniu
print("Czy zdanie jest prawdziwe dla przypisania {}: {}".format(m, evaluate(S, m)))
