import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        int size = 100;

        Data trainData = new Data();
        Data testData = new Data();
        try {
            trainData.inputData("train.data");
            testData.inputData("test.data");
        } catch (Exception e) {
            e.printStackTrace();
        }

        for (int j = 0; j < 20; j++) {
            ArrayList<Chromosome> population = new ArrayList<Chromosome>();
            for (int i = 0; i < size; i++) {
                population.add(new Chromosome(5, trainData));
            }

            Chromosome bestTest = train(population);
            Double perc = ((Double.valueOf(bestTest.fitness) / 115.0) * 100);
            System.out.println("Train Result: " + perc + "%");

            bestTest.data = testData;
            perc = ((Double.valueOf(bestTest.calcFitness(bestTest.tree.root)) / 35.0) * 100);
            System.out.println("Test Result: " + perc + "%");
        }


    }

    public static Chromosome train(ArrayList<Chromosome> population) {
        int size = 100;
        Collections.sort(population, Collections.reverseOrder());

        for (int i = 0; i < 100; i++) {
            ArrayList<Chromosome> nextGeneration = new ArrayList<Chromosome>();

            for (int k = 0; k < Math.round(population.size() * 0.1); k++) {
                nextGeneration.add(population.get(k));
                // population.remove(k);
            }
            while (nextGeneration.size() < size) {
                Chromosome parent1 = tournamentSelection(population, Math.round(size / 3));
                Chromosome parent2 = tournamentSelection(population, Math.round(size / 3));
                ArrayList<Chromosome> children = parent1.mate(parent2);
                nextGeneration.add(children.get(0));
                nextGeneration.add(children.get(1));
            }
            population = nextGeneration;
            Collections.sort(population, Collections.reverseOrder());
            // System.out.print("Generation: " +i+ " Fitness: "+ population.get(0).fitness +
            // "\n");
        }

        return population.get(0);
    }

    public static Chromosome tournamentSelection(ArrayList<Chromosome> population, int k) {
        Chromosome best = null;
        for (int i = 0; i < k; i++) {
            Random random = new Random();
            int randIndex = random.nextInt(population.size());
            Chromosome ind = population.get(randIndex);
            if (best == null || ind.fitness > best.fitness) {
                best = ind;
            }
        }
        return best.copy();
    }
}