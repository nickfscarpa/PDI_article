import images_service as images_service
import os as os


def getImgsFromFolder(folder):
    return os.listdir(folder)


def getAllPaths(root, directories):
    all_images = []
    for subDirectories in directories:
        newPath = f"{root}{subDirectories}"
        currentFolder_Images = getImgsFromFolder(newPath)
        for filename in currentFolder_Images:
            if filename.endswith(".jpg"):
                all_images.append(f'{newPath}{filename}')
    return all_images
