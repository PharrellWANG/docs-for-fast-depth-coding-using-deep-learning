.. _edge-strength-analysis:

Edge Strength Analysis
======================

Motivation originated from experience
-------------------------------------
To know the motivation, first you have to know some experience.

I have tried to train the data by using 37 classes,
including mode [0, 1, 2, ..., 34, DMM1, DMM4]. (2 + 33 + 2 = 37)

Confusion matrix obtained during training process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Confusion matrix provided for downloading.

:download:`Confusion matrix after 10342 steps <csv_files/ckpt-10342.csv>`

:download:`Confusion matrix after 20622 steps <csv_files/ckpt-20622.csv>`

:download:`Confusion matrix after 30757 steps <csv_files/ckpt-30757.csv>`

:download:`Confusion matrix after 40884 steps <csv_files/ckpt-40884.csv>`

:download:`Confusion matrix after 51009 steps <csv_files/ckpt-51009.csv>`

:download:`Confusion matrix after 61168 steps <csv_files/ckpt-61168.csv>`


Statistics
~~~~~~~~~~
1. total train samples: 2900*37

2. Batch size:128

3. 61168*128/2900/37 = 73 epoch

-
 Refer to the **confusing matrix**, after 73 epochs, the model still don’t understand the features of
 mode 0, 1, 35, 36, which possibly means the CNN is not capable of
 learning features for 0, 1, 35, 36.
 Or it can mean my network size is
 not large enough to learn the features inside mode 0, 1, 35, 36.
 Or it can mean CNN is not enough for learn them.
 I think RNN is able to gain much lifting in classification accuracy by taking
 the information related to time into consideration. But due to the limited time,
 i have not tried it yet.

-
 Refer to the **confusing matrix**, the CNN must be able to distinguish between angular modes.


After visualizing the angular modes, the blocks with very weak edges
for each mode are frequently observed. They looks like the planar or DC mode.

I've tried to train the model while the blocks with weak edges are kept in
the training data. Results are not good.

Then it is natural to come to the conclusion that it is not good to mix smooth block with
angular blocks for classification under the confidence that our neural net is
good in the sense of both architecture and hyper params. (The confidence
originated from the high accuracy on CIFAR-10/100 data set, and the conclusion
in the paper of **wide residul network** are verified clearly.)

The conclusion ``smooth regions will trap CNN in ill condition`` is also
found in the journal paper below:

:download:`CU Partition Mode Decision for HEVC Hardwired Intra Encoder Using CNN<papers/[Journal]CU Partition Mode Decision for HEVC Hardwired Intra Encoder Using CNN.pdf>`

So we decided to remove the smooth regions.

When trying to remove the smooth region, we are facing a question:

``How to define the smooth regions?``

Well, see below for the answer.


Algorithm designed for edge analysis
------------------------------------

We can think like this: can we define the sharpness of the edges?

Yes. We can.

Strongly encouraging the readers to check the python codes provided for
downloading below for understanding the algorithm here.

Edge analysis algorithm implemented in python is provided for downloading.

:download:`Edge Analysis in Python<snippets/edge_strength_analysis.py>`


See below for code snippets for a quick sense.

This is how we define the edge strength:

.. code-block:: python

    for each sample (a row) in the collected data set (a csv file):
        feature = the_pixel_data_of_a_square_block_as_a_matrix
            for i in range(width_of_the_block - 1):
                for j in range(width_of_the_block - 1):
                    #calculating the hor and ver strength
                    horizontal_strength = \
                        features[i][j] + \
                        features[i + 1][j] - \
                        features[i][j + 1] - \
                        features[i + 1][j + 1]
                    vertical_strength = \
                        features[i][j] + \
                        features[i][j + 1] - \
                        features[i + 1][j] - \
                        features[i + 1][j + 1]
                    # calculating the power
                    strength = horizontal_strength ** 2 + vertical_strength ** 2
                    # put each strength into an numpy array to get the
                    # total strength of a block (or you can say a line
                    # in the csv file)
                    data = np.append(data, np.array([strength]))
                    total_strength += strength

            assert (data.ndim == 1)

Then calculating top (width*2 && non-zero) average.

.. code-block:: python

            # calculating top (width*2 && non-zero) average.
            # step1: top width*2 values in the numpy arrary
            top_k = data[np.argsort(data)][data.size - RESHAPE * 2:]
            assert (top_k.ndim == 1)
            # step2: non-zero values (because sometimes the edge length can be
            # short. We only want the sharpness. We do not want smooth regions
            # to affect the sharpness.)
            data = top_k[top_k.nonzero()]
            # e.g., [[2, 0], [0, 0]], i exclude it from the concept of sharp
            data = data[np.where(data > 8)]
            # all the strength are zero. (that is to say , it is like DC mode)
            if data.size == 0:
                ave = 0
                data = np.array([0])
            else:
                ave = np.mean(data)
                data = np.array([ave])

            # add ave of the blocks grouping by each mode.
            # calculate the ave by dividing the number of blocks of each mode
