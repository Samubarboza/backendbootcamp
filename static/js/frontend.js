// obtener referencias 
const link = document.getElementById("favorites-link");
const overlay = document.getElementById("portal-overlay");

// veriicar que los dos existen 
if (link && overlay){
    link.onclick = function (e){
        // frenar la navegacion inmediata 
        e.preventDefault();

        // mostrar el portal 
        overlay.style.display = "flex";

        // navegar despues de un delay corto
        setTimeout(() => {
            window.location.href = link.href; //favoritos
        }, 600);
    }
}
