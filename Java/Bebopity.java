// Bebopity
// https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z12zwjawytypdvf1s23vudxgqvbde1nn0

double prob = 0;
int count = 0;
for(int i = 0; i <10000; i++)
{
    int rand1  = (int)(Math.random()*100000 +1);
    int rand2  = (int)(Math.random()*100000 +1);
    for(int j = 2; j < rand1 && j < rand2; j++)
    {
        if(rand1 % j == 0 && rand2 % j ==0){
            count++;
            break;
        }
    }
}
prob = 10000-count;
prob /= 10000;
prob = Math.sqrt(6/prob);
System.out.println(prob);﻿
