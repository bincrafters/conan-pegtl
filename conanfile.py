from conans import ConanFile, tools
import os

class PEGTLConan(ConanFile):
    name = "pegtl"
    version = "2.5.1"
    description = "C++11 header-only parser combinator library for creating PEG parsers"
    url = None
    license = "MIT"
    homepage = "https://github.com/taocpp/PEGTL"
    exports = ["LICENSE.md"]
    source_subfolder = "source_subfolder"

    def source(self):
        source_url = "https://github.com/taocpp/PEGTL"
        tools.get("{}/archive/{}.zip".format(source_url, self.version))
        extracted_dir = "PEGTL-" + self.version

        os.rename(extracted_dir, self.source_subfolder)

    def package(self):
        self.copy(pattern="LICENSE", src=self.source_subfolder)
        self.copy(pattern="*", dst="include/tao", src="{}/include/tao".format(self.source_subfolder))

    def package_id(self):
        self.info.header_only()
