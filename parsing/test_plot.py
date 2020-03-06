import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


main_polyline_data = [
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
                      ]

main_polyline_data2 = [
                        # {"x": 34.2433, "y": 34.8131}, {"x": 34.2809, "y": 22.5561}, {"x": 34.2433, "y": 10.2991},

                        {"x": 35.2433, "y": 35.8131}, {"x": 35.2809, "y": 22.5561}, {"x": 35.2433, "y": 9.2991},

                        {"x": 21.627, "y": 8.9958}, {"x": 20.8195, "y": 9.2975}, {"x": 19.7383, "y": 9.5307},
                        {"x": 18.526, "y": 9.6569}, {"x": 17.334, "y": 9.687}, {"x": 15.8938, "y": 9.6639},
                        {"x": 14.5217, "y": 9.5574}, {"x": 13.444, "y": 9.4198}, {"x": 11.6291, "y": 9.3117},

                        {"x": 9.3544, "y": 19.0818}, {"x": 10.971, "y": 19.2249}, {"x": 11.9908, "y": 19.5745},
                        {"x": 12.9388, "y": 20.0796}, {"x": 13.3905, "y": 20.4738}, {"x": 13.771, "y": 20.9557},
                        {"x": 13.963, "y": 21.3949}, {"x": 14.0955, "y": 21.857}, {"x": 14.1623, "y": 22.2907},
                        {"x": 14.1822, "y": 22.5561}, {"x": 14.1306, "y": 23.0643}, {"x": 13.8878, "y": 23.9012},
                        {"x": 13.5301, "y": 24.5392}, {"x": 13.0933, "y": 24.9331}, {"x": 12.5026, "y": 25.2862},
                        {"x": 11.4175, "y": 25.7369}, {"x": 10.3544, "y": 26.0304}, {"x": 12.6291, "y": 34.8004},
                        {"x": 13.3993, "y": 34.707}, {"x": 14.4711, "y": 34.586}, {"x": 15.7303, "y": 34.4848},
                        {"x": 16.9377, "y": 34.4373}, {"x": 18.304, "y": 34.4405}, {"x": 19.2595, "y": 34.5262},
                        {"x": 20.3902, "y": 34.7088}, {"x": 21.215, "y": 34.9489}, {"x": 21.627, "y": 35.1163},

                        # {"x": 34.2433, "y": 34.8131}
                      ]


def draw_common(my_data):

    df = pd.DataFrame(my_data)
    # df.plot(x='x', y='y', marker='.')
    df.plot('x', 'y', marker='.', markerfacecolor='red', markersize=12, color='skyblue', linewidth=4)
    plt.show()


def draw_common2(my_data):

    plt.plot('x', 'y', data=my_data, marker='.', markerfacecolor='red', markersize=12, color='skyblue', linewidth=4)
    plt.show()


def test_plot():

    # df2 = pd.DataFrame({'x': range(1, 11), 'y2': np.random.randn(10), 'y3': np.random.randn(10)+range(11,21)})

    df = pd.DataFrame(main_polyline_data)
    df2 = pd.DataFrame(main_polyline_data2)
    # df.plot(x='x', y='y', marker='.')

    # plt.plot(df.xvalues, df.yvalues)
    # plt.plot(df.x)

    plt.plot('x', 'y', data=df, marker='.', markerfacecolor='blue', markersize=3, color='skyblue', linewidth=1)
    plt.plot('x', 'y', data=df2, marker='.', markerfacecolor='olive', markersize=3, color='red', linewidth=1)
    # plt.plot('x', 'y2', data=df2, marker='o', color='olive', linewidth=2)
    # plt.plot('x', 'y3', data=df2, marker='o', color='red', linewidth=2, linestyle='dashed', label="toto")
    plt.show()
    # plt.legend()


def main():
    # draw_common(main_polyline_data)
    # draw_common2(main_polyline_data)
    test_plot()


if __name__ == '__main__':
    main()

