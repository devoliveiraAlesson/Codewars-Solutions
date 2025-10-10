def people_with_age_drink(age):
    i = sum([age < 14, age < 18, age < 21])
    return "drink " + ["whisky", "beer", "coke", "toddy"][i]