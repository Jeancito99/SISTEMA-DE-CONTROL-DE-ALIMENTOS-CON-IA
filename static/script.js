async function actualizarDatos() {

    try {

        const response = await fetch(
            "/api/lecturas"
        );

        const datos = await response.json();

        if (datos.length > 0) {

            const ultima = datos[0];

            document.getElementById(
                "alimento"
            ).innerText = ultima.alimento;

            document.getElementById(
                "estado"
            ).innerText = ultima.estado;

            document.getElementById(
                "temperatura"
            ).innerText =
                ultima.temperatura + " °C";

            document.getElementById(
                "humedad"
            ).innerText =
                ultima.humedad + " %";

            document.getElementById(
                "vida_util"
            ).innerText =
                ultima.vida_util + " días";

        }

    } catch(error) {

        console.log(error);

    }
}

// Actualizar cada 5 segundos
setInterval(
    actualizarDatos,
    5000
);

// Primera carga
actualizarDatos();