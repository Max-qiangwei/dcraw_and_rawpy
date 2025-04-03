# How to make *rawpy* the same as *dcraw*
*Max Chen*

## Introduction

*rawpy* and *dcraw* are commonly used for processing raw image files, but if the wrong commands are used, the results from the same raw image can end up being completely different. 

Here, I provide some examples that demonstrate common methods for processing raw images, ensuring that the results from both *rawpy* and *dcraw* are exactly the same. 

The usage of *dcraw* can be referenced here: https://github.com/Max-qiangwei/dcraw_usage.git or offical reference here: https://www.dechifro.org/dcraw/. 
For more details on using *rawpy*, you can refer to: https://pypi.org/project/rawpy/.

Additionally, methods for obtaining the raw, demosaicked 2D image are also included. *dcraw* typically ignores optical black fields, while *rawpy* allows you to output images either with or without the optical black field. 

(P.S.: The optical black field refers to the area of the sensor that is covered by a mask and does not capture any light, typically used for measuring the sensor's dark current noise.)"


## Prerequisites

Before running the program, you need to download dcraw and add "dcraw.exe" to the system environment variables.

You can download "dcraw.exe" or other versions on: https://www.dechifro.org/dcraw/

## Provided materials

This project provide:

- **dcraw_tool.py:** An runable python program, shows how to use *dcraw* command with Python (No other settings such as white balance are applied, just simple demosaicing).
- **rawpy_tool.py:** An runable python program, shows how to use *rawpy* command with Python (Same as *dcraw*).
- **Comparation.py:** The processed results are downsampled and compared in rg space. Where, r = R/(R+G+B), g = G/(R+G+B).
- **optical_black.py:** Shows how to use *dcraw* and *rawpy* to get a 2D image without demosaic. *rawpy* can get a 2D image with or without optical black field.


