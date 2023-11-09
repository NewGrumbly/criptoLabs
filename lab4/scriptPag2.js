// ==UserScript==
// @name         Lab 4 Cripto Script Pagina 2
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  El titulo lo dice todo
// @author       You
// @match        https://magenta-larine-68.tiiny.site/
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.2.0/crypto-js.min.js#sha512-a+SUDuwNzXDvz4XrIcXHuCf089/iJAoN4lmrXJg18XnduKK6YlDHNRalv4yd1N40OKI80tFidF+rqTFKGPoWFQ==
// @icon         https://www.google.com/s2/favicons?sz=64&domain=tiiny.site
// @grant        none
// ==/UserScript==

(function() {
  'use strict';
// Obtener el texto dentro del elemento <p>
const parrafo = document.querySelector('p').textContent;

// Dividir el texto en oraciones basadas en el punto "."
const oraciones = parrafo.split('.');

// Inicializar la variable para almacenar las primeras letras
let primerasLetras = '';

// Iterar a través de las oraciones
for (let i = 0; i < oraciones.length; i++) {
const oracion = oraciones[i].trim(); // Eliminar espacios en blanco alrededor de la oración
if (oracion.length > 0) {
  // Obtener la primera letra de la oración
  const primeraLetra = oracion[0];
  primerasLetras += primeraLetra;
}
}
// Imprimir las primeras letras con el formato deseado en la consola
console.log(`La llave es: ${primerasLetras}`);

// Contar la cantidad de elementos <div> con clases que comienzan con 'M'
var cantDivs = document.querySelectorAll('div[class^="M"]').length;
// Imprimir cantidad de mensajes cifrados por consola
console.log('Los mensajes cifrados son: ' + cantDivs);

// Obtener todos los elementos <div> con clases que empiezan con 'M'
var divElements = document.querySelectorAll('div[class^="M"]')

// Creación elemento div que contendrá los mensajes descifrados
const resultadosDiv = document.createElement('div');
// Se asigna el id 'resultados-div' al div
resultadosDiv.id = 'resultados-div';
// Agrega al body de la página el div creado
document.body.appendChild(resultadosDiv);

// Iterar a través de los elementos div
for(var i = 0; i < divElements.length; i++){

// Se obtiene el atributo id del div
var mensajeCifrado = divElements[i].id;

// Se configura el modo de operación ECB para el cifrado 3DES
const configure = {
    mode: CryptoJS.mode.ECB
};

// Se convierte la variable primerasLetras en un formato que CryptoJS pueda entender como clave de cifrado
const llave = CryptoJS.enc.Utf8.parse(primerasLetras);
// Se aplica el descifrado del mensaje que utiliza el algoritmo 3DES a partir de la llave y el modo de operación ECB
var descifrado = CryptoJS.TripleDES.decrypt(mensajeCifrado, llave, configure);
// Imprimir mensaje cifrado y descifrado en consola
console.log(mensajeCifrado + ' '+ descifrado.toString(CryptoJS.enc.Utf8));

// Se crea un elemento <p>
const mensajeDescifrado = document.createElement('p');
// Se añade al elemento <p> el mensaje descifrado
mensajeDescifrado.textContent = descifrado.toString(CryptoJS.enc.Utf8);
// Se agrega a resultadosDiv el elemento <p> con el mensaje descifrado
resultadosDiv.appendChild(mensajeDescifrado);
}
})();