How to Obtain BD-BR & BD-PSNR
=============================

PSNR and bitrate are two important metrics to obtain the BDBR, BDPSNR which
are two common criteria for measuring the average PSNR differences between
RD-curves.

**step 1**

use ``TAppRenderer`` to synthesize intermediate views using

    - original YUVs
    - (four QPs) the YUVs obtained by your method
    - (four QPs) the YUVs obtained by standard method (or any other method that you want to compare with)

separately.

**step 2**

1. (four QPs) Calculate PSNR using [synthesized_views_from_origin, synthesized_views_from_your_method]
2. (four QPs) Calculate PSNR using [synthesized_views_from_origin, synthesized_views_from_ref_method]

**step 3**

calculate BD-BR, BD-PSNR for each sequence.