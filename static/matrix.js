const matrixSize = document.getElementById('matrixSize');
const firstMatrixField = document.getElementById('firstMatrixField');
const secondMatrixField = document.getElementById('secondMatrixField');

refresh();
matrixSize.addEventListener('change', refresh);
getFunctions();

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

async function getFunctions() {
    const respone = await request('/functions/', {type: 'matrix'});
    const functionSelect = document.getElementById('function');
    for (let func of respone.functions) {
        let optionElem = document.createElement('option');
        optionElem.textContent = func.name;
        optionElem.value = func.value;
        functionSelect.append(optionElem);
    }
}

function getMatrix(matrixElem) {
    const inputElems = matrixElem.querySelectorAll('input');
    let matrix = [];
    for (let cRow = 0; cRow < matrixSize.value; cRow++) {
        let row = [];
        for (let cCell = 0; cCell < matrixSize.value; cCell++) {
            row.push(+inputElems[cRow*matrixSize.value+cCell].value);
        }
        matrix.push(row);
    }
    return matrix;
}

async function send() {
    const func = document.getElementById('function').value;

    const m1 = getMatrix(firstMatrixField);
    const m2 = getMatrix(secondMatrixField);

    const data = {
        'func': func,
        'first_matrix': m1, 
        'second_matrix': m2,
    }
    const response = await request(`/matrix/calc/`, data);
    console.log(response.result);

}

function refresh() {
    buildMatrixField(matrixSize.value, firstMatrixField); 
    buildMatrixField(matrixSize.value, secondMatrixField); 
}