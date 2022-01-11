from matplotlib import pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
sns.set()
import numpy
data = numpy.load('pie_data.npy')
labels = '野球部', 'パイソン講座', '合唱部', '卓球部'
unique, counts = numpy.unique(data, return_counts=True)
sizes = counts
explode = (0, 0.4, 0, 0)  # only "explode" the 2nd slice

fig1, ax1 = plt.subplots()
patches, texts, autotexts = ax1.pie(
        sizes,
        explode=explode,
        labels=labels,
        autopct='%1.1f%%',
        shadow=True,
        startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
props = fm.FontProperties()
props.set_name('Hiragino Sans')
props.set_size('large')
plt.setp(texts, fontproperties=props)
plt.show()
