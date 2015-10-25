
# This is the directory of each type of resource (css, js, jsx) and should be adjacent to the src dir
BUILD_SUBDIR=build/
SOURCE_SUBDIR=src/

all:deps build

deps:
	npm install

build: css-build js-build jsx-build

### Build Static ###

css-build:
	echo "Building CSS"
	compass compile

js-build:
	echo "Building JS"

jsx-build:
	echo "Building JSX"
	node_modules/.bin/jsx ${SOURCE_SUBDIR}/jsx ${BUILD_SUBDIR}/js

### Clean ###

clean:
	echo "Cleaning"
