import json
maindata=[]
data={}
skills=[]
qualification={}
listdata=[]

data["id"]=int(input("please enter student id:"))
data["name"]=input("please enter student name:")
data["experience"]=input("please enter the experience:")

skill1=input("please enter first skills:")
skills.append(skill1)

skill2=input("please enter second skills:")
skills.append(skill2)

skill3=input("please enter third skills:")
skills.append(skill3)

skill4=input("please enter fourth skills:")
skills.append(skill4)
data["skills"]=skills

qualification["qualificationname"]=input("qualification of student:")
qualification["passingyear"]=input("please enter the passingyear:")
listdata.append(qualification)

qualification={}
qualification["qualificationname"]=input("qualification of student:")
qualification["passingyear"]=input("please enter the passingyear:")
listdata.append(qualification)

data["qualification"]=listdata
maindata.append(data)

data={}
skills=[]
qualification={}
listdata=[]

data["id"]=id(input("please enter student id:"))
data["name"]=input("please enter student name:")
data["experience"]=input("please enter the experience:")

skill1=input("please enter first skills:")
skills.append(skill1)

skill2=input("please enter second skills:")
skills.append(skill2)

skill3=input("please enter third skills:")
skills.append(skill3)

skill4=input("please enter fourth skills:")
skills.append(skill4)

data["skills"]=skills

qualification["qualificationname"]=input("qualification of student:")
qualification["passingyear"]=input("please enter the passingyear:")
listdata.append(qualification)

data["qualification"]=listdata
maindata.append(data)

print(json.dumps(maindata,indent=4))