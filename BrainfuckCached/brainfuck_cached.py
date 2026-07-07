# BrainfuckCached/brainfuck_cached.py
#
# Brainfuck interpreter implemented with bracket location caching
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
from pathlib import Path
from dataclasses import dataclass


@dataclass
class Caches:
    start_to_end_brackets_cache: dict[int, int]
    end_to_start_brackets_cache: dict[int, int]


class Brainfuck:
    def __init__(self, file_name: str | Path):
        with open(file_name, "r") as text_file:
            self.source_code: str = text_file.read()

    def create_caches(self) -> Caches:
        # Setup state
        cells: list[int] = [0] * 30000
        cell_index = 0
        instruction_index = 0
        # Stack to keep track of matching square brackets.
        # Holds the indicies of `[` that will be matched with the
        # indices of their corresponding `]` characters
        stack = []
        # Cache `[`s as keys and their matching `]`s as values
        start_to_end_brackets_cache = {}
        # Cache `]`s as keys and their matching `[`s as values
        end_to_start_brackets_cache = {}
        # Keep going as long as there are potential instructions left
        while instruction_index < len(self.source_code):
            instruction = self.source_code[instruction_index]
            match instruction:
                case "[":
                    stack.append(instruction_index)
                case "]":
                    if len(stack) > 0:
                        matching_bracket_index = stack.pop()
                        start_to_end_brackets_cache[matching_bracket_index] = (
                                instruction_index)
                        end_to_start_brackets_cache[instruction_index] = (
                                matching_bracket_index)
            instruction_index += 1
        return Caches(start_to_end_brackets_cache, end_to_start_brackets_cache)

    def execute(self):
        # Cache starting and ending bracket locations
        caches = self.create_caches()
        # Setup state
        cells: list[int] = [0] * 30000
        cell_index = 0
        instruction_index = 0
        # Keep going as long as there are potential instructions left
        while instruction_index < len(self.source_code):
            instruction = self.source_code[instruction_index]
            match instruction:
                case ">":
                    cell_index += 1
                case "<":
                    cell_index -= 1
                case "+":
                    cells[cell_index] = clamp0_255_wraparound(
                            cells[cell_index] + 1)
                case "-":
                    cells[cell_index] = clamp0_255_wraparound(
                            cells[cell_index] - 1)
                case ".":
                    print(chr(cells[cell_index]), end='', flush=True)
                case ",":
                    cells[cell_index] = clamp0_255_wraparound(int(input()))
                case "[":
                    if cells[cell_index] == 0:
                        instruction_index = self.find_bracket_match(
                                instruction_index, caches, True)
                case "]":
                    if cells[cell_index] != 0:
                        instruction_index = self.find_bracket_match(
                                instruction_index, caches, False)
            instruction_index += 1

    # Find the location of the corresponding bracket to the one at
    # *start*
    # If *forward* is true go to the right looking for a matching "]"
    # Otherwise do the reverse
    def find_bracket_match(
            self, start: int, caches: Caches, forward: bool) -> int:
        if forward:
            return caches.start_to_end_brackets_cache[start]
        else:
            return caches.end_to_start_brackets_cache[start]


# Simulate a 1 byte unsigned integer
def clamp0_255_wraparound(num: int) -> int:
    if num > 255:
        return 0
    elif num < 0:
        return 255
    else:
        return num
