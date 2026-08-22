import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
sys.path.append(str(BASE_DIR))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from conversiones import convertir, operacion_alu
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DatosConversion(BaseModel):

    valor: str
    base: int
    bits: int

class DatosALU(BaseModel):

    operando1: str
    operando2: str
    operacion: str

@app.post("/convertir")
def convertir_numero(datos: DatosConversion):

    return convertir(
        datos.valor,
        datos.base,
        datos.bits
    )

@app.post("/alu")
def ejecutar_alu(datos: DatosALU):

    return operacion_alu(
        datos.operando1,
        datos.operando2,
        datos.operacion
    )

@app.get("/")
def read_index():
    index_path = BASE_DIR.parent / "index.html"
    return FileResponse(index_path)
app.mount("/", StaticFiles(directory=str(BASE_DIR.parent)), name="static")