import numpy as np
import matplotlib.pyplot as plt

# Load the npz file
data_path = r"C:\Myfiles\OPENAI_DIR\samples_36x128x128x1.npz"
data = np.load(data_path)

# Get the array from the npz file
images = data.f.arr_0  

rows = 3
cols = 3
fig, axes = plt.subplots(rows, cols, figsize=(10, 10))

# Plot each image
for i in range(9):
    row = i // cols
    col = i % cols
    
    img = images[i].squeeze()
    
    axes[row, col].imshow(img, cmap='gray')
    axes[row, col].axis('off')
    axes[row, col].set_title(f'Image {i+1}')

plt.tight_layout()
plt.show()

# Optionally save the plot
# plt.savefig('samples_visualization.png', dpi=300, bbox_inches='tight')
