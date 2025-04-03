import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import subprocess
import os
import shutil
import imageio.v3 as iio

path = 'test_images/Canon.CR2'
output_dir = 'result_images\\dcraw'
output_filename = 'Canon_result.tiff'

'''
-v: Enable verbose mode to output detailed information during the run, such as decoding progress, image parameters, etc.
-4: Linear 16-bit output mode.
-T: Output TIFF format (default is ppm format)
-o 0: The original camera color profile is used (no additional color correction is performed)
    -o 1: Use sRGB color space.
    -o 2: Use Adobe RGB color space.
    -o 3: Use wide gamut color space.
-W: Automatic white balance. If -W is not specified, dcraw uses the white balance value recorded by the camera.
-H 0: Preserve all highlight details (no highlight clipping).
    -H 1: Clip highlights (set overexposed areas to their maximum value).
    -H 2: Blending mode (tries to recover some highlight detail).
-r 1 1 1 1: Manually set the white balance factor as 1,1,1,1.
-g 1 1: Setting the gamma curve as 1,1

For more detailed usage, please refer to: 
Official: https://www.dechifro.org/dcraw/
My own conclusion: https://github.com/Max-qiangwei/dcraw_usage.git
'''


dcraw_command = [
    "dcraw", "-v", "-4", "-T", "-o", "0", "-W", "-H", "0", "-r", "1", "1", "1", "1", "-g", "1", "1", path
]

try:
    subprocess.run(dcraw_command, check=True)
    print("dcraw command executed successfully！")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while executing the dcraw command: {e}")
except FileNotFoundError:
    print("The dcraw executable was not found, please make sure dcraw is installed and configured in the system path.")

# move to target folder
default_output_filename = os.path.splitext(os.path.basename(path))[0] + ".tiff"
shutil.move(os.path.join('test_images',default_output_filename), os.path.join(output_dir, output_filename))


#  Use all default settings
dcraw_standard_command = [
    "dcraw", path
]

try:
    subprocess.run(dcraw_standard_command, check=True)
    print("dcraw command executed successfully！")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while executing the dcraw command: {e}")
except FileNotFoundError:
    print("The dcraw executable was not found, please make sure dcraw is installed and configured in the system path.")

# move to target folder
default_output_filename = os.path.splitext(os.path.basename(path))[0] + ".ppm"
shutil.move(os.path.join('test_images',default_output_filename), os.path.join(output_dir, 'Canon_standard.ppm'))


# show result
rgb_stander = iio.imread('result_images/dcraw/Canon_standard.ppm')
rgb = iio.imread('result_images/dcraw/Canon_result.tiff')

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(rgb_stander)
plt.title('Standard')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(rgb/(2**16)) #The image is saved as 16-bit, normalization is required
plt.title('Result')
plt.axis('off')

plt.show()