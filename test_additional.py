from fixed import merge_all


def test_empty_lists():
    assert merge_all([[], []]) == []


def test_duplicates():
    parts = [[1, 2, 2], [2, 3, 3]]

    assert merge_all(parts) == [1, 2, 2, 2, 3, 3]


def test_three_parts():
    parts = [
        [1, 5],
        [2, 4],
        [3, 6],
    ]

    assert merge_all(parts) == [1, 2, 3, 4, 5, 6]


def test_negative_numbers():
    parts = [
        [-5, -1, 3],
        [-3, 0, 2],
    ]

    assert merge_all(parts) == [-5, -3, -1, 0, 2, 3]
