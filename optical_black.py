import rawpy
import imageio.v3 as iio
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import subprocess


path = 'test_images/Canon.CR2'

with rawpy.imread(path) as raw:
    raw_image = raw.raw_image.copy()
    raw_image_visiable = raw.raw_image_visible.copy()
iio.imwrite('result_images/grey/rawpy_raw.tiff', raw_image)
iio.imwrite('result_images/grey/rawpy_visibleraw.tiff', raw_image_visiable)

dcraw_command = [
    "dcraw", "-D", "-4", "-T", path
]
# 执行命令
try:
    subprocess.run(dcraw_command, check=True)
    print("dcraw 命令执行成功！")
except subprocess.CalledProcessError as e:
    print(f"执行 dcraw 命令时发生错误: {e}")
except FileNotFoundError:
    print("未找到 dcraw 可执行文件，请确保 dcraw 已安装并配置在系统路径中。")

dcraw_raw = iio.imread('test_images/Canon.tiff')

plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.imshow(raw_image/65535)
plt.title('rawpy with optical black')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(raw_image_visiable/(2**16))
plt.title('rawpy without optical black')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(dcraw_raw/(2**16))
plt.title('dcraw')
plt.axis('off')

plt.show()