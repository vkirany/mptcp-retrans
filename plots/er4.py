import numpy as np
import matplotlib.pyplot as plt

#data = np.loadtxt(sys.argv[1])

n_groups = 5 

s2020 = (183,481)

s2030 = (185,542)

s3020 = (214,532)

s20120 = (185,552)

s12020 = (236,887)


fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.18

opacity = 0.4

rects1 = plt.bar(index, s2020 , bar_width,
                 alpha=opacity,
                 color='b',
                 label='20-20')

rects2 = plt.bar(index + bar_width, s2030, bar_width,
                 alpha=opacity,
                 color='r',
                 label='20-30')

rects3 = plt.bar(index + 2*bar_width, s3020, bar_width,
                 alpha=opacity,
                 color='g',
                 label='30-20')

rects4 = plt.bar(index + 3*bar_width, s20120, bar_width,
                 alpha=opacity,
                 color='m',
                 label='20-120')

rects5 = plt.bar(index + 4*bar_width, s12020, bar_width,
		alpha=opacity,
		color='c',
		label='120-20')


plt.xlabel('Scenarios')
plt.ylabel('AvgDelay (ms)')
#plt.title('AvgDelay with Std. Dev ')
plt.xticks(0.185 + index + bar_width, ('20-20', '20-30', '30-20', '20-120', '120-20'))
#plt.legend()
plt.tight_layout()
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=4)
plt.savefig('avgDelay.pdf')

#plt.show()
