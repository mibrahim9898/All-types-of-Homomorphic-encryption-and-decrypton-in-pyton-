"""
FILE SIZE

Calculates the size of files.
"""

import os


class FileSize:

    def getFileSize(self, filePath):

        fileSize = os.path.getsize(filePath)

        return fileSize

    def displayFileSize(self, filePath, fileType):

        fileSize = self.getFileSize(filePath)

        print(f"{fileType} File Size: {fileSize} bytes")

        return fileSize
