% 梁瑋瀚
% https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z13swh55mpjdc1kxo04cefyq3lepgpdozrg0k

function pi = baselpi(n,max)
k = ceil(max*rand(n,2));
for i = 1:n
    if gcd(k(i,1),k(i,2)) == 1
        a(i) = 1;
    end
end
x = sum(a)/n;
sqrt(6/x)
end﻿
