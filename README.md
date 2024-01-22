# packer
This is my current working project.

How to replicate what I have done:
1. Download **initdirectory**, **multipacker.py**, and **feature_extractionv2.py** into the same directory.
2. Run **multipacker.py** using the command "python3 multipacker.py initdirectory -o [your output directory]".
3. Run **feature_extractionv2.py** using the command "python3 feature_extractionv2.py [your output directory]".
4. For the next step, it is recommended to go to https://www.kaggle.com/code/elizabethorton/model-classification and create a copy of the notebook in Kaggle, but it is also possible to download **model-classification.ipnyb** and run the notebook on your device. You might have to download some of the packages used in the notebook.
5. On Kaggle, **vectorfilev2.csv** is prepopulated into the Jupyter notebook. If your vectorfile csv is different, you can upload it into Kaggle separately and import it into the notebook. Change the filepath in block 4 to the path to your file.
6. If you would like to step through the model, run each block in order from top to bottom. Otherwise, use the "Run All" button and the notebook will run itself.
7. If you would like to test an individual file using the model, first upload the file to Kaggle and import it into your notebook, then edit the last code block with the path to your file as instructed in the comments of that block. 
