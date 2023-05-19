from lambda_function import lambda_handler


event = {"a": 1, "b": 2}

def test_handler(event):
    assert lambda_handler(event) == 3