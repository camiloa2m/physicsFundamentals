import numpy as np
import matplotlib.pyplot as plt

periodo = [4.28849193637064,
0.881047552656396,
4.5025569027927,
2.18040721097885,
7.48319361176675,
3.44158027979643,
2.35251633437425,
13.6985214108124,
18.4911885463561,
8.94816507629757,
]

semieje_mayor=[2.63958953904757,
0.919036795174895,
2.72671328054463,
1.68148013048979,
3.82582106926869,
2.27949478535437,
1.76883951546003,
5.72509189321286,
6.99267297182358,
4.31011963486432,
]

for i in range(len(periodo)):
    periodo[i] = np.log(periodo[i])
    semieje_mayor[i] = np.log(semieje_mayor[i])

fig, ax = plt.subplots()
ax.plot(semieje_mayor, periodo, 'ro', label='Euler-Cromer')

ax.set(xlabel='ln(a)', ylabel='ln(T)',
       title='Kepler\'s Third Law')
ax.grid()

plt.legend()
plt.show()

print("hey")
