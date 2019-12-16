import os
from conans import ConanFile, CMake
from conans.tools import download, untargz, patch

class ProjConan(ConanFile):
    name = "meteoio"
    description = """The MeteoIO library aims at making data access easy and safe for numerical simulations in environmental sciences requiring general meteorological data."""
    version = "2.8.0"
    generators = "cmake"
    # settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False],
                "PLUGIN_A3DIO":[True,False],
                "PLUGIN_ALPUG":[True,False],
                "PLUGIN_ARCIO":[True,False],
                "PLUGIN_ARPSIO":[True,False],
                "PLUGIN_BORMAIO":[True,False],
                "PLUGIN_CSVIO":[True,False],
                "PLUGIN_COSMOXMLIO":[True,False],
                "PLUGIN_DBO":[True,False],
                "PLUGIN_GEOTOPIO":[True,False],
                "PLUGIN_GRASSIO":[True,False],
                "PLUGIN_GRIBIO":[True,False],
                "PLUGIN_GSNIO":[True,False],
                "PLUGIN_IMISIO":[True,False],
                "PLUGIN_NETCDFIO":[True,False],
                "PLUGIN_OSHDIO":[True,False],
                "PLUGIN_PGMIO":[True,False],
                "PLUGIN_PNGIO":[True,False],
                "PLUGIN_PSQLIO":[True,False],
                "PLUGIN_SMETIO":[True,False],
                "PLUGIN_SNIO":[True,False],
                "PLUGIN_SASEIO":[True,False],
                "PROJ4":[True,False]
}

    default_options = {"shared": True,
                        "PLUGIN_A3DIO":False,
                        "PLUGIN_ALPUG":False,
                        "PLUGIN_ARCIO":False,
                        "PLUGIN_ARPSIO":False,
                        "PLUGIN_BORMAIO":False,
                        "PLUGIN_CSVIO":False,
                        "PLUGIN_COSMOXMLIO":False,
                        "PLUGIN_DBO":False,
                        "PLUGIN_GEOTOPIO":False,
                        "PLUGIN_GRASSIO":False,
                        "PLUGIN_GRIBIO":False,
                        "PLUGIN_GSNIO":False,
                        "PLUGIN_IMISIO":False,
                        "PLUGIN_NETCDFIO":False,
                        "PLUGIN_OSHDIO":False,
                        "PLUGIN_PGMIO":False,
                        "PLUGIN_PNGIO":False,
                        "PLUGIN_PSQLIO":False,
                        "PLUGIN_SMETIO":False,
                        "PLUGIN_SNIO":False,
                        "PLUGIN_SASEIO":False,
                        "PROJ4":False}


    url="https://models.slf.ch/p/meteoio/"
    license="LGPL v3"

 
    def source(self):
        zip_name ="MeteoIO-%s-src.tar.gz" % self.version
        download("https://models.slf.ch/p/meteoio/downloads/get/%s" % zip_name , zip_name)
        untargz(zip_name)
        os.unlink(zip_name)

    def configure_cmake(self):
        cmake = CMake(self)

        cmake.definitions["BUILD_SHARED_LIBS"]=self.options.shared
        cmake.definitions["PLUGIN_A3DIO"]=self.options.PLUGIN_A3DIO
        cmake.definitions["PLUGIN_ALPUG"]=self.options.PLUGIN_ALPUG
        cmake.definitions["PLUGIN_ARCIO"]=self.options.PLUGIN_ARCIO
        cmake.definitions["PLUGIN_ARPSIO"]=self.options.PLUGIN_ARPSIO
        cmake.definitions["PLUGIN_BORMAIO"]=self.options.PLUGIN_BORMAIO
        cmake.definitions["PLUGIN_CSVIO"]=self.options.PLUGIN_CSVIO
        cmake.definitions["PLUGIN_COSMOXMLIO"]=self.options.PLUGIN_COSMOXMLIO
        cmake.definitions["PLUGIN_DBO"]=self.options.PLUGIN_DBO
        cmake.definitions["PLUGIN_GEOTOPIO"]=self.options.PLUGIN_GEOTOPIO
        cmake.definitions["PLUGIN_GRASSIO"]=self.options.PLUGIN_GRASSIO
        cmake.definitions["PLUGIN_GRIBIO"]=self.options.PLUGIN_GRIBIO
        cmake.definitions["PLUGIN_GSNIO"]=self.options.PLUGIN_GSNIO
        cmake.definitions["PLUGIN_IMISIO"]=self.options.PLUGIN_IMISIO
        cmake.definitions["PLUGIN_NETCDFIO"]=self.options.PLUGIN_NETCDFIO
        cmake.definitions["PLUGIN_OSHDIO"]=self.options.PLUGIN_OSHDIO
        cmake.definitions["PLUGIN_PGMIO"]=self.options.PLUGIN_PGMIO
        cmake.definitions["PLUGIN_PNGIO"]=self.options.PLUGIN_PNGIO
        cmake.definitions["PLUGIN_PSQLIO"]=self.options.PLUGIN_PSQLIO
        cmake.definitions["PLUGIN_SMETIO"]=self.options.PLUGIN_SMETIO
        cmake.definitions["PLUGIN_SNIO"]=self.options.PLUGIN_SNIO
        cmake.definitions["PLUGIN_SASEIO"]=self.options.PLUGIN_SASEIO
        cmake.definitions["PROJ4"]=self.options.PROJ4

        cmake.configure(source_folder="MeteoIO-%s-src" % self.version)
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()
        cmake.install()

    # def install(self):
    #     cmake = self.configure_cmake()
        

    def package(self):
        # all include files should go in include/gsl
        self.copy("*.h", dst="include/meteoio", src="meteoio")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.libs = ["meteoio"]
