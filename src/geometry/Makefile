all: build/libgeometry.so

.PHONY: build/libgeometry.so
build/libgeometry.so:
	cmake -S . -B build -G Ninja -D CMAKE_EXPORT_COMPILE_COMMANDS=True
	ln -sf build/compile_commands.json compile_commands.json
	cmake --build build --verbose

.PHONY: clean
clean:
	rm -rf build
