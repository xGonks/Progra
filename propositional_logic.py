# ------------------------------------------------------------------------------------------------------------------
#   Propositional logic examples
#
#   This script contains some examples of propositional logic exercises solved in python using the
#   AIMA code. For more examples, visit https://github.com/aimacode
#
# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
#   Imports
# ------------------------------------------------------------------------------------------------------------------

from utils import *
from logic import *

# ------------------------------------------------------------------------------------------------------------------
#   Definition of symbols in propositional logic
# ------------------------------------------------------------------------------------------------------------------
A = Symbol('A')

# lower case letters are variables and upper case letters represent propositions.
(x, y, P, Q, R, S) = symbols('x, y, P, Q, R, S')

# ------------------------------------------------------------------------------------------------------------------
#   Definition of sentences
# ------------------------------------------------------------------------------------------------------------------

r1 = P & Q                          # AND
r2 = P | Q                          # OR
r3 = ~Q                             # NOT
r4 = P | '==>' | Q                    # Implication
r5 = P | '<==' | Q                    # Reverse implication
r6 = P | '<=>' | Q                    # Biconditional
r7 = (P & ~Q) | R | '==>' | S        # Combination of connectors

# ------------------------------------------------------------------------------------------------------------------
#   Evaluation of models
# ------------------------------------------------------------------------------------------------------------------

print(pl_true(P & ~Q, {P: True, Q: False}))
print(pl_true(P & ~Q, {P: True, Q: True}))
print(pl_true(P | '==>' | ~Q, {P: True, Q: False}))
print(pl_true(P | '==>' | ~Q, {P: True, Q: True}))
print(pl_true(r7, {P: True, Q: True, R: True}))
print(pl_true(r7, {P: True, Q: True, R: True, S: False}))

# ------------------------------------------------------------------------------------------------------------------
#   CNF
# ------------------------------------------------------------------------------------------------------------------

print(to_cnf(r7))
print(to_cnf(r1 & r2 & r3 & r4))
print(to_cnf("P & Q <=> (R | ~S)"))
print(to_cnf(P & Q | '<=>' | (R | ~S)))

# ------------------------------------------------------------------------------------------------------------------
#   Definition of a knowledge base
# ------------------------------------------------------------------------------------------------------------------

# Symbols
(P11, P12, P21, P22, P31, B11, B21) = symbols(
    'P11, P12, P21, P22, P31, B11, B21')

# Sentences
R1 = ~P11
R2 = B11 | '<=>' | (P12 | P21)
R3 = B21 | '<=>' | (P11 | P22 | P31)
R4 = ~B11
R5 = B21

# Knowledge base
wumpus_kb = PropKB()

wumpus_kb.tell(R1)
wumpus_kb.tell(R2)
wumpus_kb.tell(R3)
wumpus_kb.tell(R4)
wumpus_kb.tell(R5)

print(wumpus_kb.clauses)

# Inference
print("~P11? ", wumpus_kb.ask_if_true(~P11))

print("P11? ", wumpus_kb.ask_if_true(P11))

print("~P12? ", wumpus_kb.ask_if_true(~P12))

print("P12? ", wumpus_kb.ask_if_true(P12))

print("~P21? ", wumpus_kb.ask_if_true(~P21))

print("P21? ", wumpus_kb.ask_if_true(P21))

print("~P22? ", wumpus_kb.ask_if_true(~P22))

print("P22? ", wumpus_kb.ask_if_true(P22))

print("~P31? ", wumpus_kb.ask_if_true(~P31))

print("P31? ", wumpus_kb.ask_if_true(P31))


# New knowledge
(B12, P13) = symbols('B12, P13')

wumpus_kb.tell(~B12)
wumpus_kb.tell(B12 | '<=>' | (P11 | P22 | P13))

print("~P22? ", wumpus_kb.ask_if_true(~P22))

print("P22? ", wumpus_kb.ask_if_true(P22))

print("~P13? ", wumpus_kb.ask_if_true(~P13))

print("P13? ", wumpus_kb.ask_if_true(P13))

print("~P31? ", wumpus_kb.ask_if_true(~P31))

print("P31? ", wumpus_kb.ask_if_true(P31))

# ------------------------------------------------------------------------------------------------------------------
#   Inference methods
# ------------------------------------------------------------------------------------------------------------------

# TT-Entails (it works on KB expressions (conjunction of facts))
print(tt_entails(P & Q, Q))

(A, B, C, D, E, F, G) = symbols('A, B, C, D, E, F, G')
print(tt_entails(A & (B | C) & D & E & ~(F | G), A & D & E & ~F & ~G))

# Resolution (it works on PropKB objects because it requires the clauses method)

print(pl_resolution(wumpus_kb, ~P31), pl_resolution(wumpus_kb, P31))

# Forward chaining (it works on PropDefiniteKB objects because it needs an object that handles horn clauses)
clauses = ['(B & F)==>E',
           '(A & E & F)==>G',
           '(B & C)==>F',
           '(A & B)==>D',
           '(E & F)==>H',
           '(H & I)==>J',
           'A',
           'B',
           'C']
definite_clauses_KB = PropDefiniteKB()
for clause in clauses:
    definite_clauses_KB.tell(expr(clause))

print(pl_fc_entails(definite_clauses_KB, expr('G')))
print(pl_fc_entails(definite_clauses_KB, expr('H')))
print(pl_fc_entails(definite_clauses_KB, expr('I')))
print(pl_fc_entails(definite_clauses_KB, expr('J')))

# DPLL (it determines whether an expression is satisfiable)
A, B, C, D = expr('A, B, C, D')

print(dpll_satisfiable(A & B & ~C & D))

print(dpll_satisfiable((A & B) | (C & ~A) | (B & ~D)))

print(dpll_satisfiable(A | '<=>' | B))

print(dpll_satisfiable((A | '<=>' | B) | '==>' | (C & ~A)))

print(dpll_satisfiable((A | (B & C)) | '<=>' | ((A | B) & (A | C))))

# DPLL in the wumpus world
kb_string = ""
for elem in wumpus_kb.clauses:
    elem = to_cnf(str(elem))
    kb_string = kb_string + str(elem) + " & "

# Test P31
kb_alpha_string = kb_string + str(to_cnf(str(~P31)))
print(dpll_satisfiable(expr(kb_alpha_string)))

# Test ~P31
kb_alpha_string = kb_string + str(to_cnf(str(P31)))
print(dpll_satisfiable(expr(kb_alpha_string)))

# WalkSAT (it determines whether an expression is satisfiable)
print(WalkSAT([A, B, ~C, D], 0.5, 100))

print(WalkSAT([A & B, A & C], 0.5, 100))

print(WalkSAT([A & B, C & D, C & B], 0.5, 100))

print(WalkSAT([A & B, C | D, ~(D | B)], 0.5, 1000))

# ------------------------------------------------------------------------------------------------------------------
#   End of file
# ------------------------------------------------------------------------------------------------------------------
