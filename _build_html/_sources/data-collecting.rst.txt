Data Collecting
===============

This document will show you how to collect the data for both training and
testing the deep leaning model.

Path of collected data
----------------------
``/Volumes/XssdPharrell/data_collecting/``

.. figure:: ./images/data-path.png
   :scale: 100 %
   :alt: data path

   A screen capture of the data path.

.. _effort-from-ho:

Effort from Ho
--------------

.. todo:: Add Ho's efforts here. Shall be done before the presentation.


Effort from me
--------------

Modifications
~~~~~~~~~~~~~
Based on the :ref:`effort-from-ho`, I made some modifications to better
facilitate the *model training process*.

**We collect the data by encoding the video sequences.**

When encoding the video sequences, for every block:

- ``if`` DIS has been assigned (where ``DIS_FLAG == 1``), we **skip** it (since none of the conventional intra modes including DMMs will be used). *Skip it* means we don't collect data from it.
- ``else if`` DIS has **not** been assigned (where ``DIS_FLAG == 0``), let's identify the partition mode:

    - ``if`` HTM encoder decides to implement a partition for the block (where ``partition_number == 4`` (NXN)):

        - ``uidepth += 1`` (add 1 to uidepth), let's **collect** data from the four sub-blocks using ``for`` loop (instead of collecting data from the block of size 2NX2N).

    - ``else if`` HTM encoder decides **not** to implement a partition:

        - let's **collect** the ``INTRA_PRED[0]`` along with the **1-D Depth Data**.


.. note:: **1-D Depth Data** means the pixel value of the depth block being **flattened** into 1 dimension. For example, to store an M x N matrix of pixel values (you can imagine those pixels forming an image, hence it is like we are storing an image), the **1-D Depth Data** (pixel values) must contain M*N values, with M rows of N contiguous values each.  That is, the 1-D data must store the matrix as: ``.... row 0 .... .... row 1 .... // ...........  // ... row M-1 ....``

.. attention:: when collecting the data, I have made it to write 35 for mode 37, and 36 for mode 38. Hence a little time/energy is saved for the data processing.

Project
~~~~~~~
Based on the above ideas, I have created a project in Python for pre processing the data.

Anyone can clone the codebase of the project from GitHub. You can view the codes after you obtained your copy.

* Project name: **data-processing-for-fdc**

* GitHub Repository: `data-processing-for-fast-depth-coding <https://github.com/PharrellWANG/data-processing-for-fdc>`_.

* License: `MIT License <https://choosealicense.com/licenses/mit/>`_.
