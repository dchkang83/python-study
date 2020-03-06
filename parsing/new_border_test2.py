import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json, os, traceback
import math
from core import test_calcu as calcu

x_list = np.array(
    [67.6119, 69.4202, 69.6362, 69.9784, 70.1925, 70.424, 70.6564, 70.8728, 71.1199, 71.3872, 71.655, 71.9038, 72.1467,
     72.4088, 72.6712, 72.9148, 73.1676, 73.4406, 73.7139, 73.9677, 74.1764, 74.4015, 74.6264, 74.8344, 74.9576,
     75.0879, 75.2227, 75.3596, 75.496, 75.6294, 75.7573, 75.8773, 75.9818, 76.0919, 76.2052, 76.3195, 76.4327, 76.5424,
     76.6465, 76.7427, 76.829, 76.9185, 77.0094, 77.0996, 77.1873, 77.2705, 77.3472, 77.4154, 77.4634, 77.5173, 77.628,
     77.7533, 90.6457, 90.7046, 90.7566, 90.8106, 90.8452, 90.8619, 90.875, 90.8854, 90.8936, 90.906, 90.9261, 90.9427,
     90.9261, 90.906, 90.8936, 90.8855, 90.875, 90.8619, 90.8451, 90.8106, 90.7566, 90.7046, 90.6457, 77.7533, 77.628,
     77.5173, 77.4634, 77.4154, 77.3472, 77.2704, 77.1873, 77.0996, 77.0093, 76.9184, 76.8289, 76.7427, 76.6466,
     76.5424, 76.4326, 76.3194, 76.2049, 76.0916, 75.9816, 75.8773, 75.7575, 75.6297, 75.4963, 75.3598, 75.2228,
     75.0879, 74.9576, 74.8344, 74.7336, 74.6264, 74.4016, 74.1765, 73.9677, 73.7139, 73.4407, 73.1677, 72.9148,
     72.6711, 72.4088, 72.1467, 71.9038, 71.655, 71.3872, 71.1199, 70.8728, 70.6564, 70.424, 70.1924, 69.9784, 69.6362,
     69.4202, 67.6119, 67.7934, 67.9464, 68.0753, 68.1841, 68.2982, 68.4095, 68.5096, 68.591, 68.6752, 68.756, 68.8273,
     68.8701, 68.9137, 68.9999, 69.0796, 69.1151, 69.1465, 69.1766, 69.2062, 69.2628, 69.3138, 69.3565, 69.3892,
     69.4209, 69.4493, 69.4719, 69.4833, 69.4934, 69.5089, 69.5184, 69.5268, 69.5351, 69.5268, 69.5184, 69.5089,
     69.4931, 69.4719, 69.4496, 69.421, 69.389, 69.3565, 69.3141, 69.2629, 69.2061, 69.1764, 69.1465, 69.1152, 69.0798,
     68.9998, 68.9135, 68.8273, 68.7562, 68.6752, 68.5908, 68.5096, 68.4098, 68.2985, 68.1842, 68.0753, 67.9464,
     67.7934

        , 67.6119
     ])

