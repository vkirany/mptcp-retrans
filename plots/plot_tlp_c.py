import numpy as np
import matplotlib.pyplot as plt

#data = np.loadtxt(sys.argv[1])

n_groups = 5 

p1e0=(422,484,453,445,582)
p1e2=(423,484,453,444,582)
p1e3=(432,482,463,443,592)
p1e4=(433,483,464,443,592)

p2e0=(378,438,409,493,581)
p2e2=(378,437,407,494,582)
p2e3=(301,352,355,362,676)
p2e4=(481,542,532,552,887)

p1pe0=(423,483,454,534,583)
p1pe2=(423,483,453,536,582)
p1pe3=(646,742,668,698,957)
p1pe4=(647,741,667,700,956)


tp1e0=(490,489,540,491,1002)
tp2e0=(586,585,645,585,1279)
tp1pe0=(1004,1004,1073,1004,1746)

tp1e2=(491,490,541,490,1003)
tp2e2=(585,586,646,586,1279)
tp1pe2=(1004,1004,1073,1003,1743)

tp1e3=(491,490,541,491,1003)
tp2e3=(462,460,533,462,1187)
tp1pe3=(748,748,807,747,1375)

tp1e4=(490,490,540,491,1004)
tp2e4=(657,657,728,658,1371)
tp1pe4=(748,747,808,748,1376)


fig, ax = plt.subplots()

index = np.arange(n_groups)

margin = 0.05
bar_width = (1-2*margin)/3


rects1 = plt.bar(index+margin, tp2e0 , bar_width,
                 color='b',
                 label='er=0')

rects2 = plt.bar(index+margin + bar_width, tp2e2 , bar_width,
                 color='g',
                 label='er=2')

rects3 = plt.bar(index+margin + 2*bar_width, tp2e3, bar_width,
                 color='r',
                 label='er=3')

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
plt.ylim(0,1350)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=4)
plt.savefig('Delay.pdf')

#plt.show()
