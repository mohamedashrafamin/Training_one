from main import remove_exclamation_marks, remove_exclamation_marks1


def test1(benchmark):
    assert benchmark(remove_exclamation_marks, "Hello World!") == "Hello World"


def test(benchmark):
    assert benchmark(remove_exclamation_marks1, "Hello World!") == "Hello World"

# py.test