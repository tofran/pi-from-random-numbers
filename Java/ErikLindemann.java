// Erik Lindemann AKA eLindemann
// https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z12djj2hatbxtzlha04cefibzuvrjpoqgoo0k
// https://github.com/eLindemann/PiGenerator

import java.math.BigInteger;
import java.util.Random;
import java.util.Scanner;

/**
 *
 * @author Erik Lindemann <lindemannerik@gmail.com>
 */
public class PiGenerator {
    int numberOfTrials;
    int bound;
    Random generator;
    int coPrimes;

    public PiGenerator(int numberOfTrials, int bound) {
        this.numberOfTrials = numberOfTrials;
        this.bound = bound;
        this.generator = new Random();
        this.coPrimes = 0;
    }

    public void Run() {
        for (int i = 0; i < numberOfTrials; i++) {
            BigInteger firstRandom = BigInteger.valueOf(generator.nextInt(bound));
//            System.out.println("firstRandom: " + firstRandom);
            BigInteger secondRandom = BigInteger.valueOf(generator.nextInt(bound));
//            System.out.println("secondRandom: " + secondRandom);
            BigInteger greatestCommon = firstRandom.gcd(secondRandom);
//            System.out.println("GCD: " + greatestCommon);

            if (greatestCommon.intValue() == 1) {
                coPrimes++;
            }
        }
        double probability = (double) coPrimes / numberOfTrials;
        double piEstimate = Math.sqrt(6.0/probability);
        System.out.println("Pi Estimate: " + piEstimate);
    }

    public static void main(String[] args) {

        Scanner reader = new Scanner(System.in);
        System.out.println("Pi Estimator Tool!");
        System.out.print("How many trials: ");
        int trials = Integer.parseInt(reader.nextLine());
        System.out.print("Upper bound for randomization: " );
        int bound = Integer.parseInt(reader.nextLine());

        PiGenerator generatomatic = new PiGenerator(trials, bound);
        generatomatic.Run();

    }
}
