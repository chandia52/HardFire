// Preview de elementos
const change = src => {
document.getElementById('main').src = src
};



const addtocart=() =>{
    Swal.fire({
        icon: "success",
        title: "Se ha agregado su articulo al carrito exitosamente",
        showConfirmButton: true,
        timer: 3500
    });
}

const empty=()=>{
    Swal.fire({
        title: "No hay productos?",
        text: "Por favor seleccione algun producto",
        icon: "info"
    });
}