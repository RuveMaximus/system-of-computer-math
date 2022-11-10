const matrixSize = document.getElementById('matrixSize');
const matrixField = document.getElementById('matrixField');

buildMatrixField(matrixSize.value); 

matrixSize.addEventListener('change', function() {
    matrixField.innerHTML = "";
    buildMatrixField(matrixSize.value);    
});

function buildMatrixField(size) {
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