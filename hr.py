import math
do=str(input("what have to do: "))
if(do == "sum"):
        x=int(input("enter the no:"))
        y=int(input("enter the no:"))
        sum=x+y
        print(sum)
elif(do=="difference"):
        x=int(input("enter the no:"))
        y=int(input("enter the no:"))
        difference=x-y
        print(difference)
elif(do=="division"):
        x=int(input("enter the no:"))
        y=int(input("enter the no:"))
        division=x//y
        print(division)
elif(do=="multiply"):
        x=int(input("enter the no:"))
        y=int(input("enter the no:"))
        multiply=x*y
        print(multiply)
elif(do=="power"):
        x=int(input("enter the no:"))
        y=int(input("enter the no:"))
        power=x**y
        print(power)
elif(do=="SI"):
        x=int(input("enter Principle:"))
        y=int(input("enter rate in %:"))
        z=int(input("enter time in year:"))
        p=x*y*z//100
        print("SI is:",p)
elif(do=="CI"):
        pr=float(input("enter Principle:"))
        r=float(input("enter rate in %:"))
        t=float(input("enter time in year:"))
        sa=r/100
        ty=1+sa
        yu=ty**t
        a=pr*yu
        ci=a-pr
        print(ci)
elif do =="square_root":
       h=float(input("enter any no. : "))
       print(h^1/2)
elif do =="fxn of x":
       y=str(input("enter any fxn_for_inverse_ write_with_prefix_a : " ))
       fa=float(input("enter any no. : "))
       i=getattr(math,y)(fa)
       print("in radian",i)
else:
        print("node")

