import java.util.*;

public class Tree {
    Node root = null;

    public Tree(Node copyRoot){
        root = copyRoot;
    }

    public Tree(int level) {
        while (!testValidity()) {
            ArrayList<Node> parentArr = new ArrayList<Node>();
            root = Node.generateRandomNode(false);
            parentArr.add(root);
            for (int i = 1; i < level; i++) {
                if (i == level - 1) {
                    parentArr = recInit(parentArr, true);
                } else {
                    parentArr = recInit(parentArr, false);
                }
            }
        }
    }

    private ArrayList<Node> recInit(ArrayList<Node> currParents, Boolean isLastLevel) {
        ArrayList<Node> newParentsArr = new ArrayList<Node>();
        Node child1 = null;
        Node child2 = null;

        for (Node parent : currParents) {
            if (isLastLevel) {
                child1 = Node.generateRandomNode(true);
                child2 = Node.generateRandomNode(true);
            } else {
                child1 = Node.generateRandomNode(false);
                child2 = Node.generateRandomNode(false);
            }
            parent.leftChild = child1;
            parent.rightChild = child2;

            newParentsArr.add(child1);
            newParentsArr.add(child2);
        }

        return newParentsArr;
    }

    public Boolean testValidity() {
        Set<String> allValues = new HashSet<String>();

        if (root == null) {
            return false;
        }

        Queue<Node> nodes = new LinkedList<>();
        nodes.add(root);

        while (!nodes.isEmpty() && allValues.size() < 7) {

            Node node = nodes.remove();
            allValues.add(node.nodeValue);

            if (node.leftChild != null) {
                nodes.add(node.leftChild);
            }

            if (node.rightChild != null) {
                nodes.add(node.rightChild);
            }
        }

        if (allValues.size() == 7) {
            return true;
        }
        return false;
    }

    public void output() {
        if (root == null) {
            return;
        }

        Queue<Node> nodes = new LinkedList<>();
        nodes.add(root);

        while (!nodes.isEmpty()) {

            Node node = nodes.remove();

            System.out.print(" " + node.nodeValue);
            
            if (node.leftChild != null) {
                nodes.add(node.leftChild);
            }
            
            if (node.rightChild != null) {
                nodes.add(node.rightChild);
            }
        }
        System.out.println(" ");
    }
}
