#include <geometry.h>
#include <geometry_wrap.h>

Rectangle *rectangle_new(int a, int b) {
  return new Rectangle(a, b);
}

void rectangle_delete(Rectangle *r) {
  delete r;
}

int rectangle_area(Rectangle const *r) {
  return r->area();
}
