import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#data = np.loadtxt(sys.argv[1])

matplotlib.rc('axes',labelsize=18)
matplotlib.rc('xtick',labelsize=14)
matplotlib.rc('ytick', labelsize=14)


#data = np.loadtxt(sys.argv[1])

n_groups = 5 

p1e3=(386,432,464,394,927)
p2e3=(277,280,355,289,1148)
p1pe3=(627,680,667,639,1442)


p1e0=(385,432,453,394,878)
p2e0=(385,397,407,435,877)
p1pe0=(384,443,453,495,878)


tp1e0=(474,474,540,474,1613)
tp2e0=(469,469,645,469,1631,)
tp1pe0=(973,973,1070,973,2594)


tp1e3=(474,474,540,474,1612)
tp2e3=(326,326,533,326,1645)
tp1pe3=(722,722,808,722,2103)


fig, ax = plt.subplots()

index = np.arange(n_groups)

margin = 0.05
bar_width = (1-2*margin)/3


rects1 = plt.bar(index+margin, p1pe0 , bar_width,
                 color='b',
                 label='RTO')

rects2 = plt.bar(index+margin + bar_width, p1pe3 , bar_width,
                 color='g',
                 label='TLP')

#rects3 = plt.bar(index+margin + 2*bar_width, tp2e3, bar_width,
#                 color='r',
#                 label='er=3')

#rects4 = plt.bar(index+margin + 3*bar_width, p1pe4, bar_width,
#                 color='g',
#                 label='er=4')

#rects5 = plt.bar(index+margin + 4*bar_width, tp1pe0, bar_width,
#                 color='c',
#                 label='ter=0')
#rects6 = plt.bar(index+margin + 5*bar_width, tp1pe2, bar_width,
#                 color='y',
#                 label='ter=2')
#rects7 = plt.bar(index+margin + 6*bar_width, tp1pe3, bar_width,
#                 color='k',
#                 label='ter=3')
#rects8 = plt.bar(index+margin + 7*bar_width, tp1pe4, bar_width,
#                 color='#B47CC7',
#                 label='ter=4')


plt.xlabel('Scenarios')
plt.ylabel('Burst Completion Time (ms)')
#plt.title('AvgDelay with Std. Dev ')
plt.xticks(index+0.5,('20-20', '20-30', '30-20', '20-120', '120-20'))
#plt.legend()
plt.tight_layout()
plt.ylim(0,1500)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3)
plt.savefig('Delay.pdf')

#plt.show()
