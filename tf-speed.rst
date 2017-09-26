Time Cost of Tensorflow in C++
==============================

Motivation
----------

When using Tensorflow(TF) C++ APIs, if you want to run the prediction,
you have to call ``session->Run()``. (When you call the ``session->Run()``,
TF will initialize a session and run the prediction in that session for you.)

We want to know the time cost of ``session->Run()``, since initializing
1 session for 1 block is easier to implement in HTM (It has already
been implemented). But that can be expensive when we talk about time
cost. See experiments for details.

Experiments
-----------

Here we present the experiments for evaluating the time cost
of ``session->Run()``.

Now we want to run predictions for blocks of size 8x8 from a frame in one video sequence.

Total 12288 predictions. (``1024/8*768/8=12288``)

Here we have two choices:

1. Running all samples from one video frame in one session (:ref:`figure1`)
2. Running one sample in one session ((:ref:`figure2`))

.. _figure1:
.. figure:: ./images/session_one.png
   :scale: 30 %
   :alt: session_one
   :align: center

   Figure 1. Running all samples in one session

.. _figure2:
.. figure:: ./images/session_many.png
   :scale: 30 %
   :alt: session_many
   :align: center

   Figure 2. Running one sample in one session

Look at the time cost.

   +----+----------------------------------------+------------+---------------------------------+
   | #  | Scenario                               | Time Cost  | the difficulty of implementation|
   +====+========================================+============+=================================+
   | 1  | Init one  session  for many block      |   21.37 s  |   not easy                      |
   +----+----------------------------------------+------------+---------------------------------+
   | 2  | Init many sessions for many blocks     |   47.81 s  |   easy                          |
   +----+----------------------------------------+------------+---------------------------------+


Conclusions
-----------

Running 1 sample in 1 session is much easier to implement. But the time cost will be *more than doubled*.
