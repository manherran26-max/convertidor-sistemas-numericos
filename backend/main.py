from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from conversiones import convertir, operacion_alu


app = FastAPI()

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# DATOS DEL CONVERSOR
# ==========================================

class DatosConversion(BaseModel):

    valor: str
    base: int
    bits: int


# ==========================================
# DATOS DE LA ALU
# ==========================================

class DatosALU(BaseModel):

    operando1: str
    operando2: str
    operacion: str


# ==========================================
# ENDPOINT CONVERSOR
# ==========================================

@app.post("/convertir")
def convertir_numero(datos: DatosConversion):

    return convertir(
        datos.valor,
        datos.base,
        datos.bits
    )


# ==========================================
# ENDPOINT ALU
# ==========================================

@app.post("/alu")
def ejecutar_alu(datos: DatosALU):

    return operacion_alu(
        datos.operando1,
        datos.operando2,
        datos.operacion
    )