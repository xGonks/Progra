# ========================================
# Importación de librerías
# ========================================
from utils import *
from logic import *

# ========================================
# General knowledge
# ========================================
clauses = []

# Ejemplo de uso
"""# Diseases
clauses.append(expr("Sintoma(x, CuerpoCortado) & Sintoma(x, Escurrimiento) ==> Enfermo(x, Resfrio)"))
clauses.append(expr("Sintoma(x, Tos) & Sintoma(x, Fiebre) ==> Enfermo(x, Covid19)"))
clauses.append(expr("Sintoma(x, CuerpoCortado) & Sintoma(x, Fiebre) ==> Enfermo(x, Covid19)"))
clauses.append(expr("Sintoma(x, Escurrimiento) & Sintoma(x, Fiebre) ==> Enfermo(x, Covid19)"))
clauses.append(expr("Sintoma(x, PositivoExamenCovid19) ==> Enfermo(x, Covid19)"))
clauses.append(expr("Sintoma(x, Cansancio) & Sintoma(x, Sueno) ==> Enfermo(x, Flojera)"))

# Treatments for diseases
clauses.append(expr("Enfermo(x, Resfrio) ==> Tratamiento(x, Reposo)"))
clauses.append(expr("Enfermo(x, Resfrio) ==> Tratamiento(x, Liquidos)"))
clauses.append(expr("Enfermo(x, Covid19) ==> Tratamiento(x, Reposo)"))
clauses.append(expr("Enfermo(x, Covid19) ==> Tratamiento(x, Antivirales)"))
clauses.append(expr("Enfermo(x, Flojera) ==> Tratamiento(x, Dormir)"))"""

# ========================================
# Cláusulas de Makenly (síntomas comunes)
# ========================================
# Síntomas Normales
clauses.append(expr("Sintoma(x, DolorCabeza) ==> Enfermo(x, Migraña)"))
clauses.append(expr(
    "Sintoma(x, DolorGarganta) & Sintoma(x, Fiebre) ==> Enfermo(x, Faringitis)"))
clauses.append(expr(
    "Sintoma(x, DolorEstomago) & Sintoma(x, Nauseas) ==> Enfermo(x, Gastroenteritis)"))
clauses.append(expr(
    "Sintoma(x, DolorEspalda) & Sintoma(x, Cansancio) ==> Enfermo(x, Lumbalgia)"))
clauses.append(expr(
    "Sintoma(x, Tos) & Sintoma(x, DificultadRespirar) ==> Enfermo(x, Bronquitis)"))
clauses.append(expr(
    "Sintoma(x, DolorArticular) & Sintoma(x, Inflamacion) ==> Enfermo(x, Artritis)"))
clauses.append(
    expr("Sintoma(x, PerdidaOlfato) & Sintoma(x, Fiebre) ==> Enfermo(x, Covid19)"))
clauses.append(expr("Sintoma(x, DolorOidos) ==> Enfermo(x, Otitis)"))
clauses.append(expr(
    "Sintoma(x, VisionBorroza) & Sintoma(x, DolorCabeza) ==> Enfermo(x, Migraña)"))
clauses.append(expr(
    "Sintoma(x, Vomito) & Sintoma(x, DolorAbdomen) ==> Enfermo(x, Apendicitis)"))
# Síntomas Medibles
clauses.append(expr("Sintoma(x, GlucosaAlta) ==> Enfermo(x, Diabetes)"))
clauses.append(expr("Sintoma(x, HemoglobinaBaja) ==> Enfermo(x, Anemia)"))
clauses.append(
    expr("Sintoma(x, ColesterolAlto) ==> Enfermo(x, Hipercolesterolemia)"))
clauses.append(
    expr("Sintoma(x, TrigliceridosAltos) ==> Enfermo(x, Hipertrigliceridemia)"))
clauses.append(
    expr("Sintoma(x, CreatininaAlta) ==> Enfermo(x, InsuficienciaRenal)"))
# Tratamientos a Síntomas Normales
clauses.append(expr("Enfermo(x, Migraña) ==> Tratamiento(x, Analgesicos)"))
clauses.append(expr("Enfermo(x, Faringitis) ==> Tratamiento(x, Antibioticos)"))
clauses.append(
    expr("Enfermo(x, Gastroenteritis) ==> Tratamiento(x, Hidratacion)"))
clauses.append(expr("Enfermo(x, Lumbalgia) ==> Tratamiento(x, Fisioterapia)"))
clauses.append(
    expr("Enfermo(x, Bronquitis) ==> Tratamiento(x, Broncodilatadores)"))
