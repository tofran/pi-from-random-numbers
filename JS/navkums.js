// navkums
// https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z12qg1tw2prghb32t23jg52jawrisroaa04
// https://jsbin.com/meduluy/edit?output﻿

function compute() {
    //document.getElementById("pi").innerHTML = calculatePi(100000);
    console.log(calculatePi(100000));
}

function calculatePi(n) {

    function gcd(a, b) {
        if (b === 0) return a;
        return gcd(b, a % b);
    }

    var coprime = 0;
    var cofactor = 0;

    for (var i = 0; i < n; i++) {
        var a = Math.round(Math.random() * 1e6);
        var b = Math.round(Math.random() * 1e6);
        if (gcd(a, b) == 1) {
            coprime++;
        } else {
            cofactor++;
        }

    }
    var x = coprime / (coprime + cofactor);
    return Math.sqrt(6 / x);
}
