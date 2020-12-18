# Q4. Part 1

import requests
url = "https://api.github.com"
r =  requests.get(url)
print("Status Code: ", r.status_code)

#Part 2
# import requests
# url = "http://api.github.com"
# r = requests.get(url)
# print(r.headers)

#part 3
# import requests
# url = "http://api.github.com"
# r = requests.get(url)
# print("text:", r.text)

# Part 4
# import requests
# NewHeader = {"user-agent":"IPhone 10"}
# url = "http://api.github.com"
# r = requests.get(url, headers=NewHeader)
# print("text:", r.text)


# def myfile_reader(file_name):
#     fobj = open(file_name)
#     for line in fobj:
#         if(line != 'None'):
#             print(line.rstrip())
#         elif(line == 'None'):
#             break

#     fobj.close()
# mygen = myfile_reader("final.csv")
    


