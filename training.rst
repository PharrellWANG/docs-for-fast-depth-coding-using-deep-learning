Deep Learning
=============

All the models are trained from scratch.

Settings
~~~~~~~~
1. No padding, cropping, flipping applied. No data augmentation applied. The orignal data is distorted enough by nature. See :ref:`data-visu` section to get a taste.
2. Momentum optimizer 0.9.
3. Learning rate schedule: 0.01 (<20k), 0.001 (<40k), 0.0001 (<60k), 0.00001 (else).
4. Weight decay rate: 0.0002.
5. Batch size 128.
6. Filters [16, 16, 32, 64], residual units for last three layers: 5

Training for block size 4x4
---------------------------

Results
~~~~~~~
The model cannot learn well for size 4x4, only top-28 is fine.

.. figure:: images/blk-4--top-20.png
   :width: 720px
   :alt: top 20 accuracy for block size 04x04

   Figure 1.1 Top 20 Accuracy


.. figure:: images/blk-4--top-28.png
   :width: 720px
   :alt: top 28 accuracy for block size 04x04

   Figure 1.2 Top 28 Accuracy


Training for block size 8x8
---------------------------

Results
~~~~~~~
The model indeed can learn something for size 8x8. Top 16 is fine, which can
reduce the angular modes by half.

.. figure:: images/blk-8--top-16.png
   :width: 720px
   :alt: top 16 accuracy for block size 08x08

   Figure 2.1 Top 16 Accuracy