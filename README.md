# c_project_compiler

This is a simple tool which allows you to build **small** C projects without requiring to have BUILD/Makefile files.

To use to tool for running your binary `main.c`:

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

**If** your project is built according to the required structure below, the tool will find all dependencies
to build and run `main.c`, and then will run the following command (approximatelly) to assemble the binary:

```gcc main.c path/to/dependency1.c path/to/dependency2.c ...```

The tool will not compile project files that `main.c` doesn't depend on. Thus, the tool will compile binary faster than simply including all project files into the compilation process (i.e. faster than running ```gcc main.c *.c```).

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

`WORKSPACE` is a text file (could be empty) which marks that the project root is in this directory. It's required for the tool to figure
out the project root from any directory.

Library code needs to be in some subdirectory, such as `library/` subdirectory. We require this because
`#include "function.h"` is ambiguous - should gcc include `function.h` from the root directory, or from the subdirectory we're currently at?
`#include "library/function.h"` resolves the ambiguity.

`main.c` is the binary we want to run, containing the `int main(...)` function. The binary file can be anywhere, including the root directory.
You can also create the `your_test.c` file and place it anywhere, the **c_project_compiler** will compile it.

Every file in this project should include other files as follows:

```
#include <stdio.h> // for standard system includes
#include "library/function.h" // to include project specific files
```

## Example

See `tests/data/project5` for an example project structure that this tool can manage:

```
// This should print some text to the console
run_c tests/data/project5/dir/main.c
```

