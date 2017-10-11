Encoder Integration in C++
==========================

- **Tensorflow r1.1** is used in this work. (Tensorflow r1.3 is the newest stable version; Tensorflow r1.1 is the last version that Tensorflow supports Mac GPU.)

- **macOS** is used in this work.

.. note:: Linux desktop with GPU is highly recommended (Windows OS is not recommended). (Ubuntu is the first choice since it has the largest community support.)

Pre-requisites
--------------

1. `Build tensorflow from source <https://www.tensorflow.org/versions/r1.1/install/install_sources>`_

2. `Build shared library for using the TensorFlow C++ library <https://github.com/FloopCZ/tensorflow_cc>`_

3. `CMake <https://cmake.org/>`_

.. note:: **Archive/Static library** (.a) VS **Shared library** (.so)

         *Archive libraries* (.a) are statically linked i.e when you compile your program with -c option in gcc. So, if there's any change in library, you need to compile and build your code again.

         The advantage of .so (*shared object*) over .a library is that *they are linked during the runtime*, i.e. after creation of your .o file -o option in gcc. So, if there's any change in .so file, you don't need to recompile your main program. But make sure that your main program is linked to the new .so file with in command.

Integrate the model into HTM
----------------------------
Download codebase from GitHub: https://github.com/PharrellWANG/HTM162-Bazel-Cmake

There are two Apps in the above project.

- TAppClassifier
- TAppEncoder

**TAppClassifier** is the skeleton code which can help you understand how to
load graph in C++ and run the prediction using Tensorflow.
It is a self-contained c++ Application which can be built from both
Bazel and CMake.

ResNet engine has been integrated to **TAppEncoder** for
*depth map angular modes [2, 34] prediction* and *the DMM1 searching process*.

For the DMM1 searching process, we are making use of wedgelet slope to reduce
the number of wedgelet candidates to be evaluated in DMM1 searching process.
If top-16 is used, then almost half of the candidates will be skipped.
Hence the time reduction for wedgelet decision shall be reduced roughly by half.

.. note:: If have time, try to estimate the time cost of ResNet size [4, 4, 8, 16], units 3.
            Prediction accuracy will be decreased by 2%~3%. But since flops
            has been reduced from 600k to 130k,
            the speed of prediction in c++ should be faster.

Devices
-------
.. figure:: images/devices.JPG
   :width: 300px
   :alt: Devices

   Devices for this project

Device for Data Processing
~~~~~~~~~~~~~~~~~~~~~~~~~~
- **iMac (21.5-inch 2017)**
- Processor 3GHz Intel Core i5
- Memory 8GB 2400 MHz DDR4

Device for Training Models
~~~~~~~~~~~~~~~~~~~~~~~~~~
- **Macbook Pro (15-inch, Mid 2015)**
- Processor 2.2GHz Intel Core i7
- Memory 16GB 1600MHz DDR3
- Nvidia GTX980, Memory 4GB (External GPU)

Thank you for reading.
