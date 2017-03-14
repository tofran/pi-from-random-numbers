// John Lindstedt
// https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z13mgb05brywgjn0123fxlrpttuxenbla
//Some c++ code

#include <iostream>
#include <iomanip>
#include <random>
#include <cmath>
#include <climits>

using namespace std;

long double simulate(long int const& Nr_s);
bool coPrime (int const& a, int const& b);


int main(){
    long int Nr_s;
    long double pi{};
    cout << "How many throws: ";
    cin >> Nr_s;
    pi = sqrt(6/(long double)simulate(Nr_s));
    cout << "Pi was simulated to:" << fixed << setprecision(13) << pi << endl;

    return 0;
}
long double simulate(const long int &Nr_s){
    long int coprime{0};
        // Seed with a real random value, if available
    random_device rd;
    mt19937 gen(rd()); //Standard mersenne_twister_engine seeded with rd()
    cout << endl;
    for(long int i{}; i < Nr_s; i++){
        uniform_int_distribution<int> uniform_dist(1, 1000000);
        if(coPrime(uniform_dist(gen),uniform_dist(gen))){
            coprime++;
        }
    }
    long double san = coprime/(long double)Nr_s;
    return san;
}
bool coPrime (const int &a, const int &b) { // Assumes a, b > 0
   return (a<b) ? coPrime(b,a) : !(a%b) ? (b==1) : coPrime (b, a%b);
}﻿
