#!/bin/bash

conan create . -s compiler.cppstd=14 --build missing

if [[ $OSTYPE == 'darwin'* ]]; then
  conan create . --build missing --profile:build profiles/macos-profile --profile:host profiles/android-armv7-profile
  conan create . --build missing --profile:build profiles/macos-profile --profile:host profiles/android-armv8-profile
else
  echo 'Cross-building profiles only provided for macOS.'
fi
