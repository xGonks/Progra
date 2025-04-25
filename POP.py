from utils import *
from logic import *

# Simbolos
(AC, AM, AG, AT, AS, AP) = symbols('AC, AM, AG, AT, AS, AP')
(BC, BM, BG, BT, BS, BP) = symbols('BC, BM, BG, BT, BS, BP')
(CC, CM, CG, CT, CS, CP) = symbols('CC, CM, CG, CT, CS, CP')
(DC, DM, DG, DT, DS, DP) = symbols('DC, DM, DG, DT, DS, DP')
(EC, EM, EG, ET, ES, EP) = symbols('EC, EM, EG, ET, ES, EP')
(FC, FM, FG, FT, FS, FP) = symbols('FC, FM, FG, FT, FS, FP')

# Sentencias
Sentencia_1 = AT | '==>' | BT
Sentencia_2 = BT | '==>' | CT
Sentencia_3 = (AT & CT) | '==>' | (AG | CG)
Sentencia_4 = AT & ~CG
Sentencia_5 = (CC & DP) | '==>' | (~DG & ~DC)
Sentencia_6 = CM | '==>' | (~DS & ~ES & ~FS)
Sentencia_7 = ~AC | '==>' | (DP & DC)
Sentencia_8 = EG | '==>' | (DG | '<=>' | FG)
Sentencia_9 = (DC & EC) | (DM & EM) | (DG & EG)
Sentencia_10 = (DT & ET) | (DS & ES) | (DP & EP)
Sentencia_11 = FG | '==>' | (FS | FP)
Sentencia_12 = ((CG & EM) | (CG & EC) | (CM & EC)) | '==>' | (
    (BG & CM) | (BG & CC) | (BM & CC))

# Solo una forma y un tamaño por figura
Sentencia_13 = (AT & ~AS & ~AP) | (AS & ~AT & ~AP) | (AP & ~AT & ~AS)
Sentencia_14 = (AC & ~AM & ~AG) | (AM & ~AC & ~AG) | (AG & ~AC & ~AM)
Sentencia_15 = (BT & ~BS & ~BP) | (BS & ~BT & ~BP) | (BP & ~BT & ~BS)
Sentencia_16 = (BC & ~BM & ~BG) | (BM & ~BC & ~BG) | (BG & ~BC & ~BM)
Sentencia_17 = (CT & ~CS & ~CP) | (CS & ~CT & ~CP) | (CP & ~CT & ~CS)
Sentencia_18 = (CC & ~CM & ~CG) | (CM & ~CC & ~CG) | (CG & ~CC & ~CM)
Sentencia_19 = (DT & ~DS & ~DP) | (DS & ~DT & ~DP) | (DP & ~DT & ~DS)
Sentencia_20 = (DC & ~DM & ~DG) | (DM & ~DC & ~DG) | (DG & ~DC & ~DM)
Sentencia_21 = (ET & ~ES & ~EP) | (ES & ~ET & ~EP) | (EP & ~ET & ~ES)
Sentencia_22 = (EC & ~EM & ~EG) | (EM & ~EC & ~EG) | (EG & ~EC & ~EM)
Sentencia_23 = (FT & ~FS & ~FP) | (FS & ~FT & ~FP) | (FP & ~FT & ~FS)
Sentencia_24 = (FC & ~FM & ~FG) | (FM & ~FC & ~FG) | (FG & ~FC & ~FM)

# Base de Conocimiento
prueba_KB = PropKB()

prueba_KB.tell(Sentencia_1)
prueba_KB.tell(Sentencia_2)
prueba_KB.tell(Sentencia_3)
prueba_KB.tell(Sentencia_4)
prueba_KB.tell(Sentencia_5)
prueba_KB.tell(Sentencia_6)
prueba_KB.tell(Sentencia_7)
prueba_KB.tell(Sentencia_8)
prueba_KB.tell(Sentencia_9)
prueba_KB.tell(Sentencia_10)
prueba_KB.tell(Sentencia_11)
prueba_KB.tell(Sentencia_12)
prueba_KB.tell(Sentencia_13)
prueba_KB.tell(Sentencia_14)
prueba_KB.tell(Sentencia_15)
prueba_KB.tell(Sentencia_16)
prueba_KB.tell(Sentencia_17)
prueba_KB.tell(Sentencia_18)
prueba_KB.tell(Sentencia_19)
prueba_KB.tell(Sentencia_20)
prueba_KB.tell(Sentencia_21)
prueba_KB.tell(Sentencia_22)
prueba_KB.tell(Sentencia_23)
prueba_KB.tell(Sentencia_24)

# Generar expresión conjunta para DPLL
kb_string = ""
for elem in prueba_KB.clauses:
    elem = to_cnf(str(elem))
    kb_string += str(elem) + " & "
kb_string = kb_string[:-3]

print("RESPUESTA \n", dpll_satisfiable(expr(kb_string)))
