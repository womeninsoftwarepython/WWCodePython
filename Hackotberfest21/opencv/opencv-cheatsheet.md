# OpenCV Cheatsheet

## Installing OpenCV

`pip install opencv-python`

## Working on images
  
  1. Read an image from path
  2. Image Resizing
  3. Blurring an Image
  4. Grayscaling of images

## Working with Videos 

  1. Play videos with OpenCv: <br> 
  * Find an video to use 
  - If using Google Colab upload a video to your google drive to use. Add the following code to let google colab access your google drive: 
  ```
      from google.colab import drive
  ``` 
  - Find your video url and add into the wget code inside the double quotes: 
  ```
    !wget = "put your video url here"
  ``` 
  - Also put your ending part of the video url in the cap code inside the parentheses and quote: 
  ``` 
    cap = cv2.VideoCapture('number part.mp4')
  ``` 
  - It will play the video frame by frame. Warning it will be very slow on Google Colab.
  - [sample code](https://github.com/quinnrenee/WWCodePython/blob/master/notebooks/Play_A_Video_with_OpenCV.ipynb)
  2. Extract frames from a video


