% seevernet1
% https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z12xch3rzubds3ghj04chx44fzatg1qiji0

%Happy Pi Day
%Estimates pi based on if two random integers are coprime or not in matlab
rolls=500; %how many rolls you want to do
max=120; %size of your dice
count=0;

for i=1:rolls
   a=round(rand()*max,0);
   b=round(rand()*max,0);
    if gcd(a,b)==1
        count=count+1;
    end

end

ratio=count/rolls;
pie=sqrt(6/ratio) %doesn't suppress output because this is what we want﻿