y_list = np.array(
    [44.0912, 48.9391, 48.876, 48.779, 48.7235, 48.6672, 48.6142, 48.5687, 48.5225, 48.4774, 48.4355, 48.3989, 48.3661,
     48.3334, 48.3028, 48.2765, 48.2527, 48.2315, 48.215, 48.2054, 48.2044, 48.2102, 48.2222, 48.2396, 48.2542, 48.2728,
     48.2951, 48.3204, 48.3481, 48.3778, 48.4089, 48.4407, 48.4716, 48.5075, 48.5476, 48.5913, 48.6378, 48.6866,
     48.7369, 48.7881, 48.8389, 48.8965, 48.9596, 49.0271, 49.0978, 49.1705, 49.2439, 49.3169, 49.3759, 49.4485,
     49.6083, 49.7999, 50.4797, 49.3695, 48.4334, 47.4462, 46.8792, 46.5849, 46.3119, 46.0069, 45.6781, 45.0441,
     43.7845, 40.0726, 36.3607, 35.1011, 34.4671, 34.1383, 33.8333, 33.5603, 33.266, 32.699, 31.7118, 30.7757, 29.6655,
     30.3453, 30.5369, 30.6967, 30.7693, 30.8283, 30.9013, 30.9747, 31.0473, 31.1179, 31.1854, 31.2485, 31.3062,
     31.3571, 31.4083, 31.4584, 31.5069, 31.5532, 31.5967, 31.6368, 31.6729, 31.7045, 31.737, 31.7682, 31.7977, 31.8251,
     31.8499, 31.8719, 31.8906, 31.9055, 31.9154, 31.9236, 31.9352, 31.9406, 31.9398, 31.9304, 31.9136, 31.892, 31.8687,
     31.8428, 31.8119, 31.7789, 31.7463, 31.7102, 31.6681, 31.6227, 31.5765, 31.531, 31.478, 31.4217, 31.3662, 31.2692,
     31.206, 36.054, 36.1932, 36.3134, 36.4195, 36.5174, 36.6265, 36.7386, 36.8454, 36.9391, 37.0431, 37.1497, 37.2513,
     37.3175, 37.389, 37.5418, 37.698, 37.7738, 37.8462, 37.9217, 38.0027, 38.1744, 38.3479, 38.5101, 38.6504, 38.8024,
     38.9551, 39.0973, 39.1886, 39.2873, 39.478, 39.6461, 39.8421, 40.0726, 40.3031, 40.4991, 40.6672, 40.8578, 41.0479,
     41.1902, 41.3428, 41.4948, 41.6351, 41.7973, 41.9708, 42.1424, 42.2234, 42.299, 42.3714, 42.4472, 42.6033, 42.756,
     42.8939, 42.9955, 43.102, 43.2059, 43.2998, 43.4068, 43.5189, 43.6279, 43.7257, 43.8317, 43.9519

        , 44.0912
     ])


