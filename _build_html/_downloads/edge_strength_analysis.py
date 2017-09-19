# ==============================================================================
# Author: Pharrell_WANG
# Date: 2017/6/28
# ==============================================================================

import os
import numpy as np
import pandas as pd
import datetime

from collections import OrderedDict


def edge_analyzer(INPUT_FILE, SEQUENCE):
    homedir = os.environ['HOME']
    start_timestamp = datetime.datetime.now()
    print('=================================================')
    print('++++++++++++++++++++')
    print('start at: ')
    print(start_timestamp)
    print('++++++++++++++++++++')
    print('Name of the data file: ' + str(INPUT_FILE))
    x_dict = OrderedDict()
    strength_dict = OrderedDict()

    mode_0 = 0
    mode_1 = 0
    mode_2 = 0
    mode_3 = 0
    mode_4 = 0
    mode_5 = 0
    mode_6 = 0
    mode_7 = 0
    mode_8 = 0
    mode_9 = 0
    mode_10 = 0
    mode_11 = 0
    mode_12 = 0
    mode_13 = 0
    mode_14 = 0
    mode_15 = 0
    mode_16 = 0
    mode_17 = 0
    mode_18 = 0
    mode_19 = 0
    mode_20 = 0
    mode_21 = 0
    mode_22 = 0
    mode_23 = 0
    mode_24 = 0
    mode_25 = 0
    mode_26 = 0
    mode_27 = 0
    mode_28 = 0
    mode_29 = 0
    mode_30 = 0
    mode_31 = 0
    mode_32 = 0
    mode_33 = 0
    mode_34 = 0
    mode_35 = 0
    mode_36 = 0
    edge_strength_of_mode_0 = 0
    edge_strength_of_mode_1 = 0
    edge_strength_of_mode_2 = 0
    edge_strength_of_mode_3 = 0
    edge_strength_of_mode_4 = 0
    edge_strength_of_mode_5 = 0
    edge_strength_of_mode_6 = 0
    edge_strength_of_mode_7 = 0
    edge_strength_of_mode_8 = 0
    edge_strength_of_mode_9 = 0
    edge_strength_of_mode_10 = 0
    edge_strength_of_mode_11 = 0
    edge_strength_of_mode_12 = 0
    edge_strength_of_mode_13 = 0
    edge_strength_of_mode_14 = 0
    edge_strength_of_mode_15 = 0
    edge_strength_of_mode_16 = 0
    edge_strength_of_mode_17 = 0
    edge_strength_of_mode_18 = 0
    edge_strength_of_mode_19 = 0
    edge_strength_of_mode_20 = 0
    edge_strength_of_mode_21 = 0
    edge_strength_of_mode_22 = 0
    edge_strength_of_mode_23 = 0
    edge_strength_of_mode_24 = 0
    edge_strength_of_mode_25 = 0
    edge_strength_of_mode_26 = 0
    edge_strength_of_mode_27 = 0
    edge_strength_of_mode_28 = 0
    edge_strength_of_mode_29 = 0
    edge_strength_of_mode_30 = 0
    edge_strength_of_mode_31 = 0
    edge_strength_of_mode_32 = 0
    edge_strength_of_mode_33 = 0
    edge_strength_of_mode_34 = 0
    edge_strength_of_mode_35 = 0
    edge_strength_of_mode_36 = 0

    d = {}
    for item in range(37):
        d['strength_data_for_mode_%02d' % item] = np.array([])

    RESHAPE = 8  # INIT
    csv = pd.read_csv(INPUT_FILE, header=None).values
    print('total num of rows in csv file:')
    print(csv.shape[0])
    print('total elements in a row:')
    print(csv.shape[1])

    if csv.shape[1] == 17:
        RESHAPE = 4
    elif csv.shape[1] == 65:
        RESHAPE = 8
    elif csv.shape[1] == 257:
        RESHAPE = 16
    elif csv.shape[1] == 1025:
        RESHAPE = 32
    elif csv.shape[1] == 4097:
        RESHAPE = 64
    assert (csv.shape[1] == RESHAPE * RESHAPE + 1)

    with open(INPUT_FILE, 'r') as r:
        cnt = 0
        for num, line in enumerate(r):
            data = np.array([])
            cnt += 1
            # sys.stdout.write(
            #     '\r>> processing line: %d / %d' % (cnt, csv.shape[0]))
            # sys.stdout.write(
            #     '\r>> processing percent: %d ' % round(cnt / csv.shape[0], 3))
            if line[-3:-2] == ',':
                # print("yes, it is a comma.===============!!~~~~~~~~")
                last_char_in_line = int(line[-2:-1])
            else:
                # print("no, not comma.-------------~~~~~~~~`")
                last_char_in_line = int(line[-3:-1])

            mode = last_char_in_line

            # edge strength analysis
            # read one line every time
            total_strength = 0

            row = csv[cnt - 1]
            # local_counter = 0
            features, label = row[:-1], row[-1]
            features = features.reshape(RESHAPE, RESHAPE)
            for i in range(RESHAPE - 1):
                for j in range(RESHAPE - 1):
                    # local_counter += 1
                    # sys.stdout.write(
                    #     '\r>> processing %d/%d' % (local_counter,
                    #                                RESHAPE ** 2))
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
                    strength = horizontal_strength ** 2 + vertical_strength ** 2
                    data = np.append(data, np.array([strength]))  # total strength of a block (or you can say a line in the csv file)
                    total_strength += strength

            assert (data.ndim == 1)
            # top RESHAPE*2 && non-zero average.
            # step1: top RESHAPE*2 values in the numpy arrary
            top_k = data[np.argsort(data)][data.size - RESHAPE * 2:]
            assert (top_k.ndim == 1)
            # step2: non-zero values (because sometimes the edge length can be short. We only want the sharpness. We do not want smooth regions to affect the sharpness.)
            data = top_k[top_k.nonzero()]
            data = data[np.where(data > 8)]  # for [[2, 0], [0, 0]], i exclude it from the concept of sharp
            if data.size == 0:  # all the strength are zero. (that is to say , it is like the DC mode)
                ave = 0
                data = np.array([0])
            else:
                ave = np.mean(data)
                data = np.array([ave])

            assert (data.ndim == 1)

            if mode == 0:
                mode_0 += 1
                edge_strength_of_mode_0 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 1:
                mode_1 += 1
                edge_strength_of_mode_1 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 2:
                mode_2 += 1
                edge_strength_of_mode_2 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 3:
                mode_3 += 1
                edge_strength_of_mode_3 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 4:
                mode_4 += 1
                edge_strength_of_mode_4 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 5:
                mode_5 += 1
                edge_strength_of_mode_5 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 6:
                mode_6 += 1
                edge_strength_of_mode_6 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 7:
                mode_7 += 1
                edge_strength_of_mode_7 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 8:
                mode_8 += 1
                edge_strength_of_mode_8 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 9:
                mode_9 += 1
                edge_strength_of_mode_9 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 10:
                mode_10 += 1
                edge_strength_of_mode_10 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 11:
                mode_11 += 1
                edge_strength_of_mode_11 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 12:
                mode_12 += 1
                edge_strength_of_mode_12 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 13:
                mode_13 += 1
                edge_strength_of_mode_13 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 14:
                mode_14 += 1
                edge_strength_of_mode_14 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 15:
                mode_15 += 1
                edge_strength_of_mode_15 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 16:
                mode_16 += 1
                edge_strength_of_mode_16 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 17:
                mode_17 += 1
                edge_strength_of_mode_17 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 18:
                mode_18 += 1
                edge_strength_of_mode_18 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 19:
                mode_19 += 1
                edge_strength_of_mode_19 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 20:
                mode_20 += 1
                edge_strength_of_mode_20 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 21:
                mode_21 += 1
                edge_strength_of_mode_21 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 22:
                mode_22 += 1
                edge_strength_of_mode_22 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 23:
                mode_23 += 1
                edge_strength_of_mode_23 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 24:
                mode_24 += 1
                edge_strength_of_mode_24 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 25:
                mode_25 += 1
                edge_strength_of_mode_25 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 26:
                mode_26 += 1
                edge_strength_of_mode_26 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 27:
                mode_27 += 1
                edge_strength_of_mode_27 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 28:
                mode_28 += 1
                edge_strength_of_mode_28 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 29:
                mode_29 += 1
                edge_strength_of_mode_29 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 30:
                mode_30 += 1
                edge_strength_of_mode_30 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 31:
                mode_31 += 1
                edge_strength_of_mode_31 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 32:
                mode_32 += 1
                edge_strength_of_mode_32 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 33:
                mode_33 += 1
                edge_strength_of_mode_33 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 34:
                mode_34 += 1
                edge_strength_of_mode_34 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 35:
                mode_35 += 1
                edge_strength_of_mode_35 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)
            elif mode == 36:
                mode_36 += 1
                edge_strength_of_mode_36 += ave
                d['strength_data_for_mode_%02d' % mode] = np.append(
                    d['strength_data_for_mode_%02d' % mode], data)

        x_dict['mode__0'] = mode_0
        x_dict['mode__1'] = mode_1
        x_dict['mode__2'] = mode_2
        x_dict['mode__3'] = mode_3
        x_dict['mode__4'] = mode_4
        x_dict['mode__5'] = mode_5
        x_dict['mode__6'] = mode_6
        x_dict['mode__7'] = mode_7
        x_dict['mode__8'] = mode_8
        x_dict['mode__9'] = mode_9
        x_dict['mode_10'] = mode_10
        x_dict['mode_11'] = mode_11
        x_dict['mode_12'] = mode_12
        x_dict['mode_13'] = mode_13
        x_dict['mode_14'] = mode_14
        x_dict['mode_15'] = mode_15
        x_dict['mode_16'] = mode_16
        x_dict['mode_17'] = mode_17
        x_dict['mode_18'] = mode_18
        x_dict['mode_19'] = mode_19
        x_dict['mode_20'] = mode_20
        x_dict['mode_21'] = mode_21
        x_dict['mode_22'] = mode_22
        x_dict['mode_23'] = mode_23
        x_dict['mode_24'] = mode_24
        x_dict['mode_25'] = mode_25
        x_dict['mode_26'] = mode_26
        x_dict['mode_27'] = mode_27
        x_dict['mode_28'] = mode_28
        x_dict['mode_29'] = mode_29
        x_dict['mode_30'] = mode_30
        x_dict['mode_31'] = mode_31
        x_dict['mode_32'] = mode_32
        x_dict['mode_33'] = mode_33
        x_dict['mode_34'] = mode_34
        x_dict['mode_35'] = mode_35
        x_dict['mode_36'] = mode_36

        veri_1 = 0
        print('=================================================')
        print("COUNTING START...")
        for m, n in x_dict.items():
            print(str(m) + " :   " + str(
                n) + '   <<------ ||-------->>      ' + str(
                m) + " / total (%) :   " + str(
                float(n) / float(cnt)))
            veri_1 += float(n) / float(cnt)

        print('*** Verification ***')
        print(
            "Sum of the percentages (output should be nearly equal to 1 or 0.999999..) : " + str(
                veri_1))

        sorted_x = OrderedDict(sorted(x_dict.items(), key=lambda t: t[1]))

        print("")
        print('Below are the sorted list of all the modes (smallest first)')
        veri_2 = 0
        for m, n in sorted_x.items():
            print(str(m) + " :   " + str(n) + '  <<------ ||-------->> ' + str(
                m) + " / total (%) :   " + str(
                float(n) / float(cnt)))
            veri_2 += float(n) / float(cnt)

        print('===================')
        print('*** Verification ***')
        print(
            "Sum of the percentages (output should be nearly equal to 1 or 0.999999..) : " + str(
                veri_2))
        print("total lines/records in the csv file : " + str(cnt))
        print("COUNTING END...")
        print('=================================================')

        strength_dict[
            'edge_strength_of_mode_00'] = edge_strength_of_mode_0 / mode_0
        strength_dict[
            'edge_strength_of_mode_01'] = edge_strength_of_mode_1 / mode_1
        strength_dict[
            'edge_strength_of_mode_02'] = edge_strength_of_mode_2 / mode_2
        strength_dict[
            'edge_strength_of_mode_03'] = edge_strength_of_mode_3 / mode_3
        strength_dict[
            'edge_strength_of_mode_04'] = edge_strength_of_mode_4 / mode_4
        strength_dict[
            'edge_strength_of_mode_05'] = edge_strength_of_mode_5 / mode_5
        strength_dict[
            'edge_strength_of_mode_06'] = edge_strength_of_mode_6 / mode_6
        strength_dict[
            'edge_strength_of_mode_07'] = edge_strength_of_mode_7 / mode_7
        strength_dict[
            'edge_strength_of_mode_08'] = edge_strength_of_mode_8 / mode_8
        strength_dict[
            'edge_strength_of_mode_09'] = edge_strength_of_mode_9 / mode_9
        strength_dict[
            'edge_strength_of_mode_10'] = edge_strength_of_mode_10 / mode_10
        strength_dict[
            'edge_strength_of_mode_11'] = edge_strength_of_mode_11 / mode_11
        strength_dict[
            'edge_strength_of_mode_12'] = edge_strength_of_mode_12 / mode_12
        strength_dict[
            'edge_strength_of_mode_13'] = edge_strength_of_mode_13 / mode_13
        strength_dict[
            'edge_strength_of_mode_14'] = edge_strength_of_mode_14 / mode_14
        strength_dict[
            'edge_strength_of_mode_15'] = edge_strength_of_mode_15 / mode_15
        strength_dict[
            'edge_strength_of_mode_16'] = edge_strength_of_mode_16 / mode_16
        strength_dict[
            'edge_strength_of_mode_17'] = edge_strength_of_mode_17 / mode_17
        strength_dict[
            'edge_strength_of_mode_18'] = edge_strength_of_mode_18 / mode_18
        strength_dict[
            'edge_strength_of_mode_19'] = edge_strength_of_mode_19 / mode_19
        strength_dict[
            'edge_strength_of_mode_20'] = edge_strength_of_mode_20 / mode_20
        strength_dict[
            'edge_strength_of_mode_21'] = edge_strength_of_mode_21 / mode_21
        strength_dict[
            'edge_strength_of_mode_22'] = edge_strength_of_mode_22 / mode_22
        strength_dict[
            'edge_strength_of_mode_23'] = edge_strength_of_mode_23 / mode_23
        strength_dict[
            'edge_strength_of_mode_24'] = edge_strength_of_mode_24 / mode_24
        strength_dict[
            'edge_strength_of_mode_25'] = edge_strength_of_mode_25 / mode_25
        strength_dict[
            'edge_strength_of_mode_26'] = edge_strength_of_mode_26 / mode_26
        strength_dict[
            'edge_strength_of_mode_27'] = edge_strength_of_mode_27 / mode_27
        strength_dict[
            'edge_strength_of_mode_28'] = edge_strength_of_mode_28 / mode_28
        strength_dict[
            'edge_strength_of_mode_29'] = edge_strength_of_mode_29 / mode_29
        strength_dict[
            'edge_strength_of_mode_30'] = edge_strength_of_mode_30 / mode_30
        strength_dict[
            'edge_strength_of_mode_31'] = edge_strength_of_mode_31 / mode_31
        strength_dict[
            'edge_strength_of_mode_32'] = edge_strength_of_mode_32 / mode_32
        strength_dict[
            'edge_strength_of_mode_33'] = edge_strength_of_mode_33 / mode_33
        strength_dict[
            'edge_strength_of_mode_34'] = edge_strength_of_mode_34 / mode_34
        strength_dict[
            'edge_strength_of_mode_35'] = edge_strength_of_mode_35 / mode_35
        strength_dict[
            'edge_strength_of_mode_36'] = edge_strength_of_mode_36 / mode_36

        for item in range(37):
            df = pd.DataFrame(d['strength_data_for_mode_%02d' % item])
            # SEQUENCE [balloons, ghost_fly, kendo, newspaper, poznan_hall_1920x1088, poznan_street_1920x1088, shark_1920x1088, undo_dancer_1920x1088 ]')
            df.to_csv(
                homedir + '/PycharmProjects/data-processing-for-fdc/sample_data/%s/csv/size_%s_hist_data_for_mode_%02d.csv' % (
                    str(SEQUENCE), str(RESHAPE), item),
                index=False)

        print('=================================================')
        print("COUNTING START...")
        for m, n in strength_dict.items():
            print(str(m) + " :   " + str(n))
        sorted_x = OrderedDict(
            sorted(strength_dict.items(), key=lambda t: t[1]))

        print('Below are the sorted list of all the modes (smallest first)')
        for m, n in sorted_x.items():
            print(str(m) + " :   " + str(n))
        print('=================================================')
        end_timestamp = datetime.datetime.now()

        time_duration = end_timestamp - start_timestamp

        print('++++++++++++++++++++')
        print('end at: ')
        print(end_timestamp)
        print('++++++++++++++++++++')
        print('The time spent is:')
        print(time_duration)
        print('++++++++++++++++++++')

        return x_dict, strength_dict
