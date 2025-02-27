HW_SOURCE_FILE = __file__


def num_eights(n):
    """Returns the number of times 8 appears as a digit of n.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
    True
    """
    if n < 10:
        return 1 if n == 8 else 0
    return num_eights(n // 10) + (1 if n % 10 == 8 else 0)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    def pingpong_helper(index, value, direction):
        if index == n + 1:  # 因为从 1 开始，n+1 时停止
            return value
        if num_eights(index) > 0 or index % 8 == 0:
            return pingpong_helper(index + 1, value + direction, -direction)
        return pingpong_helper(index + 1, value + direction, direction)
    
    return pingpong_helper(1, 0, 1)  # 从索引 1、值 0、方向 1 开始

def next_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> next_larger_coin(1)
    5
    >>> next_larger_coin(5)
    10
    >>> next_larger_coin(10)
    25
    >>> next_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def next_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> next_smaller_coin(25)
    10
    >>> next_smaller_coin(10)
    5
    >>> next_smaller_coin(5)
    1
    >>> next_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    def count_with_max_coin(remaining, max_coin):
        # remaining: 剩余金額
        # max_coin: 当前允许使用的最大硬币面值
        if remaining == 0:  # 剩余金额为 0，找到一种有效方法
            return 1
        if remaining < 0 or max_coin is None:  # 金额为负或无硬币可用
            return 0
        
        # 递归计算：
        # 使用 max_coin 的方法数 + 不使用 max_coin 的方法数
        include = count_with_max_coin(remaining - max_coin, max_coin)  # 使用当前硬币
        exclude = count_with_max_coin(remaining, next_smaller_coin(max_coin))  # 不使用当前硬币
        return include + exclude
    
    return count_with_max_coin(change, 25)  # 从最大硬币 25 开始
