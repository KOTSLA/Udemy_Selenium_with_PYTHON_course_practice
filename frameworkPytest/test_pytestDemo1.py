#any pytest file should start with test_ or end with _test
# pytest method names should start with test
#pip3 install pytest
#any code should be wrapped in method only
# -k stands for method names execution, -s logs in out put, -v stands for more info metdata
#you can run specific file with py.test <filename>
#you can mark (tag) tests @pytest.mark.smoke and then run with -m
#can skip tests with @pytest.mark.skip
#@pytest.mark.xfail

# fixtures are used as setup and tear down methods for test cases- conftest file to generalize
#fixture and make it available to all test cases (fixture name into parameters of method)

#datadriven and parameterization can be done with return statements in tuple format
#when you define fixture scope to class only, it will run once before class is initiate and at the end


import pytest

@pytest.mark.skip
@pytest.mark.smoke                  #custom mark
def test_firstProgram():
    print("Hello")

def test_secondGreedCreditCard():
    print("Good morning")

def test_crossBrowser(crossBrowser):
    print(crossBrowser)
    print(crossBrowser[1])
