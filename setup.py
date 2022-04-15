from setuptools import setup, find_packages

classifiers = [
 	"Development Status :: 5 - Production/Stable",
 	"Intended Audience :: Education",
 	"Operating System :: Microsoft :: Windows :: Windows 10",
 	"License :: OSI Approved :: MIT License",
 	"Programming Language :: Python :: 3"
]

setup(
 	name="youtube-download-manager",
 	version="1.0",
 	description="A GUI that used to download videos from youtube",
	long_description=open("README.md").read() + "\n\n" + open("CHANGELOG.txt").read(), 
 	url="https://github.com/Mustfa1999/youtube-download-manager",
 	author="Mustafa Alhasanat",
	author_email="mustafa.hasanat99@gmail.com",
 	classifiers= classifiers,
 	keywords="GUI, youtube, download, video, music, mp3, mp4, download manager, downloader, downloader gui",
 	packages=find_packages(),
 	install_requires=["paffy", "tkinter", "PIL", "webbrowser", "urllib", "io", "threading"],
)
