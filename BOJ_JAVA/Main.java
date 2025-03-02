import java.io.*;
public class Main{
    public static void main(String args[]) throws IOException {
        BufferedReader BufferRead = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter BufferWrite = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            String A = (BufferRead.readLine());
            String B = (BufferRead.readLine());


        } catch (IOException e) {
            e.printStackTrace();
        }
        finally {
            BufferWrite.flush();
            BufferWrite.close();
            BufferRead.close();
        }

    }
}