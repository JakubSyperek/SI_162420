from constraint import Problem

# Definicja problemu
problem = Problem()

# Definicja zmiennych (obszarów) i ich dziedzin (dostępnych kolorów)
obszary = ['A', 'B', 'C', 'D', 'E']
dostepne_kolory = ['czerwony', 'zielony', 'niebieski']

for obszar in obszary:
    problem.addVariable(obszar, dostepne_kolory)

# Definicja ograniczeń (sąsiedztwa)
problem.addConstraint(lambda a, b: a != b, ('A', 'B'))
problem.addConstraint(lambda a, b: a != b, ('A', 'C'))
problem.addConstraint(lambda a, b: a != b, ('B', 'C'))
problem.addConstraint(lambda a, b: a != b, ('B', 'D'))
problem.addConstraint(lambda a, b: a != b, ('C', 'D'))
problem.addConstraint(lambda a, b: a != b, ('C', 'E'))
problem.addConstraint(lambda a, b: a != b, ('D', 'E'))

# Rozwiązanie problemu
rozwiazanie = problem.getSolutions()

# Wyświetlenie rozwiązania
for sol in rozwiazanie:
    print(sol)
