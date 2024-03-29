# The above code is importing the necessary libraries for the program to run.
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import gradio as gr
import matplotlib.pyplot as plt

# Load the model
model = load_model(r"keras_model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# Opening the labels.txt file and reading the lines.
with open('labels.txt') as f:
    lines = f.readlines()

# Creating a list of the names of the fossils.
fossils_dict_keys = []
for line in lines:
    if line.strip():
        number, name = line.split()
        fossils_dict_keys.append(name)
        
        
prediction_values_dict = {}

def plot_pie_chart(data):
    # get the sum of all values
    total = sum(data.values())

    # sort the data by value in descending order
    sorted_data = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))

    # create a new dictionary with the four biggest slices and group the rest as "others"
    new_data = dict(list(sorted_data.items())[:3])
    others_size = total - sum(new_data.values())
    new_data['others'] = others_size

    # create the pie chart
    labels = list(new_data.keys())
    sizes = list(new_data.values())

    explode = (0.1, 0, 0, 0)

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', 
            explode=explode,startangle=90 )
    ax.axis('equal')
    plt.close(fig)

    # save the pie chart as a NumPy array
    fig_canvas = fig.canvas
    fig_canvas.draw()
    fig_array = np.frombuffer(fig_canvas.buffer_rgba(), dtype=np.uint8)

    # reshape the array to the original figure size
    fig_array = fig_array.reshape(fig_canvas.get_width_height()[::-1] + (4,))

    return fig_array



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
  for i, key in enumerate(fossils_dict_keys):
    prediction_values_dict[key] = prediction[0, i]

  
  return plot_pie_chart(prediction_values_dict)



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
    outputs='image',
    title="Basic AI fossil Classifier",
    description="Simple web app that with a machine learning model takes the image of a fossil as input and outputs an pie chard with the confidence levels of the predictions",
    article = "This project is a very simple project not to be used professionaly",
    style=style
    )
  # Launch the interface
  interface.launch(share=False)
