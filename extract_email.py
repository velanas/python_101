

#Extract Email
import re

#Data 
data = """
1;Alice;Miller;79;8005 Main St, San Diego, TX;alice.miller@web.net
2;John;Smith;26;9745 Pine St, Los Angeles, CA;john.smith@service.io
3;John;Garcia;35;6281 Highland Ave, Phoenix, CA;john.garcia@mail.com
4;John;Smith;63;4463 Willow Blvd, Chicago, PA;john.smith@web.net
5;Laura;Martinez;74;6100 Highland Ave, Dallas, IL;laura.martinez@service.io
6;Alice;Hernandez;36;4296 Highland Ave, Dallas, PA;alice.hernandez@example.com
7;Michael;Smith;32;7025 Pine St, San Diego, CA;michael.smith@domain.org
8;Jane;Hernandez;77;1575 Oak Dr, Philadelphia, CA;jane.hernandez@service.io
9;Jane;Smith;50;6931 Elm St, Philadelphia, CA;jane.smith@service.io
10;Bob;Miller;39;5670 Willow Blvd, Houston, TX;bob.miller@service.io
"""
# #Data splitting and email extraction
# for line in data.strip().splitlines():
#     fields = line.split(";")
#     email = fields[-1]
#     print(email)

#Data splitting and email extraction using regex # \w+[\s\S]\w+@\w+\.\w+$
patern = re.compile(r"\w+[\s\S]\w+@\w+\.\w+$",re.MULTILINE)

match = patern.findall(data)
for email in match:
    print(email)

# Data splitting and email extraction using regex # Mathching line by line
# for line in data.strip().splitlines():
#     match = re.search(r'\w+[\s\S]\w+@\w+\.\w+$', line)
#     if match:
#         print(match.group())
