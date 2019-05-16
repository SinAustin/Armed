#     Armed.
# Object detection for protection.
![](Screenshot%20from%202019-05-16%2014-04-32.png)

## Summary:
This is a project with to see if I can use object detection to identify a firearm in someones possesion.
It is my capstone from General Assembly's Data Science Immersive.
## Problem Statement:
In modern day America nearly 79,000 people are injured  annually from gun violence.
Over 40% of those injuries result in fatalities.  From mass shootings at concerts to the use 
of firearms where the most vulnerable of us learn. The problem of unidentified individuals 
entering our most sensitive and sacred places to do harm with firearms is well known and largely 
unaddressed. 
#
![](/rm_imgs/02.jpg)
## The Proposal:
The public has no idea that someone with a gun is about to wreak havoc until they hear shots in the air. 
Where every second matters, we all wish that someone had seen this terrible act incoming and had locked
a door or given people more time. But usually not one sees or is able to warn people in time. This is were 
Armed comes in. I suggest we create an object detection based  system that is capable of  identifying a weapon 
on a person before a person before the a person intending to do harm begins his attempt.
This system could be run on surveillance cameras inside and outside of any building(say a school) an 
would alert the individuals inside or even put the location on lockdown if it detects a firearm in a person's 
possesion. This project is a base proof of concept for the object detection portion of such a system
## Data 
The images I trained and tested on are from search engines, free to use movies and videos, and personally taken images
to fill in missing angles. I used labelImg to locate and place bounding boxes on the target items in the photos.
Because my main focus was the identying a firearm quickly, I didn't focus on the models with the highest accuracy when choosing a model.
In the end, I used the tensorflow ssd_mobilenet_v1 model.
## Evaluation
This project shows that object detection of firearms works and given stronger hardware and more training data a model could be a 
viable way to protect the people we care about. The next steps in this project would be more training on security footage and the build-out of a popup and warning system.![](/rm_imgs/01.jpg)

### Things used:
###### TensorFlow
###### labelImg
###### Jupyter Notebook
###### Python
###### openCV

### Composed By: Xlegic Sin'Austin

