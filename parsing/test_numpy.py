import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def test():
    a = np.arange(4).reshape((2, 2))

    np.amax(a)  # Maximum of the flattened array
    np.amax(a, axis=0)  # Maxima along the first axis
    np.amax(a, axis=1)  # Maxima along the second axis

    print("a : ", a)
    # print("np.amax(a) : ", np.amax(a))
    # print("np.amax(a, axis=0) : ", np.amax(a, axis=0))
    # print("np.amax(a, axis=1) : ", np.amax(a, axis=1))

    main_polyline_data1 = np.array([
                        {"x": 34.2433, "y": 34.8131}, {"x": 34.2809, "y": 22.5561}, {"x": 34.2433, "y": 10.2991},
                        {"x": 21.627, "y": 9.9958}, {"x": 20.8195, "y": 10.2975}, {"x": 19.7383, "y": 10.5307},
                        {"x": 18.526, "y": 10.6569}, {"x": 17.334, "y": 10.687}, {"x": 15.8938, "y": 10.6639},
                        {"x": 14.5217, "y": 10.5574}, {"x": 13.444, "y": 10.4198}, {"x": 12.6291, "y": 10.3117},
                        {"x": 10.3544, "y": 19.0818}, {"x": 10.971, "y": 19.2249}, {"x": 11.9908, "y": 19.5745},
                        {"x": 12.9388, "y": 20.0796}, {"x": 13.3905, "y": 20.4738}, {"x": 13.771, "y": 20.9557},
                        {"x": 13.963, "y": 21.3949}, {"x": 14.0955, "y": 21.857}, {"x": 14.1623, "y": 22.2907},
                        {"x": 14.1822, "y": 22.5561}, {"x": 14.1306, "y": 23.0643}, {"x": 13.8878, "y": 23.9012},
                        {"x": 13.5301, "y": 24.5392}, {"x": 13.0933, "y": 24.9331}, {"x": 12.5026, "y": 25.2862},
                        {"x": 11.4175, "y": 25.7369}, {"x": 10.3544, "y": 26.0304}, {"x": 12.6291, "y": 34.8004},
                        {"x": 13.3993, "y": 34.707}, {"x": 14.4711, "y": 34.586}, {"x": 15.7303, "y": 34.4848},
                        {"x": 16.9377, "y": 34.4373}, {"x": 18.304, "y": 34.4405}, {"x": 19.2595, "y": 34.5262},
                        {"x": 20.3902, "y": 34.7088}, {"x": 21.215, "y": 34.9489}, {"x": 21.627, "y": 35.1163},

                        # {"x": 34.2433, "y": 34.8131}
                      ])

    maxPricedItem = max(main_polyline_data1, key=lambda x: x['x'])
    minPricedItem = min(main_polyline_data1, key=lambda x: x['x'])

    # lst = [{'price': 99, 'barcode': '2342355'}, {'price': 88, 'barcode': '2345566'}]
    # maxPricedItem = max(lst, key=lambda x: x['price'])
    # minPricedItem = min(lst, key=lambda x: x['price'])


    # print("b : ", b[0])
    # print("b : ", max(b[0]))

    print("maxPricedItem : ", maxPricedItem)
    print("minPricedItem : ", minPricedItem)

    df1 = pd.DataFrame(main_polyline_data1)
    # print(df1)

    # df1 = pd.DataFrame({'x': [1, 5, 0], 'y': [3, 5, 6]})
    # maxPricedItem = df1['x'].max()
    # minPricedItem = df1['x'].min()

    # maxPricedItem = df1.loc[df1['x'].idxmax()]

    d = {
        'Name': ['Alisa', 'Bobby', 'jodha', 'jack', 'raghu', 'Cathrine',
                 'Alisa', 'Bobby', 'kumar', 'Alisa', 'Alex', 'Cathrine'],
        'Age': [26, 24, 23, 22, 23, 24, 26, 24, 22, 23, 24, 24],

        'Score': [85, 63, 55, 74, 31, 77, 85, 63, 42, 62, 89, 77]}

    df1 = pd.DataFrame(d, columns=['Name', 'Age', 'Score'])
    maxPricedItem = df1['Age'].max()

    print("maxPricedItem : ", maxPricedItem)
    # print("minPricedItem : ", minPricedItem)

    print(df1)


    list1 = {
        ''
    }



def main():
    test()


if __name__ == '__main__':
    main()

