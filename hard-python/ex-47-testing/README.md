# Pytest notes


## Flags
`python -m pytest [flags]`

1. -v: Verbose outputs
2. -m MARK: Only run tests given a mark decorator with "MARK" 
    - `@pytest.mark.MARK`
3. -x: Stop all tests when a test fails
4. --maxfail=N: Stops after N tests have failed
5. -r: Adds reporting based on other letters that follow 'r'
    - Ex: `-rsx` shows more details for skipped tests and failed tests
        - f: Failed
        - e: Error
        - s: Skipped
        - x: Failed
        - X: Passed
6. [-s|--capture=no]: Allows for print() statements to run


## Decorators
1. @pytest.mark.skip(reason="Reason why I was skipped")
2. @pytest.mark.skipif(sys.version_info < (3,3), reason="do not run me")
    - Only skip if the condition passes
    - In the example above, sys.version_info --> (maj, min)
3. @pytest.mark.parameterize("arg1", "arg2", "result", List[Tuple[arg1, arg2, result]])
    - Useful for testing the same function, but with different inputs
    - In the decorator, list the arguments + result. Then, pass in an Iterable/List filled with Tuples. These Tuples will be passed in as the argument to the function

    ```python
    @pytest.mark.parameterize("n1", "n2", "result" [
        (7, 3, 10),
        ("Hello", " World", "Hello World"),
        (10.5, 15.5, 26.0)
    ])
    def test_add(n1, n2, result):
        assert add(n1, n2) == result
    ```


## Set Up and Tear Down
```python
db = None

def setup_module(module):
    global db
    db = PerkDB()
    db.connect("data.json")

def teardown_module(module):
    db.close()
```



## Fixtures
An alternative to setup_module and teardown_module methods.

Pytest will recognize the fixutre. Whatever is returned from the fixture is passed as a parameter to the test functions.

Without the scope argument, the fixture would run at the start of every test. (Like setUp)
With the scope set to "module", it only runs once at the very start. (Like setUpClass)

With "return", the fixture just works like setUpClass.
If "yield" is used, code after the yield runs at the very end of the module (like tearDownClass)
```python
@pytest.fixure(scope="module")
def db():
    db = PerkDB()
    db.connect('data.json')
    #return db
    yield db
    db.close()

def test_scott_data(db):
    scott = db.get("scott")

def test_mark_data(db):
    mark = db.get("mark")
```