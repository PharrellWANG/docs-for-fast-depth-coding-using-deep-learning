About GPU
=========

NVIDIA vs AMD
-------------

For machine learning, just two words: choose NVIDIA.

GPU-Accelerated Computing
-------------------------
NVDIA has a good explanation about
`What is GPU-Accelerated Computing <http://www.nvidia.com/object/what-is-gpu-computing.html>`_.

In summary, GPU-accelerated computing offloads compute-intensive portions of
the application to the GPU, while the remainder of the code still runs
on the CPU. From a user's perspective, applications simply run much faster.

Performance
-----------
There is a video (length: 1m 33s)
`GPU VS CPU <https://www.youtube.com/watch?v=-P28LKWTzrI&feature=youtu.be>`_.
It might have been exaggerated for marketing purpose. However the acceleration
provided by GPU is something that you cannot deny/ignore if you are
doing serious work using deep learning.

Time Saving for Training
~~~~~~~~~~~~~~~~~~~~~~~~
The speed of acceleration for training a deep neural network depends
on the GPU model.

According to my experience, typically the training process will be
accelerated 4~6 times with NVIDIA GTX980 if you are training a 50
layer Convolutional Neural Network.


Time Saving for Prediction
~~~~~~~~~~~~~~~~~~~~~~~~~~
I've documented the prediction acceleration in :ref:`Time-Cost-Analysis`.
Please check it out.

Here's a quick note (prediction using CPU ``Intel Quad-Core i7`` vs GPU ``NVIDIA GTX980``):

    +--------------------------+--------------+
    | Intel Quad-Core i7 (CPU) |   15.56 s    |
    +--------------------------+--------------+
    | NVIDIA GTX 980  (GPU)    |   2.03 s     |
    +--------------------------+--------------+

CUDA and cuDNN
--------------
NVIDIA Official Blog has a good explanation about
`What is CUDA <https://blogs.nvidia.com/blog/2012/09/10/what-is-cuda-2/>`_.

.. note:: CUDA is a parallel computing platform and programming model that
            makes using a GPU for general purpose computing simple and elegant.
            The developer still programs in the familiar C, C++, Fortran, or an
            ever expanding list of supported languages, and incorporates extensions
            of these languages in the form of a few basic keywords. These keywords let
            the developer express massive amounts of parallelism and direct the compiler to
            the portion of the application that maps to the GPU.

CUDA stands for Compute Unified Device Architecture developed by Nvidia .
In CUDA basic idea is to use GPU (Graphical Processing Unit) for parallel
programming which provides better performance for solving complex problems.

- CUDA : the API/language you talk to Nvidia GPUs.

- cuDNN: library for Deep Learning using CUDA.

You could use CUDA/cuDNN directly yourself, but other libraries like TensorFlow
already have built abstractions backed by cuDNN. Tensorflow will handle the
device assignments for you as long as you provide a little configurations
by writing a few lines of codes.

Computation Capabilities of CUDA GPUs
-------------------------------------

Readers may refer to `CUDA GPUs <https://developer.nvidia.com/cuda-gpus>`_ to
know the computation capability of each type of CUDA GPUs.

In short, The high-end GPU models such as **Tesla P series** will be suitable for
**data centre**; **Tesla K series** will be suitable for **work station**.
**Geforce series** will have some entertainment elements inside the design.
**Tesla series** is recommended while Geforce is not recommended if you are
not going to play video games.
