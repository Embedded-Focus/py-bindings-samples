#pragma once

#include <geometry.h>

#ifdef __cplusplus
extern "C" {
#endif

Rectangle* rectangle_new(int a, int b);
void rectangle_delete(Rectangle *r);
int rectangle_area(Rectangle const *r);

#ifdef __cplusplus
}
#endif
