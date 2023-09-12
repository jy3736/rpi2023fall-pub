import unittest
import subprocess

class TestMainScript(unittest.TestCase):
    def test_main_script(self):
        # Create a subprocess to run main.py
        cmd = ["python", "main.py"]
        input_data = "5\n3\n8\n2\n"  # Simulate user input
        expected_output = "2\n"     # Expected output

        # Run the script and capture its output
        completed_process = subprocess.run(
            cmd,
            input=input_data.encode(),  # Encode the string to bytes
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )

        # Check if the script ran successfully (exit code 0)
        self.assertEqual(completed_process.returncode, 0)

        # Check if the captured output matches the expected output
        self.assertEqual(completed_process.stdout, expected_output)

if __name__ == '__main__':
    unittest.main()
