class Patient:
    def __init__(self, name,age,height,weight,pid=None,history=""):
        self.pid=pid
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
        self.history=history
    def calc_bmi(self):
        if self.height<=0:
            return 0.0
        bmi_val= self.weight / (self.height*self.height)
        return round(bmi_val,2)
    def get_category(self,bmi_val):
        if bmi_val<18.5:
            return "Underweight"
        elif bmi_val<= 24.9:
            return "Normal"
        elif bmi_val<= 29.9:
            return "Overweight"
        else:
            return "Obese"
    def add_record(self,date_text):
        current_bmi=self.calc_bmi()
        status=self.get_category(current_bmi)
        new_entry=date_text +"|"+str(current_bmi)+"|"+ status
        if self.history=="":
            self.history=new_entry
        else:
            self.history=self.history+";"+new_entry
            print("\n -> Vitals updated, BMI is:",current_bmi,"(",status,")")
    def show_info(self):
        print("\n--- Patient Details ---")
        print("ID:    ", self.pid)
        print("Name:  ", self.name)
        print("Age:   ", self.age)
        print("Height:", self.height, "m")
        print("Weight:", self.weight, "kg")
    def show_history(self):
        if self.history == "":
            print("No past records found.")
            return
        print("\n--CHECKUP HISTORY--")
        records=self.history.split(";")
        for item in records:
            if "|" in item:
                parts = item.split('|') 
                print("Date:", parts[0], " | BMI:", parts[1], " | Status:", parts[2])
        print("-----------------------")
    def to_csv(self):
        line = str(self.pid) + "," + self.name + "," + str(self.age) + "," + \
               str(self.height) + "," + str(self.weight) + "," + self.history
        return line + "\n"
    @staticmethod
    def from_csv(line):
        parts = line.strip().split(',', 5)
        if len(parts) < 6:
            return None
        new_obj = Patient(parts[1], int(parts[2]), float(parts[3]), float(parts[4]), parts[0], parts[5])
        return new_obj