def double_eights(n):
    num_list = []
    while n != 0:
        a = n % 10
        num_list.append(a)
        n = n // 10
    i = 0
    while i < len(num_list) - 1:
        if num_list[i] == 8:
            if num_list[i + 1] == 8:
                return True
        i += 1
    return False


print(double_eights(22808821))
