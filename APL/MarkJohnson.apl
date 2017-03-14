Mark Johnson
https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z13oshxh1n24frcy404cdjzpzxnsgd1a3i4

I recreated this in the APL programming language for fun. Here are the functions I wrote for this:
avg←{(+/⍵)÷≢⍵}
factors←{((0=⍵{⍵|⍺}¨⍳⌈⍵÷2)/⍳⌈⍵÷2),⍵}
gcd←{{⊃⌽((factors ⍺)∊(factors ⍵))/(factors ⍺)}/⍵}
coprime←{1=gcd ⍵}

After defining those functions, this line of code alone redoes the math using 1000 rolls of a d120:
{(6÷(≢(coprime¨⍵)~1)÷(≢(coprime¨⍵)~0))*÷2}({?⍵}¨1000⍴120,¨{?⍵}¨1000⍴120)
This line's result is around 0.2 away from pi at most each time, but I wanted to go further.

This line of code alone does the same thing 100 times and takes the average result:
avg {(6÷(≢(coprime ¨⍵)~1)÷(≢(coprime ¨⍵)~0))*÷2}¨{{?⍵}¨1000⍴120,¨{?⍵}¨1000⍴120}¨⍳100
This line of code takes around 4 and a half seconds to run on my machine.

The results of the last line are seemingly always less than 0.02 away from pi.
There's probably a more efficient way to do this, but this was for fun anyway. Very cool stuff!﻿
