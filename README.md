# Basic_AI_Rock_classifier_with_gradio

Place here image related to the projects

---------------------------------------------------------------------------------------------------------


## Project Description

### What your application does?

Simple web app that with a machine learning model takes the image of a rock as input and outputs an histogram with the confidence levels of the predictions
 
### Why you used the technologies you used?

Python, gradio.app and teachable machine

Very simple to use and to teach to others that know little about machine learning    
    
### Some of the challenges you faced and features you hope to implement in the future?

None. This is the base for futuro projects. 

Mainy simple educational projects

-----


# Table of Contents
### [ Project Roadmap ](#Project_Roadmap)

### [ How to Install and Run the Project ](#How_to_install)

### [ How to Use the Project ](#How_to_use)

### [Credits, Authors and acknowledgment for contributions](#credits)

-----



<a name="Project_Roadmap">

#### Project Roadmap

This project is the basic arquitecture for any project that uses two main techinolgies related to python and machine learning:
- Build & share delightful machine learning apps  [gradio.app](https://gradio.app/)
- Tool to very easily create machine learning models [teachable machine](https://teachablemachine.withgoogle.com/)

</a>


<a name="How_to_install">

#### How to Install and Run the Project

See the latest version of pip
```
pip install --upgrade --user pip
```
Install and activate a virtual enviroment
```
pip install virtualenv
```
```
virtualenv <envname>
```
```
source <envname>/bin/activate
```

Install all projects dependencies with the requirements.txt
```
pip install -r requirements.txt
```

</a>

<a name="How_to_use">


#### How to Use the Project

##### By having the share parameter as true in the last value, you can have a link to show the project that can last up to 8 hours I believe:
```
  interface.launch(share=True)
```

In the last section of code in the basic_ai_rock_classifier.py file:
```
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
  interface.launch(share=Flase)
```
Otherwise, It can be used as the arquitecture for any machine learning classification projects with https://teachablemachine.withgoogle.com/ 

</a>

<a name="credits">

#### Include Credits, Authors and acknowledgment for contributions

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus feugiat fringilla eros nec mattis. Cras nec sagittis risus, vel mattis odio. Sed erat massa, commodo nec rutrum ac, tincidunt quis magna. Pellentesque non tristique ante. Phasellus convallis ante tincidunt lacus tempor aliquam. Donec quis ipsum laoreet, pretium ligula quis, pulvinar ante. Nam fringilla nunc in accumsan tempus. 

</a>

