def song (verb, adjective, object, pronoun):
    print("\n\n")
    print(f"{verb} {verb} little {object}.")
    print(f"How {pronoun} wonder what you are.")
    print(f"Up above the world so {adjective}.")
    print(f"Like a {object} in the sky.")
    print(f"{verb} {verb} little {object}.")
    print(f"How {pronoun} wonder what you are.")

input_verb = input("Enter a verb: ")
input_object = input("Enter an object: ")
input_pronoun = input("Enter an pronoun: ")
input_adjective = input("Enter a adjective: ")

song(verb=input_verb, object=input_object, pronoun=input_pronoun, adjective=input_adjective)