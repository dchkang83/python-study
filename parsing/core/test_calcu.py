import pandas as pd
import numpy as np
import math


def testCal(M, PX, PY, T) :
    # M = 10  # 기울기
    # PX = 0 # 주어진 점의 X좌표
    # PY = 0 # 주어진 점의 Y좌표
    # T = 20  # 주어진 점으로 부터 떨어진 거리

    A = (M * M) + 1
    B = (2 * (PY - (M * PX)) * M) - (2 * PX) - (2 * PY * M)
    C = (PX * PX) + (PY * PY) - (2 * PY * (PY - (M * PX))) + ((PY - (M * PX)) * (PY - (M * PX))) - (T * T)

    D = (B * B) - 4 * (A * C)

    # print("D : ", D)

    if D > 0:
        x1 = ((-1 * B) + math.sqrt(D)) / (2 * A)
        x2 = ((-1 * B) - math.sqrt(D)) / (2 * A)

        y1 = (M * x1) + (PY - (M * PX))
        y2 = (M * x2) + (PY - (M * PX))

    # print("x1 : ", x1)
    # print("y1 : ", y1)
    # print("y2 : ", y2)
    # print("x2 : ", x2)

    return {"x1": x1, "y1": y1, "x2": x2, "y2": y2}

# else if: D == 0
#     # 전제한 조건으로 부터 근이 한개만 나올 수는 없음
#     return -1
# else D < 0

# return -1


# 기울기
def get_inclination(from_point, to_point):
    x = from_point[0] - to_point[0]
    y = from_point[1] - to_point[1]

    return y/x


# 예측 포인트
def get_arc_len(df_calc, index_arc):
    """
    곡선 길이 계산
    :param df_calc: 도형 데이터프레임
    :type df_calc: pd.DataFrame
    :param index_arc: 곡선 인덱스 번호
    :type index_arc: list[int]
    :return: (float) 곡선 길이
    """
    if index_arc[0] < index_arc[1]:
        df_arc = df_calc.loc[index_arc[0]:index_arc[1]]

    if index_arc[0] > index_arc[1]:
        df_arc = pd.concat(
            (df_calc.loc[index_arc[0]:], df_calc.loc[:index_arc[1]]))

    if index_arc[0] == index_arc[1]:
        print('wrong index')

    length_arc = []
    for i in range(len(df_arc) - 1):
        length_arc.append(
            np.sqrt(np.sum(np.square(df_arc.values[i] - df_arc.values[i + 1]))))

    return sum(length_arc)


