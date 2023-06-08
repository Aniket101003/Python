
print("progrm to find most common occuring word in sample of \
10 phishing emails")
print()
phishingemail=["wintherace@supercars.com",\
               "winthelottery@lottery.com",\
               "greatindianfestival@amazon.com",\
               "bigbilliondays@flipkart.com",\
               "grabasupercar@supercars.com",\
               "thewinterrace@supercars.com",\
               "diwalisale@amazon.com",\
               "thebmw@bikers.com",\
               "himalayanrace@bikers.com",\
               "win10lakhs@makemoney.com"]
myd={}
for i in phishingemail:
    x=i.split('@')
    for j in x:
        if j not in myd:
            myd[j]=1
        else:
            myd[j]+=1
key_max=max(myd,key=myd.get)
print("most common occuring word is", key_max)
