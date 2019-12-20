import java.util.*;

class Individual implements Comparable< Individual > {
    public ArrayList<Integer> nodes;
    public List<List<Long>> nodeInfoArray;
    public Integer fitness;

    public Individual(ArrayList<Integer> nodesInput, List<List<Long>> infoInput) {
        nodes = nodesInput;
        nodeInfoArray = infoInput;
        fitness = calcFitness();
    }

    public ArrayList<Individual> mate(Individual parent2) {
        ArrayList<Individual> result = new ArrayList<Individual>();
        ArrayList<Integer> child1 = new ArrayList<Integer>(); 
        ArrayList<Integer> child2 = new ArrayList<Integer>(); 
        Random rand = new Random();

        int size = nodes.size();
        //crossover
        for (int i = 0; i < size-1; i++) {
            child1.add(nodes.get(i));
            child2.add(parent2.nodes.get(i));
        }
        int limit = rand.nextInt(Math.round(size/2));
        for (int i = 0; i < limit; i++) {
            Integer temp = child1.get(i);
            int index = child1.indexOf(parent2.nodes.get(i));
            child1.set(i, parent2.nodes.get(i));
            child1.set(index, temp);
            
            Integer temp2 = child2.get(i);
            int index2 = child2.indexOf(nodes.get(i));
            child2.set(i, nodes.get(i));
            child2.set(index2, temp2);

        }
        //mutate
        int probabilityMutate = rand.nextInt(100);
        if(probabilityMutate < 20){
            int num = rand.nextInt(size-1);
            for (int i = 0; i < num; i++) {
                int randIndex1 = rand.nextInt(size-1);
                int randIndex2 = rand.nextInt(size-1);

                Integer temp = child1.get(randIndex1);
                child1.set(randIndex1, child1.get(randIndex2));
                child1.set(randIndex2, temp);
                
                Integer temp2 = child2.get(randIndex1);
                child2.set(randIndex1, child2.get(randIndex2));
                child2.set(randIndex2, temp2);
            }
        }
        child1.add(child1.get(0));
        child2.add(child2.get(0));

        result.add(new Individual(child1, nodeInfoArray));
        result.add(new Individual(child2, nodeInfoArray));
        return result;
    }

    public int calcFitness() {
        Integer currentNode = -1;
        Integer prevNode = nodes.get(0);
        int totalDistance = 0;

        for (int i = 1; i < nodes.size(); i++) {
            currentNode = nodes.get(i);
            totalDistance += nodeInfoArray.get(prevNode).get(currentNode);
            prevNode = currentNode;
        }
        return totalDistance;
    }

    public Long getDistance(Integer node1, Integer node2){
        return nodeInfoArray.get(node1).get(node2);
    }

    @Override
    public int compareTo(Individual i) {
        return fitness.compareTo(i.fitness);
    }
}
