// Apunta a la carpeta /api tanto en local como en Vercel
const API_URL = window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1" 
    ? "http://127.0.0.1:8000/api" 
    : "/api";

document.getElementById("convertButton").addEventListener("click", async function () {
    const valor = document.getElementById("inputValue").value.trim();
    const base = Number(document.getElementById("baseEntrada").value);
    const bits = Number(document.getElementById("tamanoPalabra").value);

    if (valor === "") {
        alert("Ingrese un valor.");
        return;
    }

    try {
        // La URL final será /api/convertir
        const respuesta = await fetch(`${API_URL}/convertir`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                valor: valor,
                base: base,
                bits: bits
            })
        });

        const datos = await respuesta.json();

        if (!respuesta.ok || datos.error) {
            alert(datos.error || "Error al realizar la conversión.");
            return;
        }

        document.getElementById("binario").value = datos.binario;
        document.getElementById("octal").value = datos.octal;
        document.getElementById("decimal").value = datos.decimal;
        document.getElementById("hexadecimal").value = datos.hexadecimal;

    } catch (error) {
        console.error("Error:", error);
        alert("No se pudo conectar con el servidor.");
    }
});

document.getElementById("ejecutarALU").addEventListener("click", async function () {
    const operando1 = document.getElementById("operando1").value.trim();
    const operando2 = document.getElementById("operando2").value.trim();
    const operacion = document.getElementById("operacion").value;

    if (operando1 === "" || operando2 === "") {
        alert("Ingrese los dos operandos.");
        return;
    }

    try {
        // La URL final será /api/alu
        const respuesta = await fetch(`${API_URL}/alu`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                operando1: operando1,
                operando2: operando2,
                operacion: operacion
            })
        });

        const datos = await respuesta.json();

        if (!respuesta.ok || datos.error) {
            alert(datos.error || "Error al ejecutar la ALU.");
            return;
        }

        document.getElementById("resultadoALU").value = datos.resultado;

    } catch (error) {
        console.error("Error:", error);
        alert("No se pudo conectar con el servidor.");
    }
});