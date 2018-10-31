
# conan-polars
A conan wrapper for https://github.com/felix-org/polars


### Build instructions


To add Polars to your conan cache:
```sh
$ conan create . user/channel -s cppstd=14
```

#### Dependencies
Polars requires the following prebuilt package to be available for the environment you are building for in your local conan cache
* `Armadillo/9.200.1@felix/stable`
* `Date/2.4.1@felix/stable`

:warning: Conan wrappers for these have not yet been published. [coming soon]
