def gen_check_digit(tracking):
    '''
    The purpose of this function is for a PIC(package identification code), generate its 10th check digit.
    The method is from Page40 in PUB199IMPBImpGuide.pdf
    :param tracking: tracking would bw
    :return: the full tracking number, it will be a format correct tracking number
    '''
    tracking_reverse = tracking[::-1]
    count_even = count_odd = 0
    for i in range(len(tracking_reverse)):
        if i % 2 == 0:
            count_even += int(tracking_reverse[i])
        else:
            count_odd += int(tracking_reverse[i])

    sum_num = count_even * 3 + count_odd
    sum_ten = int(sum_num / 10) * 10
    if sum_ten == sum_num:
        return str(0)
    else:
        return str(sum_ten + 10 - sum_num)