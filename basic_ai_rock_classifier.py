# The above code is importing the necessary libraries for the program to run.
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import gradio as gr

# Load the model
model = load_model(r"keras_model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

rocks_dict_keys = ["Arenito", "Basalto", "Calcite", "Halite", "Marga", "marmore", "Quartzo"]

prediction_values_dict = {}

def histogram(data):
    labels = list(data.keys())
    values = list(data.values())

    fig = gr.data_to_histogram(values)
    fig.update_layout(xaxis_tickvals=list(range(len(labels))),
                      xaxis_ticktext=labels)
    
    return fig

def classify_image(img):
  """
  It takes an image as input, resizes it to be at least 224x224, converts it to an RGB image,
  normalizes it, and then runs it through the model to get a prediction
  
  :param img: The image to classify
  :return: The class name and the confidence score
  """

  '''
  The above code is converting the image to a PIL image, converting the image to RGB format, and
  resizing the image to be at least 224x224 and then cropping from the center.
  '''
  # Convert the input image to a PIL image
  image = Image.fromarray(np.uint8(img))
  # Convert the image to RGB format
  image = image.convert("RGB")
  # Resize the image to be at least 224x224 and then crop from the center
  size = (224, 224)
  image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

  # Turn the image into a numpy array
  image_array = np.asarray(image)
  # Normalize the image
  normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
  #Image size used in training dataset are different from images sizes given as inpt
  correct_size_normalized_image_array = np.reshape(normalized_image_array, (1, 224, 224, 3))


# Predicting the image and then creating a dictionary with the prediction values.
  prediction = model.predict(correct_size_normalized_image_array)
  for i, key in enumerate(rocks_dict_keys):
    prediction_values_dict[key] = prediction[0, i]
  
  return prediction_values_dict



# Changing the style of the output textbox.
style = {
    ".gr-output": {
        "background-color": "#e0e0e0",
        "padding": "20px",
        "font-size": "24px",
    },
}


# Creating the Gradio interface and launching it.
if __name__ == "__main__":
  # Create the Gradio interface
  interface = gr.Interface(
    fn=classify_image, 
    inputs=gr.inputs.Image(), 
    outputs=gr.outputs.Textbox(), 
    title="Basic AI Rock Classifier",
    description="Simple web app that with a machine learning model takes the image of a rock as input and outputs an histogram with the confidence levels of the predictions",
    article = "This project is a very simple project not to be used professionaly",
    style=style
    )
  # Launch the interface
  interface.launch(share=False)