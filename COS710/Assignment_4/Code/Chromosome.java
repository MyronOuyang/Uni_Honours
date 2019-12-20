import java.util.*;

public class Chromosome implements Comparable< Chromosome >{
    Integer fitness;
    Tree tree;
    Data data;

    public Chromosome(){
        fitness = -1;
        tree = null;
        data = null;
    }

    public Chromosome(int size, Data dataInput){
        data = dataInput;
        tree  = new Tree(size);
        fitness = calcFitness(tree.root);
    }

    public Chromosome copy(){
        Chromosome newChromo = new Chromosome();
        newChromo.data = this.data;
        newChromo.fitness = this.fitness;
        newChromo.tree = new Tree(this.tree.root.copy());

        return newChromo;
    }

    public ArrayList<Chromosome> mate(Chromosome partner){
        Random rand = new Random();
        ArrayList<Chromosome> children = new ArrayList<Chromosome>();

        crossOverNode(this, partner);
                
        int probabilityMutate = rand.nextInt(100);
        if(probabilityMutate < 30){
            mutateNode(this);
            mutateNode(partner);
        }

        children.add(this);
        children.add(partner);
        return children;
    }

    public void crossOverNode(Chromosome self, Chromosome partner){
        Integer oriFitnessSelf = self.fitness;
        Integer oriFitnessPartner = partner.fitness;
        Integer newFitnessSelf = 0;
        Integer newFitnessPartner = 0;
        int limit = 0;
        Node newRootSelf = self.tree.root.copy();
        Node newRootPartner = partner.tree.root.copy();
        // System.out.println(oriFitness);
        while((limit < 40 ) && ((newFitnessSelf < oriFitnessSelf) || (newFitnessPartner < oriFitnessPartner))){
            crossOver(newRootSelf, newRootPartner);
            newFitnessSelf = calcFitness(newRootSelf);
            newFitnessPartner = calcFitness(newRootPartner);
            limit++;
        }

        if((newFitnessSelf >= oriFitnessSelf) && (newFitnessPartner >= oriFitnessPartner)){
            self.tree.root = newRootSelf;
            self.fitness = newFitnessSelf;

            partner.tree.root = newRootPartner;
            partner.fitness = newFitnessPartner;
        }else if(newFitnessSelf >= oriFitnessSelf){
            self.tree.root = newRootSelf;
            self.fitness = newFitnessSelf;
        } else if (newFitnessPartner >= oriFitnessPartner){
            partner.tree.root = newRootPartner;
            partner.fitness = newFitnessPartner;
        }
    }
    public void crossOver(Node self, Node partner){
        Random rand = new Random();
        Node prevNodeSelf = null;
        Node currNodeSelf = self;
        Node prevNodePartner = null;
        Node currNodePartner = partner;
        int counter1 = rand.nextInt(4)+1;
        int counter2 = rand.nextInt(4)+1;

        while((!currNodeSelf.isLeaf) && (counter1 > 0)){
            int randChild = rand.nextInt(2);
            prevNodeSelf = currNodeSelf;
            if(randChild == 0){
                currNodeSelf = currNodeSelf.leftChild;
            }else{
                currNodeSelf = currNodeSelf.rightChild;
            }
            counter1--;
        }
        while((!currNodePartner.isLeaf) && (counter2 > 0)){
            int randChild = rand.nextInt(2);
            prevNodePartner = currNodePartner;
            if(randChild == 0){
                currNodePartner = currNodePartner.leftChild;
            }else{
                currNodePartner = currNodePartner.rightChild;
            }
            counter2--;
        }

        if(prevNodeSelf.leftChild.equals(currNodeSelf)){
            prevNodeSelf.leftChild = currNodePartner;
        }else{
            prevNodeSelf.rightChild = currNodePartner;
        }

        if(prevNodePartner.leftChild.equals(currNodePartner)){
            prevNodePartner.leftChild = currNodeSelf;
        }else{
            prevNodePartner.rightChild = currNodeSelf;
        }
    }

    public void mutateNode(Chromosome ind){
        Integer oriFitness = ind.fitness;
        Integer newFitness = 0;
        int limit = 0;
        Node newRoot = ind.tree.root.copy();
        // System.out.println(oriFitness);
        while((limit < 20 ) && (newFitness < oriFitness)){
            mutate(newRoot);
            newFitness = calcFitness(newRoot);
            limit++;
        }
        if(newFitness >= oriFitness){
            ind.tree.root = newRoot;
            ind.fitness = newFitness;
            // System.out.println(ind.fitness);
        }
    }

    public void mutate(Node node) {
        if (node != null) {
            mutate(node.leftChild);
            Random rand = new Random();
            int probabilityMutate = rand.nextInt(100);
            if(probabilityMutate < 20){
                ArrayList<String> functions = new ArrayList<String>(Arrays.asList(new String[]{"SL","SW","PL","PW"}));
                ArrayList<String> terminal = new ArrayList<String>(Arrays.asList(new String[]{"virginica","versicolor","setosa"}));

                if(node.isLeaf){
                    terminal.remove(node.nodeValue);
                    int randIndex = rand.nextInt(terminal.size());
                    node.nodeValue = terminal.get(randIndex);
                }else{
                    functions.remove(node.nodeValue);
                    int randIndex = rand.nextInt(functions.size());
                    node.nodeValue = functions.get(randIndex);
                    node.compareValue = 0.1 + rand.nextDouble() * (7.9 - 0.1);
                }

            }
            mutate(node.rightChild);
        }
    }
    public Integer calcFitness(Node root){
        ArrayList<String> functions = new ArrayList<String>(Arrays.asList(new String[]{"SL","SW","PL","PW"}));
        Integer counter = 0;

        for (int i = 0; i < data.inputData.size(); i++) {
            Node current = root;      
            String set = data.inputData.get(i);
            String[] line = set.split(",");

            while(!current.isLeaf){
                int index = functions.indexOf(current.nodeValue);
                if(Double.parseDouble(line[index]) <= current.compareValue){
                    current = current.leftChild;
                }else{
                    current = current.rightChild;
                }
            }
            if(current.nodeValue.equals(data.resultData.get(i))){
                counter++;
            }
        }
        return counter;
    }

    @Override
    public int compareTo(Chromosome i) {
        return fitness.compareTo(i.fitness);
    }
}
