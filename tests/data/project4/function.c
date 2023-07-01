#include <stdio.h>

#include "function.h"
#include "structure.h"

int function(void) {
  Structure structure;
  structure.number = 123;
  return last_digit(structure);
}
