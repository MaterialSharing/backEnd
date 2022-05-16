import random as rand


class Randoms:
    def get_range_randoms( low: int = 20, high: int = 100, size: int = 10, contain_high: int = 0,
                          sorted: int = 1) -> list[int]:
        '''

        :param low: 随机数下界
        :type low:
        :param high: 随机数上界
        :type high:
        :param size: 需要取出多少个随机数
        :type size:
        :param contain_high:默认开区间; 0表示开区间;1表示闭区间
        :type contain_high:
        :param sorted: 默认排序;0表示排序;1表示排序;
        :type sorted:
        :return:
        :rtype:
        '''
        if contain_high:
            high += 1
        range_list = list(range(low, high))  # 如果需要闭区间,可以为upper_bound+1
        rand.shuffle(range_list)
        shuffled_list = range_list
        sized_list = shuffled_list[:size]
        # print(randon_list)
        ##
        # 可选(排序这些随机数)
        if (sorted):
            sized_list.sort()

        # 查看结果
        return sized_list
