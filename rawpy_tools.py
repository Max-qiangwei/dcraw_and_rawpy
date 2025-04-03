import rawpy
import imageio.v3 as iio
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import subprocess

path = 'test_images/Canon.CR2'

'''
For more features, please refer to: https://pypi.org/project/rawpy/
'''

with rawpy.imread(path) as raw:
    print(f'black level:{raw.black_level_per_channel}')
    print(f'white level:{raw.camera_white_level_per_channel}')
    print(f'pattern:{raw.raw_pattern}')
    rgb = raw.postprocess(
        gamma=(1,1),
        output_bps=16,
        use_auto_wb = False,
        use_camera_wb = False,
        user_wb = [1,1,1,1],
        output_color = rawpy.ColorSpace.raw,
        no_auto_bright = True,
    )
iio.imwrite('result_images/rawpy/Canon_result.tiff', rgb)

with rawpy.imread(path) as raw:
    rgb_stander = raw.postprocess()
iio.imwrite('result_images/rawpy/Canon_standard.tiff', rgb_stander)


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