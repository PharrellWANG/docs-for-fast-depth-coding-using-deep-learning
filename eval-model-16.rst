Model trained from blocks of size 16x16
=======================================

.. note:: This model is trained using the data of size 16x16. But the
            evaluation results clearly proved: this model is applicable to
            size 32x32 and size 64x64 by using Bilinear Interpolation to do
            resizing for the larger blocks.

**Statistics**

   +----+-------------------+------------+
   | 1  | global step       |304857      |
   +----+-------------------+------------+
   | 2  | batch size        |128         |
   +----+-------------------+------------+
   | 3  | samples each class|3075        |
   +----+-------------------+------------+
   | 4  | number of classes |32          |
   +----+-------------------+------------+
   | 5  | training time     |11h 47m 50s |
   +----+-------------------+------------+
   | 6  | epoch             |396         |
   +----+-------------------+------------+

**Epoch calculating**

.. code-block:: python

    >>> 304857*128/3075/32.0
    396.53125

Using blocks of size 16x16
==========================
Model Performance on Validating Dataset
---------------------------------------
Evaluation batch size 100, number of batches 192.

Using validating dataset, the details are documented below:

    +----+-----------------+---------------+
    | 0.1| Name of dataset | val_16x16.csv |
    +----+-----------------+---------------+
    | 0.2| Size of dataset | 15.6 MB       |
    +----+-----------------+---------------+
    | 0.3| Samples         | 600*32        |
    +----+-----------------+---------------+
    | 0.4| Usage of dataset| validation    |
    +----+-----------------+---------------+
    | 1  | top  5 accuracy | 0.801         |
    +----+-----------------+---------------+
    | 2  | top  6 accuracy | 0.842         |
    +----+-----------------+---------------+
    | 3  | top  7 accuracy | 0.873         |
    +----+-----------------+---------------+
    | 4  | top  8 accuracy | 0.895         |
    +----+-----------------+---------------+
    | 5  | top  9 accuracy | 0.912         |
    +----+-----------------+---------------+
    | 6  | top 10 accuracy | 0.924         |
    +----+-----------------+---------------+
    | 7  | top 11 accuracy | 0.934         |
    +----+-----------------+---------------+
    | 8  | top 12 accuracy | 0.942         |
    +----+-----------------+---------------+
    | 9  | top 16 accuracy | 0.965         |
    +----+-----------------+---------------+
    | 10 | top 17 accuracy | 0.970         |
    +----+-----------------+---------------+
    | 11 | top 18 accuracy | 0.974         |
    +----+-----------------+---------------+
    | 12 | top 19 accuracy | 0.977         |
    +----+-----------------+---------------+
    | 13 | top 20 accuracy | 0.980         |
    +----+-----------------+---------------+
    | 14 | top 28 accuracy | 0.995         |
    +----+-----------------+---------------+

Model Performance on Testing Dataset
------------------------------------
Evaluation batch size 100, number of batches 192.

Using testing dataset, the details are documented below:

    +----+-----------------+---------------+
    | 0.1| Name of dataset | test_16x16.csv|
    +----+-----------------+---------------+
    | 0.2| Size of dataset | 15.9 MB       |
    +----+-----------------+---------------+
    | 0.3| Samples         | 600*32        |
    +----+-----------------+---------------+
    | 0.4| Usage of dataset| test          |
    +----+-----------------+---------------+
    | 1  | top  5 accuracy | 0.739         |
    +----+-----------------+---------------+
    | 2  | top  6 accuracy | 0.794         |
    +----+-----------------+---------------+
    | 3  | top  7 accuracy | 0.829         |
    +----+-----------------+---------------+
    | 4  | top  8 accuracy | 0.859         |
    +----+-----------------+---------------+
    | 5  | top  9 accuracy | 0.877         |
    +----+-----------------+---------------+
    | 6  | top 10 accuracy | 0.894         |
    +----+-----------------+---------------+
    | 7  | top 11 accuracy | 0.911         |
    +----+-----------------+---------------+
    | 8  | top 12 accuracy | 0.924         |
    +----+-----------------+---------------+
    | 9  | top 16 accuracy | 0.958         |
    +----+-----------------+---------------+
    | 10 | top 17 accuracy | 0.963         |
    +----+-----------------+---------------+
    | 11 | top 18 accuracy | 0.970         |
    +----+-----------------+---------------+
    | 12 | top 19 accuracy | 0.974         |
    +----+-----------------+---------------+
    | 13 | top 20 accuracy | 0.977         |
    +----+-----------------+---------------+
    | 14 | top 28 accuracy | 0.995         |
    +----+-----------------+---------------+

Using blocks of size 32x32
==========================

We have tried four resizing method:

1. `Bilinear interpolation <https://en.wikipedia.org/wiki/Bilinear_interpolation>`_.

