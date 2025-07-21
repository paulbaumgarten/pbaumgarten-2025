# https://poe.com/chat/itwcdgfrqg4padgz3p

import os
import sys
import unittest
from unittest.mock import patch
from io import StringIO
import importlib.util

"""
Naming conventions for the tests to be automatically discovered and executed:
* The name of this file must start `test_` (or be manually specified with the --pattern option).
* Classes containing the tests must inherit from `unittest.TestCase`.
* By convention Class names should also start with `Test`.
* Methods within the classes containing tests must start with `test`. Only methods prefixed with test are recognized and executed as tests.
* Run `python -m unittest` to automatically discover all test files in the current directory and subdirectories, executing all tests found
"""

# Define the list of expected exercise files with different test types
TESTS = {
    "exercise_01_hello.py": {
        "type": "io",
        "inputs": [["Alice"], ["Bob"]],
        "outputs": ["Hello, Alice!", "Hello, Bob!"]
    }
}

class TestExercises(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files_found = []
        cls.files_missing = []
        
        # Check which files exist
        for filename in TESTS.keys():
            if os.path.isfile(filename):
                cls.files_found.append(filename)
            else:
                cls.files_missing.append(filename)
        
        print("\nFiles found:", cls.files_found)
        print("Files missing:", cls.files_missing)

    def load_module(self, filename):
        """Helper to load a module from a file"""
        spec = importlib.util.spec_from_file_location(filename[:-3], filename)
        module = importlib.util.module_from_spec(spec)
        sys.modules[filename[:-3]] = module
        spec.loader.exec_module(module)
        return module

    def io_test(self, filename, mock_inputs, expected_output):
        """Test structure for Input/Output mocking"""
        with patch('builtins.input', side_effect=mock_inputs):
            captured_output = StringIO()
            sys.stdout = captured_output
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    file_content = f.read()
                exec(file_content)
                sys.stdout = sys.__stdout__
                self.assertEqual(captured_output.getvalue().strip(), expected_output)
            except Exception as e:
                sys.stdout = sys.__stdout__
                self.fail(f"Error running {filename}: {str(e)}")

    def function_test(self, filename, function_name, test_cases):
        """Test structure for function calls"""
        module = self.load_module(filename)
        func = getattr(module, function_name)
        
        for case in test_cases:
            with self.subTest(case=case):
                result = func(*case["args"])
                self.assertEqual(result, case["expected"])

    def oop_test(self, filename, class_name, test_cases):
        """Test structure for OOP code"""
        module = self.load_module(filename)
        cls = getattr(module, class_name)
        
        for i, case in enumerate(test_cases):
            with self.subTest(case=f"Test {i + 1}"):
                # Initialize object
                obj = cls(*case["init_args"])
                
                # Execute methods
                for method in case["methods"]:
                    method_obj = getattr(obj, method["name"])
                    result = method_obj(*method["args"])
                    
                    # Check return value if expected is not None
                    if method["expected"] is not None:
                        self.assertEqual(result, method["expected"])
                    
                    # For methods that modify state, we might want to add attribute checks here

    def test_all_exercises(self):
        """Run all tests for all found files"""
        for filename in self.files_found:
            tests = TESTS[filename]
            
            with self.subTest(file=filename):
                if tests['type'] == "io":
                    for i in range(len(tests['inputs'])):
                        with self.subTest(case=f"IO Test {i + 1}"):
                            self.io_test(filename, tests['inputs'][i], tests['outputs'][i])
                
                elif tests['type'] == "function":
                    self.function_test(
                        filename,
                        tests['function_name'],
                        tests['test_cases']
                    )
                
                elif tests['type'] == "oop":
                    self.oop_test(
                        filename,
                        tests['class_name'],
                        tests['test_cases']
                    )

if __name__ == '__main__':
    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestExercises)
    
    # Run the tests with more detailed output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*50)
    print("Test Summary:")
    print(f"Files found: {len(TestExercises.files_found)}")
    print(f"Files missing: {len(TestExercises.files_missing)}")
    print(f"Total tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("="*50)