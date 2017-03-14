// Justin Murtagh
// https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z13xel1xjwqwihbpx04cjh3b2kuggz1ocxk0k
// https://jsfiddle.net/cmL8s4gg/1/

function gcd(a,b) {
    if (a < 0) a = -a;
    if (b < 0) b = -b;
    if (b > a) {var temp = a; a = b; b = temp;}
    while (true) {
        if (b == 0) return a;
        a %= b;
        if (a == 0) return b;
        b %= a;
    }
}

function getPi (dieSize, numberOfRolls) {
	let coprimeCount = 0;
	for (let i = 0; i < numberOfRolls; i++) {
		const a = Math.round(Math.random() * dieSize);
		const b = Math.round(Math.random() * dieSize);

		if (gcd(a, b) == 1)
			coprimeCount++;
	}

	const probability = coprimeCount / numberOfRolls;
	const pi = Math.sqrt(6 / probability);

	return pi;
}
