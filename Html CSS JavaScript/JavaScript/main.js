const contenido = document.getElementById("contenido");



let nom = "Josué Zambrano";
let edad = 17

let array = [23,45,34,12];

for(let i = 0; i < array.length; i++){
    addContent("<h3>" +"La edad es de: " + array[i] + "</h3>");
}


addContent("<h2>" + nom + "</h2>" , "<h3>" + edad + "</h3>")

if (edad > 18){
    alert("Puedes entrar en la disco");
}else if(edad > 13){
    alert("Puedes entrar solo con un adulto");
}else{
    alert("No puedes entrar");
}

for(let i = 0; i <10; i++){
    console.log(i);
}

for(let i = 0; i <=10; i++){
    addContent("<h3>" + i + "</h3>");
}


function addContent(newContent){
    console.log(newContent)
    contenido.innerHTML += newContent;
}

addContent("Hola programador");