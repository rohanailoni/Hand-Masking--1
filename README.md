
# Hand Masking Using OpenCv

When ever we heard of hand detection we all get to know about Tensorflow or mediapipe pretrained models but actully how really a hand detection works.this code is about detecting hand using thresholding,bitmasking,countur detection,Using convex hull algorithm,Finding convexvity defects for finding space between two Fingers

This was breifly discussed in the medium article [click here](https://medium.com/@rohanailoni/simple-hand-recognition-using-open-cv-1d9ad2e5d13e) 

## Environment Variables

To run this code, you will need to add the following environment variables installed

`Python 3`

`OpenCv`

`Numpy`



  
## Installation and Running

Install Hand-Masking with pip

```bash
  Pip install -r requirments.txt
  python sample.py

```
For testing over single picture used 
```bash
    python hand.py
````
## How convexivty defecty between fingers are found

![Alt text](https://github.com/rohanailoni/Hand-Masking--1/blob/main/assets/defects.png?raw=true)

When you look the space between the fingers they for a triangle 

lets say distance between the fingers as as a;

and distance between the first finger and edge is b;

and distance between the second finger and edge is c;

when we know 3 sides of a triangle the we use Heron'S formula for fining the area and with are finding angle using cosine rule

![Alt text](https://github.com/rohanailoni/Hand-Masking--1/blob/main/assets/herons.gif?raw=true)




## Disadvantages

 - We have used inrange to extract orange-brown color so any background in
 ![Alt txt](https://github.com/rohanailoni/Hand-Masking--1/blob/main/assets/frame.png?raw=true)
 
 - The numbers have been counted on basis of convexity defects so if something like Five number can be also show without convexity defects which is major drawback
 
 - Effective lightning and saturation is required to detect hands it is very difficult for the model to detect at low lightning areas as we used BGR2HSL transformation



 ## Future Work

 - Accuracy will be increased by using dilation image processing technique

 - Will not be using convexity defect for detection of number of fingers

 - An effective ROI(Region of interest ) Will be extracted and be used for training of Neural Network Such that it will not be dependent on Convexity defect between the finger

## Demo

Insert gif or link to demo

![Alt text](https://github.com/rohanailoni/Hand-Masking--1/blob/main/assets/frame%202021-08-20%2019-54-24.gif?raw=true)

  
