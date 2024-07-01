from collections import Counter
from tensorflow.keras.preprocessing import image
from keras.models import load_model
import os

import numpy as np

vgg16 = load_model('model_vgg16.h5')
vgg19 = load_model('model_vgg19.h5')
resnet50 = load_model('model_resnet50.h5')
MobileNetV2 = load_model('model_MobileNetV2.h5')
InceptionV3 = load_model('model_InceptionV3.h5')
Xception = load_model('model_Xception.h5')
voting = [0,0,0,0,0,0]
d = '/mnt/c/Users/cyber/Downloads/PDFdownloads/Imp/DESIGN_PROJECT/Malaria_Detection/DTGCN_DATA/1_Multistage_Malaria_Parasite_Recognition/Data/test'

mapping = {0: 'red_blood_cell', 1:'schizont', 2:'trophozoite', 3:'ring',}
accuracy = {'red_blood_cell': 0, 'schizont': 0, 'trophozoite': 0, 'ring': 0,}
#declare an empty 2x2 matrix
confusion_matrix = [[0 for i in range(4)] for j in range(4)]
k=0

for j in os.listdir(d):
    for i, file in enumerate(os.listdir(f'{d}/{j}')):
        accuracy = {'red_blood_cell': 0, 'schizont': 0, 'trophozoite': 0, 'ring': 0,}
        img=image.load_img(f'{d}/{j}/{file}',target_size=(224,224))
        # img.show()
        x=image.img_to_array(img)
        x=x/255
        x=np.expand_dims(x,axis=0)
        # print(mapping[np.argmax(model.predict(x), axis=1)[0]])
        # accuracy[mapping[np.argmax(temp.predict(x), axis=1)[0]]] += 1
        voting = [np.argmax(vgg16.predict(x), axis=1)[0], np.argmax(vgg19.predict(x), axis=1)[0], np.argmax(MobileNetV2.predict(x), axis=1)[0], np.argmax(InceptionV3.predict(x), axis=1)[0], np.argmax(Xception.predict(x), axis=1)[0]]
        heavy = voting[3]
        #display the most voted class
        prediction_counts = Counter(voting)
        most_common_prediction = prediction_counts.most_common(1)[0][0]
        diff = prediction_counts[heavy] - prediction_counts[most_common_prediction]
        if(diff >= -1):
            accuracy[mapping[heavy]] += 1
        else:
            accuracy[mapping[prediction_counts.most_common(1)[0][0]]] += 1
        
    print(accuracy)
    confusion_matrix[k] = accuracy
    k+=1
print(confusion_matrix)
