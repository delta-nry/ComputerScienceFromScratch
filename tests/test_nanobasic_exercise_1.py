# tests/test_nanobasic_exercise_1.py
#
# Copyright 2026 Nathan Yee
#
# Based on Computer Science from Scratch
# Copyright 2021-2022 David Kopec
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# DESCRIPTION
# Tries running all of the example NanoBASIC programs and checks their
# output against the expected output.
import unittest
import sys
from pathlib import Path
from io import StringIO
from NanoBASICExercise1.executioner import execute


# Tokenizes, parses, and interprets a NanoBASIC
# program; stores the output in a string and returns it
def run(file_name: str | Path) -> str:
    output_holder = StringIO()
    sys.stdout = output_holder
    execute(file_name)
    return output_holder.getvalue()


class NanoBASICTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.example_folder = (Path(__file__).resolve().parent.parent
                               / 'NanoBASICExercise1' / 'Examples')

    def test_print1(self):
        program_output = run(self.example_folder / "print1.bas")
        expected = "Hello World\n"
        self.assertEqual(program_output, expected)

    def test_print2(self):
        program_output = run(self.example_folder / "print2.bas")
        expected = "4\n12\n30\n7\n100\t9\n"
        self.assertEqual(program_output, expected)

    def test_print3(self):
        program_output = run(self.example_folder / "print3.bas")
        expected = "E is\t-31\n"
        self.assertEqual(program_output, expected)

    def test_variables(self):
        program_output = run(self.example_folder / "variables.bas")
        expected = "15\n"
        self.assertEqual(program_output, expected)

    def test_goto(self):
        program_output = run(self.example_folder / "goto.bas")
        expected = "Josh\nDave\nNanoBASIC ROCKS\n"
        self.assertEqual(program_output, expected)

    def test_gosub(self):
        program_output = run(self.example_folder / "gosub.bas")
        expected = "10\n"
        self.assertEqual(program_output, expected)

    def test_if1(self):
        program_output = run(self.example_folder / "if1.bas")
        expected = "10\n40\n50\n60\n70\n100\n"
        self.assertEqual(program_output, expected)

    def test_if2(self):
        program_output = run(self.example_folder / "if2.bas")
        expected = "GOOD\n"
        self.assertEqual(program_output, expected)

    def test_fib(self):
        program_output = run(self.example_folder / "fib.bas")
        expected = "0\n1\n1\n2\n3\n5\n8\n13\n21\n34\n55\n89\n"
        self.assertEqual(program_output, expected)

    def test_factorial(self):
        program_output = run(self.example_folder / "factorial.bas")
        expected = "120\n"
        self.assertEqual(program_output, expected)

    def test_gcd(self):
        program_output = run(self.example_folder / "gcd.bas")
        expected = "7\n"
        self.assertEqual(program_output, expected)

    def test_case_insensitive_variables(self):
        program_output = \
                run(self.example_folder / "case_insensitive_variables.bas")
        expected = "10\n10\n10\n10\n"
        self.assertEqual(program_output, expected)

    def test_print_item_list(self):
        program_output = \
                run(self.example_folder / "print_item_list.bas")
        expected = "1 plus 1 is\t2\tand 2 times 3 is\t6\n"
        self.assertEqual(program_output, expected)

    def test_escaped_double_quotes(self):
        program_output = \
                run(self.example_folder / "escaped_double_quotes.bas")
        expected = """Testing
\"This text contains \"escaped double quotes\"\"
Testing\t3\tTesting\t6
\"This text contains \"escaped double quotes\"\"
Testing\t3\t\"This text contains \"escaped double quotes\"\"\t6
Testing\t\"This text contains \"escaped double quotes\"\"\n"""
        self.assertEqual(program_output, expected)

if __name__ == "__main__":
    unittest.main()
