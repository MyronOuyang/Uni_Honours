import java.io.*;
import java.util.*;

class Data {
    public ArrayList<String> initialInput = new ArrayList<>();
    public List<List<Long>> computedData = new ArrayList<List<Long>>();

    public void inputData(String fileName) throws Exception {
        File file = new File(".\\Data\\"+fileName);
        BufferedReader br = new BufferedReader(new FileReader(file));
        String st;
        while ((st = br.readLine()) != null){
            String[] line = st.split(" ");
            String input = line[1]+","+line[2];
            initialInput.add(input);
        }
        for (int i = 0; i < initialInput.size(); i++) {
            computedData.add(new ArrayList<Long>());
        }
        for (int i = 0; i < initialInput.size(); i++) {
            String[] currentNode = (initialInput.get(i)).split(",");
            for (int j = 0; j < initialInput.size(); j++) {
                String[] compareNode = (initialInput.get(j)).split(",");
                Long distance = calcDistanceEuclidean(currentNode, compareNode);
                computedData.get(i).add(distance);
            }
        }
        br.close();
        System.out.print("-- Data Stored\n");
    }

    private Long calcDistanceEuclidean(String[] currentNode, String[] compareNode){
        float xd = Float.parseFloat(currentNode[0]) - Float.parseFloat(compareNode[0]); 
        float yd = Float.parseFloat(currentNode[1]) - Float.parseFloat(compareNode[1]);
        xd *= xd;
        yd *= yd;
        Long d =  Math.round(Math.sqrt(xd + yd));
        return d;
    }
}
