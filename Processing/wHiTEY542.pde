// wHiTEY 542
// https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z12iytvpnmmbyn54r04chhzimu21xn5jpvc0k
// http://pastebin.com/jBeU06mD

int maxNum = 10000000;
float maxNums = 10000000;
float Pi, prop, count, AvgPI, buffer;

void draw() {
  int[] numA = new int[round(maxNums)];
  int[] numB = new int[round(maxNums)];
  count = 0;
  for (int i = 0; i < maxNums; i++) {
    numA[i] = ceil(random(maxNum));
    numB[i] = ceil(random(maxNum));
  }
  for (int i = 0; i < maxNums; i++) {
    if (gcd(numA[i], numB[i]) == 1) {
      count++;
    }
  }
  prop = count / maxNums;
  Pi = sqrt(6/prop);
  buffer += Pi;
  AvgPI = buffer/frameCount;
  println(AvgPI);
}

int gcd(int a, int b) {
  int c;
  while ( a != 0 ) {
    c = a;
    a = b%a;
    b = c;
  }
  return b;
}
