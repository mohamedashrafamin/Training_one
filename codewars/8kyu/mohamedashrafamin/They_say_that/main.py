def is_opposite(s1, s2):
    res = False
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            return False
        if (str.upper(s1[i]) == s2[i]) or (str.upper(s2[i]) == s1[i]):
            res = True
        else:
            return False
    return res


def is_opposite1(s1, s2):
    return False if not (s1 or s2) else s1.swapcase() == s2



# ---------------------------------------------------------------------------------------- benchmark: 2 tests ----------------------------------------------------------------------------------------
# Name (time in ns)          Min                    Max                Mean              StdDev              Median               IQR             Outliers  OPS (Mops/s)            Rounds  Iterations
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# test1                   0.0000 (1.0)      21,934.5093 (22.17)    876.6716 (4.75)     899.5128 (19.33)    953.6743 (5.56)     0.0000 (1.0)      235;16669        1.1407 (0.21)      49933           1
# test                  159.7404 (inf)         989.4371 (1.0)      184.4284 (1.0)       46.5279 (1.0)      171.6614 (1.0)      9.5367 (inf)      3471;3791        5.4222 (1.0)       55925         100
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
