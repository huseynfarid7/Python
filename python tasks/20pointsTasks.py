#sual 5-3 eded daxil edin 2 sinin cemini 3 cu ye vur
a=int(input("1 ci ededi daxil edin: "))
b=int(input("2 ci ededi daxil edin: "))
c=int(input("3 cu ededi daxil edin: "))
cavab=(a+b)*c
print("netice",cavab)

# sual 10-ededin tek ve ya cut oldugunu cixaran kod
a=int(input("eded daxil edin: "))
if a%2==0:
    print("daxil etdiyiniz eded cutdur")
else:
    print("daxil etdiyiniz eded tekdir")

# sual 15-def den istifade ederek en boyuk ededi tap
def muqayise(x,y):
    if x>y:
        return x
    return y
def enboyuk(x,y,z):
    return muqayise(x,muqayise(y,z))
print(enboyuk(14,15,16))

# sual 20-def den istifade ederek icinde en kicik ededi tap
def muqayise(x,y):
    if x<y:
        return x
    return y
def enkicik(x,y,z):
    return muqayise(x,muqayise(y,z))
print(enkicik(14,15,16))

# sual 25-ic ice for ile sade ve murekkeb ededi cixart
for i in range(2,14):
    for j in range(2,i):
        if i%j==0:
            print(i,"murekkeb")
            break
    else:
        print(i,"sade eded")

# sual 30- 5,6 reqemli bir sozle ededin reqemlerinin sayini ekrana cixaran kod
eded=int(input("eded daxil edin: "))
muvef=eded
say=0
for i in str(muvef):
    muvef=muvef//10
say=say+1
print(say)

# sual 30 basqa usul
num=int(input("ədəd daxil edin:" ))
print(len(str(num)))

# sual 30 basqa usul esas
eded=int(input("ededi daxil edin: "))
say=0
while eded>0:
    say=say+1
    eded=eded//10
print("netice",say)

# sual 35 - 1 heftede olan saniyeni hesabla
gunler=int(input("gunleri daxil edin: "))
saat=gunler*24
deqiqe=saat*60
saniye=deqiqe*60
print(saniye)

# sual 40- 654321 54321 4321 321 21 1
setir=6
for i in range(0,setir+1):
    for j in range(setir-i,0,-1):
        print(j,end="")
    print()

# sual 45- daxil edilen istenilen X reqemli ededin reqemlerinin cemini ekrana cixaran kodu tertib edin
eded=12345
qaliq=0
while eded:
    qaliq=eded%10 + qaliq
    eded=eded//10
print(qaliq)

# sual 46- bir eded verilecek misal 12345 ve onun birinci reqemini tapan kodu yaz
def birinci(eded):
    if eded<10:
        return eded
    return birinci(eded//10)
print(birinci(12345))

# sual 47- 666666 55555 4444 333 22 1(tersine loop suali)
setir=6
for i in range(setir,0,-1):
    eded=i
    for j in range(0,i):
        print(eded,end=" ")
    print()

# sual 55-eded araligi verib(meselen 5,25)bu ardicilligda 7 ci den baslayaraq quvvete yukselt(defden istifade et)
def abc():
    siyahi=list()
    for i in range(5,25):
        siyahi.append(i**2)
    print(siyahi[7:])
abc()

#sual 58 setir tipinden ibaret siyahi yaradin.Bu siyahida elementlerin sayini ortaya cixaran kod tertib edin
setir=["python","java","c++"]
say=0
for i in setir:
    say=say+1
print(say)

# sual 65 bir cumle verilib ve hemin setir tipinin butun sozlerini boyukle yazmaliyiq
setir="imtahanlar bitsin"
print(setir.upper())

# sual 70 bir soz verilib bu sozu tersine cixarmaliyiq amma def ile
def tersine(verilmis_setir):
    bosh_str=""
    for i in verilmis_setir:
        bosh_str=i+bosh_str
    return bosh_str
verilmis_setir="champion"
print("cavab: ",tersine(verilmis_setir))