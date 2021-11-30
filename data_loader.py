class Disease:
    def __init__(self, name, min_age, max_age, desc, major_sym = None, minor_sym = None, treat = None):
        self.name = name
        self.min_age = min_age
        self.max_age = max_age
        self.description = desc
        self.major_symptoms = major_sym
        self.minor_symptoms = minor_sym
        self.treatment = treat
        
        
    def __str__(self):
        return f"Disease: {self.name}\nAge Range: {self.min_age}-{self.max_age}\nDescription: {self.description}\n{self.major_symptoms}" 
    
    def get_format_data(self):
        sym = ":".join(self.major_symptoms)
        return f"{self.name},{self.min_age}-{self.max_age},{self.description},{sym}\n"
    
    
    def quantify(self, symptoms):
        pass


def load_disease_data_from_file():
    fileHandle = open("diseases.csv", "r")
    lines = fileHandle.readlines()
    result = {}
    
    for line in lines:
        data = line.split(",")
        k = data[0].strip().lower()
        age_range = data[1].split("-")
        min_age = int(age_range[0])
        max_age = int(age_range[1])
        desc= data[2].strip()
        symptoms = data[3].split(":")
        
        for i, s in enumerate(symptoms):
            symptoms[i] = s.strip()
        
        d = Disease(k, min_age, max_age, desc, symptoms)
        result[k] = d
        
    
    fileHandle.close()
    return result        


def load_symptom_data_from_file():
    fileHandle = open("symptoms.csv", "r")
    lines = fileHandle.readlines()
    result = {}
    
    for line in lines:
        data = line.split(",")
        
        if len(data) > 1:
            k = data[0].strip().lower()
            data = data[1:]
            for i,d in enumerate(data):
                data[i] = d.strip().lower()
            
            if k in result:
                temp = result.get(k)
                temp = temp + data
                result[k] = temp
            else:
                result[k] = data
    
    fileHandle.close()
    return result


def save_disease_data_to_file(dise_data:dict):
    #Writing symptoms to disc    
    symptoms = {}
    
    for k, v in dise_data.items():
        for s in v.major_symptoms:
            if s in symptoms:
                symptoms[s].append(k)
            else:
                symptoms[s] = [k]
    
    output = []
    for k, v in symptoms.items():
        out = ",".join(v)
        out = k + "," + out + "\n"
        output.append(out)
    
    fileHandle = open("symptoms.csv", "w")
    fileHandle.writelines(output)
    fileHandle.close()
    
    #Writing diseases to disc
    output = []
    for k, v in dise_data.items():
        output.append(v.get_format_data())
        
    fileHandle = open("diseases.csv", "w")
    fileHandle.writelines(output)
    fileHandle.close()