import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import imageio.v3 as iio
import numpy as np

def RGB2rg(image):
    image = image.astype(np.float32)
    total = np.sum(image, axis=-1) + 1e-8
    r = image[..., 0] / total
    g = image[..., 1] / total
    return r, g


path1 = 'result_images/dcraw/Canon_result.tiff'
img1 = iio.imread(path1)[::200, ::200]  # Downsampling
r1, g1 = RGB2rg(img1)

path2 = 'result_images/rawpy/Canon_result.tiff'
img2 = iio.imread(path2)[::200, ::200]  # Downsampling
r2, g2 = RGB2rg(img2)

plt.figure(figsize=(10, 8))
plt.scatter(r1, g1, c='red', alpha=0.3, s=30, label='dcraw')
plt.scatter(r2, g2, c='blue', alpha=0.3, s=30, label='rawpy')
plt.xlabel('r')
plt.ylabel('g')
plt.title('Result comparation')
plt.legend()
plt.show()



path1 = 'result_images/dcraw/Canon_standard.ppm'
img1 = iio.imread(path1)[::200, ::200]  # Downsampling
r1, g1 = RGB2rg(img1)

path2 = 'result_images/rawpy/Canon_standard.tiff'
img2 = iio.imread(path2)[::200, ::200]  # Downsampling
r2, g2 = RGB2rg(img2)

plt.figure(figsize=(10, 8))
plt.scatter(r1, g1, c='red', alpha=0.3, s=30, label='dcraw')
plt.scatter(r2, g2, c='blue', alpha=0.3, s=30, label='rawpy')
plt.xlabel('r')
plt.ylabel('g')
plt.title('Standard comparation')
plt.legend()
plt.show()