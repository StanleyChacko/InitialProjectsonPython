print ("hello")

Para_add=[1.423, 0.34]
#Para_add1=['hello', 'SrinivasSir']
Para_add1=['hello', 4]

print Para_add

twom=[1,6]
print twom
print ("now we will find roots of a quadratic equation of form ax2+bx+c=0")
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
quadcoeff=[a,b,c]
print quadcoeff

def fun(Para_add):
    c1=Para_add[0]
    print c1
    c2=Para_add[1]
    print c2
    c3= c1+c2
    print c3

    return c3

def funm(twom):
    c4=twom[0]
    print c4
    c5=twom[1]
    print c5
    c6= c4*c5
    print c6

    return c6

c_add= fun(Para_add)
print c_add


c_multiply=funm(Para_add1)
print c_multiply
