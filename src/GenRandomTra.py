from random import randint
from GenCheckDigit import gen_check_digit
import config as cfg

def gen_valid_tra():
    """
    This function is to internally generate a random valid tracking number(based on decluttr "prefix") and return its information
    :return: orderedDict contain all information relate with one tracking number
    """
    TRADECLUTTR = cfg.tracking_prefix_str

    def generate_random_serial(a, b):
        return randint(a, b)

    # random_serial = TRADECLUTTR + str(generate_random_serial(a = 5753000, b = 5754999))
    random_serial = TRADECLUTTR + str(generate_random_serial(a=1500000, b=1599999))
    random_serial = ''.join(random_serial.split(','))
    random_serial += gen_check_digit(random_serial)
    return random_serial