clauses.append(
    expr("Enfermo(x, Artritis) ==> Tratamiento(x, Antiinflamatorios)"))
clauses.append(expr("Enfermo(x, Otitis) ==> Tratamiento(x, Analgesicos)"))
clauses.append(expr("Enfermo(x, Apendicitis) ==> Tratamiento(x, Cirugia)"))
# Tratamientos a Síntomas Medibles
clauses.append(expr("Enfermo(x, Diabetes) ==> Tratamiento(x, Insulina)"))
clauses.append(expr("Enfermo(x, Anemia) ==> Tratamiento(x, SuplementoHierro)"))
clauses.append(
    expr("Enfermo(x, Hipercolesterolemia) ==> Tratamiento(x, Estatinas)"))
clauses.append(
    expr("Enfermo(x, Hipertrigliceridemia) ==> Tratamiento(x, Fibratos)"))
clauses.append(
    expr("Enfermo(x, InsuficienciaRenal) ==> Tratamiento(x, Dialisis)"))

# ========================================
# Knowledge base
# ========================================
kb = FolKB(clauses)

# ========================================
# Knowledge about a patient
# ========================================
name = input("¿Cuál es tu nombre? ")

# Ejemplo de uso
"""# Preguntas normales de síntomas
if input("¿Tienes cuerpo cortado? ").lower() == 's':
    kb.tell(expr("Sintoma({}, CuerpoCortado)".format(name)))
if input("¿Tienes escurrimiento? ").lower() == 's':
    kb.tell(expr("Sintoma({}, Escurrimiento)".format(name)))
if input("¿Tienes sueño? ").lower() == 's':
    kb.tell(expr("Sintoma({}, Sueno)".format(name)))
if input("¿Tienes fiebre? ").lower() == 's':
    kb.tell(expr("Sintoma({}, Fiebre)".format(name)))
if input("¿Tienes cansancio? ").lower() == 's':
    kb.tell(expr("Sintoma({}, Cansancio)".format(name)))"""

# Preguntas de niveles de laboratorio


def interpretar_glucosa(nivel):
    if nivel > 125:
        return "GlucosaAlta"
    elif nivel < 70:
        return "GlucosaBaja"
    else:
        return "GlucosaNormal"


def interpretar_hemoglobina(nivel):
    if nivel < 12:
        return "HemoglobinaBaja"
    elif nivel > 18:
        return "HemoglobinaAlta"
    else:
        return "HemoglobinaNormal"


def interpretar_colesterol(nivel):
    if nivel > 200:
        return "ColesterolAlto"
    else:
        return "ColesterolNormal"


def interpretar_trigliceridos(nivel):
    if nivel > 150:
        return "TrigliceridosAltos"
    else:
        return "TrigliceridosNormales"


def interpretar_creatinina(nivel):
    if nivel > 1.3:
        return "CreatininaAlta"
    else:
        return "CreatininaNormal"


nivel_glucosa = float(input("¿Cuál es tu nivel de glucosa (mg/dL)? "))
resultado_glucosa = interpretar_glucosa(nivel_glucosa)
if resultado_glucosa != "GlucosaNormal":
    kb.tell(expr("Sintoma({}, {})".format(name, resultado_glucosa)))

nivel_hemoglobina = float(input("¿Cuál es tu nivel de hemoglobina (g/dL)? "))
resultado_hemoglobina = interpretar_hemoglobina(nivel_hemoglobina)
if resultado_hemoglobina != "HemoglobinaNormal":
    kb.tell(expr("Sintoma({}, {})".format(name, resultado_hemoglobina)))

nivel_colesterol = float(
    input("¿Cuál es tu nivel de colesterol total (mg/dL)? "))
resultado_colesterol = interpretar_colesterol(nivel_colesterol)
if resultado_colesterol != "ColesterolNormal":
    kb.tell(expr("Sintoma({}, {})".format(name, resultado_colesterol)))

nivel_trigliceridos = float(
    input("¿Cuál es tu nivel de triglicéridos (mg/dL)? "))
resultado_trigliceridos = interpretar_trigliceridos(nivel_trigliceridos)
if resultado_trigliceridos != "TrigliceridosNormales":
    kb.tell(expr("Sintoma({}, {})".format(name, resultado_trigliceridos)))

nivel_creatinina = float(input("¿Cuál es tu nivel de creatinina (mg/dL)? "))
resultado_creatinina = interpretar_creatinina(nivel_creatinina)
if resultado_creatinina != "CreatininaNormal":
    kb.tell(expr("Sintoma({}, {})".format(name, resultado_creatinina)))

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
    print("No hay diagnóstico.")

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
