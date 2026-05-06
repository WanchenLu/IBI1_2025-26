genes = {'TP53':12.4,'EGFR':15.1,'BRCA1':8.2,'PTEN':5.3,'ESR1':10.7}
print (genes)
genes ['MYC'] = 11.6
import matplotlib.pyplot as plt
expression = list(genes.values())
gene_names = list(genes.keys())
ind = list(range(len(gene_names)))
width = 0.35
pl = plt.bar(ind,expression,width)
plt.ylabel('Expression')
plt.xlabel('Gene')
plt.title('Expression values of genes')
plt.xticks(ind,gene_names)
plt.yticks(range(0,21,3))
plt.bar_label(pl,fmt='%.1f')
plt.show()
# Here is the variable
interest = 'TP53' #
if interest in genes :
    print ("the expression value of ",interest," is ",genes[interest])
else :
    print (interest," is not in the dictionary")
total = 0
number = 0
for e in expression :
    total += e
    number += 1
average = total/number
print ("the average gene expression level across all genes is ",average)