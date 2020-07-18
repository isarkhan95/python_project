import os,matplotlib.pyplot as p
import matplotlib.text as txt
import pandas as pd
import datetime as dt


df =  pd.read_excel("D:\\all docs\DSR.xlsx",index_col=None)
ctrot=0
ctcompleted=0
ctdelayed=0
cthold=0
status=df["Status"]
for i in status:
    if i=="Running on track":
        ctrot+=1
    elif i=="Completed":
        ctcompleted+=1
    elif i=="Delayed":
        ctdelayed+=1
    elif i=="On Hold":
        cthold+=1
plot=[ctcompleted,ctrot,ctdelayed,cthold]
colors=['darkgreen','lightgreen','red','purple']
Labels=['Completed','Running on Track','Delayed','Onhold']
p.figure(figsize=(10.5,3))
p.pie(plot,labels=Labels,colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
p.legend(Labels,loc="best")
p.axis('equal')
p.tight_layout()
p.savefig("D:\chart.png")
p.show()



dt=dt.datetime.now()
curdt=dt.date()
fig=p.figure(figsize=(10.5,3))
fig.text(0.07,0.8,"BIDW PRODUCTION LOAD STATUS",fontsize=14,fontweight='heavy',color='navy')
fig.text(0.75,0.8,"DATE: %s"%curdt,fontsize=14,fontweight='heavy',color='navy')
fig.text(0.07,0.7,"Application Status",fontsize=12,fontweight='bold')
fig.text(0.75,0.7,"Health Counts",fontsize=12,fontweight='bold')
fig.text(0.07,0.6,"Completed Applications",fontsize=10)
fig.text(0.75,0.6,ctcompleted,fontsize=10)
fig.text(0.07,0.5,"Applications On Track",fontsize=10)
fig.text(0.75,0.5,ctrot,fontsize=10)
fig.text(0.07,0.4,"Applications Running Behind",fontsize=10)
fig.text(0.75,0.4,ctdelayed,fontsize=10)
fig.text(0.07,0.3,"Applications On Hold",fontsize=10)
fig.text(0.75,0.3,cthold,fontsize=10)
p.savefig("D:/text.png")
p.show()