import data_loader as dl

def find_possible_diseases(data, symptoms):
    result = {}
    for sym in symptoms:
        if sym in data:
            diseases = data[sym]
            for d in diseases:
                result[d] = 1
    
    ordered_result = []
    for k, v in result.items():
        ordered_result.append(k)
    
    return ordered_result
            

def rank_order_disease(diseases:list, symptoms:list, age:int, dise_data:dict):
    
    result = {}
    for d in diseases:
        r = dise_data[d].quantify(symptoms, age)
        result[d] = r
        
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    
    return result


def main():
    symp_data = dl.load_symptom_data_from_file()
    dise_data = dl.load_disease_data_from_file()
    
    symptoms = []
    print("Enter '0' to exit.")
    print("Enter the symptoms(One at a time).")
    
    while True:
        sym = input("> ")
        
        if sym.strip().lower() == "0":
            break
        
        symptoms.append(sym.strip().lower())
        
    age = input("Enter the patients age.\n>")
    age = int(age)

    diseases = find_possible_diseases(symp_data, symptoms)
    
    outcome = rank_order_disease(diseases, symptoms, age, dise_data)
    
    print()
    for k in outcome:
        dise_data[k[0]].output_format_data()
        print()
 
if __name__ == "__main__":
    main()