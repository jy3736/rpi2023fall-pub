import unittest
import subprocess
import random

class TestMainScript(unittest.TestCase):
    def test_main_script(self):
        cmd = ["python", "main.py"]

        for _ in range(100):
            a, b, c, d = [random.randint(1,100) for _ in range(4)]
            input_data = f"{a}\n{b}\n{c}\n{d}\n"    
            expected_output = f"{min(a,b,c,d)}"  # Expected output
            print(f"Test case: {a}, {b}, {c}, {d}")
            completed_process = subprocess.run(
                cmd,
                input=input_data,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,  # Use text mode for input/output
            )
            self.assertEqual(completed_process.returncode, 0)
            result = completed_process.stdout.strip()
            self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
