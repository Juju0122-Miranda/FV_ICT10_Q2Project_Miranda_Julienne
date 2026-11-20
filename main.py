#2Q Project
from pyscript import document, display

#--------------------------------------------------------------------------------------------
# 1. MEMBER VERIFICATION SYSTEM
club_members = ["Johanna Ramos", "Kailey Gayas", "Hope Benitez", "Mhicaela Belen", "Angel Canino"]

# Verifying member name
def verify_member(e):
    document.getElementById("message").innerHTML = ""

    firstname = document.getElementById("Fname").value
    surname = document.getElementById("Sname").value
    fullname_ = (firstname + " " + surname).title()

    # Verifies if typed name is a member of the club
    is_member = fullname_ in club_members

    messages = {
        True: "Congratulations " + fullname_ + "! You are now part of OBFV GIRLS' VOLLEYBALL CLUB.",
        False: "Sorry " + fullname_ + ", your name is not on the list."
    }

    # Displays the result
    display(messages[is_member], target="message")


# Clears the boxes
def clear_verification(e):
    document.getElementById("Fname").value = ""
    document.getElementById("Sname").value = ""
    document.getElementById("message").innerHTML = ""

#---------------------------------------------------------------------------------
# 2. CLUB MEMBERS LIST
Grade_7 = {"Klee Ali", "Kaedehara Kazuha", "Mona Schmentti"}
Grade_8 = {"Raiden Shogun", "Rex Lapis", "Ayaka Kamisato"}
Grade_9 = {"Odette Gonzales", "Arlecchino Smith", "Columbina Perez"}
Grade_10 = {"Furina Lopez", "Xianyun Xi", "Ganyu Mel"}

all_members = Grade_7 | Grade_8 | Grade_9 | Grade_10


# Adds new club members
def add_member(event):
    first_name = document.getElementById("Fname").value
    last_name = document.getElementById("Sname").value
    new_member = (first_name + " " + last_name).title()

    all_members.add(new_member) # Adds the new member to the set

    members_list = "<br>".join(sorted(all_members))
    total_members = len(all_members)

    # Displays the full member list
    document.getElementById("result").innerHTML = f"""
        <h4>Club Members</h4>
        {members_list}
        <p>Total Members: {total_members}</p>
    """

# Clears the input fields
def clear_members(event):
    document.getElementById("Fname").value = ""
    document.getElementById("Sname").value = ""
    document.getElementById("result").innerHTML = ""

#--------------------------------------------------------------------------------  
# 3. NON-METAL ELEMENTS LOCATOR
# Dictionary of non-metal elements
elements = {
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.003),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.948),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I": ("Iodine", 53, 126.904),
    "Xe": ("Xenon", 54, 131.293),
    "Rn": ("Radon", 86, 222)
}

# Function to search for an element
def search_element(e):

    # Gets the input from HTML
    Element1 = document.getElementById("Element").value.capitalize()

    # Retrieves information from the dictionary
    result = elements.get(Element1, ("Element not found...", "-", "-"))

    # Displays the result in HTML
    document.getElementById("message").innerHTML = f"""
    Element Symbol: {Element1}<br>
    Element Name: {result[0]}<br>
    Atomic Number: {result[1]}<br>
    Atomic Mass: {result[2]}
    """

# Function to clear the input and result
def clear_locator(e):

    document.getElementById("Element").value = ""
    document.getElementById("message").innerHTML = ""
