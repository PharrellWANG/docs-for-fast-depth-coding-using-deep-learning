.. _data-visu:

Data Visualization
==================

In the python project for pre-processing the data, which is `data-processing-for-fast-depth-coding <https://github.com/PharrellWANG/data-processing-for-fdc>`_, you can visualize the collected data by typing commands from terminal:

.. code-block:: python

   python data_visu/visualize_blocks.py --block_size=32 --mode=2


.. _figure0-0:
.. figure:: ./images/running_visu.png
   :scale: 50 %
   :alt: running visu
   :align: center

   Figure 0-0. running the visualization

:ref:`figure0-1` and :ref:`figure0-2` are **the illustrations of Intra modes in HEVC** in case you want to refresh your memory. (DMMs are not illustrated here).

Other figures are **the visualization of some collected data**.

.. note::  Posting all the visualization images here would be possibly overwhelming and unnecessary. However, if you want to see all the visualizations, that is also doable (by spending a *little* more time running the python script then capturing screen). Please just let me know if there's a need :D

.. important::
   Please compare :ref:`figure2-2` with :ref:`figure2-34`. Compare the two blocks in red circle. You should be able to find the patterns are very similar to each other while their modes are totally different. This is the reason why we need to use TOP-5 accuracy instead of TOP-1 for evaluating the machine learning model.

   .. glossary::

   TOP-5
      To compare models, we examine how often the model fails to predict the correct answer as one of their top 5 guesses -- termed "top-5 error rate".

.. how to use term: ======>>> :term: asdf; asdfasd

.. tip:: Feel free to click on the figures for inspecting their features carefully by enlarging or downloading. They are licensed under `MIT License <https://choosealicense.com/licenses/mit/>`_.


Intra modes in HEVC
-------------------

.. _figure0-1:
.. figure:: ./images/mode_dirs.png
   :scale: 25 %
   :alt: size8_mode0
   :align: center

   Figure 0-1. Illustration of Intra modes [0, 34]

.. _figure0-2:
.. figure:: ./images/mode_dirs_b.png
   :scale: 30 %
   :alt: size8_mode0
   :align: center

   Figure 0-2. Examples of 8x8 luma prediction blocks generated with all the HEVC intra prediction modes.


Examples for block size 8x8
---------------------------

.. figure:: ./images/size_8/size8_mode0.png
   :scale: 100 %
   :alt: size8_mode0
   :align: center

   Figure 1-0. Intra Mode: 0, Block Size: 8x8

.. figure:: ./images/size_8/size8_mode1.png
   :scale: 100 %
   :alt: size8_mode1
   :align: center

   Figure 1-1. Intra Mode: 1, Block Size: 8x8

.. figure:: ./images/size_8/size8_mode2.png
   :scale: 100 %
   :alt: size8_mode2
   :align: center

   Figure 1-2. Intra Mode: 2, Block Size: 8x8

.. figure:: ./images/size_8/size8_mode3.png
   :scale: 100 %
   :alt: size8_mode3
   :align: center

   Figure 1-3. Intra Mode: 3, Block Size: 8x8

.. figure:: ./images/size_8/size8_mode4.png
   :scale: 100 %
   :alt: size8_mode4
   :align: center

   Figure 1-4. Intra Mode: 4, Block Size: 8x8

.. figure:: ./images/size_8/size8_mode5.png
   :scale: 100 %
   :alt: size8_mode5
   :align: center

   Figure 1-5. Intra Mode: 5, Block Size: 8x8

.. figure:: ./images/size_8/size8_mode6.png
   :scale: 100 %
   :alt: size8_mode6
   :align: center

   Figure 1-6. Intra Mode: 6, Block Size: 8x8

.. figure:: ./images/size_8/size8_mode7.png
   :scale: 100 %
   :alt: size8_mode7
   :align: center

   Figure 1-7. Intra Mode: 7, Block Size: 8x8

.. figure:: ./images/size_8/size8_mode33.png
   :scale: 100 %
   :alt: size8_mode33
   :align: center

   Figure 1-33. Intra Mode: 33, Block Size: 8x8

.. figure:: ./images/size_8/size8_mode35.png
   :scale: 100 %
   :alt: size8_mode35
   :align: center

   Figure 1-35. Intra Mode: 35, Block Size: 8x8

.. figure:: ./images/size_8/size8_mode36.png
   :scale: 100 %
   :alt: size8_mode36
   :align: center

   Figure 1-36. Intra Mode: 36, Block Size: 8x8

Examples for block size 16x16
-----------------------------

.. figure:: ./images/size_16/size16_mode0.png
   :scale: 100 %
   :alt: size16_mode0
   :align: center

   Figure 2-0. Intra Mode: 0, Block Size: 16x16

