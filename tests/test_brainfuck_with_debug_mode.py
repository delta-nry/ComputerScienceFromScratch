# tests/test_brainfuck_with_debug_mode.py
#
# Tests for the Brainfuck interpreter implemented using bracket
# location caching and debug mode
# Copyright 2026 Nathan Yee
#
# Based on tests for the Brainfuck interpreter from Computer Science
# from Scratch
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
# Tries running all of the example Brainfuck programs in non-debug mode
# and debug mode, while checking their output against the expected
# output.
import unittest
import sys
from pathlib import Path
from io import StringIO
from BrainfuckWithDebugMode.brainfuck_with_debug_mode import Brainfuck


# Tokenizes, parses, and interprets a Brainfuck program in non-debug
# mode; stores the output in a string and returns it
def run(file_name: str | Path) -> str:
    output_holder = StringIO()
    sys.stdout = output_holder
    Brainfuck(file_name).execute()
    return output_holder.getvalue()


# Tokenizes, parses, and interprets a Brainfuck program in debug mode;
# stores the output in a string and returns it
def run_debug_mode(file_name: str | Path) -> str:
    output_holder = StringIO()
    sys.stdout = output_holder
    # Create input mock object and assign it to `sys.stdin`
    input_holder = StringIO(initial_value="c\n", newline="\n")
    sys.stdin = input_holder
    Brainfuck(file_name).execute_debug_mode()
    # Close the input IO stream/buffer
    input_holder.close()
    return output_holder.getvalue()


class BrainfuckTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.example_folder = (Path(__file__).resolve().parent.parent
                               / 'BrainfuckWithDebugMode' / 'Examples')

    def test_hello_world(self):
        program_output = run(self.example_folder / "hello_world_verbose.bf")
        expected = "Hello World!\n"
        self.assertEqual(program_output, expected)

    def test_fibonacci(self):
        program_output = run(self.example_folder / "fibonacci.bf")
        expected = "1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89"
        self.assertEqual(program_output, expected)

    def test_cell_size(self):
        program_output = run(self.example_folder / "cell_size.bf")
        expected = "8 bit cells\n"
        self.assertEqual(program_output, expected)

    def test_beer(self):
        program_output = run(self.example_folder / "beer.bf")
        with open(self.example_folder / "beer.out", "r") as text_file:
            expected = text_file.read()
            self.assertEqual(program_output, expected)


class BrainfuckDebugModeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.example_folder = (Path(__file__).resolve().parent.parent
                               / 'BrainfuckWithDebugMode' / 'Examples')

    def test_hello_world(self):
        program_output = run_debug_mode(self.example_folder / "hello_world_verbose.bf")
        expected = """
---

Cell index: 0
Instruction index: 0
Cells:
[
...
]
Enter "s" to step or "c" to continue: Hello World!\n"""
        self.assertEqual(program_output, expected)

    def test_fibonacci(self):
        program_output = run_debug_mode(self.example_folder / "fibonacci.bf")
        expected = """
---

Cell index: 0
Instruction index: 0
Cells:
[
...
]
Enter "s" to step or "c" to continue: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89"""
        self.assertEqual(program_output, expected)

    def test_cell_size(self):
        program_output = run_debug_mode(self.example_folder / "cell_size.bf")
        expected = """
---

Cell index: 0
Instruction index: 0
Cells:
[
...
]
Enter "s" to step or "c" to continue: 8 bit cells\n"""
        self.assertEqual(program_output, expected)

    def test_beer(self):
        program_output = run_debug_mode(self.example_folder / "beer.bf")
        with open(self.example_folder / "beer.out", "r") as text_file:
            expected = """
---

Cell index: 0
Instruction index: 0
Cells:
[
...
]
Enter "s" to step or "c" to continue: """
            expected += text_file.read()
            self.assertEqual(program_output, expected)

if __name__ == "__main__":
    unittest.main()
