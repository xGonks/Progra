from utils import *
from logic import *

# Simbolos
(AT, BT, CT, DT, ET, FT) = symbols("AT BT CT DT ET FT")
(AS, BS, CS, DS, ES, FS) = symbols("AS BS CS DS ES FS")
(AP, BP, CP, DP, EP, FP) = symbols("AP BP CP DP EP FP")
(AG, BG, CG, DG, EG, FG) = symbols("AG BG CG DG EG FG")
(AM, BM, CM, DM, EM, FM) = symbols("AM BM CM DM EM FM")
(AC, BC, CC, DC, EC, FC) = symbols("AC BC CC DC EC FC")

# Reglas
R1 = AT | '==>' | BT
R2 = BT | '==>' | CT
R3 = (AT & CT) | '==>' | (AG | CG)
R4 = (AT & ~CG)
R5 = (CC & DP) | '==>' | (~DG & ~DC)
R6 = CM | '==>' | (~DS & ~ES & ~FS)
R7 = ~AC | '==>' | (DP & DC)
R8 = EG | '==>' | (DG | '<=>' | FG)
R9 = (DG & EG) | (DM & EM) | (DC & DC)
R10 = (DT & ET) | (DS & ES) | (DP & EP)
R11 = FG | '==>' | (FS | FP)
R12 = ((CG & EM) | (CG & EC) | (CM & EC)) | '==>' | (
    (BG & CM) | (BG & CC) | (BM & CC))

# Reglas de unicidad
R13 = (AT & ~AS & ~AP) | (AS & ~AT & ~AP) | (AP & ~AT & ~AS)
R14 = (AG & ~AM & ~AC) | (AM & ~AG & ~AC) | (AC & ~AG & ~AM)
R15 = (BT & ~BS & ~BP) | (BS & ~BT & ~BP) | (BP & ~BT & ~BS)
R16 = (BG & ~BM & ~BC) | (BM & ~BG & ~BC) | (BC & ~BG & ~BM)
R17 = (CT & ~CS & ~CP) | (CS & ~CT & ~CP) | (CP & ~CT & ~CS)
R18 = (CG & ~CM & ~CC) | (CM & ~CG & ~CC) | (CC & ~CG & ~CM)
R19 = (DT & ~DS & ~DP) | (DS & ~DT & ~DP) | (DP & ~DT & ~DS)
R20 = (DG & ~DM & ~DC) | (DM & ~DG & ~DC) | (DC & ~DG & ~DM)
R21 = (ET & ~ES & ~EP) | (ES & ~ET & ~EP) | (EP & ~ET & ~ES)
R22 = (EG & ~EM & ~EC) | (EM & ~EG & ~EC) | (EC & ~EG & ~EM)
R23 = (FT & ~FS & ~FP) | (FS & ~FT & ~FP) | (FP & ~FT & ~FS)
R24 = (FG & ~FM & ~FC) | (FM & ~FG & ~FC) | (FC & ~FG & ~FM)

# Base de conocimiento
ejercicio4_kb = PropKB()

for regla in [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12,
              R13, R14, R15, R16, R17, R18, R19, R20, R21, R22, R23, R24]:
    ejercicio4_kb.tell(regla)

# Generar expresión conjunta para DPLL
kb_string = ""
for elem in ejercicio4_kb.clauses:
    elem = to_cnf(str(elem))
    kb_string += str(elem) + " & "

kb_string = kb_string[:-3]

print("RESPUESTA \n", dpll_satisfiable(expr(kb_string)))
