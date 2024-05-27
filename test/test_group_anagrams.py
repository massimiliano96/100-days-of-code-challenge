from src.examples.group_anagrams import group_anagrams


# Verify that anagrams are grouped together correctly
def test1():
    inputs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    result = group_anagrams(inputs)
    assert sorted([sorted(group) for group in result.values()]) == sorted(
        [sorted(group) for group in expected]
    )


# Input list is empty
def test2():
    inputs = []
    expected = []
    result = group_anagrams(inputs)
    assert list(result.values()) == expected
