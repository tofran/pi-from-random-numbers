// elijah finn
// https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z12nd5eirr2djf2ew23qttvjuqyserklk

import java.util.concurrent.ThreadLocalRandom;
public class Pi
{
   public static void main(String [] args)
   {
      double sum=0;
      int max=100000000;
      double tries=10000000;
      int a,b;
      double pi=0;
      while(pi!=Math.PI)
      {
         for (int i=0;i<=tries;i++)
         {
            a=ThreadLocalRandom.current().nextInt(0, max + 1);
            b=ThreadLocalRandom.current().nextInt(0, max + 1);

            sum= sum +cop(gcd(a,b));
         }


         if (Math.abs(findPi(sum,tries)-Math.PI)<Math.abs(pi-Math.PI))
         {
            pi=findPi(sum,tries);
            System.out.println(pi);
         }
      //System.out.println(Math.abs(findPi(sum,tries)-Math.PI));
      //System.out.println(Math.abs(pi-Math.PI));

         sum=0;

      }
   }


   public static double findPi(double sum,double tries)
   {

      double temp=sum/tries;
      return Math.sqrt(6/temp);
   }

   public static int cop(int coPrime)
   {
      if (coPrime==1)
         return 1;
      return 0;
   }

   public static int gcd(int a, int b)
   {
      if (b==0)
         return a;
      return gcd(b,a%b);
   }

}﻿
