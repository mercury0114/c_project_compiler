# c_project_compiler

`c_project_compiler` is a tool to compile and run **small** C projects without creating BUILD/Makefile files.

To use the tool for running your binary `main.c`:

1) Download the project

2) Create a convenient alias for the `run_program_c.sh` script located in the directory where you downloaded the project:

    ```
    alias run_c=/path/to/c_project_compiler/run_program_c.sh
    ```

    (Note: you can save an alias for permanent use in the `~/.bashrc` file)

3) Run the program specifying a **relative** path from the current directory to the `main.c` file:

    ```
    // If you are in the same directory where main.c is:
    run_c main.c

    // If you are in a different directory than where main.c is:
    run_c relative/path/to/main.c

    // Note that backward paths are also supported, for example:
    run_c ../../main.c
    ```

**IF** your project is built according to the required structure below, the tool will:

1. Find all dependencies to compile `main.c`.
2. Compile `main.c` into a binary by running the command similar to:
```
gcc main.c path/to/dependency1.c path/to/dependency2.c ...
```
3. Run the compiled binary

The tool will not compile project files that `main.c` doesn't depend on. Thus, the tool will compile the binary faster than simply including all project files into the compilation process (i.e. faster than running ```gcc main.c *.c```).

## Required Structure

Project directory should have the following structure:

```
    project_root/
                 WORKSPACE
                 main.c
                 library/
                        function.h
                        function.c
                
```

`WORKSPACE` is a text file (could be empty) which marks that the project root is in this directory. The tool requires `WORKSPACE` file to figure out the project root directory from any directory.

Library code needs to be in some subdirectory, such as `library/` subdirectory. Otherwise it is not clear whether `#include "function.h"` refers to the file in the root directory, or the
subdirectory we're currently at. `#include "library/function.h"` resolves the ambiguity.

For every library implementation file `function.c` there must be a header file `function.h` with the same name in the same directory, otherwise the tool will not find the implementation file.

`main.c` is the binary we want to run, containing the `int main(...)` function. The binary file can be anywhere, including the root directory.
You can also create `your_test.c` file and place it anywhere, the **c_project_compiler** will compile it.

Every file in this project should include other files as follows:

```
#include <stdio.h> // for standard system includes
#include "library/function.h" // to include project specific files
```

## Example

See `tests/data/project5` for an example project structure that this tool can manage:

```
// Successful run should print some text to the console
run_c tests/data/project5/dir/main.c
```

