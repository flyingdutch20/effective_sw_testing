

def substrings_between(str, open, close):
    """
    The program returns a String Array of substrings, or null if no match.
    Example: if ="axcaycazc", open="a", and close="c", the output would be an array
    containing ["x", "y", "z"], as we have the a<something>c substring three times
    in the original string, the first one containing "x" in between, the second one
    "y", and the last one "z".
    """
    if str == None or len(open) == 0 or len(close) == 0:
        return None
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