# DeepClassifyML


A Web Application made with Flask to classify Respiratory Diseases from Chest X-rays

## Requirements
- Python 3.6
- [Google Collab]() (To re-train or fine tune the model)

## Installation

### Web App
1) Clone the repository and open DeepClassifyML
2) Use `pip install -r requirements.txt` to install all the packages necessary to run the Web App.

### Jupyter Notebook
1) Export the file `Inception_v3_fine_tune.ipynb` to [Google Colab]() if you want to fine tune the model and export your own `model.h5` file.


## Running it
There are currently two ways of running this and obtaining predictions.
1) **URL Prediction**
> To use this option run `python3 server.py` and open `0.0.0.0:8080` in your browser. This will let you add a chest x-ray image already uploaded to the internet and diagnose the the patients condition.
2) **Image Upload Prediction**
> To use this option (which is still very buggy at the momemnt) run `python3 server_new.py` and open `0.0.0.0:8080` This will let you upload a chest x-ray image file from your system and diagnose the the patients condition.

## Notes
- The Dataset used to train the model is [ChestXray14]() you can find out more about it [here]()
- Transfer Learning was used to make [ImageNet]() predict and give output pased off of the [dataset]()
- The Image Upload method is currenty very buggy, WIP.


## Contributors
- [Prince Canuma]()
- [Daniel Phiri]()
- [Vishwa Mehta]()
- [Mayur Patil]()
- [Parth Purohit]()

Based off [this]() Image Classifer Web Application. 
Feel free to open up an issue or contribute to the project.

