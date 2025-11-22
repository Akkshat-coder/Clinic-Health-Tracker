from patient import Patient
db_filename = "clinic_data.txt"
def save_to_file(records):
    print("... Attempting to save data ...")
    try:
        text_file = open(db_filename, "w")
        for person in records:
            data_line = person.to_csv()
            text_file.write(data_line)
        text_file.close()
        print("->Success,Data saved.")
    except:
        print("->Error,Could not save to file.")
def load_from_file():
    my_list = []
    try:
        text_file = open(db_filename, "r")
        full_text = text_file.read()
        text_file.close()
        rows = full_text.split("\n")
        for row in rows:
            if len(row)>5:
                p_obj=Patient.from_csv(row)
            if p_obj!= None:
                my_list.append(p_obj)
        print("->Loaded previous records from file.")
    except:
        print("-> No save file found. Starting with an empty database.")
    return my_list