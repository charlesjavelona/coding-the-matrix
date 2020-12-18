from Vec import Vec
def zero_vec(D):
    return Vec(D, {d:0 for d in D })


if __name__ == '__main__':
    print(zero_vec({'a': 1, 'b': 2}).F)

