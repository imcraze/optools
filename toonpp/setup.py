from distutils.core import setup, Extension

def main():
    setup(name="toonpp",
          version="0.0.3",
          description="Utility functions written in C++ for shit python wont do properly.",
          author="harold",
          author_email="suck@your.mum",
          ext_modules=[Extension("toonpp", ["toonpp.cpp"])])

if __name__ == "__main__":
    main()
