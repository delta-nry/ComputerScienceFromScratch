# BrainfuckWithDebugMode/__main__.py
#
# The `__main__.py` file for the Brainfuck interpreter implemented with
# bracket location caching and debug mode
# Copyright 2026 Nathan Yee
#
# Based on the Brainfuck interpreter from Computer Science from Scratch
# Copyright 2024 David Kopec
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
from argparse import ArgumentParser
from BrainfuckWithDebugMode.brainfuck_with_debug_mode import Brainfuck

if __name__ == "__main__":
    # Parse the file argument
    file_parser = ArgumentParser("BrainfuckWithDebugMode")
    file_parser.add_argument("brainfuck_file",
                             help="A file containing Brainfuck source code.")
    file_parser.add_argument("-d", "--debug",
                             action="store_true",
                             help="Enable debug mode.")
    arguments = file_parser.parse_args()
    if arguments.debug:
        Brainfuck(arguments.brainfuck_file).execute_debug_mode()
    else:
        Brainfuck(arguments.brainfuck_file).execute()
