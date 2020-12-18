from chapter2.quiz_2_9_4 import list_dot

def needle_in_haystack(needle, haystack):
    """
    Input: Needle as a unordered list. Haystack as an ordered list
    Output: The dot product that computes the best match between the needle and the haystack

    Example haystack[1, 2, 3, 4] needle[2, 3] 
    """
    needle_len = len(needle)
    return [list_dot(haystack[i:needle_len+i], needle) for i in range(len(haystack) - needle_len+1)]
