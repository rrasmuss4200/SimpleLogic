import matplotlib.pyplot as plt
import numpy as np

def my_lines(ax, pos, *args, **kwargs):
    if ax == 'x':
        for p in pos:
            plt.axvline(p, *args, **kwargs)
    else:
        for p in pos:
            plt.axhline(p, *args, **kwargs)

#pass in the results of the truth table into this list of ints
#This will be values of the key-value pairs from the dictionary truth_table
bits = [0,1,0,1,0,0,1,1,1,0,0,1,0]
data = np.repeat(bits, 2)
clock = 1 - np.arange(len(data)) % 2
manchester = 1 - np.logical_xor(clock, data)
t = 0.5 * np.arange(len(data))


my_lines('x', range(13), color='.5', linewidth=2)
my_lines('y', [0.5, 2, 4], color='.5', linewidth=2)
#makes timing diagram
plt.step(t, data + 2, 'r', linewidth = 2, where='post')

plt.ylim([-1,6])

for tbit, bit in enumerate(bits):
    plt.text(tbit + 0.5, 1.5, str(bit))

plt.gca().axis('off')
plt.show()
plt.savefig("Example.png")