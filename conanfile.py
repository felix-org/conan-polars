from conans import ConanFile, CMake, tools


class PolarsConan(ConanFile):
    name = "Polars"
    version = "0.1"
    license = "MIT License"
    url = "https://github.com/felix-org/polars"
    description = "A C++ TimeSeries library that aims to mimic pandas Series"
    settings = "cppstd", "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    build_policy = "missing"
    requires = "Armadillo/9.200.1@felix/stable", "Date/2.4.1@felix/stable"

    def source(self):
        git = tools.Git()
        git.clone("https://github.com/felix-org/polars.git", "master")

        # Add conan_basic_setup() to ensure resolved dependencies are linked
        tools.replace_in_file("src/cpp/polars/CMakeLists.txt", "add_library(polars_cpp ${CPP_SOURCES})",
        '''include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
        conan_basic_setup()
        add_library(polars_cpp ${CPP_SOURCES})''')


    def configure(self):
        del self.settings.compiler.libcxx

    def build(self):
        cmake = CMake(self)
        cmake.definitions["WITH_TESTS"] = "OFF"
        cmake.definitions["WITH_SUBMODULE_DEPENDENCIES"] = "OFF"
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="src/cpp")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["polars_cpp"]
