// ==UserScript==
// @name         Lab 4 Cripto
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  El titulo lo dice todo
// @author       You
// @match        https://cripto.tiiny.site/
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
})();
