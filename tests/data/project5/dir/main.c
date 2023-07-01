#include "dir/function.h"
#include "dir/subdir/function.h"
#include "dir2/function.h"

int main(void) {
  dir_function();
  dir_subdir_function();
  dir2_function();

  return 0;
}
