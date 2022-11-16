from src.ValidParentheses import Solution


def test1():
    given = "(([]){})"
    assert Solution().isValid(given)


def test2():
    given = "[({(())}[()])]"
    assert Solution().isValid(given)