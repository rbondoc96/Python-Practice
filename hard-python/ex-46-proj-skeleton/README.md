# How to Create the Project Skeleton

Folder Structure
```
enclosing_folder/
    |__ project_name/           # Root folder for project source
        |__ __init__.py
        |__ submodule1/         # Submodules
            |__ __init__.py
        |__ submodule2/
            |__ __init__.py
    |__ bin/                    # Scripts run on the command line, no modules!
    |__ docs/                   # Any documentation
    |__ tests                   # Root folder for test files
        |__ __init__.py
        |__ test_01.py
        |__ reports/            # Test reporting files
        |__ subtests1/          # Organize categorized tests
            |__ __init__.py
            |__ test_sub_01.py
    |__ setup.py                # Setup file for project distribution
```

1. Initialize virtual environment with the python version desired
`python -m venv folder_name`

2. Start the virtual environment
```
source env/bin/activate     # Linux/MacOS
./env/Scripts/activate      # Windows
```

3. Build module for use in current venv
`python setup.py develop`
    - In the skeleton above, NAME and NAME2 can then be imported.
```
import NAME
import NAME2
```

4. Uninstall module used in current venv
`python setup.py develop --uninstall`

5. Build module for upload to PyPi
`python setup.py sdist`