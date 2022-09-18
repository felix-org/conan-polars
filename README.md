
# conan-polars
A conan wrapper for https://github.com/felix-org/polars


### Build instructions


To add Polars to your conan cache:
```sh

conan create . -s compiler.cppstd=14 --build missing

```


#### Dependencies
Polars requires the following prebuilt package to be available for the environment you are building for in your local conan cache
* `Armadillo/9.200.1`
* `Date/2.4.1`
