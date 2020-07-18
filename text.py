import matplotlib.pyplot as p
import datetime as dt


dt=dt.datetime.now()
curdt=dt.date()
fig=p.figure(figsize=(10.5,3))


fig.text(0.07,0.8,"BIDW PRODUCTION LOAD STATUS",fontsize=14,fontweight='heavy',color='navy')
fig.text(0.75,0.8,"DATE: %s"%curdt,fontsize=14,fontweight='heavy',color='navy')
fig.text(0.07,0.7,"Application Status",fontsize=12,fontweight='bold')
fig.text(0.75,0.7,"Health Counts",fontsize=12,fontweight='bold')
fig.text(0.07,0.6,"Completed Applications",fontsize=10)
fig.text(0.75,0.6,"13",fontsize=10)
fig.text(0.07,0.5,"Applications On Track",fontsize=10)
fig.text(0.75,0.5,"9",fontsize=10)
fig.text(0.07,0.4,"Applications Running Behind",fontsize=10)
fig.text(0.75,0.4,"2",fontsize=10)
fig.text(0.07,0.3,"Applications On Hold",fontsize=10)
fig.text(0.75,0.3,"1",fontsize=10)
p.savefig("D:/text.png")
p.show()