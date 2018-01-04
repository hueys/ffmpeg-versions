import os.path
import sys

def usage():
	print("Usage: python ffmpeg-versions.py [ffmpeg-dir]")

def libs():
	return ["libavcodec", "libavdevice", "libavfilter", "libavformat", 
	        "libavresample", "libavutil", "libpostproc", "libswresample", 
	        "libswscale"]

def getVersion(file, version):
	for line in file:
		if (line.startswith("#define") and version in line):
			components = line.split()
			
			if (3 == len(components)):
				return str(components[-1])

	return ""

def getMajorVersion(file):
	return getVersion(file, "VERSION_MAJOR")

def getMinorVersion(file):
	return getVersion(file, "VERSION_MINOR")

def getMicroVersion(file):
	return getVersion(file, "VERSION_MICRO")

def getVersionNumber(filePath):
	file = open(filePath, "r")

	major = getMajorVersion(file)
	minor = getMinorVersion(file)
	micro = getMicroVersion(file)

	file.close()

	return ".".join([major, minor, micro])

def printLibraryVersions(ffmpegDir):
	if os.path.isdir(ffmpegDir):
		for lib in libs():
			filePath = os.path.join(ffmpegDir, lib, "version.h")
			print("{} {}".format(lib, getVersionNumber(filePath)))
	else:
		print("{} isn't a directory".format(ffmpegDir))



if __name__ == "__main__":
	if (len(sys.argv) != 2):
		usage()
	else:
		printLibraryVersions(sys.argv[1])
