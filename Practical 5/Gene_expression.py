import matplotlib.pyplot as plt
import numpy as np

gene_expr = {'TP53': 12.4, 'EGFR': 15.1, 'BRCA1': 8.2, 'PTEN': 5.3, 'ESR1': 10.7}
print ("gene expression dictionary")
print (gene_expr)
gene_expr["MYC"]=11.6

gene_of_interest = "MYC"
if gene_of_interest in gene_expr:
    print("the expression of", gene_of_interest, "is", gene_expr[gene_of_interest])
    #print(f"the expression of {gene_of_interest} is {gene_expr[gene_of_interest]}")
else:
    print("error, this gene is not in the list")

expression_values = list(gene_expr.values())
average_expression = sum(expression_values) / len(expression_values)
print("the average expression is", average_expression)

N = 6
expressions = (12.4, 15.1, 8.2, 5.3, 10.7, 11.6)
ind = np.arange(N)
width = 0.3
p1 = plt.bar(ind, expressions, width)
plt.ylabel('expressions')
plt.xlabel('genes')
plt.title('expressions of genes')
plt.xticks(ind, ('TP53', 'EGFR', 'BRCA', 'PTEN', 'ESR1', 'MYC',))
plt.yticks(np.arange(0,21,2))

plt.show()