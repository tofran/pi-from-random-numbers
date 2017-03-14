(*Cody Woodard*)
(*https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z13vwjrymvugfr3av04ccjzjpvqtdl4g0rk0k*)

dieSize = 120;
numOfTrials = 500;

diceRolls = # -> CoprimeQ @@ # & /@
  Table[{RandomInteger[{1, dieSize}], RandomInteger[{1, dieSize}]},
   numOfTrials]

ourPi = N[Sqrt[6/(Counts[Values[diceRolls]][True]/numOfTrials)]]

NumberLinePlot[{{Pi}, {ourPi}}, PlotRange -> {Pi*.95, Pi*1.05}]﻿
