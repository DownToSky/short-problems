from utils import fib

def get_position(l):
    """
        returns 0 if in p postion
        returns 1 if in n postion
    """
    if l is [0]*len(l):
        return 0
    for index in range(0,len(l)):
        for to_subtract in range(1,l[index]+1):
            new_l = l[:]
            new_l[index]-= to_subtract
            if get_position(new_l)==0:
                return 1
    return 0


if __name__ == "__main__":
    #print(fib.Fib(32))
    for e in range(1,31):
        counter = 0
        for i in range(1,(2**e)+1):
            if i^(2*i)^(3*i) == 0:
                counter+=1
        print("exponent:{} number of P positions: {}".format(e , counter))
