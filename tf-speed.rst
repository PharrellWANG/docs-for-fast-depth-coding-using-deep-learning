Time Cost of TF in C++
======================

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

Session Run
~~~~~~~~~~~

Here we have two choices:

1. Running all samples from one video frame in one session (:ref:`figure1`)
2. Running one sample in one session (:ref:`figure2`)

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
   | 1  | Init one  session  for many block      |   21.37 s  |   not intuitive                 |
   +----+----------------------------------------+------------+---------------------------------+
   | 2  | Init many sessions for many blocks     |   47.81 s  |   intuitive                     |
   +----+----------------------------------------+------------+---------------------------------+


Session Run with AVX, AVX2, SSE4.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here we have two choices:

1. Running all samples from one video frame in one session (:ref:`figure3`)
2. Running one sample in one session (:ref:`figure4`)

.. _figure3:
.. figure:: ./images/cpu_session_one.png
   :scale: 30 %
   :alt: gpu_session_one
   :align: center

   Figure 3. Running all samples in one session

.. _figure4:
.. figure:: ./images/cpu_session_many.png
   :scale: 30 %
   :alt: gpu_session_many
   :align: center

   Figure 4. Running one sample in one session

Look at the time cost.

   +----+----------------------------------------+------------+---------------------------------+
   | #  | Scenario                               | Time Cost  | the difficulty of implementation|
   +====+========================================+============+=================================+
   | 1  | Init one  session  for many block      |   15.56 s  |   not intuitive                 |
   +----+----------------------------------------+------------+---------------------------------+
   | 2  | Init many sessions for many blocks     |   33.91 s  |   intuitive                     |
   +----+----------------------------------------+------------+---------------------------------+


Session Run with AVX, AVX2, SSE4.2 and GPU Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here we have two choices:

1. Running all samples from one video frame in one session (:ref:`figure5`)
2. Running one sample in one session (:ref:`figure6`)

.. _figure5:
.. figure:: ./images/gpu_session_one.png
   :scale: 30 %
   :alt: gpu_session_one
   :align: center

   Figure 5. Running all samples in one session

.. _figure6:
.. figure:: ./images/gpu_session_many.png
   :scale: 30 %
   :alt: gpu_session_many
   :align: center

   Figure 6. Running one sample in one session

Look at the time cost.

   +----+----------------------------------------+------------+---------------------------------+
   | #  | Scenario                               | Time Cost  | the difficulty of implementation|
   +====+========================================+============+=================================+
   | 1  | Init one  session  for many block      |  **2.03** s|   not intuitive                 |
   +----+----------------------------------------+------------+---------------------------------+
   | 2  | Init many sessions for many blocks     |   55.26 s  |   intuitive                     |
   +----+----------------------------------------+------------+---------------------------------+


Conclusions
-----------

Fastest way: Run a large batch of predictions in a single session using GPU.
