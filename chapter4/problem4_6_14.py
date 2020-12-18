def prove_transpose(M, u, v):
    """
    M is R * C
    C vecs are u and v

    Prove that M * (u + v) = M * u + M * v
    """
    return M * (u + v) == M * u + M * v
