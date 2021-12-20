x = range(1,13)
x2 = range(1,16)

y1 = [0.70681,0.66543,0.62276,0.60450,0.59170,0.57705,0.56719,0.56075,0.55331, 0.54485,0.53763,0.53216]
y2 = [0.79778,0.72851,0.68667, 0.63355,
        0.60126,0.58862,0.57764,0.56284,0.54910,0.54041, 0.53564, 0.53097,0.52433,0.51664, 0.50988 ]

import matplotlib.pyplot as plt

# plt.plot(x,y1,label ='p1 loss')
# plt.plot(x2,y2,label='p2 loss')

# plt.legend()



# plt.show()



test_percent = list(range(1,10) ) 

test_percent = [i/10 for i in test_percent]

p1_acc = [0.69,0.68 , 0.7166, 0.70,0.636,0.680,0.664,0.651,0.647]


p2_acc = [0.784,0.779,0.686,0.696,0.708,0.6675, 0.666, 0.6649,0.606]

bert_p1_acc = [0.8,0.78, 0.815,0.82,0.81,0.817,0.82,0.85,0.87]
bert_p2_acc = [0.69,0.76,0.775,0.825,0.8,0.835,0.84,0.79,0.86]



plt.plot(test_percent,p2_acc ,label='GNN p2')
plt.plot(test_percent,bert_p2_acc,label='BERT p2')

plt.legend()



plt.show()


print(test_percent)