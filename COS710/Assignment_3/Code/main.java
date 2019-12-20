import java.util.*;

class GeneticAlgorithm {
    public static void main(String args[]) {
        Data data = new Data();
        ArrayList<Individual> directPopulation = new ArrayList<Individual>();
        ArrayList<IndirectIndividual> indirectPopulation = new ArrayList<IndirectIndividual>();

        try {
            data.inputData("berlin52.txt");
            int size = data.computedData.size();

            for (int i = 0; i < 5; i++) {
                int resInd = testIndirect(size, indirectPopulation, data);
                int resDir = testDirect(size, directPopulation, data);
                System.out.print("Indirect: "+resInd+" ");
                System.out.print("Direct: "+resDir);
            }
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static Individual tournamentSelection(ArrayList<Individual> population, int k) {
        Individual best = null;
        for (int i = 0; i < k; i++) {
            Random random = new Random();
            int randIndex = random.nextInt(population.size());
            Individual ind = population.get(randIndex);
            if (best == null || ind.fitness < best.fitness) {
                best = ind;
            }
        }
        return best;
    }

    public static IndirectIndividual indirectTournamentSelection(ArrayList<IndirectIndividual> population, int k) {
        IndirectIndividual best = null;
        for (int i = 0; i < k; i++) {
            Random random = new Random();
            int randIndex = random.nextInt(population.size());
            IndirectIndividual ind = population.get(randIndex);
            if (best == null || ind.fitness < best.fitness) {
                best = ind;
            }
        }
        return best;
    }

    public static int testIndirect(int size, ArrayList<IndirectIndividual> population, Data data) {
        String[] instructionSet = { "A", "B", "M", "D", "L" };
        int gen = 0;
        Random rand = new Random();

        for (int i = 0; i < size * 2; i++) {
            ArrayList<String> instructionList = new ArrayList<String>();
            int instructionLen = rand.nextInt(size * 2) + size;
            for (int k = 0; k < instructionLen; k++) {
                String instruction = instructionSet[rand.nextInt(instructionSet.length)];
                instructionList.add(instruction);
            }

            population.add(new IndirectIndividual(instructionList, data.computedData));
        }

        for (int i = 0; i < 10000; i++) {
            Collections.sort(population);
            ArrayList<IndirectIndividual> nextGeneration = new ArrayList<IndirectIndividual>();

            for (int k = 0; k < Math.round(population.size() * 0.1); k++) {
                nextGeneration.add(population.get(k));
            }
            while (nextGeneration.size() < size * 2) {
                IndirectIndividual parent1 = indirectTournamentSelection(population, size / 2);
                IndirectIndividual parent2 = indirectTournamentSelection(population, size / 2);
                ArrayList<IndirectIndividual> children = parent1.mate(parent2);
                nextGeneration.add(children.get(0));
                nextGeneration.add(children.get(1));
            }
            population = nextGeneration;
            // System.out.print("Generation: " + gen + " Instruction: " + population.get(0).instructions + "Fitness: "
            //         + population.get(0).fitness + "\n");
            // System.out.print("Generation: " + gen+ " Fitness: "+ population.get(0).fitness + "\n");
            gen++;
        }
        return population.get(0).fitness;
    }

    public static int testDirect(int size, ArrayList<Individual> population, Data data) {
        Integer[] arr = new Integer[size];
        for (int i = 0; i < size; ++i) {
            arr[i] = i;
        }
        // Initial Population
        for (int i = 0; i < size * 2; i++) {
            ArrayList<Integer> list = new ArrayList<Integer>(Arrays.asList(arr));
            Collections.shuffle(list);
            list.add(list.get(0));
            Individual individual = new Individual(list, data.computedData);
            population.add(individual);

        }

        for (int i = 0; i < 10000; i++) {
            Collections.sort(population);
            ArrayList<Individual> nextGeneration = new ArrayList<Individual>();

            for (int k = 0; k < Math.round(population.size() * 0.1); k++) {
                nextGeneration.add(population.get(k));
            }
            while (nextGeneration.size() < size * 2) {
                Individual parent1 = tournamentSelection(population, size / 2);
                Individual parent2 = tournamentSelection(population, size / 2);
                ArrayList<Individual> children = parent1.mate(parent2);
                nextGeneration.add(children.get(0));
                nextGeneration.add(children.get(1));
            }
            population = nextGeneration;
            // System.out.print("Generation: "+i+" Traverse:
            // "+population.get(0).nodes+"Fitness: "+population.get(0).fitness+"\n");
        }
        // System.out.print("Fitness: " + population.get(0).fitness + "\n");
        return population.get(0).fitness;
    }
}