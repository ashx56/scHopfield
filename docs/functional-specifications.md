# Functional Specification

## Background
Single-cell RNA sequencing (scRNAseq) data provides insights into the gene expression profiles of individual cells, which can reveal distinct cell states and differentiation pathways. Modeling the "differentiation potency" of cells — their potential to transition into other states — is critical for understanding developmental biology, regenerative medicine, and cell reprogramming.

However, scRNAseq data poses challenges due to its high dimensionality, sparsity, and complexity. Current methods often fail to accurately capture intermediate states or predict likely differentiation routes with precision. 

This project aims to address these challenges by applying classical Hopfield networks to model cell state transitions and identify differentiation pathways. By leveraging Hopfield network energies and gene expression variability, this package will allow researchers to better visualize and quantify cell differentiation trajectories, providing insights into the most variable genes driving these transitions.

## User Profile
Computational biologists, bioinformaticians, and research scientists working in the field of single-cell genomics, developmental biology, or regenerative medicine. Likely to have a foundational understanding of biology, particularly in cellular differentiation and gene expression, as well as familiarity with scRNAseq data analysis.

## Use Cases

### Use Case 1: Calculate Hopfield Energies and plot along PC1

- **Objective**: The user aims to calculate the Hopfield energies of all cells in the dataset and visualize them along the first principal component (PC1), colored by cell type. This provides insight into the relative "potency" of cells, with cells showing higher energies being more "pluripotent," while cells with lower energies are closer to terminal differentiation. This also helps in identifying the probable differentiation trajectory.

- **User-System Interaction**:
  1. The user inputs an scRNAseq count matrix (preprocessed) and specifies the desired cell type annotations.
  2. The system normalizes and filters the data, selecting highly variable genes for the Hopfield network model.
  3. The user initiates the calculation of Hopfield energies across all cells.
  4. The system calculates the energies using a classical Hopfield network and applies dimensionality reduction to plot these energies along PC1.
  5. The system outputs a plot of Hopfield energies across PC1, colored by cell type, allowing the user to visualize potency and potential differentiation routes.

### Use Case 2: Simulate Differentiation Process between Cell Types and Identify Key Genes

- **Objective**: The user wants to simulate the differentiation process from one annotated cell type (e.g., progenitor) to another (e.g., mature cell type) and identify genes that vary most significantly along this trajectory. This will assist users in developing or refining differentiation protocols by highlighting target genes that are dynamically regulated during the transition.

- **User-System Interaction**:
  1. The user inputs an scRNAseq count matrix and selects the starting and ending cell types for differentiation.
  2. The system preprocesses the data, identifying highly variable genes and constructing a Hopfield network with the specified cell type information.
  3. The user initiates the simulation for transitioning from cell type 1 to cell type 2.
  4. The system simulates the differentiation trajectory and calculates gene expression changes along this path.
  5. The system outputs a ranked list of genes with significant variability along the transition and provides a heatmap, enabling the user to review genes that could serve as markers or regulators in differentiation protocols.