2. `Nearest neighbor interpolation <https://en.wikipedia.org/wiki/Nearest-neighbor_interpolation>`_.

3. `Bicubic interpolation <https://en.wikipedia.org/wiki/Bicubic_interpolation>`_.

4. Area interpolation.

.. note:: All the data for size 32x32 after pre-processing are used for
            evaluation. We just named it as ``val_32x32.csv``,
            no need for anther ``test_32x32.csv``.


Evaluation batch size 100, number of batches 192.

Performance with Bilinear Interpolation
---------------------------------------

Using validating dataset, with Bilinear interpolation,
the details are documented below:

    +----+-----------------+---------------+
    | 0.1| Name of dataset | val_32x32.csv |
    +----+-----------------+---------------+
    | 0.2| Size of dataset | 104.9 MB      |
    +----+-----------------+---------------+
    | 0.3| Samples         | 872*32        |
    +----+-----------------+---------------+
    | 0.4| Usage of dataset| validate&test |
    +----+-----------------+---------------+
    | 1  | top  5 accuracy | 0.812         |
    +----+-----------------+---------------+
    | 2  | top  6 accuracy | 0.855         |
    +----+-----------------+---------------+
    | 3  | top  7 accuracy | 0.887         |
    +----+-----------------+---------------+
    | 4  | top  8 accuracy | 0.908         |
    +----+-----------------+---------------+
    | 5  | top  9 accuracy | 0.924         |
    +----+-----------------+---------------+
    | 6  | top 10 accuracy | 0.936         |
    +----+-----------------+---------------+
    | 7  | top 11 accuracy | 0.946         |
    +----+-----------------+---------------+
    | 8  | top 12 accuracy | 0.954         |
    +----+-----------------+---------------+
    | 9  | top 16 accuracy | 0.972         |
    +----+-----------------+---------------+
    | 10 | top 17 accuracy | 0.976         |
    +----+-----------------+---------------+
    | 11 | top 18 accuracy | 0.979         |
    +----+-----------------+---------------+
    | 12 | top 19 accuracy | 0.982         |
    +----+-----------------+---------------+
    | 13 | top 20 accuracy | 0.984         |
    +----+-----------------+---------------+
    | 14 | top 28 accuracy | 0.996         |
    +----+-----------------+---------------+

Performance with Nearest Neighbor Interpolation
-----------------------------------------------

Almost the same performance as using Linear Interpolation!
Omitted here for clarity.

Performance with Bicubic Interpolation
--------------------------------------

Almost the same performance as using Linear Interpolation!
Omitted here for clarity.

Performance with Area Interpolation
-----------------------------------

Almost the same performance as using Linear Interpolation!
Omitted here for clarity.

Using blocks of size 64x64
==========================

Based on the observations of the testing results of block size 32x32, we believe there should not be such differences among different interpolation method.

Here we only use **Bilinear Interpolation**.

Performance with Bilinear Interpolation
---------------------------------------

Using validating dataset, with Bilinear interpolation,
the details are documented below:

Total samples: 1728

.. code-block:: python

    >>> 54*32
    1728

Evaluation batch size 100, number of batches 17.


    +----+-----------------+---------------+
    | 0.1| Name of dataset | val_64x64.csv |
    +----+-----------------+---------------+
    | 0.2| Size of dataset | 24.5 MB       |
    +----+-----------------+---------------+
    | 0.3| Samples         | 54*32         |
    +----+-----------------+---------------+
    | 0.4| Usage of dataset| validate&test |
    +----+-----------------+---------------+
    | 1  | top  5 accuracy | 0.764         |
    +----+-----------------+---------------+
    | 2  | top  6 accuracy | 0.821         |
    +----+-----------------+---------------+
    | 3  | top  7 accuracy | 0.868         |
    +----+-----------------+---------------+
    | 4  | top  8 accuracy | 0.892         |
    +----+-----------------+---------------+
    | 5  | top  9 accuracy | 0.916         |
    +----+-----------------+---------------+
    | 6  | top 10 accuracy | 0.932         |
    +----+-----------------+---------------+
    | 7  | top 11 accuracy | 0.946         |
    +----+-----------------+---------------+
    | 8  | top 12 accuracy | 0.956         |
    +----+-----------------+---------------+
    | 9  | top 16 accuracy | 0.973         |
    +----+-----------------+---------------+
    | 10 | top 17 accuracy | 0.979         |
    +----+-----------------+---------------+
    | 11 | top 18 accuracy | 0.982         |
    +----+-----------------+---------------+
    | 12 | top 19 accuracy | 0.984         |
    +----+-----------------+---------------+
    | 13 | top 20 accuracy | 0.987         |
    +----+-----------------+---------------+
    | 14 | top 28 accuracy | 0.994         |
    +----+-----------------+---------------+