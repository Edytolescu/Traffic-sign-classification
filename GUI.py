from tkinter import*
from tkinter import filedialog
from PIL import Image, ImageTk
from tensorflow import keras

import numpy as np

classes = { 0:'Speed limit (20km/h)',
            1:'Speed limit (30km/h)', 
            2:'Speed limit (50km/h)', 
            3:'Speed limit (60km/h)', 
            4:'Speed limit (70km/h)', 
            5:'Speed limit (80km/h)', 
            6:'End of speed limit (80km/h)', 
            7:'Speed limit (100km/h)', 
            8:'Speed limit (120km/h)', 
            9:'No passing', 
            10:'No passing veh over 3.5 tons', 
            11:'Right-of-way at intersection', 
            12:'Priority road', 
            13:'Yield', 
            14:'Stop', 
            15:'No vehicles', 
            16:'Veh > 3.5 tons prohibited', 
            17:'No entry', 
            18:'General caution', 
            19:'Dangerous curve left', 
            20:'Dangerous curve right', 
            21:'Double curve', 
            22:'Bumpy road', 
            23:'Slippery road', 
            24:'Road narrows on the right', 
            25:'Road work', 
            26:'Traffic signals', 
            27:'Pedestrians', 
            28:'Children crossing', 
            29:'Bicycles crossing', 
            30:'Beware of ice/snow',
            31:'Wild animals crossing', 
            32:'End speed + passing limits', 
            33:'Turn right ahead', 
            34:'Turn left ahead', 
            35:'Ahead only', 
            36:'Go straight or right', 
            37:'Go straight or left', 
            38:'Keep right', 
            39:'Keep left', 
            40:'Roundabout mandatory', 
            41:'End of no passing', 
            42:'End no passing veh > 3.5 tons' }

root1 = Tk()

screen_width = root1.winfo_screenwidth()
screen_height = root1.winfo_screenheight()

root1_width = 990
root1_height = 830

x1 = (screen_height / 2) - (root1_height / 2) 
y1 = (screen_width / 2) - (root1_width / 2)

root1.overrideredirect(True)

bg = PhotoImage(file=r"C:\Users\edyto\Desktop\licenta2\background_mai_mic.png")

my_label = Label(root1, image=bg)
my_label.place(x=0, y=0, relheight=1, relwidth=1)           

root1.geometry(f"{root1_width}x{root1_height}+{int(y1)}+{int(x1)}")



def main_screen():
    root1.destroy()
    root = Tk()
    global my_button, my_button_1
    root_width = 700
    root_height = 500
    x = (screen_height / 2) - (root_height / 2)
    y = (screen_width / 2) - (root_width / 2)
    root.title('Application')
    

    def open():
        global my_image, my_image1       
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select an image", filetypes=(("All files", "*.*"), ("jpg files","*.jpg"), ("png files","*.png")))
        pil_image = Image.open(root.filename)
        resized_image = pil_image.resize((30, 30))
        my_image = ImageTk.PhotoImage(resized_image)
        my_image1 = np.array(resized_image)
        top = Toplevel(root)
        top.title('Selected Image')
        my_label = Label(top, image=my_image)
        my_label.pack()
        result_label.destroy()

    my_button = Button(root, text="Select an image", command=open)
    my_button.pack()        

    def detection():
        global result_label
        retea = keras.models.load_model('model.h5')
        reshaped_image = my_image1.reshape(1, 30, 30, 3)
        pred = retea.predict(reshaped_image)
        pred_class = pred.argmax()
        pred_label = classes[pred_class]
        result_label=Label(root, text=pred_label)
        result_label.place(relx=0.5, rely=0.2, anchor=CENTER)

        
    root.geometry(f'{root_width}x{root_height}+{int(y)}+{int(x)}')       
    
    my_button_1 = Button(root, text="Detectare", height=5, width=10, command=detection)
    my_button_1.place(relx=0.5, rely=0.5, anchor=CENTER)

root1.after(5000, main_screen)

mainloop()