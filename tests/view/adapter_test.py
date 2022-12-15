from view.adapter import ViewAdapter


def test_under_limit():
    s = 'This is text\n\nof two lines'
    adapter = ViewAdapter(s, 100)
    adapted = adapter.adapt()
    assert len(adapted) == 1
    assert adapted[0] == s


def test_cuts():
    s = 'This is text\n\nof two lines'
    adapter = ViewAdapter(s, 20)
    adapted = adapter.adapt()
    assert len(adapted) == 2
    assert adapted[0] == 'This is text'
    assert adapted[1] == '...\nof two lines'


def test_uncutable():
    s = 'This is text of two lines\nwhich are long enough and this is thewordwhichistoolongtoprocess'
    adapter = ViewAdapter(s, 20)
    adapted = adapter.adapt()
    assert len(adapted) == 6
    assert adapted[0] == 'This is text of two...'
    assert adapted[1] == '...lines'
    assert adapted[2] == '...\nwhich are long...'
    assert adapted[3] == '...enough and this is...'
    assert adapted[4] == '...thewordwhichistoolong...'
    assert adapted[5] == '...toprocess'


def test_multiple_breaks():
    s = 'This is text\n\nof two lines\n\nwhich are long'
    adapter = ViewAdapter(s, 20)
    adapted = adapter.adapt()
    assert len(adapted) == 3
    assert adapted[0] == 'This is text'
    assert adapted[1] == '...\nof two lines'
    assert adapted[2] == '...\nwhich are long'


def test_exactly_three_cuts():
    s = '12345\n\n23456\n\n34567'
    adapter = ViewAdapter(s, 5)
    adapted = adapter.adapt()
    assert len(adapted) == 3
    assert adapted[0] == '12345'
    assert adapted[1] == '...\n23456'
    assert adapted[2] == '...\n34567'


def test_approx_three_cuts_1():
    s = '12345\n\n23456\n\n34567'
    adapter = ViewAdapter(s, 6)
    adapted = adapter.adapt()
    assert len(adapted) == 3
    assert adapted[0] == '12345'
    assert adapted[1] == '...\n23456'
    assert adapted[2] == '...\n34567'


def test_approx_three_cuts_2():
    s = '12345\n\n23456\n\n34567'
    adapter = ViewAdapter(s, 9)
    adapted = adapter.adapt()
    assert len(adapted) == 3
    assert adapted[0] == '12345'
    assert adapted[1] == '...\n23456'
    assert adapted[2] == '...\n34567'


def test_top_three_cuts_2():
    s = '12345\n\n23456\n\n34567'
    adapter = ViewAdapter(s, 11)
    adapted = adapter.adapt()
    assert len(adapted) == 3
    assert adapted[0] == '12345'
    assert adapted[1] == '...\n23456'
    assert adapted[2] == '...\n34567'
