import lambda_function


def test_handler(event):
    assert lambda_function.lambda_handler(event, "") == 3