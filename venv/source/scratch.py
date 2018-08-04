from MyRSA import RSA
from MyRSA import Certficate
from sort import *
import time
import random
'''
RSA 测试代码
r1=RSA.RsaKey()
r2=RSA.RsaKey()
attrlist={}

rootcert=Certficate.Certficate()
rootcert.loadcert("rootca.cer","rootca.key")

attrlist["cn"]="rootCA"
attrlist["notAfter"]=b"20280630235959+0800"
attrlist["notBefore"]=b"20180613010101+0800"
attrlist["serial_num"]=1
rootcert.createcert(attrlist)
rootcert.signcert(rootcert)
rootcert.dumpcert("rootca.key","rootca.cer")
'''
'''

attrlist["cn"]="yanxing"
attrlist["serial_num"]=2
attrlist["notAfter"] = b"20190630235959+0800"
attrlist["notBefore"] = b"20180613010101+0800"
cert2=Certficate.Certficate()
cert2.createcert(attrlist)
rootcert.signcert(cert2)
keyfile=attrlist["cn"]+".key"
certfile=attrlist["cn"]+".cer"
cert2.dumpcert(keyfile,certfile)
'''
'''SORT 测试代码'''
#random.seed(100)
x=[]
for i in range(1,1000):
    x.append(random.randint(1,100000))
starttime=time.time()
shellsort(x)
endtime=time.time()
print("shellsort:",endtime-starttime)
print(x)
'''
x=[]
for i in range(1,2000):
    x.append(random.randint(1,2000))
starttime=time.time()
selectsort(x)
endtime=time.time()
print("selectsort:",endtime-starttime)

x=[]
for i in range(1,2000):
    x.append(random.randint(1,2000))
starttime=time.time()
insertsort(x)
endtime=time.time()
print("insertsort:",endtime-starttime)
'''




