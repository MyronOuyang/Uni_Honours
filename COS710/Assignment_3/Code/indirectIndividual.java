import java.util.*;


class IndirectIndividual implements Comparable<IndirectIndividual> {
    public ArrayList<String> instructions;
    public ArrayList<Integer> nodes;
    public List<List<Long>> nodeInfoArray;
    public Integer fitness;

    public IndirectIndividual(ArrayList<String> nodesInput, List<List<Long>> infoInput) {
        instructions = nodesInput;
        nodeInfoArray = infoInput;
        fitness = decode();
    }

    public ArrayList<IndirectIndividual> mate(IndirectIndividual parent2) {
        ArrayList<IndirectIndividual> result = new ArrayList<IndirectIndividual>();
        ArrayList<String> child1 = new ArrayList<String>();
        ArrayList<String> child2 = new ArrayList<String>();
        ArrayList<String> longerParent = new ArrayList<String>();
        ArrayList<String> shorterParent = new ArrayList<String>();
        Random rand = new Random();

        int size1 = Math.round(instructions.size()/2);
        int size2 = Math.round(parent2.instructions.size()/2);

        // crossover
        if(size1 < size2){
            longerParent = parent2.instructions;
            shorterParent = instructions;
        }else{
            longerParent = instructions;
            shorterParent = parent2.instructions;
        }
        for (int i = 0; i < longerParent.size(); i++) {
            if(i < Math.round(shorterParent.size()/2)){
                child1.add(shorterParent.get(i));
            }else{
                child1.add(longerParent.get(i));
            }
        }
        for (int i = 0; i < shorterParent.size(); i++) {
            if(i < Math.round(shorterParent.size()/2)){
                child2.add(longerParent.get(i));
            }else{
                child2.add(shorterParent.get(i));
            }
        }

        // mutate
        int probabilityMutate = rand.nextInt(100);
        if (probabilityMutate < 30) {
            String[] instructionSet = {"A","B","M","D","L"};

            int num1 = rand.nextInt(child1.size())+1;
            int num2 = rand.nextInt(child2.size())+1;
            for (int i = 0; i < num1; i++) {
                int randIndex = rand.nextInt(child1.size());
                String randomInstruction = instructionSet[rand.nextInt(instructionSet.length)];
                child1.set(randIndex, randomInstruction);
            }
            for (int i = 0; i < num2; i++) {
                int randIndex = rand.nextInt(child2.size());
                String randomInstruction = instructionSet[rand.nextInt(instructionSet.length)];
                child2.set(randIndex, randomInstruction);
            }
        }

        result.add(new IndirectIndividual(child1, nodeInfoArray));
        result.add(new IndirectIndividual(child2, nodeInfoArray));
        return result;
    }

    public int decode() {
        ArrayList<Integer> nodes = new ArrayList<Integer>();
        int fitness = 0;
        int size = nodeInfoArray.size();

        ArrayList<Integer> available = new ArrayList<Integer>();
        for (int i = 0; i < size; ++i) {
            available.add(i);
        }

        for (int i = 0; i < instructions.size(); i++) {
            Random rand = new Random();

            switch (instructions.get(i)) {
            case "A":
                if (available.size() > 0) {
                    int index = rand.nextInt(available.size());
                    nodes.add(available.get(index));
                    available.remove(index);
                }
                break;
            case "B":
                if (available.size() > 0 && nodes.size() > 0) {
                    Integer lastNode = nodes.get(nodes.size() - 1);
                    Integer bestNextNode = available.get(0);
                    for (int j = 0; j < available.size(); j++) {
                        if (getDistance(lastNode, available.get(j)) < getDistance(lastNode, bestNextNode)) {
                            bestNextNode = available.get(j);
                        }
                    }
                    nodes.add(bestNextNode);
                    available.remove(bestNextNode);
                } else if (available.size() > 0 && nodes.size() == 0) {
                    int index = rand.nextInt(available.size());
                    nodes.add(available.get(index));
                    available.remove(index);
                }
                break;
            case "M":
                if (nodes.size() > 1) {
                    int randIndex1 = rand.nextInt(nodes.size());
                    int randIndex2 = rand.nextInt(nodes.size());
                    Integer temp = nodes.get(randIndex1);
                    nodes.set(randIndex1, nodes.get(randIndex2));
                    nodes.set(randIndex2, temp);
                }
                break;
            case "D":
                if (nodes.size() > 0) {
                    int index = rand.nextInt(nodes.size());
                    available.add(nodes.get(index));
                    nodes.remove(index);
                }
                break;
            case "L":
                if (nodes.size() > 1) {
                    Integer prev = nodes.get(0);
                    Integer longestPrev = nodes.get(0);
                    Integer longestNext = nodes.get(1);
                    for (int j = 1; j < nodes.size(); j++) {
                        Integer current = nodes.get(j);
                        if (getDistance(prev, current) > getDistance(longestPrev, longestNext)) {
                            longestPrev = prev;
                            longestNext = current;
                        }
                    }
                    available.add(longestNext);
                    nodes.remove(longestNext);
                }
                break;
            }
        }
        if(nodes.size() > 0)
            nodes.add(nodes.get(0));
        this.nodes = nodes;
        fitness = calcFitness();
        fitness += available.size() * 1000000;
        this.fitness = fitness;
        // System.out.print(this.nodes);
        // System.out.print(this.fitness);
        return this.fitness;
    }

    public int calcFitness() {
        if(nodes.size() == 0)
            return 0;
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

    public Long getDistance(Integer node1, Integer node2) {
        return nodeInfoArray.get(node1).get(node2);
    }

    @Override
    public int compareTo(IndirectIndividual i) {
        return fitness.compareTo(i.fitness);
    }
}
