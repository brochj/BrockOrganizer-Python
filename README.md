# Organize Files with Python 


#### @author: Oscar Broch - [Github](https://github.com/brochj)  
>Created on May 27, 2018  
Last Update: July 22, 2019  
based on: [junk file organizer python](https://www.geeksforgeeks.org/junk-file-organizer-python/)

- ## How to use

    ### 1. Put the script inside the folder that you want to organize.
    ### 2. Run the script.
---
- ## Screenshots
  - **Before run the script**   
     ![Before][before]
  - **During**   
     ![during][during]
  - **After run the script**   
     ![after][after]
---
- ## Adding more extensions files  

- ### Just add your extension inside the existing list. 

    ```python
    EXTENSIONS = {
        "EXECUTABLES": ['.exe', '.msi', '.jar', '.apk', ..., '.YOUR_NEW_EXTENSION' ],
        "IMAGES": ['.jpeg', '.jpg', '.tiff', '.gif', ..., '.YOUR_NEW_EXTENSION' ],
        "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ... ],
        "DOCUMENTS": ['.txt', '.epub', '.pages', '.docx', ... ],
        "PDFS": ['.pdf'],
        "COMPRESSED": ['.rar', '.zip', '.7z', '.bzip2', ... ],
        "SCRIPTS": ['.ahk', '.js', '.json', ... ],
    }
    ```
## or

- ### Create your new category adding a new key inside the dictionary
   ```python
    EXTENSIONS = {
        "EXECUTABLES": ['.exe', '.msi', '.jar', '.apk', ... ],
        "IMAGES": ['.jpeg', '.jpg', '.tiff', '.gif', ... ].
        ...
        ...        
        "YOUR_CUSTOM_FOLDER_NAME": ['.exe','.jpeg','.json', '.example1', ... ]
    }
    ```

<!-- IMAGES -->
[before]: https://github.com/brochj/BrockOrganizer-Python/blob/master/assets/before.PNG "before run script"   
[during]: https://github.com/brochj/BrockOrganizer-Python/blob/master/assets/during.PNG "during run script"   
[after]: https://github.com/brochj/BrockOrganizer-Python/blob/master/assets/after.PNG "after run script"  