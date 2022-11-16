import io
from tkinter import filedialog
import base64
import requests

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import matplotlib.image as mpimg



def main_window():
    def upload_image():
        filename = get_image_file_name()
        b64_string = convert_file_to_b64(filename)
        # print(b64_string)

        result = upload_b64_to_server(b64_string)

    def get_image_file_name():
        filename = filedialog.askopenfilename(
            initialdir='Images'
        )
        # filename = 'Images/2022-11-13_181249.jpg'
        return filename

    def convert_file_to_b64(filename):
        with open(filename, "rb") as image_file:
            b64_bytes = base64.b64encode(image_file.read())
        b64_string = str(b64_bytes, encoding='utf-8')
        return b64_string

    def upload_b64_to_server(b64_string):
        out_data = {
            'image': b64_string,
            'net_id': 'jl922',
            'id_no': 1
        }
        r = requests.post('http://vcm-21170.vm.duke.edu/add_image',
                          json=out_data)
        return 0

    def get_image():
        r = requests.get('http://vcm-21170.vm.duke.edu/get_image/jl922/1')
        if r.ok:
            return r.text

    def b64_string_to_ndarray(b64_string):
        image_bytes = base64.b64decode(b64_string)
        image_buf = io.BytesIO(image_bytes)
        img_ndarray = mpimg.imread(image_buf, format='JPG')
        return img_ndarray

    def ndarray_to_tk_image(img_ndarray):
        image_obj = Image.fromarray(img_ndarray)
        tk_image = ImageTk.PhotoImage(image_obj)
        return tk_image

    def b64_string_to_image(b64_string):
        image_bytes = base64.b64decode(b64_string)
        with open('Images/returned.jpg', "wb") as out_file:
            out_file.write(image_bytes)
        return 0

    def upload_cmd():
        upload_image()
        b64_str = get_image()
        upload_b64_to_server(b64_str)

    def display_cmd():
        b64_string = get_image()
        img_ndarray= b64_string_to_ndarray(b64_string)
        tk_image = ndarray_to_tk_image(img_ndarray)


    root = tk.Tk()
    root.title('Image upload and display')

    ttk.Button(
        root,
        text='Choose an image to upload',
        command=upload_cmd
    ).grid(column=0, row=0)



    root.mainloop()

if __name__ == '__main__':


    main_window()
