girls_names = ["Evelyn","Jessica","Somto","Edith","Liza","Madonna","Waje","Tola","Aisha","latifa"]
boys_names = ["Chinedu","Liam","Wale","Gbenga","Abiola","Kola","Kunle","George","Thomas","Wesley"]
girls_ages = [17,16,17,18,16,18,17,20,19,17]
boys_ages = [19,16,18,17,20,19,16,18,17,19]
girls_height = [5.5,6.0,5.4,5.9,5.6,6.1,6.0,5.7,5.5,5.4]
boys_height = [5.7,5.9,5.8,6.1,5.9,5.5,6.1,5.4,5.8,5.7]
girls_scores = [80,85,70,60,76,66,87,95,50,49]
boys_scores = [74,87,75,68,66,78,87,98,54,60]
print("                 GIRLS LIST")

print("Name         |Age         |Height         |Score")

for i in range(10):
    print(f"{girls_names[i]}       |{girls_ages[i]}          |{girls_height[i]}            |{girls_scores[i]}")

print("                 BOYS LIST")
print("Name         |Age         |Height         |Score")

for i in range(10):
    print(f"{boys_names[i]}       |{boys_ages[i]}          |{boys_height[i]}            |{boys_scores[i]}")