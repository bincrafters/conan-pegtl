from conans import ConanFile, tools
import os

class PEGTLConan(ConanFile):
    name = "pegtl"
    version = "2.5.1"
    description = "C++11 header-only parser combinator library for creating PEG parsers"
    url = "https://github.com/bincrafters/conan-pegtl/"
    homepage = "https://github.com/taocpp/PEGTL"
    license = "MIT"
    author = "Bincrafters <bincrafters@gmail.com>"
    exports = ["LICENSE.md"]
    source_subfolder = "source_subfolder"
    no_copy_source = True

    def source(self):
        tools.get("{}/archive/{}.tar.gz".format(self.homepage, self.version))
        extracted_dir = "PEGTL-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)
        self.copy(pattern="*.hpp", dst="include", src="{}/include".format(self.source_subfolder))

    def package_id(self):
        self.info.header_only()