def test1():
    """
    다각형의 최소/최대 4점을 알면 중심점을 구할 수 있습니다.
    x1 : 다각형의 x 좌표 중 가장 작은 값
    y1 : 다각형의 y 좌표 중 가장 작은 값
    x2 : 다각형의 x 좌표 중 가장 큰 값
    y2 : 다각형의 y 좌표 중 가장 큰 값

    center.x = x1 + ((x2 - x1) / 2)
    center.y = y1 + ((y2 - y1) / 2)

    :return:
    """
    df_list1 = pd.DataFrame({"x": x_list, "y": y_list})

    minX = df_list1['x'].min()
    maxX = df_list1['x'].max()
    minY = df_list1['y'].min()
    maxY = df_list1['y'].max()
    # print("minX : %s maxX : %s minY : %s maxY : %s " % (minX, maxX, minY, maxY))

    center = {}
    center['x'] = minX + ((maxX - minX) / 2)
    center['y'] = minY + ((maxY - minY) / 2)
    # print("center : %s" % center)

    landmarks = {'neck': [127, 0], 'shoulder': [126, 1], 'hem': [74, 52], 'height': [159, 63], 'chest': [75, 51]}

    df_list2 = df_list1.copy()
    # df_list2 = pd.concat((df_list1.loc[0:1], df_list1.loc[75:]))
    # print("df_list2 : ", df_list2)
    # df_tem = pd.concat((df_ori.loc[index_aroundpoint[0]:], df_ori.loc[:target_index]))



    """
    print("landmarks : ", landmarks)
    index_flat = np.hstack(landmarks.values()).tolist()
    print("index_flat : ", index_flat)
    index_flat.sort()
    print("index_flat : ", index_flat)
    print(index_flat.index(127))
    print(index_flat[index_flat.index(127)])
    print("max(index_flat) : ", max(index_flat))
    """

    for key, landmark in landmarks.items():
        # print("key : %s, landmark : %s / %s" % (key, landmark[0], landmark[1]))
        # if key in ['neck', 'hem']:
        if key in ['neck']:
            # print("############## test : ", test)
            if landmark[1] == 0:
                # print("landmark : ", landmark)
                # print("max(landmark) : ", max(landmark))
                # print("len : ", df_list2)

                for idx in range(landmark[0], len(df_list2)):
                    """
                    inclination = calcu.get_inclination([center['x'], center['y']], df_list2.iloc[idx])
                    cal_point = calcu.testCal(inclination, df_list2.iloc[idx].x, df_list2.iloc[idx].y, 1)
                    df_list2.iloc[idx].x = cal_point['x2']
                    df_list2.iloc[idx].y = cal_point['y2']
                    """
                    continue

                # ============= 랜드마크 1 ~ 0 기준으로
                # 기울기
                print(df_list2.iloc[1])
                print(df_list2.iloc[0])
                inclination = calcu.get_inclination(df_list2.iloc[0], df_list2.iloc[1])
                # 예측 포인트
                cal_point = calcu.testCal(inclination, df_list2.iloc[0].x, df_list2.iloc[0].y, 1)

                xxx = cal_point['x2'] - df_list2.iloc[0].x
                yyy = cal_point['y2'] - df_list2.iloc[0].y
                cur_grading_data = {'name': 'neck_depth', 'target_index': 0, 'grading_size': xxx, 'axis': 'x'}
                df_list2 = calcu.move_landmark(df_list2, landmarks,
                                               cur_grading_data["target_index"],
                                               cur_grading_data["grading_size"],
                                               cur_grading_data["axis"])

                cur_grading_data = {'name': 'neck_depth', 'target_index': 0, 'grading_size': yyy, 'axis': 'y'}
                df_list2 = calcu.move_landmark(df_list2, landmarks,
                                               cur_grading_data["target_index"],
                                               cur_grading_data["grading_size"],
                                               cur_grading_data["axis"])

                # ============= 랜드마크 126 ~ 127 기준으로
                # 기울기
                inclination = calcu.get_inclination(df_list2.iloc[126], df_list2.iloc[127])
                # 예측 포인트
                cal_point = calcu.testCal(inclination, df_list2.iloc[127].x, df_list2.iloc[127].y, 1)

                xxx = cal_point['x2'] - df_list2.iloc[127].x
                yyy = cal_point['y2'] - df_list2.iloc[127].y

                cur_grading_data = {'name': 'neck_depth', 'target_index': 127, 'grading_size': xxx, 'axis': 'x'}
                df_list2 = calcu.move_landmark(df_list2, landmarks,
                                               cur_grading_data["target_index"],
                                               cur_grading_data["grading_size"],
                                               cur_grading_data["axis"])

                cur_grading_data = {'name': 'neck_depth', 'target_index': 127, 'grading_size': yyy, 'axis': 'y'}
                df_list2 = calcu.move_landmark(df_list2, landmarks,
                                               cur_grading_data["target_index"],
                                               cur_grading_data["grading_size"],
                                               cur_grading_data["axis"])

                """
                이걸로 계속 테스트 함
                """
                cur_grading_data = {'name': 'neck_depth', 'target_index': 159, 'grading_size': -1.0, 'axis': 'x'}
                df_list2 = calcu.move_landmark(df_list2, landmarks,
                                              cur_grading_data["target_index"],
                                              cur_grading_data["grading_size"],
                                              cur_grading_data["axis"])


            else:
                # for idx in range(min(landmark), max(landmark)+1):
                #     # x_1 = df_list2.iloc[idx].x
                #     # y_1 = df_list2.iloc[idx].y
                #     # print("[%s] x_1 : %s, y_1 : %s" % (idx, x_1, y_1))
                #     df_list2.iloc[idx].x -= 1
                continue


    list1_x = df_list1.iloc[0].x
    list1_y = df_list1.iloc[0].y
    list2_x = df_list2.iloc[0].x
    list2_y = df_list2.iloc[0].y

    width = list1_x - list2_x
    height = list1_y - list2_y

    print("list1[x, y] : [%s, %s]" % (list1_x, list1_y))
    print("list2[x, y] : [%s, %s]" % (list2_x, list2_y))

    print("width : %s" % width)
    print("height : %s" % height)

    diagonal_length = math.sqrt(math.pow(width, 2) + math.pow(height, 2))
    print("diagonalLength : ", diagonal_length)

    # print("df_list1.iloc[159].x : ", df_list1.iloc[159].x)
    # print("df_list2.iloc[159].x : ", df_list2.iloc[159].x)

    print("neck-height : ", df_list1.iloc[159].x - df_list2.iloc[159].x)

    print("math.sqrt() : ", (math.sqrt(100)))

    plt.plot('x', 'y', data=df_list1, marker='.', markerfacecolor='blue', markersize=3, color='skyblue', linewidth=1)
    plt.plot('x', 'y', data=df_list2, marker='.', markerfacecolor='olive', markersize=3, color='red', linewidth=1)
    plt.show()


def main():
    try:
        test1()

    except Exception as exp:
        print("########### Exception : %s" % str(exp))
        # app.logger.error("########### Exception : %s", str(exp))
        traceback.print_exc()


if __name__ == '__main__':
    main()

