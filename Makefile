test: src/geometry/build/libgeometry.so
	LD_LIBRARY_PATH=src/geometry/build pytest -s -vv

.PHONY: src/geometry/build/libgeometry.so
src/geometry/build/libgeometry.so:
	$(MAKE) -C src/geometry build/libgeometry.so

trace-symbols: src/geometry/build/libgeometry.so
	nm --demangle $<

.PHONY: check
check:
	ruff check

.PHONY: format
format:
	ruff format

.PHONY: clean
clean:
	$(MAKE) -C src/geometry clean
