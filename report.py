


import pandas as pd
import torch 
import torch.nn as nn 
from PIL import Image
from torch.utils.data import Dataset,DataLoader
from chat.utils import*
from torchvision import transforms



#cnn model for anaylazing the image
class cnn_model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3,16,3,1,1)
        self.polling = nn.MaxPool2d(2,2,0)
        self.fc1 = nn.Linear(16*64*64,128)
        self.fc2 = nn.Linear(128,3) # assuming three class fat ,skinny, athlete person
    def forward(self,x):
        x = self.polling(torch.relu(self.conv1(x)))
        #x = x.view(-1,16*64*64,128)
        x = x.view(x.size(0), -1) # Flatten the tensor, keeping the batch size
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)

        return x
    
model =cnn_model()

# Load the state dictionary 
model.load_state_dict(torch.load('my_model_weights.pth')) 
# Set the model to evaluation mode model.eval()


def image_checker(image_path):
    image = Image.open(image_path)
    image = image.convert("RGB")
    transform_pipeline =transforms.Compose([
        transforms.Resize((128,128)),#resize the image
        transforms.ToTensor(),#covert image to tensor
        transforms.Normalize(mean = [0.485,0.456,0.406],std = [0.229,0.224,0.225])#normailze if need
    ])
    image = transform_pipeline(image)
    image = image.unsqueeze(0) # add batch and dimension
    #get model prediction
    with torch.no_grad():
        y_val = model(image)
        pred = torch.argmax(y_val)
    label_mapping = {0: 'athletic person', 1: 'fat person', 2: 'skinny person'}
    predection = label_mapping[pred.item()]
    return predection




def prompt_genrate(body_type,name,age,gender):
    
# Example usage
    prompt = f"""
    create a html template that include this with intreactive desgin and write only html and css code not say anything and give explaniation
    Generate a weekly workout and meal table that include please use your own knowledge to fill for:
    -name: {name}
    - Body type: {body_type}
    - Age: {age}
    - Gender: {gender}

    Include:
    - Day
    - Workout (type and duration)
    - Meals (breakfast, lunch, dinner)
    - Notes

    Format: Day, Workout, Meals, Notes

    """
    output = get_germini(prompt)

    return output



def report_genrate(image,name,age,gender):
    image_path =f"media\{image}"
    body_type = image_checker(image_path)
    output =prompt_genrate(body_type,name,age,gender)
    html_content =output
    with open("templates/report.html","w") as file:
        file.write(html_content)
    print("html file successfully created..............")
    #return output



    

    







