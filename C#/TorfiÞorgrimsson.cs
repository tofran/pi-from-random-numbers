// Torfi Þorgrímsson
// https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z135grnzwuixs3vv222rv3o5dna4wxobt04


public static int GetGCD(int value1, int value2)
{
    while (value1 != 0 && value2 != 0)
    {
        if (value1 > value2)
            value1 %= value2;
        else
            value2 %= value1;
    }
    return Math.Max(value1, value2);
}

public static bool Coprime(int value1, int value2)
{
    return GetGCD(value1, value2) == 1;
}

public static double checkProbe(int range, int trys)
{
    Random rand = new Random();

    bool[] coprimeNum = new bool[trys];

    for (int i = 0; i < trys; i++)
    {
        int val1 = rand.Next(1, range), val2 = rand.Next(1, range);

        if (Coprime(val1, val2))
        {
            coprimeNum[i] = true;
        }
        else
        {
            coprimeNum[i] = false;
        }
    }

    int coprimeCount = 0;

    for (int i = 0; i < coprimeNum.Count(); i++)
    {
        if (coprimeNum[i])
        {
            coprimeCount++;
        }
    }

    return Convert.ToDouble(coprimeCount) / trys;
}

public static double pi(int range, int trys)
{
    return Math.Sqrt(6 / checkProbe(range, trys));
}﻿
