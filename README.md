# face-smile-detector

## Follow these step to run this application:-
 
1. Clone code  and open code in VS code (recommended)
2. Create a virtual environment:
   **macos/linux** : `python3 -m venv venv`
   **winodws** : `py -3 -m venv venv`
3. Activate virtual environment:
   **macos/linux** :  `. venv/bin/activate`
   **windows** : `venv\Scripts\activate`
4. Install all python package:
   `pip install -r requirements.txt`
5. Command for training your model:
   `python train.py --dataset ./datasets/smileD  --model ./output/lenet.hdf5`
6. Command for detect face smile:
    `python detect_smile.py --cascade haarcascade_frontalface_default.xml  --model ./output/lenet.hdf5`
 
