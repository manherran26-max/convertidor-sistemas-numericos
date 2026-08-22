document.getElementById("convertButton").addEventListener("click", async function() {

    let valor = document.getElementById("inputValue").value;

    let base = Number(
        document.getElementById("baseEntrada").value
    );

    let bits = Number(
        document.getElementById("tamanoPalabra").value
    );


    let respuesta = await fetch("http://127.0.0.1:8000/convertir", {

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


    let datos = await respuesta.json();


    if (datos.error) {

        alert(datos.error);

        return;
    }


    document.getElementById("binario").value =
        datos.binario;

    document.getElementById("octal").value =
        datos.octal;

    document.getElementById("decimal").value =
        datos.decimal;

    document.getElementById("hexadecimal").value =
        datos.hexadecimal;

});

document.getElementById("ejecutarALU").addEventListener("click", async function() {

    let operando1 = document.getElementById("operando1").value.trim();

    let operando2 = document.getElementById("operando2").value.trim();

    let operacion = document.getElementById("operacion").value;


    if (operando1 === "" || operando2 === "") {
        alert("Ingrese los dos operandos.");
        return;
    }


    try {

        let respuesta = await fetch("http://127.0.0.1:8000/alu", {

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


        let datos = await respuesta.json();


        if (datos.error) {

            alert(datos.error);

            return;
        }


        document.getElementById("resultadoALU").value =
            datos.resultado;


    } catch (error) {

        console.error(error);

        alert("No se pudo conectar con el servidor FastAPI.");

    }

});