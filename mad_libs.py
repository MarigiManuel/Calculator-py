def mad_libs_generator():
    # Mad Libs template with placeholders
    template = "I went to the {} and {} a {} {}."

    # Ask the user for different types of words
    place = input("Enter a place: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")

    # Fill in the template with user inputs
    mad_libs_story = template.format(place, verb, adjective, noun)

    # Display the generated Mad Libs story
    print("\nYour Mad Libs Story:")
    print(mad_libs_story)

if __name__ == "__main__":
    mad_libs_generator()
