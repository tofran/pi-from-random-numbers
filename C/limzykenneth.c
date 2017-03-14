// limzykenneth
// https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z12ow1yiwyq1d12eq221wjtqvm2vvp54y04


#include <iostream>
#include <math.h>
#include <stdint.h>
#include <random>
#include <chrono>

using namespace std;

uint64_t gcd(uint64_t a, uint64_t b);

uint64_t iterations = 1000000000;
int main(){
 cout<<"Calculating PI..."<<endl;
 unsigned seed1 = chrono::system_clock::now().time_since_epoch().count();
 mt19937_64 g1 (seed1);

 uint64_t i = 1;
 uint64_t count = 0;
 while(i < iterations){
  uint64_t n1 = g1();
  uint64_t n2 = g1();

  if(gcd(n1, n2) == 1){
   count++;
  }

  i++;
 }

 double probability = (double)count/(double)iterations;
 double pi = sqrt(6/probability);

 cout<<pi<<endl;

 return 0;
}

uint64_t gcd(uint64_t a, uint64_t b) {
    return b == 0 ? a : gcd(b, a % b);
}﻿
