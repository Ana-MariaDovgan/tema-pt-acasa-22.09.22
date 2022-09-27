x=int(input("Dati primul nr: "))
y=int(input("Dati al doilea nr: "))
z=int(input("Dati al treilea nr: "))
import math
def nrmax(a,b,c):
    d=[a,b,c]
    max=0
    for numar in d:
        if numar>max:
            max = numar
    return max
print("Cel mai mare numar este:",nrmax(x,y,z))

def nrmin(a,b,c):
    d=[a,b,c]
    min=a
    for numar in d:
        if numar<min:
            min = numar
    return min
print("Cel mai mic numar este:",nrmin(x,y,z))

def cel_mai_mare_div(a,b,c):
    cel_mai_mare_div=0
    i=nrmin(a,b,c)
    while(i>1):
        if(a%i==0 and b%i==0 and c%i==0):
            cel_mai_mare_div = i
            break
        i-=1
    if(i<=1):
        cel_mai_mare_div = "Cel mai mare divizor comun este: 1"
        return print(cel_mai_mare_div)
    return print("Cel mai mare divizor comun al numerelor este: ",cel_mai_mare_div)
(cel_mai_mare_div(x,y,z))

def cel_mai_mic_multiplu(a,b,c):
    i=nrmax(a,b,c)
    while True:
        if(i%a==0) and (i%b==0) and (i%c==0):
            cel_mai_mic_multiplu= i
            break
        i+=1
    return print("Cel mai mic multiplu comun al numerelor este: ",cel_mai_mic_multiplu)
(cel_mai_mic_multiplu(x,y,z))

def m_c_c_m_primii_3(a,b,c):
    c_m_m_m=[]
    if a>b:
        multiplu=a
    elif b>a:
        multiplu=b
    else:
        multiplu=a
    while len(c_m_m_m)<3:
        if ((multiplu%a==0)and(multiplu%b==0)):
            c_m_m_m.append(multiplu)
            multiplu +=1
        else:
            multiplu +=1
    return print("Primii 3 multipli comuni al numerelor  sunt: ",c_m_m_m)
(m_c_c_m_primii_3(x,y,z))

def lat_triunghi(a,b,c):
    #import math#
    if (a+b>c) and (a+c>b) and (b+c>a):
        sp=(a+b+c)/2
        aria=round(math.sqrt(sp*(sp-a)*(sp-b)*(sp-c)),2)
        perimetru=sp*2
        return print("Laturile pot forma un triunghi, astfel aria acestuia va fi: ",aria,", iar perimetrul: ",perimetru)
    else:
        return print("Laturile nu pot forma un triunghi!")
(lat_triunghi(x,y,z))

def ech_grad_2(a,b,c):
    #import math
    delta=((b**2)-(4*(a*c)))
    if delta>0:
        rad_delta=math.sqrt(int(delta))
        x1=round((-b-rad_delta)/(2*a),2)
        x2=round((-b+rad_delta)/(2*a),2)
        return print("Solutiile ecuatiei sunt: ",x1,"si",x2)
    elif delta==0:
        rad_delta=math.sqrt(int(delta))
        x1=x2=round((-b)/(4*a),2)
        return print("Solutiile sunt egale si valoarea lor este: ",x1)
    elif delta<0:
        return print("Ecuatia nu are solutii reale.")
(ech_grad_2(x,y,z))