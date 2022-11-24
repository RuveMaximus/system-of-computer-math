const matrixSize = document.getElementById('matrixSize');
const firstMatrixField = document.getElementById('firstMatrixField');
const secondMatrixField = document.getElementById('secondMatrixField');

refresh();

matrixSize.addEventListener('change', refresh);

function buildMatrixField(size, matrixField) {
    matrixField.innerHTML = "";
    for (let i=0; i < size; i++) {
        for (let j=0; j < size; j++) {
            let elem = document.createElement('input');
            elem.setAttribute('type', 'number');
            elem.classList.add('matrix-node');
            matrixField.append(elem);
        }
        matrixField.innerHTML += "</br>";
    }   
}

async function send() {
    const func = document.getElementById('function').value;
    console.log(await request(`/matrix/calc?func=${func}`))
}
send()

function refresh() {
    buildMatrixField(matrixSize.value, firstMatrixField); 
    buildMatrixField(matrixSize.value, secondMatrixField); 
}