# by total length
def fit_arc(df_ori, landmarks, target_index, arc_indices, total_arc_length, axis):
    """
    곡선 방식으로 하나의 점을 이동시키는 함수
    (점을 옮겼을때 곡선의 길이가 arc_length_new에 최대한 가깝도록 최적화)
    :param df_ori: 도형 데이터프레임
    :type df_ori: pd.DataFrame
    :param landmarks: 랜드마크 인덱스 정보
    :type landmarks: dict[list]
    :param target_index: 이동할 점의 인덱스 번호
    :type target_index: int
    :param arc_indices: 곡선 길이를 계산할 인덱스들의 번호
    :type arc_indices: list[int]
    :param total_arc_length: 점이 이동한 후에 곡선의 총 길이
    :type total_arc_length: float
    :param axis: 이동할 축 ("x", "y")
    :type axis: str
    :return:
    """
    if target_index not in arc_indices:
        return 'wrong index_target or index_arc'

    if axis == 'y':
        dis_min = abs(df_ori.loc[arc_indices[0]].x - df_ori.loc[arc_indices[1]].x)

        size_max = 10
        size_min = -10

    if axis == 'x':
        dis_min = abs(df_ori.loc[arc_indices[0]].y - df_ori.loc[arc_indices[1]].y)

        index_flat = np.hstack(landmarks.values()).tolist()
        index_flat.sort()

        if (max(index_flat) != target_index) & (min(index_flat) != target_index):
            index_aroundpoint = [index_flat[index_flat.index(target_index) - 1], index_flat[index_flat.index(target_index) + 1]]

        if max(index_flat) == target_index:
            index_aroundpoint = [index_flat[index_flat.index(target_index) - 1], min(index_flat)]

        if min(index_flat) == target_index:
            index_aroundpoint = [max(index_flat), index_flat[index_flat.index(target_index) + 1]]

        size_max = max(df_ori.loc[index_aroundpoint[0]].x, df_ori.loc[index_aroundpoint[1]].x) - df_ori.loc[target_index].x
        size_min = min(df_ori.loc[index_aroundpoint[0]].x, df_ori.loc[index_aroundpoint[1]].x) - df_ori.loc[target_index].x

        if size_max > 10:
            size_max = 10
        if size_min < -10:
            size_min = -10

    if total_arc_length < (dis_min - 0.01):
        return 'arc_length is too small'

    if (total_arc_length >= dis_min - 0.01) & (total_arc_length <= dis_min + 0.01):
        return True

    if total_arc_length > (dis_min + 0.01):

        size = np.linspace(size_min, size_max, 20000).tolist()
        cell_size = [0]
        len_diff = [get_arc_len(df_ori, arc_indices) - total_arc_length]

        for i in range(len(size)):
            print("### i : ", i)
            cell_size.append(size[len(size) // 2])
            df_grading = move_landmark(df_ori, landmarks, target_index, cell_size[-1], axis)
            len_diff.append(get_arc_len(df_grading, arc_indices) - total_arc_length)

            if cell_size[-1] > cell_size[-2]:
                # print("11111111")

                if (abs(len_diff[-1]) > abs(len_diff[-2])) & (len_diff[-1] * len_diff[-2] > 0):
                    size = size[size.index(size[0]):size.index(cell_size[-1])]

                if (abs(len_diff[-1]) > abs(len_diff[-2])) & (len_diff[-1] * len_diff[-2] < 0):
                    size = size[size.index(size[0]):size.index(cell_size[-1])]

                if (abs(len_diff[-1]) < abs(len_diff[-2])) & (len_diff[-1] * len_diff[-2] > 0):
                    size = size[size.index(cell_size[-1]):size.index(size[-1])]

                if (abs(len_diff[-1]) < abs(len_diff[-2])) & (len_diff[-1] * len_diff[-2] < 0):
                    size = size[size.index(size[0]):size.index(cell_size[-1])]

            if cell_size[-1] < cell_size[-2]:
                # print("222222222")

                if (abs(len_diff[-1]) > abs(len_diff[-2])) & (len_diff[-1] * len_diff[-2] > 0):
                    size = size[size.index(cell_size[-1]):size.index(size[-1])]

                if (abs(len_diff[-1]) > abs(len_diff[-2])) & (len_diff[-1] * len_diff[-2] < 0):
                    size = size[size.index(cell_size[-1]):size.index(size[-1])]

                if (abs(len_diff[-1]) < abs(len_diff[-2])) & (len_diff[-1] * len_diff[-2] > 0):
                    size = size[size.index(size[0]):size.index(cell_size[-1])]

                if (abs(len_diff[-1]) < abs(len_diff[-2])) & (len_diff[-1] * len_diff[-2] < 0):
                    size = size[size.index(cell_size[-1]):size.index(size[-1])]

            if abs(len_diff[-1]) <= 0.01:
                return df_grading
                # return len_diff (this is loss value)

            # print("size : ", size)
            if len(size) == 1:
                return 'there is no right fix arc, please grading other part first or adjust arc_length_new'

            if (i == (len(size) - 1)) & (abs(len_diff[-1]) > 0.01):
                return 'it should be adjust frequency or range of size'


# by modify size
def move_landmark(df_grading, landmarks, target_index, moving_length, axis):
    """
        직선 방향으로 하나의 점을 이동하는 함수
        :param df_grading       : 도형 데이터프레임
        :type df_grading        : pd.DataFrame

        :param landmarks        : 랜드마크 인덱스 정보
        :type landmarks         : dict

        :param target_index     : 이동할 점의 인덱스
        :type target_index      : int

        :param moving_length    : 이동할 길이
        :type moving_length     : float

        :param axis             : 이동할 축
        :type axis              : str

        :return: df_ori(pd.DataFrame): 변경된 도형 데이터프레임
    """
    df_ori = df_grading[['x', 'y']]
    # find around_landmark
    # #get around dataframe
    index_flat = np.hstack(landmarks.values()).tolist()
    index_flat.sort()
    if (max(index_flat) != target_index) & (min(index_flat) != target_index):
        index_aroundpoint = [index_flat[index_flat.index(target_index) - 1],
                             index_flat[index_flat.index(target_index) + 1]]

        df_around = [df_ori[(df_ori.index >= index_aroundpoint[0]) & (df_ori.index <= target_index)],
                     df_ori[(df_ori.index >= target_index) & (df_ori.index <= index_aroundpoint[1])]]

    if max(index_flat) == target_index:
        index_aroundpoint = [index_flat[index_flat.index(target_index) - 1], min(index_flat)]
        df_tem = pd.concat((df_ori.loc[target_index:], df_ori.loc[:index_aroundpoint[1]]))
        df_around = [df_ori[(df_ori.index <= target_index) & (df_ori.index >= index_aroundpoint[0])], df_tem]
        # print("index_aroundpoint : ", index_aroundpoint)

    if min(index_flat) == target_index:
        index_aroundpoint = [max(index_flat), index_flat[index_flat.index(target_index) + 1]]
        df_tem = pd.concat((df_ori.loc[index_aroundpoint[0]:], df_ori.loc[:target_index]))
        df_around = [df_tem, df_ori[(df_ori.index <= index_aroundpoint[1]) & (df_ori.index >= target_index)]]

    point_target = df_ori[df_ori.index == target_index]

    point_around = []
    for i in range(len(index_aroundpoint)):
        point_around.append(df_ori[df_ori.index == index_aroundpoint[i]])

    # select the algorithm
    # get point_base and all_len
    algorithm = []
    point_base = []
    all_len = []

    # print("df_around : ", df_around)
    # print("point_around : ", point_around)
    # print("point_target : ", point_target)
    ############### 67.26241430950778 , 43.154258298436474

    # print("len(df_around) : ", len(df_around))
    for i in range(len(df_around)):
        if (len(df_around[i].x.unique()) == 1) & (len(df_around[i].y.unique()) != 1):
            # print("## 11")
            point_base.append(point_around[i].y.values[0])
            all_len.append(abs(point_around[i].y.values[0] - point_target.y.values[0]))
            algorithm.append('basey')
            continue

        if (len(df_around[i].x.unique()) != 1) & (len(df_around[i].y.unique()) == 1):
            # print("## 22")
            point_base.append(point_around[i].x.values[0])
            all_len.append(abs(point_around[i].x.values[0] - point_target.x.values[0]))
            algorithm.append('basex')
            continue

        if (max(df_around[i].x) == point_around[i].x.values[0]) & (min(df_around[i].x) == point_target.x.values[0]):
            # print("## 33")
            point_base.append(point_around[i].x.values[0])
            all_len.append(abs(point_around[i].x.values[0] - point_target.x.values[0]))
            algorithm.append('basex')
            continue

        if (min(df_around[i].x) == point_around[i].x.values[0]) & (max(df_around[i].x) == point_target.x.values[0]):
            # print("## 44")
            # print("## point_around[%s].x.values[0] : %s" % (i, point_around[i].x.values[0]))

            point_base.append(point_around[i].x.values[0])
            all_len.append(abs(point_around[i].x.values[0] - point_target.x.values[0]))
            algorithm.append('basex')
            continue

        if (max(df_around[i].y) == point_around[i].y.values[0]) & (min(df_around[i].y) == point_target.y.values[0]):
            # print("## 55")
            point_base.append(point_around[i].y.values[0])
            all_len.append(abs(point_around[i].y.values[0] - point_target.y.values[0]))
            algorithm.append('basey')
            continue

        if (min(df_around[i].y) == point_around[i].y.values[0]) & (max(df_around[i].y) == point_target.y.values[0]):
            # print("## 66")
            point_base.append(point_around[i].y.values[0])
            all_len.append(abs(point_around[i].y.values[0] - point_target.y.values[0]))
            algorithm.append('basey')
            continue

    # print("## point_base : ", point_base)
    # print("## all_len : ", all_len)
    # print("## algorithm : ", algorithm)

    # grading
    if axis == 'y':
        for i in range(len(df_around)):
            for j in range(len(df_around[i])):
                indextemp = df_around[i].iloc[j].name

                if algorithm[i] == 'basex':
                    if all_len[i] != 0:
                        ratio = abs(df_around[i].iloc[j].x - point_base[i]) / all_len[i]
                    if all_len[i] == 0:
                        ratio = 1

                if algorithm[i] == 'basey':
                    if all_len[i] != 0:
                        ratio = abs(df_around[i].iloc[j].y - point_base[i]) / all_len[i]
                    if all_len[i] == 0:
                        ratio = 1

                df_ori.loc[indextemp, 'y'] = df_around[i].iloc[j].y + moving_length * ratio

    if axis == 'x':
        for i in range(len(df_around)):
            for j in range(len(df_around[i])):
                indextemp = df_around[i].iloc[j].name

                if algorithm[i] == 'basex':
                    if all_len[i] != 0:
                        ratio = abs(df_around[i].iloc[j].x - point_base[i]) / all_len[i]
                    if all_len[i] == 0:
                        ratio = 1

                if algorithm[i] == 'basey':
                    if all_len[i] != 0:
                        ratio = abs(df_around[i].iloc[j].y - point_base[i]) / all_len[i]
                    if all_len[i] == 0:
                        ratio = 1
                # print(target_index, indextemp, moving_length, ratio)

                df_ori.loc[indextemp, 'x'] = df_around[i].iloc[j].x + moving_length * ratio


    return df_ori


if __name__ == '__main__':
    a = [-2, 0]
    b = [0, -2]

    inclination = get_inclination(a, b)

    # M = 10  # 기울기
    # PX = 0 # 주어진 점의 X좌표
    # PY = 0 # 주어진 점의 Y좌표
    # T = 20  # 주어진 점으로 부터 떨어진 거리
    cal_point = testCal(inclination, 0, 0, 20)

    print("inclination : ", inclination)
    print("cal_point : ", cal_point)


