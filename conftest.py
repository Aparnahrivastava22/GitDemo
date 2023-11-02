import pytest


@pytest.fixture()
def setup():
    print("I'm  fixture  executing  first")
    yield
    print("mai  last")
#datadrivendataloading
@pytest.fixture()
def dataLoad():
    print("user profile data being created")
    return["Aparna","Shrivastava","rahulshettyacademy"]
#paarametrizing
@pytest.fixture(params=[("chrome","rahul","shetty"),("firefox","sharma"),("IE","ss")])
def crossBrowser(request):#
    return request.param
