from src.pre_built.counter import count_ocurrences


def test_counter():
    counter = count_ocurrences('data/jobs.csv', 'Python')
    assert counter == 1639
    counter_lower = count_ocurrences('data/jobs.csv', 'python')
    assert counter_lower == 1639
