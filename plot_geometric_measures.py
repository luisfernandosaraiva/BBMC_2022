#!/usr/bin/env python3

import os, argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

def plottingData():
    
    df = pd.read_csv(os.getcwd()+"/"+args.data, delimiter= '\t', header=0, sep='\t')

    if ',' in args.option and not args.pdf:

        # Spliting variable
        numVar = args.option.split(',')

        # Deleting quotes
        numVar[0].strip('"')
        numVar[1].strip('"')
        fig, (ax1) = plt.subplots(nrows=1)
        
        # Color by the Probability Density Function. 
        # Kernel density estimation is a way to estimate 
        # the probability density function (PDF) of a random 
        # variable in a non-parametric way
        
        # Setting data
        x = df[numVar[0]]
        y = df[numVar[1]]

        # Calculate the point density
        xy = np.vstack([x,y])
        z = gaussian_kde(xy)(xy)

        # Sort the points by density, so that the densest points are plotted last
        idx = z.argsort()
        x, y, z = x[idx], y[idx], z[idx]

        # Setting plot type 
        pdf = ax1.scatter(x, y, c = z, s = 50, edgecolor = '')

        # Plot title
        ax1.set_title(numVar[0] + ' by ' + numVar[1])

        # Hide right and top spines
        ax1.spines['right'].set_visible(False)
        ax1.spines['top'].set_visible(False)
        ax1.yaxis.set_ticks_position('left')
        ax1.xaxis.set_ticks_position('bottom')

        # Set x and y limits
        xmin = df[""+numVar[0]+""].min() - 1
        xmax = df[""+numVar[0]+""].max() + 1
        ymin = df[""+numVar[1]+""].min() - 1
        ymax = df[""+numVar[1]+""].max() + 1        
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)

        # Set x and y labels
        plt.xlabel(numVar[0])
        plt.ylabel(numVar[1])

        # Adding the color bar 
        colbar = plt.colorbar(pdf)
        colbar.set_label('Probability Density Function')     
        plt.show()

    elif not ',' in args.option:

        fig, (ax1) = plt.subplots(nrows=1)
        ax1.plot(df['#Frame'], df[args.option])
        ax1.set_title(args.option + ' by Time')
        ax1.spines['right'].set_visible(False)
        ax1.spines['top'].set_visible(False)
        ax1.yaxis.set_ticks_position('left')
        ax1.xaxis.set_ticks_position('bottom')
        plt.xlabel('Time (ps)')
        xmin1 = df['#Frame'].min() - 1
        xmax1 = df['#Frame'].max() + 1
        plt.xlim(xmin1, xmax1)
        plt.ylabel(args.option)        
        plt.show()
        
    elif ',' in args.option and args.pdf == 'kde':

        import seaborn.apionly as sns; sns.set(style = 'white')
        numVar = args.option.split(',')
        numVar[0].strip('"')
        numVar[1].strip('"')

        # Distribution plot of two variables using KDE method with seaborn 
        sns.jointplot(x = numVar[0], y = numVar[1], data = df, kind = "kde", space = 0, color = "b")
        plt.show()


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Plot All Geometric Analysis .', formatter_class = argparse.RawTextHelpFormatter)
    parser.add_argument('-p', '--MultiPDB\t\t\t', action='store', required=False, dest='data', help="The trajectory file must be a Multi-PDB.")
    parser.add_argument('-t', '--analysisType\t\t', action='store', required=False, dest='option', type = str, help="Specify the type of your analysis: Angle, Dihedral, Area, DistAB, DistAC, DistBC.")
    parser.add_argument('-dist', '--PDFDistribution\t\t', action='store', required=False, dest='pdf', type = str, help="Type 'kde'.")

    args = parser.parse_args()
    plottingData()