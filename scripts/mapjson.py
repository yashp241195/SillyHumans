import json

allmembers = []

with open('memberdetails.json') as json_file:
    data = json.load(json_file)
    for key in data:
        myvalue = data[key]
        member = {}
        name = myvalue["Name"]
        dp = myvalue["Profile Pic Image URL"]
        headline = myvalue["Headline"]
        tags = myvalue["Work Tags"]
        email = myvalue["Email"]
        linkedin = myvalue["LinkedIn URL"]
        instagram = myvalue["Instagram URL"]
        portfolio = myvalue["Portfolio URL"]
        description = myvalue["Description"]

        email = "#" if email == "" else email
        linkedin = "#" if linkedin == "" else linkedin
        instagram = "#" if instagram == "" else instagram
        portfolio = "#" if portfolio == "" else portfolio

        member["name"] = name
        member["dp"] = dp
        member["headline"] = headline
        member["tags"] = tags
        member["email"] = email
        member["linkedin"] = linkedin
        member["instagram"] = instagram
        member["portfolio"] = portfolio
        member["description"] = description
        allmembers.append(member)

print(json.dumps(allmembers, indent = 1))

f = open("members.js", "w")
f.write("var allmembers = ")
f.write(json.dumps(allmembers, indent = 1))

f.close()