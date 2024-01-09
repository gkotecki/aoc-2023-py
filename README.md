# Advent of Code 2023

## Python solutions
Python solutions are located in /days/*/**.py, organized by day and part. Input files on same folder.

Just run the appropriate file directly, no dependencies.

## Rust solutions
Rust solutions are using the same input files as the Python solutions, but are located in /src/bin/ to facilitate execution of multiple binaries through cargo.

To compile and run a `05.rs` file, run the following command from the root directory of the project:

```bash
cargo run --bin 05
```
```bash
cargo run --release --bin 05
```

Debug mode is default, use `--release` flag for _blazingly fast (r)_ mode.
