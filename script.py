f = open('vet_data.txt', 'r')

content = f.read()


content_replaced = content.replace(";;", "+")


new_patients = content_replaced.replace("//", ",").split(",")


new_patients_split = []


for patient in new_patients:
    new_patients_split.append(patient.split("+"))

print(new_patients_split)