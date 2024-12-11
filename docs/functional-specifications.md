# Functional Specification

## Background

Single-cell RNA sequencing (scRNAseq) data provides insights into the gene expression profiles of individual cells, revealing distinct cell states and differentiation pathways. Modeling the "differentiation potency" of cells — their potential to transition into other states — is critical for understanding developmental biology, regenerative medicine, and cell reprogramming.

However, scRNAseq data poses challenges due to its high dimensionality, sparsity, and complexity. This project addresses these challenges by applying classical Hopfield networks to model cell state transitions and identify differentiation pathways. By leveraging Hopfield network energies and gene expression variability, the `HopfieldModel` package allows researchers to better visualize and quantify cell differentiation trajectories, providing insights into the most variable genes driving these transitions.

---

## User Profile

The package is intended for:
- Computational biologists
- Bioinformaticians
- Research scientists

These users are likely working in the fields of single-cell genomics, developmental biology, or regenerative medicine. They should have a foundational understanding of:
- Cellular differentiation and gene expression.
- Single-cell RNA sequencing (scRNAseq) data analysis.

---

## Use Cases

### **Use Case 1: Calculate Hopfield Energies and Visualize Along PC1**

- **Objective**: Calculate the Hopfield energies of all cells in the dataset and visualize them along the first principal component (PC1), grouped by cell type. This provides insight into the relative "potency" of cells and helps identify potential differentiation trajectories.
  
- **Features Involved**:
  1. **Normalization**: Standardize the input gene expression data using Z-score normalization.
  2. **Highly Variable Gene Selection**: Select the top genes based on variance.
  3. **Hopfield Network Construction**: Create a weight matrix for each cell.
  4. **Energy Computation**: Calculate Hopfield energy for each cell.
  5. **Visualization**: Plot energies along PC1, with points colored by cell type.

- **Workflow**:
  1. User inputs an scRNAseq count matrix (preprocessed) and cell type annotations.
  2. System normalizes the data and selects highly variable genes.
  3. User initiates the Hopfield energy calculation.
  4. System computes the Hopfield energies and plots them along PC1, highlighting the differentiation trajectory.

---

### **Use Case 2: Visualize Hopfield Energy Across Cell Types**

- **Objective**: Generate a boxplot to compare Hopfield energy distributions across different cell types, providing a high-level summary of cell state variability.

- **Features Involved**:
  1. **Energy Computation**: Calculate Hopfield energy for each cell.
  2. **Grouped Visualization**: Create a boxplot of average Hopfield energies grouped by cell type.

- **Workflow**:
  1. User inputs the scRNAseq count matrix and cell type annotations.
  2. System calculates Hopfield energies for all cells.
  3. User initiates grouped visualization.
  4. System produces a boxplot of average energies per cell type.

---

### **Use Case 3: PCA Visualization of Energy-Colored Cells**

- **Objective**: Plot cells in PCA space, where each point is colored by its Hopfield energy, with distinct colors for each cell type. This helps identify clusters and energy trends in PCA space.

- **Features Involved**:
  1. **Energy Computation**: Calculate Hopfield energy for all cells.
  2. **Dimensionality Reduction**: Perform PCA on the highly variable genes.
  3. **Visualization**: Scatter plot of PCA results, with cells colored by energy.

- **Workflow**:
  1. User inputs the scRNAseq count matrix and cell type annotations.
  2. System calculates Hopfield energies and reduces dimensions using PCA.
  3. User initiates PCA visualization.
  4. System produces a PCA plot, with cells colored by Hopfield energy and distinct colors for each cell type.

---

### **Use Case 4: Simulate Differentiation Process Between Two Cell Types**

- **Objective**: Simulate the differentiation process between two cell types and identify the genes that vary most significantly during this transition. This enables users to pinpoint key regulators of differentiation.

- **Features Involved**:
  1. **Energy Computation**: Calculate Hopfield energies for cells of the two selected types.
  2. **Dimensionality Reduction**: Plot energies along PC1 for the two cell types.
  3. **Gene Transition Analysis**: Identify genes with significant variability and visualize their state changes using a heatmap.

- **Workflow**:
  1. User selects two cell types (e.g., progenitor and mature).
  2. System identifies highly variable genes and constructs a Hopfield network for the selected cells.
  3. User initiates the simulation.
  4. System computes the differentiation trajectory, plots energies along PC1, and identifies variable genes.
  5. System outputs:
     - A transition energy plot.
     - A heatmap of gene state changes, clustered hierarchically.
     - A ranked list of top genes for each cell type.

