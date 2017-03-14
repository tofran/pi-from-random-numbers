// GLaDHuRriCAn
// https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z12gth1a1oydwjbyr04cejpaituzvznafh4

#include <iostream>
#include <algorithm>
#include <math.h>

int main (int argc, char** argv)
{
 int ITER = 1;
 while( ITER < (1 << 30) )
 {
  int sum = 0;
  for( int i=0; i < ITER; i++)
   std::__gcd(rand(), rand()) == 1 ? sum++ :0;
  std::cout << "Pi is approx " << sqrt( 6.f/ (sum/(float)ITER) ) << " with " << ITER << " iterations." << std::endl;
  ITER *= 10;
 }
 std::cout << "Stopped at a maximum of " << ITER << " iterations" << std::endl;
 return 0;
}﻿
