// MDuh Gaming
// https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z12nvl0pmyr4snxet22sf1vrhyngdrehl04
// https://github.com/mdnpascual/GCDPi/blob/master/GCDPi/Program.cs

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Security.Cryptography;
using System.Numerics;
using System.Diagnostics;

namespace GCDPi
{
    class Program
    {
        private static RNGCryptoServiceProvider rngCsp = new RNGCryptoServiceProvider();
        private static RNGCryptoServiceProvider rngCsp2 = new RNGCryptoServiceProvider();
        static void Main(string[] args)
        {
            Double max;
            int iter;
            Console.WriteLine("Number of Iteration? ");
            int.TryParse(Console.ReadLine(), out iter);
            Console.WriteLine("Max Val? ");
            double.TryParse(Console.ReadLine(), out max);

            Double Log = Math.Log(max, 2);  //Get bitlength n(2^n = max val) of arraybytes to be used with the BigInteger.
            Double bits = Math.Floor(Log);
            int bit = (int)bits;
            Console.WriteLine("Using Max Value: " + Math.Pow(2,bit));
            Double power = Math.Pow(2, bit);

            byte[] data = new byte[bit];    //Arraybytes storage
            byte[] data2 = new byte[bit];   //Spawned 2 RNG for 2 numbers generated per loop cycle
            double count = 0;

            Stopwatch stopWatch = new Stopwatch();  //Time Elapsed timer
            stopWatch.Start();
            //Console.Write("Progress: 0 of "+ iter);
            using (Process p = Process.GetCurrentProcess())
                p.PriorityClass = ProcessPriorityClass.RealTime;    //Set process priority to Realtime
            for (int i = 0; i < iter; i++)
            {
                rngCsp.GetBytes(data);  //Generate random bytes for BigInteger
                rngCsp2.GetBytes(data2);

                BigInteger big = new BigInteger(data);  //Get Arraybytes and convert to BigInteger (can generate negative numbers)
                big = BigInteger.ModPow(big, BigInteger.One, new BigInteger(power));    //BigInteger mod maxval
                BigInteger big2 = new BigInteger(data2);
                big2 = BigInteger.ModPow(big2, BigInteger.One, new BigInteger(power));
                BigInteger gcd = BigInteger.GreatestCommonDivisor(big, big2);
                if (gcd.IsOne){
                    count++;
                }
                //Console.Write("\rProgress: " + (i+1) + " of " + iter); //Printing progress eats too much of the processing time so I disabled it
            }
            stopWatch.Stop();
            Double prob = count / (double)iter;
            Double pi = Math.Sqrt(6.0 / prob);
            Console.WriteLine("\nPi Estimate: " + pi);
            Console.WriteLine("Time spent: " + stopWatch.Elapsed.ToString());
            Console.WriteLine("Press Any key to close");
            Console.ReadLine();
        }
    }
}
