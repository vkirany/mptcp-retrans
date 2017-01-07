import numpy as np
import matplotlib.pyplot as plt

#data = np.loadtxt(sys.argv[1])

n_groups = 5 

p1e3=(433,482,463,443,592)
p2e3=(301,352,355,362,676)
p1pe3=(646,742,668,698,957)


np1e3=(423,390,453,389,581)
np2e3=(303,407,407,403,674)
np1pe3=(423,483,452,443,581)

tp1e3=(491,490,541,491,1003)
tp2e3=(462,460,533,462,1187)
tp1pe3=(748,748,807,747,1375)



fig, ax = plt.subplots()

index = np.arange(n_groups)

margin = 0.05
bar_width = (1-2*margin)/3


rects1 = plt.bar(index+margin, p1pe3 , bar_width,
                 color='b',
                 label='mptcp')

rects2 = plt.bar(index+margin + bar_width, np1pe3 , bar_width,
                 color='g',
                 label='mptcp-New')

rects3 = plt.bar(index+margin + 2*bar_width, tp1pe3, bar_width,
                 color='r',
                 label='tcp')



plt.xlabel('Scenarios')
plt.ylabel('Burst Completion Time (ms)')
#plt.title('AvgDelay with Std. Dev ')
plt.xticks(index+0.5,('20-20', '20-30', '30-20', '20-120', '120-20'))
#plt.legend()
plt.tight_layout()
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=5)
#plt.ylim(0,650)
plt.savefig('Delay.pdf')

#plt.show()
