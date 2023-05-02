categorii = open("categorii.txt", "w")
taskuri = open("taskuri.txt", "w")

categories = []
print("Introduceți categoriile de taskuri (introduceți 'stop' pentru a opri introducerea):")
while True:
    category = input()
    if category == "stop":
        break
    categories.append(category)
    categorii.write(category + "\n")
categorii.close()

tasks = []
print("Introduceți task-uri (introduceți 'stop' pentru a opri introducerea):")
while True:
    task = input("Task: ")
    if task == "stop":
        break
    deadline = input("Data limită: ")
    responsible_person = input("Persoană responsabilă: ")
    category = input("Categorie: ")
    if category not in categories:
        print("Categoria introdusă nu există. Introduceți o categorie validă.")
        continue
    task_info = [task, deadline, responsible_person, category]
    tasks.append(task_info)
    taskuri.write(task + "|" + deadline + "|" + responsible_person + "|" + category + "\n")
taskuri.close()

