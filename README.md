# Ensemble-Transfer-Learning-for-Accurate-Malaria-Detection-with-Stage-Classification-Explainable-AI.-
Malaria is a mosquito borne disease that is very dangerous and spreads through air as well as the bite of a female Anopheles mosquito. This repository contains a novel approach to identify the presence of Malaria in a given blood sample as well as to identify the stage of malaria which is further explained using XAI (Explainable AI). 
<p> "We used image set BBBC041v1, available from the Broad Bioimage Benchmark Collection [Ljosa et al., Nature Methods, 2012].". The images and ground truth are licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License by Jane Hung. Appreciation to Sen Li et al <a href="https://github.com/senli2018/DTGCN_2021">Here</a> who have cropped these images in their study to carefully choose the prominent cells which were used in this study as well. 
<p>
  The dataset was heavily unbalanced so they had to be had to be pre-processed using techniques like Dropping unwanted classes, Data Augmentation, Feature Engineering.
  <p>
    After the data was augmented, some of the classes were increased from tiny amounts to enormous, this leads to a great problem as it tests the limit of augmentation of images. Due to this reason the dataset could not perform well with any custom or transfer learning models. To overcome this issue the dataset was trained over 5 different transfer learning models. This allows different models trained for capturing features in different types of datasets to identify a pattern in this dataset individually.  
  </p>
  The model was then tested by forming an Ensemble Learning Model with all the available models. The final prediction made was done using majority voting. Since some of the models did not perform very well with the datasets, a custom algorithm was formed that would give a just prediction of the input image.-
</p>
## Models
<p>
  The dataset was trained over the following models 
  <ul>
    <li> VGG 16</li>
    <li> VGG19< /li>
    <li> MobileNetV2</li>
    <li> InceptionV3</li>
    <li> Exception</li>
  </ul>
</p>
