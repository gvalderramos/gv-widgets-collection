import setuptools
import subprocess

with open("README.md", "r") as fh:
    long_description = fh.read()


with open("requirements.txt", "r") as fh:
    req = fh.readlines()


class BuildSphinx(setuptools.Command):
    """Build Sphinx documentation."""

    description = 'Build Sphinx documentation'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        subprocess.run(["sphinx-build", "-b", "html", "docs/source/", "docs/build/html"], stdout=subprocess.PIPE)


cmdclasses = {}
cmdclasses['build_sphinx'] = BuildSphinx


setuptools.setup(
    name="gvalderramos",
    version="0.1.0",
    author="Gabriel Valderramos",
    author_email="gabrielvalderramos@gmail.com",
    description="A collections of qt widgets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gvalderramos/gv-widgets-collection",
    packages=["GVWidgetsCollection", "GVWidgetsCollection.cards_widget", "GVWidgetsCollection.loading_widget"],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    cmdclass=cmdclasses,
    install_requires=req
)