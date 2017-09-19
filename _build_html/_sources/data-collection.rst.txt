Data Collection
===============

This document will show you how to collect the data.

Training Data Source
--------------------
**We collect the data by encoding the video sequences.**

Data are collected from four video sequences.

   +----+-------------------------+------------+-----------------------+--------+
   | #  | Name of the Sequence    | Resolution | Usage                 | Frames |
   +====+=========================+============+=======================+========+
   | 1  | Balloons                |1024x768    | train/test/validation | 300    |
   +----+-------------------------+------------+-----------------------+--------+
   | 2  | kendo                   |1024x768    | train/test/validation | 300    |
   +----+-------------------------+------------+-----------------------+--------+
   | 3  | poznan_street           |1920x1088   | train/test/validation | 250    |
   +----+-------------------------+------------+-----------------------+--------+
   | 4  | undo_dancer             |1920x1088   | train/test/validation | 250    |
   +----+-------------------------+------------+-----------------------+--------+


Method for Collecting the data
------------------------------
Based on the :ref:`effort-from-ho`:

When encoding the video sequences, for every block (of size 4x4, 8x8, 16x16, 32x32, 64x64):

- ``if`` DIS has been assigned (where ``DIS_FLAG == 1``), we **skip** it (since none of the conventional intra modes including DMMs will be used). *Skip it* means we don't collect data from it.
- ``else if`` DIS has **not** been assigned (where ``DIS_FLAG == 0``), let's identify the partition mode:

    - ``if`` HTM encoder decides to implement a partition for the block (where ``partition_number == 4`` (NXN)):

        - **collect** the ``INTRA_PRED[1]``, ``INTRA_PRED[2]``, ``INTRA_PRED[3]``, ``INTRA_PRED[4]`` for each sub parts along with their **1-D Depth Data**.

    - ``else if`` HTM encoder decides **not** to implement a partition:

        - let's **collect** the ``INTRA_PRED[0]`` along with the **1-D Depth Data**.


.. note::

      1. **1-D Depth Data** means the pixel value of the depth block being **flattened** into 1 dimension. For example, to store an M x N matrix of pixel values (you can imagine those pixels forming an image, hence it is like we are storing an image), the **1-D Depth Data** (pixel values) must contain M*N values, with M rows of N contiguous values each.  That is, the 1-D data must store the matrix as: ``.... row 0 .... .... row 1 .... // ...........  // ... row M-1 ....``

      2. when collecting the data, I have made it to write 35 for mode 37, and 36 for mode 38. Hence a little time/energy is saved for the data processing.


.. _effort-from-ho:

Effort from Ho
--------------

The pdf file contributed by Ho are provided for downloading.

:download:`20170621 Fast Depth Coding Via TensorFlow (Data Collection) v1 <pdf_files/effort_ho.pdf>`
