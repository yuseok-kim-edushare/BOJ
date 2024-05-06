import sys
import math
input = sys.stdin.readline
pi = math.pi

p = int(input())
for i in range(p):
    t, n, m = map(int, input().split())
    tan0 = math.tan(pi/n)
    sin0 = math.sin(pi/n)
    r_n = (1/(1-sin0)-1)
    m_term = (tan0**2*(1/(tan0*sin0)+1+math.sqrt((1/(tan0*sin0)+1)**2-(1/tan0)**2*(1/sin0**2-1))))**(m-1)
    r_nm = r_n*m_term
    net_l = round(2*r_nm*(pi+n), 3)
    print(t, round(r_nm, 3), f"{net_l:.3f}")
