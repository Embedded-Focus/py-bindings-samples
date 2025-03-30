#pragma once

class Rectangle {
public:
  Rectangle(int a, int b) : a{a}, b{b} {}

  int area() const;

private:
  int a;
  int b;
};
