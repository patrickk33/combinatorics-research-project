# This script plots the matrix of binary mixtures to a graph

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    # Create a pandas dataframe from the csv file containing the solvents, solutes, and activity coefficients
    df = pd.read_csv('./Solvent-Solute-Activity-Coeff.csv')

    # Create lists containing the solvents solutes
    solvents = []
    solutes = []
    for solv in df['Solvent']:
        if solv not in solvents:
            solvents.append(solv)
    for solu in df['Solute']:
        if solu not in solutes:
            solutes.append(solu)

    # Map the solvent and solute names to numbers for plotting
    solv_dict = dict((j, i) for i, j in enumerate(solvents))
    solu_dict = dict((j, i) for i, j in enumerate(solutes))
    x_coord = []
    y_coord = []
    for solv in df['Solvent']:
        x_coord.append(solv_dict.get(solv))
    for solu in df['Solute']:
        y_coord.append(solu_dict.get(solu))

    # Create and format the plot
    plt.clf()
    plt.figure(figsize=(20, 20))
    plt.scatter(y_coord, x_coord, s=300, c='blue')  # Matplotlib does x and y backwards
    plt.gca().invert_yaxis()
    plt.subplot().set_title('Binary Mixture Matrix Representation', fontsize=32)
    plt.subplot().set_xlabel(r'Solvent $j$', fontsize=24)
    plt.subplot().set_ylabel(r'Solute $i$', fontsize=24)
    plt.subplot().set_xticklabels([])
    plt.subplot().set_yticklabels([])
    plt.locator_params(axis='x', nbins=42)
    plt.locator_params(axis='y', nbins=46)
    plt.grid(visible=True)

    plt.savefig('binary-mixture-matrix-rep.png')  # Save the plot to a png file


if __name__ == '__main__':
    main()
