from chapter2.quiz_2_9_4 import list_dot

def dot_product_list(needle, haystack):
    """
    Input: A short list needle and a long list haystack, both containing n numbers
    Output: A list of length len(haystack-len(needle)) such that entry i of the output list equals the dot product 
            of the needle with the equal sublist of haystack starting at position i
    """
    needle_len = len(needle)
    return [list_dot(needle, haystack[i:i+needle_len]) for i in range(len(haystack) - needle_len)]
