function isNumber(value) {
    try {
        if (value === '0') return true;
        return parseFloat(value); 
    } catch(err) {
        return false;
    }
}

function getPoints(points) {
    let vector = [];
    for (point of points) {
        if (!isNumber(point.value)) { 
            showResult('Одна (или более) из введенных точек не явлется числом!');
            return;
        }
        vector.push(point.value);
    }
    return vector;
}

function calc() {
    let func = document.getElementById('func').value;
    let v1Points = document.getElementById('v1').querySelectorAll('input');
    let v2Points = document.getElementById('v2').querySelectorAll('input');

    let v1 = getPoints(v1Points);
    let v2 = getPoints(v2Points);

    if (v2.length == 1) {
        func += '_scalar';
    }

    let v1_str_points = v1.join(';');
    let v2_str_points = v2.join(';');

    let url = `/calc?func=${func}&v1=${v1_str_points}&v2=${v2_str_points}`; 

    fetch(url).then(response => response.text()).then(result => showResult(result));
}

function addPoint(elem) {
    let vector = elem.closest('.vector');
    let newPoint = document.createElement('input');
    newPoint.setAttribute('type', 'number');
    newPoint.setAttribute('value', '0');
    vector.querySelector('.points-list').append(newPoint);
}

function deletePoint(elem) {
    let point = elem.closest('.vector').querySelectorAll('input')[0];
    if (point) point.remove();
}

function showResult(message) {
    document.getElementById('result').innerText = message;
}