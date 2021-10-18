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
  * find an video to use 
  - if using google colab upload a video to your google drive to use Add the following code to let google colab access your google drive: 
  ```
      from google.colab import drive
  ``` 
  - Find your video url and add into the wget code inside the double quotes: 
  ```
    !wget = "put your video url here"
  ``` 
  -Also put your ending part of the video url in the cap code inside the parentheses and quote: 
  ``` 
    cap = cv2.VideoCapture('number part.mp4')
  ``` 
  - just play the code and it'll the video frame by frame, warning it'll be very slow on google colab
  [sample code](https://github.com/quinnrenee/WWCodePython)
  2. Extract frames from a video


