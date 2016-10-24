import numpy as np
import matplotlib.pyplot as plt

#data = np.loadtxt(sys.argv[1])

n_groups = 5 

p1e0=(422,484,453,445,582)
p1e3=(432,482,463,443,592)
p1e4=(433,483,464,443,592)

p2e0=(378,438,409,493,581)
p2e3=(301,352,355,362,676)
p2e4=(481,542,532,552,887)

p1pe0=(423,483,454,534,583)
p1pe3=(646,742,668,698,957)
p1pe4=(647,741,667,700,956)

fig, ax = plt.subplots()

index = np.arange(n_groups)

margin = 0.05
bar_width = (1-2*margin)/3


rects1 = plt.bar(index+margin, p1pe0 , bar_width,
                 color='b',
                 label='er=0')

rects2 = plt.bar(index+margin + bar_width, p1pe3, bar_width,
                 color='r',
                 label='er=3')

rects3 = plt.bar(index+margin + 2*bar_width, p1pe4, bar_width,
                 color='g',
                 label='er=4')


plt.xlabel('Scenarios')
plt.ylabel('AvgDelay (ms)')
#plt.title('AvgDelay with Std. Dev ')
plt.xticks(index+0.5,('20-20', '20-30', '30-20', '20-120', '120-20'))
#plt.legend()
plt.tight_layout()
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=5)
plt.savefig('Delay.pdf')

#plt.show()
