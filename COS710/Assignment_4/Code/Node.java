import java.util.*;

class Node {
    Boolean isLeaf;
    String nodeValue;
    double compareValue;
    Node leftChild;
    Node rightChild;

    Node(Boolean isLeafInput, String nodeValueInput, double compareValueInput, Node leftChildInput,
            Node rightChildInput) {
        isLeaf = isLeafInput;
        nodeValue = nodeValueInput;
        compareValue = compareValueInput;
        leftChild = leftChildInput;
        rightChild = rightChildInput;
    }

    public Node copy() {
        Node left = null;
        Node right = null;
        if (this.leftChild != null) {
            left = this.leftChild.copy();
        }
        if (this.rightChild != null) {
            right = this.rightChild.copy();
        }
        return new Node(isLeaf, nodeValue, compareValue, left, right);
    }

    public static Node generateRandomNode(Boolean isTerminal){
        String[] functions = new String[]{"SL","SW","PL","PW"};
        String[] terminal = new String[]{"virginica","versicolor","setosa"};

        Random random = new Random();
        // random.setSeed(20);
        int randIndex = random.nextInt(functions.length);
        String func = functions[randIndex];
        Boolean leaf = false;
        Double[] minMax = getMinMax(func);
        double randComp = minMax[0] + random.nextDouble() * (minMax[1] - minMax[0]);
        

        if(isTerminal){
            randIndex = random.nextInt(terminal.length);
            func = terminal[randIndex];
            leaf = true;
            randComp = 0;
        }

        return new Node(leaf, func, randComp, null, null);
    }

    private static Double[] getMinMax(String function){
        if(function.equals("SL")){
            return new Double[]{4.3, 7.9};
        }else if(function.equals("SW")){
            return new Double[]{2.0, 4.4};
        }else if(function.equals("PL")){
            return new Double[]{1.0, 6.9};
        }else{
            return new Double[]{0.1, 2.5};
        }
    }
}