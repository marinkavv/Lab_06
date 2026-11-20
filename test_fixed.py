from fixed import merge_all


def test_merge_sorted_parts():

    parts = [
        [1, 4, 7],
        [2, 3, 8],
    ]

    result = merge_all(parts)

    expected = [1, 2, 3, 4, 7, 8]

    assert result == expected
