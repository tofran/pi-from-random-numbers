-- Altoids The Destroyer
-- https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z13xwr05qoucxh1se23uv3l4fkelvppz004

-- The probability that two random numbers don't share a factor other than 1, == 6 / (pi^2)
-- I will now be using this to calculate pi.
-------------------------------------------------------------------------------
function isprime(n) -- Returns whether something is prime with only as many modulo operations as there are primes below it's sqrt
-- Putting a big composite into this immediately returns true
 if primes == nil then -- Creates the prime array. Could've been in int main(), but this makes it self-contained.
  primes = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197}
 end
 if n > primes[#primes]^2 + 1 then
  error("USER ERROR: Number is too large for the array already generated!\nStart with a smaller n and increment up!")
 end
 squirt = math.sqrt(n) + 1
   ----
   if n == 1 then
  return false
 end
 for _,v in ipairs(primes) do
  if v >= squirt then -- If so, we've gone thru all the primes that could be its factor, so it has to be prime.
   if n > primes[#primes] then
    primes[#primes+1] = n -- Sets the next prime to n, improving the array over time
   end
   return true
  elseif n%v == 0 then
   return false
  end
 end
end
function prime_gen(i) -- Generates all the primes between 1 and i (default i == 1,000,000 )
 for a=197,i,2 do
  b = isprime(a)
 end
 print("Primes are done generating!")
end
function shares_factor() -- Returns true if a and b share a factor, false if not
 for _,v in ipairs(primes) do
  if a%v == 0 and b%v == 0 then
   return true
  end
 end
 return false
end
math.randomseed(os.time())
it = 100000 -- How many times it will compare the two random numbers
max_ = 1000000000 -- The largest number that will be used for the test
prime_gen(math.ceil(math.sqrt(max_)))
main_array = {0,0}
counter = 0
for i=1,it do
 a = math.random(max_)
 b = math.random(max_)
 if shares_factor() then
  main_array[1] = main_array[1] + 1 -- Stores how many share a factor
 else
  main_array[2] = main_array[2] + 1 -- Stores how many that don't.
 end
 counter = counter + 1
 if counter == it/1000 then
  counter = 0
  print(i/it*100 .. "%...")
 end
end
-- The probability that two random numbers don't share a factor other than 1, == 6 / (pi^2) ~= 0.601 == 60.1%
x = main_array[2] / (main_array[1] + main_array[2]) -- Should be 0.601
print("X seems to be: "..x)
pie = math.sqrt(6/x)
print("Pi seems to be: "..pie)
pi = 3.1415926535897 -- Recited from memory!
erreur = math.abs((pi - pie))/pi*100
print("This has an error of " .. erreur .. "% !")﻿
