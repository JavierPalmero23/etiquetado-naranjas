# importing the modules 
import cv2 
import math
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

# Initialize global variables
start_point = None
end_point = None
drawing = False
NombreImagen = ""

# function to display the coordinates of 
# of the points clicked on the image  
def click_event(event, x, y, flags, params):
    global start_point, end_point, drawing
  
    # checking for left mouse button press 
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)
  
    # checking for mouse movement
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            end_point = (x, y)
            img_copy = img.copy()
            cv2.circle(img_copy, start_point, int(math.hypot(end_point[0] - start_point[0], end_point[1] - start_point[1])), (255, 0, 0), 2)
            cv2.imshow('image', img_copy)
  
    # checking for left mouse button release
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        end_point = (x, y)
        
        # Calculating the radius
        radius = int(math.hypot(end_point[0] - start_point[0], end_point[1] - start_point[1]))
        
        # displaying the coordinates and radius on the Shell 
        print(f'Center: {start_point}, Radius: {radius}')
        
        # displaying the coordinates and radius on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX 
        cv2.putText(img, f'({start_point[0]},{start_point[1]}), R={radius}', start_point, font, 1, (255, 255, 0), 1)
        cv2.circle(img, start_point, radius, (255, 0, 0), 2)
        cv2.imshow('image', img)
        
        # Append-adds at last
        base_name = os.path.splitext(NombreImagen)[0]
        with open(base_name + ".txt", "a") as file1:
            file1.write(f'{start_point[0]},{start_point[1]},{radius}\n')

def select_image():
    global NombreImagen
    root = Tk()
    root.withdraw()  # Hide the root window
    root.update()
    file_path = askopenfilename()
    root.destroy()
    return file_path

# driver function 
if __name__ == "__main__": 
    NombreImagen = select_image()
    if NombreImagen:
        # reading the image
        img = cv2.imread(NombreImagen, 1)
        
        if img is None:
            print("Error: Could not read the image.")
        else:
            # displaying the image 
            cv2.imshow('image', img) 
          
            # setting mouse handler for the image 
            # and calling the click_event() function 
            cv2.setMouseCallback('image', click_event) 
          
            # wait for a key to be pressed to exit 
            cv2.waitKey(0) 
          
            # close the window 
            cv2.destroyAllWindows()
    else:
        print("No image selected.")

