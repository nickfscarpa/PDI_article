import images_service as images_service
import images_utilities as images_utilities


path1 = 'higher-resolution-bright/'
path2 = 'higher-resolution-dark/'
path3 = 'higher-resolution-vague/'
path4 = 'lower-resolution/'


root = 'C:/Users/User/Documents/GitHub/Math2237/PDI_article/AGAR_dataset/'
subDirectories = [path1, path2, path3, path4]
all_paths = images_utilities.getAllPaths(root, subDirectories)


for path in all_paths:
    images_service.insertImage(path)
