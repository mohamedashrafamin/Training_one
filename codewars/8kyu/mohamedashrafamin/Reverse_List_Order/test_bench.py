from main import reverse_list


def test1(benchmark):
    assert benchmark(reverse_list, [1, 2, 3, 4]) == [4, 3, 2, 1]


def test(benchmark):
    assert benchmark(reverse_list, [1, 2, 3, 4]) == [4, 3, 2, 1]

# py.test
