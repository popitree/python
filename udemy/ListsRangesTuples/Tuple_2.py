# Tuple can contain tuples
indranil = "indranil", 1986, "RKM", (
    ("Bengali", 10), ("English", 8))
studentName, dob, school, subjectMarks = indranil
print(studentName)
print(subjectMarks)
print(indranil[3][0])
print(indranil[3][0][0])
print("Subject Marks")
for subMark in subjectMarks:
    subject, mark = subMark
    print(subject, "\t", mark)

# Tuple is immutable but if it contain mutable object as list
# then content of the list can be changed
albumCollection = "indranil", 2018, ["Bengali", "English"]
albumCollection[2].append("Hindi")
print(albumCollection)
print("="*5)

indranil = "indranil", 1986, "RKM", [
    ("Bengali", 10), ("English", 8)]
indranil[3].append(("Physics", 10))
studentName, dob, school, subjectMarks = indranil
subjectMarks.append(("Chemistry", 6))

print("Subject Marks")
for subMark in subjectMarks:
    subject, mark = subMark
    print(subject, "\t", mark)