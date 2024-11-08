## Software Components

### 1. Data Manager
- **Function**: Preprocesses scRNAseq data, selecting highly variable genes 
- **Inputs**: 
  - Raw or normalized count matrix (cells x genes).
  - Cell type or metadata annotations.
  - Preprocessing parameters (e.g., normalization, variance threshold).
- **Outputs**: 
  - Filtered, normalized count matrix with highly variable genes only.

### 2. Network Manager
- **Function**: Constructs a fully connected classical Hopfield network, storing edge weights for each cell based on the Hebbian learning rule, and computes Hopfield energies for potency analysis.
- **Inputs**: 
  - Preprocessed count matrix from the Data Manager.
- **Outputs**: 
  - Hopfield network with edge weights for each cell.
  - Hopfield energy values for each cell.

### 3. Visualization Manager
- **Function**: Generates visualizations for data interpretation, including energy plots along PC1, differentiation trajectories, and gene variability plots.
- **Inputs**: 
  - Hopfield energies, PCA results, and counts data.
- **Outputs**: 
  - Plots of Hopfield energies by PC1, colored by cell type.
  - Heatmaps of key genes varying across transitions.

## Interactions to Accomplish Use Cases

### Use Case 1: Calculate Hopfield Energies and Plot along PC1

1. **Data Manager**:
   - The user inputs the scRNAseq count matrix and cell type annotations.
   - The Data Manager preprocesses the data by normalizing it and selecting highly variable genes based on specified criteria.
   - The resulting filtered matrix is passed to the Network Manager.

2. **Network Manager**:
   - Using the preprocessed data, the Network Manager constructs a Hopfield network, calculating edge weights for each cell according to the Hebbian learning rule.
   - It then computes Hopfield energy values for each cell, which represent each cell's "potency" in the differentiation landscape.
   - These energy values are then forwarded to the Visualization Manager.

3. **Visualization Manager**:
   - The Visualization Manager receives the Hopfield energies and performs principal component analysis (PCA) to reduce the dimensionality of the data.
   - It plots the Hopfield energies along the first principal component (PC1), coloring each point by cell type to visualize the distribution of potency and differentiation trajectory.
   - The final plot is output to the user, providing insight into pluripotency and differentiation pathways among cell types.



