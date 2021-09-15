#quadratic formula = ax2+bx+c=0, quadratic equation = -b+-sqrt(b2-4ac)/2a
import cmath
a = 4
b = 2
c = 8
dis = (b**2)- (4*a*c)
ans1 = (-b-cmath.sqrt(dis))/(2*a)
ans2 = (-b+cmath.sqrt(dis))/(2*a)
print(f'the roots are: {ans1} and {ans2}')