# Create a GUI for image segmentation using k-means clustering

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from sklearn.cluster import KMeans


# Read image
img = plt.imread('image.jpg')

# Convert image to 2D array
img2D = img.reshape(img.shape[0]*img.shape[1], img.shape[2])

# Create a figure
fig = plt.figure(figsize=(10, 5))

# Add a subplot for the image
ax = fig.add_subplot(1, 2, 1)
ax.imshow(img)

# Add a subplot for the histogram
axHist = fig.add_subplot(1, 2, 2)
axHist.set_title('Histogram')
axHist.set_xlabel('Color')
axHist.set_ylabel('Frequency')

# Add a slider for the number of clusters
axSlider = fig.add_axes([0.25, 0.05, 0.65, 0.03])
slider = Slider(axSlider, 'Number of clusters', 1, 10, valinit=3)

# Add a button for the segmentation
axButton = fig.add_axes([0.8, 0.1, 0.1, 0.04])
button = Button(axButton, 'Segment')

# Add a radio button for the color space
axRadio = fig.add_axes([0.05, 0.4, 0.1, 0.15])
radio = RadioButtons(axRadio, ('RGB', 'HSV', 'LAB'))

# Add a check box for the histogram
axCheck = fig.add_axes([0.05, 0.2, 0.1, 0.15])
check = RadioButtons(axCheck, ('Show', 'Hide'))

# Add a text box for the number of clusters
axText = fig.add_axes([0.05, 0.05, 0.1, 0.04])
text = axText.text(0.5, 0.5, '3', transform=axText.transAxes,
                     ha='center', va='center')

# Define a function for the segmentation
def segment(event):
    # Get the number of clusters
    nClusters = int(slider.val)

    # Get the color space
    colorSpace = radio.value_selected

    # Convert the image to the selected color space
    if colorSpace == 'RGB':
        img2D = img.reshape(img.shape[0]*img.shape[1], img.shape[2])
    elif colorSpace == 'HSV':
        img2D = plt.colors.rgb_to_hsv(img)
        img2D = img2D.reshape(img2D.shape[0]*img2D.shape[1], img2D.shape[2])
    elif colorSpace == 'LAB':
        img2D = plt.colors.rgb_to_lab(img)
        img2D = img2D.reshape(img2D.shape[0]*img2D.shape[1], img2D.shape[2])

    # Perform k-means clustering
    kmeans = KMeans(n_clusters=nClusters, random_state=0).fit(img2D)

    # Get the cluster labels
    labels = kmeans.labels_

    # Get the cluster centers
    centers = kmeans.cluster_centers_

    # Convert the cluster centers to the original color space
    if colorSpace == 'HSV':
        centers = plt.colors.hsv_to_rgb(centers)
    elif colorSpace == 'LAB':
        centers = plt.colors.lab_to_rgb(centers)

    # Get the segmented image
    segmented = centers[labels].reshape(img.shape[0], img.shape[1], img.shape[2])

    # Display the segmented image
    ax.imshow(segmented)

    # Display the histogram
    if check.value_selected == 'Show':
        axHist.cla()
        axHist.hist(labels, bins=nClusters)
        axHist.set_title('Histogram')
        axHist.set_xlabel('Color')
        axHist.set_ylabel('Frequency')

    # Display the number of clusters
    text.set_text(str(nClusters))

    # Redraw the figure
    fig.canvas.draw_idle()

# Define a function for the slider
def updateSlider(val):
    # Get the number of clusters
    nClusters = int(slider.val)

    # Display the number of clusters
    text.set_text(str(nClusters))

    # Redraw the figure
    fig.canvas.draw_idle()

# Define a function for the radio button
def updateRadio(label):
    # Redraw the figure
    fig.canvas.draw_idle()

# Define a function for the check box
def updateCheck(label):
    # Redraw the figure
    fig.canvas.draw_idle()

# Connect the event handlers
slider.on_changed(updateSlider)
button.on_clicked(segment)
radio.on_clicked(updateRadio)
check.on_clicked(updateCheck)

# Show the figure
plt.show()
