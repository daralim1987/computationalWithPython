#####################################
## Plotting features of the sklearn iris dataset covered in
## Ch. 2, Richert & Coeho. “Building ML Systems with Py.”
##
## Bugs to vladimir dot kulyukin at usu dot edu
#####################################
from matplotlib import pyplot as plt
import sys

# We load the data with load_iris from sklearn
from sklearn.datasets import load_iris

# load_iris returns an object with several fields
data = load_iris()
feature_names = data.feature_names
## 0 - sepal length (cm)
## 1 - sepal width  (cm)
## 2 - petal length (cm)
## 3 - petal width  (cm)
data_items = data.data
## target - target_name
## 0 - setosa
## 1 - versicolor
## 2 - virginica
target = data.target
target_names = data.target_names

## we will do a figure of 2 rows and 3 columns
fn_pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

# Set up 3 different pairs of (color, marker)
color_markers = [
        ('r', '>'), ## setosa is red triangle
        ('g', 'o'), ## versicolor is green circle
        ('b', 'x'), ## virginica is blue x
        ]

## enumerate(fn_pairs) results in the
## following 
## (0, (0, 1))
## (1, (0, 2))
## (2, (0, 3))
## (3, (1, 2))
## (4, (1, 3))
## (5, (2, 3))

def save_feature_vs_feature_plot_as_figure(png_image_path):
    fig, axes = plt.subplots(2, 3)
    ## axes is a 2x3 array of AxesSubplot objects
    ##[[<matplotlib.axes.AxesSubplot object at 0x7f244ed4e9d0>
    ##  <matplotlib.axes.AxesSubplot object at 0x7f244dd192d0>
    ##  <matplotlib.axes.AxesSubplot object at 0x7f244dc57c90>]
    ## [<matplotlib.axes.AxesSubplot object at 0x7f244dbdd790>
    ##  <matplotlib.axes.AxesSubplot object at 0x7f244db50810>
    ##  <matplotlib.axes.AxesSubplot object at 0x7f244dad4b90>]]
    for i, (fn0, fn1) in enumerate(fn_pairs):
        ax = axes.flat[i]
        for t in xrange(3):
            # Use a different color/marker for each class t
            c, marker = color_markers[t]
            ## find all feature values for target==t and feature fn0, i.e.,
            ## data_items[target==t, fn0]
            x = data_items[target==t, fn0]
            ## find all feature values for target==t and feature fn1, i.e.,
            ## data_items[target==t, fn1]
            y = data_items[target==t, fn1]
            ax.scatter(x, y, marker=marker, c=c)
        ## set the label of x to the name of feature whose number is fn0
        ax.set_xlabel(feature_names[fn0])
        ## set the label of y to the name of feature whose number is fn1
        ax.set_ylabel(feature_names[fn1])
        ## eliminate the ticks
        ax.set_xticks([])
        ax.set_yticks([])
    fig.tight_layout()
    fig.savefig(png_image_path)

if __name__ == '__main__':
    save_feature_vs_feature_plot_as_figure(sys.argv[1])
