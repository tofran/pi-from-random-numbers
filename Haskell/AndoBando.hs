-- Ando Bando
-- https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z13rydqgqkipw13xy04cfxnauzqiwrgonjs

generatePi (upper) = sqrt(6/p)
    where
        gcdTable = [gcd x y | x <- [1..upper] , y <-[1..upper]]
        coPrimeCount = length $ filter (==1) gcdTable
        p = fromIntegral (coPrimeCount) / fromIntegral (upper ^ 2)
