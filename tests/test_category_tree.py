from src.category_tree import Category, create_tree


def test_create_tree():
    given = [
        Category(1, None),
        Category(2, None),
        Category(3, 1),
        Category(4, 1),
        Category(5, 2),
        Category(6, 4)
    ]
    expected = {
        given[0]:
            {
                given[2]: None,
                given[3]:
                    {
                        given[5]: None
                    }
            },
        given[1]:
            {
                given[4]: None
            }
    }
    result = create_tree(given.copy())
    print(result)
    assert result == expected
