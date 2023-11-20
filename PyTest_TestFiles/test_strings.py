def concat_strings(str1, str2):
    return str1 + str2

def test_concat():
    assert concat_strings('Hello', ' World') == 'Hello World'
    assert concat_strings('Py', 'Test') == 'PyTest'