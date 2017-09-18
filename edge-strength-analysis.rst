.. _edge-strength-analysis:

Edge Strength Analysis
======================

Motivation
----------
To know the motivation, first you have to know some experience.

My Experience on training model for intra mode classification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
First, I have tried to train the data by using 37 classes,
including mode [0, 1, 2, ..., 34, DMM1, DMM4].

2 + 33 + 2 = 37

total train samples: 2900*37

Batch size:128

61168*128/2900/37 = 73 epoch

After 73 epochs, the model still don’t understand the features of
mode 0, 1, 35, 36, which possibly means the CNN is not capable of
learning features for 0, 1, 35, 36.
Or it can mean my network size is
not large enough to learn the features inside mode 0, 1, 35, 36.
Or it can mean CNN is not enough for learn them.
I think RNN is able to gain much lifting in classification accuracy by taking
the information related to time into consideration. But due to the limited time,
i have not tried it yet.

Refer to the **confusing matrix**, the CNN must be able to distinguish between angular modes.

Confusion matrix provided for downloading.

:download:`Confusion matrix after 10342 steps <csv_files/ckpt-10342.csv>`

:download:`Confusion matrix after 20622 steps <csv_files/ckpt-20622.csv>`

:download:`Confusion matrix after 30757 steps <csv_files/ckpt-30757.csv>`

:download:`Confusion matrix after 40884 steps <csv_files/ckpt-40884.csv>`

:download:`Confusion matrix after 51009 steps <csv_files/ckpt-51009.csv>`

:download:`Confusion matrix after 61168 steps <csv_files/ckpt-61168.csv>`

Second, after visualizing the angular modes, the blocks with very weak edges
for each mode are frequently observed. They looks like the planar or DC mode.

I've tried to train them with the weak edges blocks kept. But results
are not good.

Then we come to the conclusion that it is not good to mix smooth block with
angular blocks for classification.

The conclusion ``smooth regions will trap CNN in ill condition`` is also
found in the journal paper below:

:download:`CU Partition Mode Decision for HEVC Hardwired Intra Encoder Using CNN<papers/[Journal]CU Partition Mode Decision for HEVC Hardwired Intra Encoder Using CNN.pdf>`

So i decided to remove the smooth regions.

When trying to remove the smooth region, we are facing a question:

``How to define the smooth regions?``

We can think like this: can we define how to define the sharpness of the edges?
