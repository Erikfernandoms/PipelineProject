from pytest import fixture

@fixture
def event():
    return {"a": 1, "b": 2}