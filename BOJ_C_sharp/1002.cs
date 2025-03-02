using System.Text;

namespace BOJ_C_sharp
{
    internal class Program_1002
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            StringBuilder sb = new StringBuilder();
            
            for (int i = 0; i < n; i++)
                {
                    string[] ss = Console.ReadLine().Split(' ', StringSplitOptions.RemoveEmptyEntries);
                    int x1 = int.Parse(ss[0]);
                    int y1 = int.Parse(ss[1]);
                    int r1 = int.Parse(ss[2]);
                    int x2 = int.Parse(ss[3]);
                    int y2 = int.Parse(ss[4]);
                    int r2 = int.Parse(ss[5]);

                    int dx = x1 - x2;
                    int dy = y1 - y2;
                    int L2 = dx * dx + dy * dy;
                    int rR = (r1 + r2) * (r1 + r2);
                    int rr = (r1 - r2) * (r1 - r2);

                    int result;
                    if (L2 == 0 && r1 == r2)
                        result = -1;
                    else if (rR > L2 && L2 > rr)
                        result = 2;
                    else if (rR == L2 || rr == L2)
                        result = 1;
                    else
                        result = 0;

                    sb.AppendLine(result.ToString());
                }

             Console.Write(sb.ToString());
        }
    }
}