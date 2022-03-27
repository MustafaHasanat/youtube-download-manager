from setuptools import setup, find_packages

classifiers = [
 	"Development Status :: 5 - Production/Stable",
 	"Intended Audience :: Education",
 	"Operating System :: Microsoft :: Windows :: Windows 10",
 	"License :: OSI Approved :: MIT License",
 	"Programming Language :: Python :: 3"
]

setup(
 	name="my project 1",
 	version="1.0",
 	description="a description for the project",
	long_description=open("README.md").read() + "\n\n" + open("CHANGELOG.txt").read(), 
 	url="www.project1.com",
 	author="my name",
	author_email="me@gmail.com",
 	classifiers= classifiers,
 	keywords="word1, word2",
 	packages=find_packages(),
 	install_requires=["paffy", "tkinter"]
)
