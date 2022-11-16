import tkinter as tk
from tkinter import ttk
import db_client
from PIL import Image, ImageTk
from tkinter import filedialog

def create_blood_type(letter, rh):
    output = '{}{}'.format(letter, rh)
    return output


def upload_data_to_server(patient_name, patient_id, patient_blood_letter,
                          patient_rh_factor):
    blood_type = create_blood_type(patient_blood_letter, patient_rh_factor)
    patient_id = int(patient_id)
    msg, code = db_client.upload_patient_info(patient_name, patient_id,
                                              blood_type)
    return msg


def main_window():
    def get_update_info():
        print('Get data')
        root.after(2000, get_update_info) #By calling itself, this function
        # will cycle itself. You can use this spattern to let the GUI to
        # update info every few ms

    def ok_cmd():  # You made a local function, so it has access to all the GUI
        # widges

        # Get data from interface
        if rh_button.get() == '':
            print('choose an rh factor')
            return
        patient_name = patient_name_entry.get()
        patient_id = patient_id_entry.get()
        patient_blood_letter = blood_letter_selection.get()
        patient_rh_factor = rh_button.get()

        # Call other testable functions to do all the work
        msg = upload_data_to_server(patient_name, patient_id,
                                    patient_blood_letter,
                                    patient_rh_factor)

        # Update GUI based on results of other functions
        status_label.configure(text=msg)

        # other_button.configure(state=tk.NORMAL)  # This activates a button
        # # whose previous state is tk.DISABLED
        #
        # print('Patient name: {}'.format(patient_name_entry.get()))  # You need
        # # get method to get the value of patient_name_entry. Without get
        # # method, the print statement will print the class of
        # # patient_name_entry
        # print('Patient ID: {}'.format(patient_id_entry.get()))
        # print('Blood type: {}{}'.format(blood_letter_selection.get(),
        #                                 rh_button.get()))
        # print('Donation center: {}'.format(donor_center.get()))
        # print('Clicked ok button')

    def cancel_cmd():
        root.destroy()  # Removes that widget. Since root is the wedge where
        # you run the mainloop, destroying that will destroy the whole GUI

    def picture_button_cmd():
        # new_file = r'Images\2022-11-13_181249.jpg'
        new_file = filedialog.askopenfilename()
        print('Filename: {}'.format(new_file))

        pil_image = Image.open(new_file)

        #Codes below lock the asspect ratio
        x_size, y_size = pil_image.size
        new_y = 100
        new_x = new_y*x_size / y_size

        pil_image = pil_image.resize((round(new_x),round(new_y)))
        tk_image = ImageTk.PhotoImage(pil_image)
        image_label.configure(image=tk_image)
        image_label.image = tk_image #You create a new attribute

    root = tk.Tk()  # root is the standard name for the root window
    root.title('Blood Donor Database')
    # root.geometry('600x300')  # Set the default size of the window. You
    # provide a
    # str of width and height for the
    # window you want to it to be

    ttk.Label(
        root,
        text='Blood Donor Database'
    ).grid(
        column=0,
        row=0,
        sticky='w'  # Same as tk.W
    )  # As
    # long as there's any content, tkinter will shrink the window to the
    # child widget. grid(column=0, row=0) will go the upper left corner
    ttk.Label(root, text='Name:').grid(column=0, row=1)  # column and row
    # needs to be in sequence so using grid(column=0, row=2) will give you
    # the same thing since there's now row 1 yet

    patient_name_entry = tk.StringVar()  # StringVar is usually made before
    # entry. It connects back and forth the Entry()
    # patient_name_entry.set('Enter a name here')  # You can use set method to
    # set the value of patient_name_entry

    ttk.Entry(
        root,
        width=50,
        textvariable=patient_name_entry
        # Save the entry into patient_name_entry
    ).grid(column=1, row=1)

    ttk.Label(root, text='ID:').grid(column=0, row=2)
    patient_id_entry = tk.StringVar()  # Default value is 0, so it'll show up in
    # the GUI as 0
    ttk.Entry(root, textvariable=patient_id_entry).grid(column=1, row=2,
                                                        sticky=tk.W)  # If
    # you input a non-numeric string in this field, then it'll give a error.
    # So you can use a try-except block for this. Or you can change the
    # patient_id_entry from IntVar to StringVar and handle the error yourself

    blood_letter_selection = tk.StringVar()
    ttk.Radiobutton(
        root,
        text='A',
        variable=blood_letter_selection,
        value='A'  # Set blood_letter_selection value to "A" once this
        # radiobutton is selected
    ).grid(
        column=0, row=3, sticky=tk.W)
    ttk.Radiobutton(root, text='B', variable=blood_letter_selection,
                    value='B'  # In this way, the 2 radio buttons are
                    # connected such that only 1 button can be selected
                    ).grid(
        column=0, row=4, sticky=tk.W)
    ttk.Radiobutton(root, text='AB', variable=blood_letter_selection,
                    value='AB').grid(column=0, row=5, sticky=tk.W)
    ttk.Radiobutton(root, text='O', variable=blood_letter_selection,
                    value='O').grid(column=0, row=6, sticky=tk.W)

    rh_button = tk.StringVar()
    ttk.Checkbutton(root, text='Rh Positive', variable=rh_button,
                    onvalue='+', offvalue='-').grid(
        column=1, row=4)

    ttk.Label(root, text='Closest Donation Center').grid(column=2, row=0)
    donor_center = tk.StringVar()
    donor_center_combo = ttk.Combobox(root, textvariable=donor_center)
    # Combobox also allows entry
    donor_center_combo.grid(column=2, row=1)
    donor_center_combo['values'] = ['Durham', 'Cary', 'Raleigh']
    donor_center_combo.state(['readonly'])  # This forces donor_center_combo
    # can only be a value from the selection and the disable the entry
    # function of combobox

    ttk.Button(
        root,
        text='Ok',
        command=ok_cmd  # You can't have () after ok_cmd; otherwise, ok_cmd
        # will be run right away once the window is made and the clicking
        # gives you nothing since ok_cmd() has no return. Without ()
        # means that's the function you want to run but don't run it now
    ).grid(column=1, row=6)
    ttk.Button(root, text='Cancel', command=cancel_cmd).grid(column=2, row=6)

    other_button = ttk.Button(root, text='Other', state=tk.DISABLED)
    other_button.grid(column=2, row=7)

    picture_button = ttk.Button(root,text='Load Picture',
                              command=picture_button_cmd)
    picture_button.grid(column=2, row=8)

    status_label = ttk.Label(root,text='Status')
    status_label.grid(column=0,row=0)

    pil_image = Image.open(r'Images\2022-11-13_181159.jpg')
    pil_image = pil_image.resize((100, 100))
    tk_image = ImageTk.PhotoImage(pil_image) #Convert the pillow image into
    # a tk image object
    image_label = ttk.Label(root,image=tk_image)
    image_label.image = tk_image #This line is actually not necessary
    image_label.grid(column=1, row=8)


    root.after(1000, get_update_info) #After 1000 ms,
    # run function get_update_info
    root.mainloop()  # Start the interface. It's a loop because you're waiting
    # for the user to make some events and then to react correspondingly


if __name__ == '__main__':
    main_window()
