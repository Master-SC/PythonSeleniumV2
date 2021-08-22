# This is a python-selenium framework based on pytest.

All the tests to be written in **TEST PACKAGE -"_tests_"**

Driver setup is done through fixtures in **conftest.py**

A **utilities** package is created for the **baseclass** and driver is driven through the fixture from that.

Provision for running the scripts in Chrome/FireFox/Edge is provided.
By default the scripts will run on **Chrome** Browser in **Headless** mode.We can customize the execution run through command line using the below command. 

To run the tests in Chrome HeadMode we have to provide :- 

**_py.test --browser_name chrome --headless_mode true -v -s_**

To run the tests in Edge Headless mode we have to provide :-

**_py.test --browser_name edge --headless_mode false -v -s_**

i.e _**--browser_name**_ and _**--headless_mode**_ is not case sensitive.

### Design Pattern

Page object Design Pattern is used in this framework.

### Reusable Method

Reusable methods which are common to all testcases is written in BaseClass under utilities package. 

For the Reusable methods which are only specific o certain pages is written inside the page object class of that 
particular Page Object class

### Parameterizing Test with DataSet
We can do parameterization using the ****@pytest.fixture(params=[(dataset1), (dataset2)]**)** we will write the getdata function in the test class itself 
as it specified to a particular test only. 
But with this approch there is one issue that the browser doesn't refresh or re trigger the test in new instance as we made our Driver Setup method on conftest file and it's scope is set as class level
to overcome that ww can do the below option 

1>  Mention the get URL method on each tests.

2> make the driver setup method from class level to method/test level. 

Params can take input from touple as well as dictionary. 

For All the Test Data a separate testData Package is created where for each page particular data is created. 
and we can all the same to our test class fixture.

### Logging
For logging we are using a custom logging method which is present in BaseClass

### Reporting

For Basic PyTest Reporting we can use **py.test --html=report.html** and all the logs will be also attached to the html report.

![img.png](img.png)

To generate Report inside the report folder we have to give the following command. 


**py.test --browser_name CHROME --headless_mode true -v -s**

For Jenkins Build command we can give it as below :- 

**py.test --browser_name CHROME --headless_mode true --html=$WORKSPACE/reports/report.html -v -s**

Where $WORKSPACE is the current project workspace



