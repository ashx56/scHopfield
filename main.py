import sys
from schopfield import HopfieldModel

def main(data, cell_types, gene_names, top_percent=5):
    """
    Main function to set up and execute the HopfieldModel.

    Parameters:
    data (numpy.ndarray): A 2D array where rows represent cells and columns represent gene expression levels.
    cell_types (numpy.ndarray): Array of cell type labels for each cell.
    gene_names (list): List of gene names corresponding to columns in the data.
    top_percent (int): The percentage of genes to select based on variance (default: 5).
    """
    # Initialize the HopfieldModel
    model = HopfieldModel(data, cell_types, gene_names)

    # Normalize the data
    model.normalize_data()

    # Select highly variable genes
    model.select_highly_variable_genes(top_percent=top_percent)

    # Construct weight matrices for each cell
    model.construct_weight_matrices()

    print("Hopfield Model setup completed. Ready for analysis.")

if __name__ == "__main__":
    print("This is a generic script for initializing the HopfieldModel.")
