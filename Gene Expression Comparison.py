import pandas as pd
data=pd.read_csv("/Users/IBR/Downloads/Brain_GSE50161.csv")

types=data.type.value_counts().to_frame()
print(types)

import matplotlib.pyplot as plt
import seaborn as sns
colors = ['#6495ED','#96DED1','#E37383','#40B5AD','#FF69B4']
sns.set_style("whitegrid")
plt.rcParams['figure.figsize']=(12,8)
plt.pie(x="type",data=types,labels=types.index,autopct='%1.1f%%',colors=colors)
plt.title("Types of Brain Cancers",fontsize=20)

genes=data.drop(["samples","type"],axis=1)
print("Total Number of Genes in the Data",len(genes.columns))

fig, axes = plt.subplots(1,3,figsize=(20,5))

sns.lineplot(x=data.samples,y="1438_at",data=data,color="#5f0f40",ax=axes[0])
axes[0].set_title("Expression of Gene1 in different Samples")
axes[0].set_xlabel("Sample Number")

sns.lineplot(x=data.samples,y="1552256_a_at",data=data,color="#0f4c5c",ax=axes[1])
axes[1].set_title("Expression of Gene2 in different Samples")
axes[1].set_xlabel("Sample Number")

sns.lineplot(x=data.samples,y="1552261_at",data=data,color="#FFC300",ax=axes[2])
axes[2].set_title("Expression of Gene3 in different Samples")
axes[2].set_xlabel("Sample Number")

normal=pd.read_csv('/Users/IBR/Desktop/pilo.csv')