groupmembers=('Swati','Erika','Abdi','Norah','Terrence')
awscourses=('Linux','python','Databases','Scrum','security', 'Networking')

print("Hello Shafan,Mike and everyone. We hope you are doing Great!")
print("welcome to our group!")
print('Our group has', groupmembers)
name=input('choose one to know their career course: ')
print('You chose',name)
if name == "Swati":
  print(name, 'is interested in', awscourses[2])
if name == "Norah":
  print(name, 'is interested in', awscourses[0], 'and', awscourses[5], 
 'and', awscourses[1])
if name == "Terrence":
  print(name, 'is interested in', awscourses[4])
if name == "Abdi":
  print(name, 'is intrested in', awscourses[0])
if name == "Erika":
    print(name,'is intrested in', awscourses[3])
 if name != (groupmembers):
  print('member is not part of this group')
