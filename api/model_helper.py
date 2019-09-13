import requests
import torch
import numpy as np

from PIL import Image
from io import BytesIO
from matplotlib.pyplot import imshow

from api.models.net import Net

classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

def download_model(url):
    '''
    Download the model from the specified url and store it in the data folder.
    '''
    return True

def load_model(filepath):
    new_model = Net()
    new_model.load_state_dict(torch.load(filepath))
    new_model.eval()
    return new_model

def build_class_dict(array, classes):
    '''
    Builds a dictionary out of the result array and provided classes.
    '''
    class_dict = {}
    print(type(array))
    if( type(array) == torch.Tensor):
        array = array.tolist()[0]
        print(array)
    
    if( len(array) != len(classes) ):
        raise Exception("Incorrect mapping of results to classes.")
    
    softmax_array = softmax_naive(array)
    
    for i in range(0, len(array)):
        class_dict[ classes[i] ] = 0.0 if softmax_array[i] < 0.0000001 else softmax_array[i]
        
    return class_dict
    
def softmax_naive(array):
    e_x = np.exp(array - np.max(array))
    return e_x / e_x.sum()

def predict_from_url(image_url, model):
    '''
    Get the output of a prediction on the model for the image at the url.
    '''
    try:
        # load image
        url_response = requests.get(image_url)

        # convert to PIL Image
        image_pil = Image.open(BytesIO(url_response.content))

        # transform PIL Image to numpy - IMPORTANT: Convert to dtype=np.float32
        image_numpy = np.asarray(image_pil, dtype=np.float32)

        # transpose the data to be in the correct format for the model. From (32,32,3) to (3,32,32) -> (2,0,1)
        image_numpy_t = np.transpose(image_numpy, (2, 0, 1))

        # build a tensor from the numpy array
        image_tensor = torch.from_numpy(image_numpy_t)

        # Make the prediction
        y_pred = model(image_tensor[None, :, :])
        return build_class_dict(y_pred, classes)
    except:
        raise Exception("Provided image could not be evaluated.")

