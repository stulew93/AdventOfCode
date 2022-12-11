import pytest
import solution as s

@pytest.mark.parametrize(
    ["expected_output", "test_input"],
    157,
    [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]
)
def test_get_total_priority(expected_output, test_input):
    test_output = s.get_total_priority(test_input)
    assert test_output == expected_output
