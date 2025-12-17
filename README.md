# Advent of Code

![CI](https://github.com/slangenbach/advent-of-code/actions/workflows/ci.yml/badge.svg)

Python-powered solutions to puzzles from [advent of code][1] from 2022 onwards.

## Prerequisites

- [uv][2]
- [Task][3]

## Installation

1. Setup the development environment: `task setup`

## Configuration

1. Get the session token from the [AOC][1] website as explained [here][4]
1. Save the token locally: `task aoc:save-token TOKEN=<YOUR_SESSION_TOKEN>`

## Usage

### Scaffolding project structure for a new season

1. Set up the project structure: `task aoc:new-year YEAR=<YEAR>`

### Scaffolding files for a new puzzle

1. Create the files for the puzzle and its test: `task aoc:new-day YEAR=<YEAR> DAY=<DAY>`
1. Download the puzzle and example data: `task aoc:get-data YEAR=<YEAR> DAY=<DAY>`
1. Extract relevant information from the example data dump (c.f limitations section)
1. Open the puzzle file and type `sn-puzzle` to populate it with the puzzle snippet
1. Open the test file and type `sn-test` to populate it with the test snippet

## Limitations

Example data is not yet cleaned automatically.

## Troubleshooting

### Session token expired

tbd


[1]: https://adventofcode.com/
[2]: https://docs.astral.sh/uv/
[3]: https://taskfile.dev/
[4]: https://github.com/wimglenn/advent-of-code-wim/issues/1
