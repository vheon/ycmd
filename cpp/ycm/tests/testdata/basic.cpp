struct Foo {
  int x; //!< A docstring.
  int y;
  char c;

  int foobar( int i = 5) {
    return i;
  }
};

int main()
{
  Foo foo;
  // The location after the dot is line 15, col 7
  foo.
}
