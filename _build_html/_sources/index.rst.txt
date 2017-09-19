.. Fast Depth Coding Using Deep Learning documentation master file, created by
   sphinx-quickstart on Thu Aug 17 10:24:42 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Fast Intra Coding for both texture and depth Using Deep Learning
================================================================

**Fast Intra Coding for both texture and depth Using Deep Learning** is
the thesis topic. The details of the implementation are documented here
for reference. (We are targeting **3D-HEVC**)

This documentation is organized into a couple sections:

* :ref:`proposed-algorithm`
* :ref:`data-processing`
* :ref:`model-training`
* :ref:`model-testing`
* :ref:`codec-integration`
* :ref:`quick-memo`

.. _proposed-algorithm:

.. toctree::
   :maxdepth: 3
   :caption: Proposed Algorithm

   proposed-algorithm

.. _data-processing:

.. toctree::
   :maxdepth: 3
   :caption: Data Processing

   data-collection
   data-statistics
   data-visu
   edge-strength-analysis

.. _model-training:

.. toctree::
   :maxdepth: 2
   :caption: Model Training

   training


.. _model-testing:

.. toctree::
   :maxdepth: 2
   :caption: Model Evaluating

   eval-model-08
   eval-model-16


.. _codec-integration:

.. toctree::
   :maxdepth: 2
   :caption: HTM Codec Integration

   integration

.. _quick-memo:

.. toctree::
   :maxdepth: 2
   :caption: Quick Memo

   quick-memo



