import data_loader as dl


def main():
    dise_data = dl.load_disease_data_from_file()
    
    d_name = input("Enter disease name: ").strip().lower()
    min_age = int(input("Enter minimum affected age: "))
    max_age = int(input("Enter maximum affected age: "))
    desc = input("Enter description: ").strip()
    
    # Treatment
    treatment = []
    print("Enter '0' to exit.")
    print("Enter the treatment(One at a time).")
    
    while True:
        treat = input("> ")
        if treat.strip().lower() == "0":
            break
        
        treatment.append(treat.strip())
        
    
    # Symptoms
    symptoms = []
    print("Enter '0' to exit.")
    print("Enter the symptoms(One at a time).")
    
    while True:
        sym = input("> ")
        if sym.strip().lower() == "0":
            break
        
        symptoms.append(sym.strip().lower())
        
    
    dise_data[d_name] = dl.Disease(d_name, min_age, max_age, desc, symptoms, treatment)
    dl.save_disease_data_to_file(dise_data)

if __name__ == "__main__":
    main()