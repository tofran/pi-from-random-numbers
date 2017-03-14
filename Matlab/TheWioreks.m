% TheWioreks
% https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z135grnzwuixs3vv222rv3o5dna4wxobt04.1489441180418487

% How to Calulate PI with random numbers
size=input('What is the number of rolls you want to use?');
number=input('What is the size of dice that you want to use?');
format long;
doublecount=1;
Consecutivecount=1;
Number_of_42s=0;
Number_of_69s=0;
Number_of_1s=0;
Dart_Perfect=0;
primecount=1;
dartcount=1;
CoPrime=0;
CoFactor=0;
x=randi(number,size,2);
k=1;
while(k<=(size))
   a=x(k,1);
   b=x(k,2);
   if(a==b)
       Double_Numbers(doublecount,1)=a;
       Double_Numbers(doublecount,2)=b;
       doublecount=doublecount+1;
   elseif((a==(b+1))||(a==(b-1)))
       Consecutive_numbers(Consecutivecount,1)=a;
       Consecutive_numbers(Consecutivecount,2)=b;
       Consecutivecount=Consecutivecount+1;
   elseif((a==42)||(b==42))
       Number_of_42s=Number_of_42s+1;
   elseif((a==69)||(b==69))
       Number_of_69s=Number_of_69s+1;
   elseif((isprime(a)==1)&&(isprime(b)==1))
       Double_Primes(primecount,1)=a;
       Double_Primes(primecount,2)=b;
       primecount=primecount+1;
       if((a+b)==180)
           Dart_Perfect(dartcount,1)=a;
           Dart_Perfect(dartcount,2)=b;
           dartcount=dartcount+1;
       end
   elseif((a+b==180))
       Dart_Perfect(dartcount,1)=a;
       Dart_Perfect(dartcount,2)=b;
       dartcount=dartcount+1;
   elseif((a==1)||(b==1));
       Number_of_1s=Number_of_1s+1;
   end
   factor=gcd(a,b);
   if(factor==1);
       CoPrime=CoPrime+1;
   else
       CoFactor=CoFactor+1;
   end

   k=k+1;
end
Probability=CoPrime/size;
Double_Numbers
Double_Primes
Consecutive_numbers
Dart_Perfect
Number_of_1s
Number_of_42s
Number_of_69s
Approximate_PI=sqrt(6/Probability)
Percent_error=100*abs((Approximate_PI-pi)/pi)
