import java.io.*;
import java.util.*;

public class Data {
    public ArrayList<String> inputData = new ArrayList<>();
    public ArrayList<String> resultData = new ArrayList<>();

    public void inputData(String fileName) throws Exception {
        File file = new File("data\\"+fileName);
        BufferedReader br = new BufferedReader(new FileReader(file));
        String st;
        while ((st = br.readLine()) != null){
            String[] line = st.split(",Iris-");
            inputData.add(line[0]);
            resultData.add(line[1]);
        }
        br.close();
        System.out.print("-- Data Stored\n");
    }
}
