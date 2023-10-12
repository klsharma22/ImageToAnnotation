# ImageToAnnotation
A manual generator of annotation file for the image dataset to use it in object detection code


Requirrements:
1.  Python
2.  Tkinter (pip install tk)
3.  opencv (pip install opencv-python)
4.  

Functionalities:
1.  Gives a GUI experience to pin point objects form the image.
2.  Stores the values of xmin, xmax, ymin, ymax of the boundary box created on the object in the image by the user
3.  Creates annotation file (in .xml format) for each image which can be used for object detection model.
