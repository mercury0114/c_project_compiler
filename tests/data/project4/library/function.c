#include <stdio.h>

#include "library/function.h"
#include "library/structure.h"

int function(void) {
  Structure structure;
  structure.number = 123;
  return last_digit(structure);
}