.. figure:: ./images/size_16/size16_mode1.png
   :scale: 100 %
   :alt: size16_mode1
   :align: center

   Figure 2-1. Intra Mode: 1, Block Size: 16x16

.. _figure2-2:
.. figure:: ./images/size_16/size16_mode2.png
   :scale: 100 %
   :alt: size16_mode2
   :align: center

   Figure 2-2. Intra Mode: 2, Block Size: 16x16

.. figure:: ./images/size_16/size16_mode3.png
   :scale: 100 %
   :alt: size16_mode3
   :align: center

   Figure 2-3. Intra Mode: 3, Block Size: 16x16

.. _figure2-34:
.. figure:: ./images/size_16/size16_mode34.png
   :scale: 100 %
   :alt: size16_mode34
   :align: center

   Figure 2-34. Intra Mode: 34, Block Size: 16x16

Examples for block size 32x32
-----------------------------

.. figure:: ./images/size_32/size32_mode0.png
   :scale: 100 %
   :alt: size32_mode0
   :align: center

   Figure 3-0. Intra Mode: 0, Block Size: 32x32

.. figure:: ./images/size_32/size32_mode1.png
   :scale: 100 %
   :alt: size32_mode1
   :align: center

   Figure 3-1. Intra Mode: 1, Block Size: 32x32

.. figure:: ./images/size_32/size32_mode2.png
   :scale: 100 %
   :alt: size32_mode2
   :align: center

   Figure 3-2. Intra Mode: 2, Block Size: 32x32

.. figure:: ./images/size_32/size32_mode3.png
   :scale: 100 %
   :alt: size32_mode3
   :align: center

   Figure 3-3. Intra Mode: 3, Block Size: 32x32

.. figure:: ./images/size_32/size32_mode30.png
   :scale: 100 %
   :alt: size32_mode30
   :align: center

   Figure 3-30. Intra Mode: 30, Block Size: 32x32

.. figure:: ./images/size_32/size32_mode33.png
   :scale: 100 %
   :alt: size32_mode33
   :align: center

   Figure 3-33. Intra Mode: 33, Block Size: 32x32

.. figure:: ./images/size_32/size32_mode34.png
   :scale: 100 %
   :alt: size32_mode34
   :align: center

   Figure 3-34. Intra Mode: 34, Block Size: 32x32

.. figure:: ./images/size_32/size32_mode35.png
   :scale: 100 %
   :alt: size32_mode35
   :align: center

   Figure 3-35. Intra Mode: 35, Block Size: 32x32

.. figure:: ./images/size_32/size32_mode36.png
   :scale: 100 %
   :alt: size32_mode36
   :align: center

   Figure 3-36. Intra Mode: 36, Block Size: 32x32

Examples for block size 64x64
-----------------------------

.. figure:: ./images/size_64/size64_mode0.png
   :scale: 100 %
   :alt: size64_mode0
   :align: center

Figure 4-0. Intra Mode: 0, Block Size: 64x64

.. figure:: ./images/size_64/size64_mode1.png
   :scale: 100 %
   :alt: size64_mode1
   :align: center

Figure 4-1. Intra Mode: 1, Block Size: 64x64

.. figure:: ./images/size_64/size64_mode2.png
   :scale: 100 %
   :alt: size64_mode2
   :align: center

Figure 4-2. Intra Mode: 2, Block Size: 64x64

.. figure:: ./images/size_64/size64_mode3.png
   :scale: 100 %
   :alt: size64_mode3
   :align: center

Figure 4-3. Intra Mode: 3, Block Size: 64x64

.. figure:: ./images/size_64/size64_mode4.png
   :scale: 100 %
   :alt: size64_mode4
   :align: center

Figure 4-4. Intra Mode: 4, Block Size: 64x64

.. figure:: ./images/size_64/size64_mode5.png
   :scale: 100 %
   :alt: size64_mode5
   :align: center

Figure 4-5. Intra Mode: 5, Block Size: 64x64

.. figure:: ./images/size_64/size64_mode32.png
   :scale: 100 %
   :alt: size64_mode32
   :align: center

Figure 4-32. Intra Mode: 32, Block Size: 64x64

.. figure:: ./images/size_64/size64_mode33.png
   :scale: 100 %
   :alt: size64_mode33
   :align: center

Figure 4-33. Intra Mode: 33, Block Size: 64x64

.. figure:: ./images/size_64/size64_mode34.png
   :scale: 100 %
   :alt: size64_mode34
   :align: center

Figure 4-34. Intra Mode: 34, Block Size: 64x64
