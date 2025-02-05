words = input("camelCase: ")

after_edite = ""
for letter in words:
    if letter.isupper() == True:
        after_edite += "_"
        after_edite += letter.lower()
    else:
        after_edite += letter

print(f"snake_case: {after_edite}")
