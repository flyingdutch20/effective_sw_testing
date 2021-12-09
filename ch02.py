

def substrings_between(str, open, close):
    """
    The program returns a String Array of substrings, or null if no match.
    Example: if ="axcaycazc", open="a", and close="c", the output would be an array
    containing ["x", "y", "z"], as we have the a<something>c substring three times
    in the original string, the first one containing "x" in between, the second one
    "y", and the last one "z".
    """
    try:
        if str == None or len(open) == 0 or len(close) == 0:
            return None
    except Exception as error:
        raise error
    str_len = len(str)
    if str_len == 0:
        return []
    close_len = len(close)
    open_len = len(open)
    my_list = []
    pos = 0
    while (pos < str_len - close_len):
        try:
            start = str.index(open, pos)
        except:
            break
        start += open_len
        try:
            end = str.index(close, start)
        except:
            break
        my_list.append(str[start:end])
        pos = end + close_len
    if len(my_list) == 0:
        return None
    return my_list

def add_lists_of_integers(left, right):
    if left is None or right is None:
        return None
    try:
        left.reverse()
        right.reverse()
    except Error as error:
        raise error
    result = []
    carry = 0
    for idx in range(0, max(len(left),len(right))):
        try:
            left_digit = left[idx]
        except:
            left_digit = 0
        try:
            right_digit = right[idx]
        except:
            right_digit = 0
        if not 0 <= left_digit <= 9 or not 0 <= right_digit <= 9:
            raise ValueError
        if not isinstance(left_digit, int) or not isinstance(right_digit, int):
            raise ValueError
        sum = left_digit + right_digit + carry
        result.append(sum % 10)
        carry = sum // 10
    result.append(carry) if carry > 0 else 0
    result.reverse()
    while len(result) > 1 and result[0] == 0:
        del(result[0])
    return result