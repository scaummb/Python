import pylab 

#make a square figure and axes
figure(1,figsize=(6,6))
ax = axes([0.1,0.1,0.8,0.8])

lables = 'flogs','hogs','Dogs','Logs'
fracs = [15,30,45,10]

explode = (0,0.05,0,0)
pie(fracs,explode=explode,lables=lables,autopct='%1.1f%%',shadow=True)
title('Raining Hogs and Dogs',bbox={'facecolor':'0.8','pad':5})
savefig('D:\\pie.png')
show()
