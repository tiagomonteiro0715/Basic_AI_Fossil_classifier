# Basic_AI_Rock_classifier_with_gradio


![Image of a montain](https://github.com/tiagomonteiro0715/Basic_AI_Rock_classifier_with_gradio/blob/main/undraw_Photo_re_5blb.png
)





## Project Description

### What your application does?

This is a simple web app that uses a machine learning model to take a rock image as input and outputs a dictionary containing the confidence levels of each rock label.

### Why you used the technologies you used?

This project employs Python, Gradio.app, and machine learning models created with teachable machine.

It's straightforward to use and teach others with limited knowledge of machine learning, and it's also easy to modify for other image types and maintain.


### Some of the challenges you faced and features you hope to implement in the future?

Choosing the technology: uncertain whether to use the Python combination or another with Tensorflow.js and mainly HTML, CSS, and JavaScript, integrated into a website and app using ElectronJS and Apache Cordova. 

No features are planned for the future as this is a simple educational project.

-----


# Table of Contents
### [ Project Roadmap ](#Project_Roadmap)

### [ How to Install and Run the Project ](#How_to_install)

### [ How to Use the Project ](#How_to_use)

### [Credits, Authors and acknowledgment for contributions](#credits)

-----



<a name="Project_Roadmap">

#### Project Roadmap

This project provides the foundation for any project using two key technologies related to Python and machine learning:

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


-----

</a>

<a name="credits">

#### Include Credits, Authors and acknowledgment for contributions

##### Programmer that wrote the code of this repository

[Tiago Monteiro](https://github.com/tiagomonteiro0715)

##### Geology student from Lisbon University guided the selection of rocks in the images

Tomás Carneiro

Email: tomascarneiro62@gmail.com


Instagram: https://www.instagram.com/tomas_carneiro_999_/

</a>

