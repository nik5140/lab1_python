import math as m
def func_print(payload):
    a = [1,2,3,4]
    for item in a:
        print(payload, end=" ")

#Next function is for calculating one itteration for first goal:
def func_y(k):
    return 1/((2*k)**2)

#Next function is for calculating one itteration for second goal:
def func_y2(k,x):
    return ((k/(k+1))-(m.cos(m.fabs(x)))**k)

def main():
    print ("This program is for 1.4.4 г (Y) and 1.4.5 ж (Y2)")
    n = func_int()
    Y = 0
    Y2 = 1
    print("You entered ",str(n))
    for k in range(1,n+1):
        Y += func_y(k)
        #print(Y) debugging thing
    print(f"Our resulting Y (first goal) is {Y}")

    x = func_float()
    for k in range(1,n+1):
        Y2 *= func_y2(k,x)
        #print(Y) debugging thing
    print(f"Our resulting Y2 (first goal) is {Y2}")

def hello():
    pass


def func_int():
    while True:
        a = input ("Enter integer (n) ")

        try:
            b = int(a)
            return b
            break
        except ValueError:
            print("!!!!")
            continue

def func_float():
    while True:
        a = input ("Enter float (for second goal) (x)")

        try:
            b = float(a)
            return b
            break
        except ValueError:
            print("!!!!")
            continue

if __name__ == "__main__":
    main()