from utils import *
from logic import *

# Symbols
(A11, B11, C11, D11, E11, F11) = symbols(
    "A_triangulo, B_triangulo, C_triangulo, D_triangulo, E_triangulo, F_triangulo")
(A12, B12, C12, D12, E12, F12) = symbols(
    "A_cuadrado, B_cuadrado, C_cuadrado, D_cuadrado, E_cuadrado , F_cuadrado ")
(A13, B13, C13, D13, E13, F13) = symbols(
    "A_pentagono, B_pentagono, C_pentagono, D_pentagono, E_pentagono, F_pentagono")
(A21, B21, C21, D21, E21, F21) = symbols(
    "A_grande, B_grande, C_grande, D_grande, E_grande, F_grande")
(A22, B22, C22, D22, E22, F22) = symbols(
    "A_mediana, B_mediana, C_mediana, D_mediana, E_mediana, F_mediana")
(A23, B23, C23, D23, E23, F23) = symbols(
    "A_chica, B_chica, C_chica, D_chica, E_chica, F_chica ")


# Sentences
R1 = A11 | '==>' | B11
R2 = B11 | '==>' | C11
R3 = (A11 & C11) | '==>' | (A21 | C21)
R4 = (A11 & ~C21)
R5 = (C23 & D13) | '==>' | (~D21 & ~D23)
R6 = C22 | '==>' | (~D12 & ~E12 & ~F12)
R7 = ~A23 | '==>' | (D13 & D23)
R8 = E21 | '==>' | (D21 | '<=>' | F21)
R9 = (D21 & E21) | (D22 & E22) | (D23 & D23)
R10 = (D11 & E11) | (D12 & E12) | (D13 & E13)
R11 = F21 | '==>' | (F12 | F13)
R12 = ((C21 & E22) | (C21 & E23) | (C22 & E23)) | '==>' | (
    (B21 & C22) | (B21 & C23) | (B22 & C23))

# TRIANG 11
# CUAD 12
# PENT 13
# GRAND 21
# MED 22
# CHIC 23

# ---SER SOLO UNA  ---
R13 = (A11 & ~A12 & ~A13) | (A12 & ~A11 & ~A13) | (A13 & ~A11 & ~A12)
R14 = (A21 & ~A22 & ~A23) | (A22 & ~A21 & ~A23) | (A23 & ~A21 & ~A22)
R15 = (B11 & ~B12 & ~B13) | (B12 & ~B11 & ~B13) | (B13 & ~B11 & ~B12)
R16 = (B21 & ~B22 & ~B23) | (B22 & ~B21 & ~B23) | (B23 & ~B21 & ~B22)
R17 = (C11 & ~C12 & ~C13) | (C12 & ~C11 & ~C13) | (C13 & ~C11 & ~C12)
R18 = (C21 & ~C22 & ~C23) | (C22 & ~C21 & ~C23) | (C23 & ~C21 & ~C22)
R19 = (D11 & ~D12 & ~D13) | (D12 & ~D11 & ~D13) | (D13 & ~D11 & ~D12)
R20 = (D21 & ~D22 & ~D23) | (D22 & ~D21 & ~D23) | (D23 & ~D21 & ~D22)
R21 = (E11 & ~E12 & ~E13) | (E12 & ~E11 & ~E13) | (E13 & ~E11 & ~E12)
R22 = (E21 & ~E22 & ~E23) | (E22 & ~E21 & ~E23) | (E23 & ~E21 & ~E22)
R23 = (F11 & ~F12 & ~F13) | (F12 & ~F11 & ~F13) | (F13 & ~F11 & ~F12)
R24 = (F21 & ~F22 & ~F23) | (F22 & ~F21 & ~F23) | (F23 & ~F21 & ~F22)


# Knowledge base
ejercicio4_kb = PropKB()

ejercicio4_kb.tell(R1)
ejercicio4_kb.tell(R2)
ejercicio4_kb.tell(R3)
ejercicio4_kb.tell(R4)
ejercicio4_kb.tell(R5)
ejercicio4_kb.tell(R6)
ejercicio4_kb.tell(R7)
ejercicio4_kb.tell(R8)
ejercicio4_kb.tell(R9)
ejercicio4_kb.tell(R10)
ejercicio4_kb.tell(R11)
ejercicio4_kb.tell(R12)

ejercicio4_kb.tell(R13)
ejercicio4_kb.tell(R14)
ejercicio4_kb.tell(R15)
ejercicio4_kb.tell(R16)
ejercicio4_kb.tell(R17)
ejercicio4_kb.tell(R18)
ejercicio4_kb.tell(R19)
ejercicio4_kb.tell(R20)
ejercicio4_kb.tell(R21)
ejercicio4_kb.tell(R22)
ejercicio4_kb.tell(R23)
ejercicio4_kb.tell(R24)

# DPLL in the wumpus world
kb_string = ""
for elem in ejercicio4_kb.clauses:
    elem = to_cnf(str(elem))
    kb_string = kb_string + str(elem) + " & "


kb_string = kb_string[:-3]

print("RESPUESTA \n", dpll_satisfiable(expr(kb_string)))
# Hallar manera aesthetic de desplegarlo
