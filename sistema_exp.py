# ========================================
# Imports
# ========================================

from logic import *
from utils import *

# ========================================
# General knowledge
# ========================================

clauses = []

# ========================================
# Cláusulas Juan Pablo
# ========================================

# Deseases 
clauses.append(expr("Sintoma(x, DolorToracico) & Sintoma(x, DificultadRespirar) & Sintoma(x, Palpitaciones) ==> Enfermo(x, PosibleAtaqueCardiaco)"))
clauses.append(expr("Sintoma(x, Palpitaciones) & Sintoma(x, Nerviosismo) ==> Enfermo(x, Ansiedad)"))
clauses.append(expr("Sintoma(x, DificultadRespirar) & Sintoma(x, Nerviosismo) ==> Enfermo(x, Ansiedad)"))
clauses.append(expr("Sintoma(x, Nauseas) & Sintoma(x, DolorEstomago) & Sintoma(x, RitmoCardiacoIrregular) ==> Enfermo(x, PosibleAtaqueCardiaco)"))
clauses.append(expr("Sintoma(x, Nauseas) & Sintoma(x, DolorEstomago) & Sintoma(x, Vomitos) ==> Enfermo(x, InfeccionEstomacal)"))

# Treatments for diseases
clauses.append(expr("Enfermo(x, PosibleAtaqueCardiaco) ==> Tratamiento(x, AyudaMedica)"))
clauses.append(expr("Enfermo(x, PosibleAtaqueCardiaco) ==> Tratamiento(x, ReanimacionCardiopulmonar)"))
clauses.append(expr("Enfermo(x, Ansiedad) ==> Tratamiento(x, RespiracionProfunda)"))
clauses.append(expr("Enfermo(x, InfeccionEstomacal) ==> Tratamiento(x, MantenerseHidratado)"))
clauses.append(expr("Enfermo(x, InfeccionEstomacal) ==> Tratamiento(x, Descansar)"))
clauses.append(expr("Enfermo(x, InfeccionEstomacal) ==> Tratamiento(x, EvitarAlimentos)"))

# Treatments for symptoms 
clauses.append(expr("NoDiagnostico(x) & Sintoma(x, DolorToracico) ==> Tratamiento(x, Aspirinas)"))
clauses.append(expr("NoDiagnostico(x) & Sintoma(x, DolorToracico) ==> Tratamiento(x, RespiracionProfunda)"))
clauses.append(expr("NoDiagnostico(x) & Sintoma(x, Nerviosismo) ==> Tratamiento(x, RespiracionProfunda)"))
clauses.append(expr("NoDiagnostico(x) & Sintoma(x, Nerviosismo) ==> Tratamiento(x, EncontrarPosicionComoda)"))
clauses.append(expr("NoDiagnostico(x) & Sintoma(x, DificultadRespirar) ==> Tratamiento(x, RespiracionProfunda)"))
clauses.append(expr("NoDiagnostico(x) & Sintoma(x, RitmoCardiacoIrregular) ==> Tratamiento(x, RespiracionProfunda)"))

# ========================================
# Cláusulas de alguien mas... 
# ========================================
# Deseases 

# Treatments for diseases

# Treatments for symptoms 


# ========================================
# Knowledge base
# ========================================

kb = FolKB(clauses)

# ========================================
# Knowledge about a patient
# ========================================

name = input("¿Cual es tu nombre? ").capitalize()

#Preguntas de sintomas

# ========================================
# Preguntas Juan Pablo
# ========================================
if (input("¿Tienes dolor torácico (pecho)? ").lower() == 's'):
    kb.tell(expr("Sintoma({}, DolorToracico)".format(name)))
if (input("¿Tienes dificultad para respirar? ").lower() == 's'):
    kb.tell(expr("Sintoma({}, DificultadRespirar)".format(name)))
if (input("¿Tienes nerviosismo? ").lower() == 's'):
    kb.tell(expr("Sintoma({}, Nerviosismo)".format(name)))
if (input("¿Tienes dolor de estómago? ").lower() == 's'):
    kb.tell(expr("Sintoma({}, DolorEstomago)".format(name)))
if (input("¿Tienes ritmo cardiaco irregular? ").lower() == 's'):
    kb.tell(expr("Sintoma({}, RitmoCardiacoIrregular)".format(name)))

# ========================================
# Preguntas de alguien mas 
# ========================================
if (input("¿Tienes palpitaciones? ").lower() == 's'):
    kb.tell(expr("Sintoma({}, Palpitaciones)".format(name)))
if (input("¿Tienes nauseas? ").lower() == 's'):
    kb.tell(expr("Sintoma({}, Nauseas)".format(name)))
if (input("¿Tienes vomitos? ").lower() == 's'):
    kb.tell(expr("Sintoma({}, Vomitos)".format(name)))

# ========================================
# Show symptoms
# ========================================
print("\nSintomas del paciente: ")
answer = fol_fc_ask(kb, expr("Sintoma({}, x)".format(name)))
answer = list(answer)

if len(answer)>0:
    for sintoms in answer:
        print(sintoms[x])
else:
    print("No hay sintomas")

# ========================================
# Show final diagnosis
# ========================================
print("\nTu diagnóstico es: ")
answer = fol_fc_ask(kb, expr("Enfermo({}, x)".format(name)))
answer = list(answer)

if len(answer) > 0:
    for diagnostic in answer:
        print(diagnostic[x])
else:
    print("No hay diagnóstico,")
    print("para sus sintomas individuales se recomienda hacer lo siguiente.")
    kb.tell(expr("NoDiagnostico({})".format(name)))


# ========================================
# Show treatments
# ========================================
print("\nTu tratamiento es: ")
answer = fol_fc_ask(kb, expr("Tratamiento({}, x)".format(name)))
answer = list(answer)

if len(answer) > 0:
    for treatment in answer:
        print(treatment[x])
else:
    print("No hay tratamiento.")

# ========================================
# End of file
# ========================================
