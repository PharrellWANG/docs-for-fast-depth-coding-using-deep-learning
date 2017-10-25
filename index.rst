.. Fast Depth Coding Using Deep Learning documentation master file, created by
   sphinx-quickstart on Thu Aug 17 10:24:42 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Fast Depth Coding Using Deep Learning
=====================================

**Fast Depth Coding Using Deep Learning** is the thesis topic.
The details of the implementation are documented here for reference.

This documentation is organized into a couple sections:

* :ref:`proposed-algorithm`
* :ref:`data-processing`
* :ref:`model-training`
* :ref:`model-testing`
* :ref:`codec-integration`
* :ref:`simulation-results`
* :ref:`references`

.. _proposed-algorithm:

.. toctree::
   :maxdepth: 1
   :caption: Propose the Algorithm

   proposed-algorithm

.. _data-processing:

.. toctree::
   :maxdepth: 1
   :caption: Pre-process the Data

   data-collection
   data-statistics
   data-visu
   edge-strength-analysis

.. _model-training:

.. toctree::
   :maxdepth: 1
   :caption: Train the Model

   training

.. _model-testing:

.. toctree::
   :maxdepth: 1
   :caption: Evaluate the Model

   eval-model-08
   eval-model-16

.. _codec-integration:

.. toctree::
   :maxdepth: 1
   :caption: Use the Learned Model

   tf-speed
   integration

.. _simulation-results:

.. toctree::
   :maxdepth: 1
   :caption: Simulation Results

   simu-results.rst

.. _quick-memo:

.. toctree::
   :maxdepth: 1
   :caption: Appendices

   debug-release
   GPU
   thesis-related
   how-to-write-thesis
   bd-br-bd-psnr

.. _references:
.. toctree::
   :maxdepth: 1
   :caption: References

   refs.rst