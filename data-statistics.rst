Data Statistics
===============

After encoding the sequences, we obtained size 4x4, 8x8, 16x16, 32x32 and 64x64 for each sequence.

Then we do the merging. i.e.,

1. Merge the data of block size 4x4 from four sequences together.

2. Merge the data of block size 8x8 from four sequences together.

3. Merge the data of block size 16x16 from four sequences together.

4. Merge the data of block size 32x32 from four sequences together.

5. Merge the data of block size 64x64 from four sequences together.

After merging, we obtained five csv files:

   +----+-------------------+------------+-----------+-----------+
   | #  | Name of the Files | Size       | Samples   | Usage     |
   +====+===================+============+===========+===========+
   | 1  | size_04.csv       |206.7 MB    | 3675428   | train     |
   +----+-------------------+------------+-----------+-----------+
   | 2  | size_08.csv       |513.6 MB    | 2372324   | train     |
   +----+-------------------+------------+-----------+-----------+
   | 3  | size_16.csv       |1.25  GB    | 1439773   | train     |
   +----+-------------------+------------+-----------+-----------+
   | 4  | size_32.csv       |2.02  GB    | 567554    | train     |
   +----+-------------------+------------+-----------+-----------+
   | 5  | size_64.csv       |1.85  GB    | 125141    | train     |
   +----+-------------------+------------+-----------+-----------+


Mode distribution data after merging are provided for downloading as text format.

:download:`mode distribution of block size 04x04 <txt_files/size_04.txt>`

:download:`mode distribution of block size 08x08 <txt_files/size_08.txt>`

:download:`mode distribution of block size 16x16 <txt_files/size_16.txt>`

:download:`mode distribution of block size 32x32 <txt_files/size_32.txt>`

:download:`mode distribution of block size 64x64 <txt_files/size_64.txt>`

Remove mode 0, 1, 34, 35, 36. We only do deep learning for angular modes. Mode 34 is removed because i believe mode 34 has the same direction feature as mode 2.

After removing 0, 1, 34, 35, 36:

   +----+-------------------+------------+-----------+-----------+
   | #  | Name of the Files | Size       | Samples   | Usage     |
   +====+===================+============+===========+===========+
   | 1  |  m_size_04.csv    |75.7  MB    | 1335970   | train     |
   +----+-------------------+------------+-----------+-----------+
   | 2  |  m_size_08.csv    |130.8 MB    | 600187    | train     |
   +----+-------------------+------------+-----------+-----------+
   | 3  |  m_size_16.csv    |377.3 MB    | 430302    | train     |
   +----+-------------------+------------+-----------+-----------+
   | 4  |  m_size_32.csv    |708.7 GB    | 195943    | train     |
   +----+-------------------+------------+-----------+-----------+
   | 5  |  m_size_64.csv    |1.37  GB    | 92034     | train     |
   +----+-------------------+------------+-----------+-----------+

Percentage of non-angular-removed data:

size  4: (3675428 - 1335970) / 3675428.0 = 0.64

size  8: (2372324 - 600187) / 2372324.0 = 0.74

size 16: (1439773 - 430302) / 1439773.0 = 0.70

size 32: (567554 - 195943) / 567554.0 = 0.65

size 64: (125141 - 92034) / 125141.0 = 0.26

The mode distribution data are provided for downloading.

:download:`mode distribution of block size 04x04 AFTER non-angular removing <txt_files/non_ang_removed_size_04.txt>`

:download:`mode distribution of block size 08x08 AFTER non-angular removing <txt_files/non_ang_removed_size_08.txt>`

:download:`mode distribution of block size 16x16 AFTER non-angular removing <txt_files/non_ang_removed_size_16.txt>`

:download:`mode distribution of block size 32x32 AFTER non-angular removing <txt_files/non_ang_removed_size_32.txt>`

:download:`mode distribution of block size 64x64 AFTER non-angular removing <txt_files/non_ang_removed_size_64.txt>`


Perform :ref:`edge-strength-analysis` for each block sample of all sizes. Observing the histogram distribution.

Flat regions will trap CNN into ill condition. I decided to remove the regions where the edge strength is under 50.

And for the blocks where the edge strength is above 25000, we only consider four modes: VER, HOR, Wedgelet, Contour.

After removing the smooth areas,

   +----+-------------------+------------+-----------+-----------+
   | #  | Name of the Files | Size       | Samples   | Usage     |
   +====+===================+============+===========+===========+
   | 1  | sm_size_04.csv    |75.7  MB    | 1335970   | train     |
   +----+-------------------+------------+-----------+-----------+
   | 2  | sm_size_08.csv    |130.8 MB    | 600187    | train     |
   +----+-------------------+------------+-----------+-----------+
   | 3  | sm_size_16.csv    |377.3 MB    | 430302    | train     |
   +----+-------------------+------------+-----------+-----------+
   | 4  | sm_size_32.csv    |708.7 GB    | 195943    | train     |
   +----+-------------------+------------+-----------+-----------+
   | 5  | sm_size_64.csv    |1.37  GB    | 92034     | train     |
   +----+-------------------+------------+-----------+-----------+

Percentage of smooth-removed data:

size  4: (1335970 - 1335970) / 3675428.0 = 0.64
size  8: (600187 - 600187) / 2372324.0 = 0.74
size 16: (430302 - 430302) / 1439773.0 = 0.70
size 32: (195943 - 195943) / 567554.0 = 0.65
size 64: (92034 - 92034) / 125141.0 = 0.26

The mode distribution data are provided for downloading.









