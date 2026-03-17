gene_express={'TP53':12.4, 'EGFR':15.1, 'BRCA1':8.2, 'PTEN':5.3, 'ESR1':10.7}
print(gene_express) #create and print a dictionary in Python containing the genes and their expression values
gene_express['MYC'] = 11.6 #add the gene to the dictionary
print(gene_express)
#bar chart

import matplotlib.pyplot as plt
import numpy as np

genes = list(gene_express.keys())
values = list(gene_express.values())
plt.bar(genes, values, width=0.35)
plt.xlabel('Gene name')
plt.ylabel('Expression')
plt.title('Expression levels of genes measured in a biological sample')
plt.show()

interest = 'abc' #the variable's value can be changed into any gene of interest
if interest in gene_express:
    print("The expression value of the gene", interest, "is:",{gene_express[interest]})
else:
    print("The gene of interest in not included in the dataset.")

#calculate the average of expression values
avrg = sum(values) / len(values)
print("The average gene expression level across all genes is:", avrg)