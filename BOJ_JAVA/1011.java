import java.io.*;
// public class Main 을 제출시 사용 해야 함
class P_1011{
	public static void main(String args[]){
		BufferedReader BufferRead = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter BufferWrite = new BufferedWriter(new OutputStreamWriter(System.out));
		try {
			int T =Integer.parseInt(BufferRead.readLine());
			int x,y,d,ans,num,num2;
			x = y = d = ans = num = num2 = 0;
			for (int i=0; i<T; i++) {
				String[] temp = BufferRead.readLine().split(" ");
				x = Integer.valueOf(temp[0]);
				y = Integer.valueOf(temp[1]);
				d=y-x;
				num2=(int) Math.sqrt(d);
				num=num2*num2;
				if(num == d) ans = num2*2 -1;
				else if(num < d - num2) ans = num2*2+1;
				else ans=num2*2;
				/*while (d>nowPosition) {
					times++;
					nowPosition+=times/2+times%2 ;
				}파이썬에선 이 로직으로 1136ms 통과했는데에*/
				BufferWrite.write(String.valueOf(ans) + "\n");}
			BufferWrite.flush();
			BufferWrite.close();
			BufferRead.close();
		} catch (NumberFormatException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}
}
 
