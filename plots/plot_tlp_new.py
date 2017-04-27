import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc('axes',labelsize=18)
matplotlib.rc('xtick',labelsize=14)
matplotlib.rc('ytick', labelsize=14)

n_groups = 5 

p1e3=(386,432,463,394,928)
p2e3=(277,280,356,288,1148)
p1pe3=(627,680,667,639,1442)


np1e3=(385,432,451,394,827)
np2e3=(231,243,272,288,752)
np1pe3=(385,443,451,499,827)

tp1e3=(474,474,540,474,1612)
tp2e3=(326,326,533,326,1645)
tp1pe3=(722,722,808,722,2103)



fig, ax = plt.subplots()

index = np.arange(n_groups)

margin = 0.05
bar_width = (1-2*margin)/3


rects1 = plt.bar(index+margin, p1pe3 , bar_width,
                 color='navy',
                 label='mptcp')

rects2 = plt.bar(index+margin + bar_width, np1pe3 , bar_width,
                 color='indigo',
                 label='mptcp-New')

rects3 = plt.bar(index+margin + 2*bar_width, tp1pe3, bar_width,
                 color='seagreen',
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
