# 1. Create and print a dictionary containing gene expression values
gene_expression = {
    "TP53": 12.4,
    "EGFR": 15.1,
    "BRCA1": 8.2,
    "PTEN": 5.3,
    "ESR1": 10.7
}

# Add the new gene 'MYC' with an expression value of 11.6
print("Gene expression dictionary:")
print(gene_expression)
gene_expression["MYC"] = 11.6

# 2. Produce a well-labelled bar chart showing expression values of all genes
import matplotlib.pyplot as plt

genes = list(gene_expression.keys())
expressions = list(gene_expression.values())

plt.bar(genes, expressions, color='green')
plt.xlabel("Gene")
plt.ylabel("Expression Level")
plt.title("Gene Expression Levels in Biological Sample")
plt.show()

# 3. Define a gene of interest and print its expression value (variable can be modified)
gene_of_interest = "TP53"
if gene_of_interest in gene_expression:
    print(f"\nThe expression value of gene {gene_of_interest} is: {gene_expression[gene_of_interest]}")
else:
    print(f"\nError: No expression data found for gene {gene_of_interest}")

# 4. Calculate and print the average gene expression level across all genes
average_expression = sum(expressions) / len(expressions)
print(f"\nThe average gene expression level across all genes is: {average_expression:.1f}")