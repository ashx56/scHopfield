# Component Specification

## Software Components

### **1. Data Manager**
- **Function**: Handles preprocessing of scRNAseq data, including normalization and selection of highly variable genes.
- **Inputs**:
  - Raw or normalized count matrix (cells x genes).
  - Cell type annotations or metadata.
  - Parameters for preprocessing (e.g., normalization method, variance threshold).
- **Outputs**:
  - Normalized count matrix.
  - Filtered matrix with only highly variable genes.

---

### **2. Network Manager**
- **Function**: Constructs a classical Hopfield network for each cell, computes edge weights using the Hebbian learning rule, and calculates Hopfield energies for differentiation potency analysis.
- **Inputs**:
  - Preprocessed count matrix from the Data Manager.
- **Outputs**:
  - Hopfield weight matrices for each cell.
  - Hopfield energy values for all cells.

---

### **3. Visualization Manager**
- **Function**: Generates plots to help users interpret the data, including energy distribution along PC1, PCA-based clustering, and gene variability heatmaps.
- **Inputs**:
  - Hopfield energies.
  - PCA results from dimensionality reduction.
  - Gene expression data.
- **Outputs**:
  - Scatter plots of Hopfield energies along PC1, grouped by cell type.
  - Heatmaps showing gene variability and transitions between cell types.
  - PCA visualizations with energy-based coloring for each cell.

---

## Interactions to Accomplish Use Cases

### **Use Case 1: Calculate Hopfield Energies and Plot Along PC1**

1. **Data Manager**:
   - The user provides the scRNAseq count matrix and cell type annotations.
   - The Data Manager normalizes the data and selects highly variable genes.
   - The filtered matrix is passed to the Network Manager.

2. **Network Manager**:
   - Constructs Hopfield weight matrices for each cell using the highly variable genes.
   - Computes Hopfield energy values for all cells.
   - Passes the energy values to the Visualization Manager.

3. **Visualization Manager**:
   - Performs PCA on the highly variable genes to reduce dimensionality.
   - Plots Hopfield energy values along PC1, coloring points by cell type.
   - Outputs the final visualization, helping the user understand differentiation potency and trajectories.

---

### **Use Case 2: Visualize Hopfield Energy Across Cell Types**

1. **Data Manager**:
   - The user provides the scRNAseq count matrix and cell type annotations.
   - The Data Manager preprocesses the data, normalizing it and filtering for highly variable genes.
   - The preprocessed matrix is passed to the Network Manager.

2. **Network Manager**:
   - Constructs Hopfield networks for each cell and computes energy values.
   - Groups energy values by cell type and forwards them to the Visualization Manager.

3. **Visualization Manager**:
   - Creates a boxplot of Hopfield energy distributions grouped by cell type.
   - Outputs the boxplot to the user for interpretation.

---

### **Use Case 3: PCA Visualization of Energy-Colored Cells**

1. **Data Manager**:
   - Preprocesses the scRNAseq data by normalizing it and selecting highly variable genes.

2. **Network Manager**:
   - Computes Hopfield energy values for all cells.

3. **Visualization Manager**:
   - Performs PCA on the preprocessed data to reduce dimensionality.
   - Creates a scatter plot in PCA space, coloring points by their Hopfield energy.
   - Outputs the PCA plot, showing clusters and energy trends.

---

### **Use Case 4: Simulate Differentiation Between Two Cell Types**

1. **Data Manager**:
   - The user provides the count matrix and selects two cell types for the transition.
   - The Data Manager normalizes the data and identifies highly variable genes.

2. **Network Manager**:
   - Constructs Hopfield weight matrices for the selected cells.
   - Computes Hopfield energy values and identifies variable genes across the transition.

3. **Visualization Manager**:
   - Performs PCA to visualize the transition trajectory along PC1.
   - Creates a heatmap of gene state transitions between the two cell types, highlighting dynamically regulated genes.
   - Outputs both visualizations and a ranked list of top variable genes.

---


