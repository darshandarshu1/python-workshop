student_names=["darshan","punith","akhilesh","dhanush","hruthik","chethan","pavan","jashwanth","lohith","harsha"]
print(student_names)
print(student_names[5])
print("\n")
print(student_names[-1])
student_names[0]="baabu"
print(student_names)
print("\n")

student_names.append("dhanu")
print(student_names.append("darshan"))
print(student_names)
print("\n")

student_names.remove("dhanu")
student_names.remove("pavan")
print(f"remove dhanu and pavan:{student_names}")
print("\n")

student_names.insert(1,"dhanu")
student_names.insert(1,"yash")
student_names.insert(3,"ganesh")
student_names.insert(7,"akash")
student_names.insert(9,"gourish")
print(student_names)
print("\n")

student_names.pop(3)
student_names.pop()
print(student_names)
print("\n")

print("length is:",len(student_names))

print(student_names.reverse())
