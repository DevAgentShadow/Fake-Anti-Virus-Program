# No virus name will be showed in this program because i think that some of you might download it on important computers
# All Virus name which will be shown are just the names which i setted, you can edit the names  by editing Virus_Name Variable
# PLS NOTE THAT THIS PROGRAM IS JUST FOR FUN! DO NOT TAKE IT SERIOUSLY!

# Virus-Types
# 1 = Dangerous Virus
# 2 = Medium Virus
# 3 = Weak Virus
# 4 = Backdoor
# 5 = Ransomware 
# The Numbers can be changed in Virus_Type

# Action
DELETE = 1.1    # Editable
LOCATE = 2.2    # Editable
ALLOW = 3.3     # Editable

# Virus_Name Variables
Virus_Name1 = "ProtaVirus 5.0"            # Editable
Virus_Name2 = "Money Generator Pro.exe"   # Editable
Virus_Name3 = "Virus Tester Program"      # Editable
Virus_Name4 = "Xeno"                      # Editable
Virus_Name5 = "EasyDisk.Pro"              # Editable

# Virus_Type Variables
Virus_Type1 = 1 # Editable
Virus_Type2 = 2 # Editable
Virus_Type3 = 3 # Editable
Virus_Type4 = 4 # Editable
Virus_Type5 = 5 # Editable

# Dictionary for virus names
viruses = {
    1: Virus_Name1,
    2: Virus_Name2,
    3: Virus_Name3,
    4: Virus_Name4,
    5: Virus_Name5
}

# Main Area 
# DO NOT EDIT UNLESS IF YOU KNOW PYTHON

Virus = int(input("Enter the Virus Type (1-5): "))

if Virus == 1:
    Action1 = float(input(f"{Virus_Name1} FOUND! DELETE NOW (1.1=Delete, 2.2=Locate, 3.3=Allow): "))
    if Action1 == DELETE:
        print("You're computer is safe now. Virus got deleted :)")
    elif Action1 == LOCATE:
        Action20 = float(input("Virus location = Central System Drive/Central Program Files\nEnter action (1.1=Delete, 2.2=Ignore, 3.3=Allow): "))
        if Action20 == DELETE:
            print("Virus Deleted :)")
        elif Action20 == LOCATE:
            print("""System.Failure = Virus.captured
(IT IS TOO LATE NOW, THE VIRUS IS IN YOUR PC)""")
        elif Action20 == ALLOW:
            print("SystemHacked.error = Files.taken")

elif Virus == 2:
    Action2 = float(input(f"{Virus_Name2} has been detected. Delete it now (1.1=Delete, 2.2=Locate, 3.3=Allow): "))
    if Action2 == DELETE:
        print("Virus has been deleted. The computer is safe :)")
    elif Action2 == LOCATE:
        Action19 = float(input("PLS SELECT THE ACTION (1.1=Delete, 2.2=Ignore, 3.3=Allow): "))
        if Action19 == DELETE:
            print("Virus Deleted")
        elif Action19 == LOCATE:
            print("Error, File damaged")
        elif Action19 == ALLOW:
            print("Important files have been taken away")
    elif Action2 == ALLOW:
        print(Virus_Name2, "has stolen important files")

elif Virus == 3:
    Action3 = float(input(f"{Virus_Name3} detected! The program is weak but delete it NOW (1.1=Delete, 2.2=Locate, 3.3=Allow): "))
    if Action3 == DELETE:
        print("VIRUS DELETED!!")
    elif Action3 == LOCATE:
        Action18 = float(input("Virus Location = Central System Drive/Central Program Files\nEnter action (1.1=Delete, 2.2=Ignore, 3.3=Allow): "))
        if Action18 == DELETE:
            print("Virus Deleted")
        elif Action18 == LOCATE:
            print("System Failure = clipboard.failure")
        elif Action18 == ALLOW:
            print("System.error = clipboard.error")
    elif Action3 == ALLOW:
        print("Virus has disabled Clipboard.exe (unfixable)")

elif Virus == 4:
    Action4 = float(input(f"{Virus_Name4} has been detected. Delete it now (1.1=Delete, 2.2=Locate, 3.3=Allow): "))
    if Action4 == DELETE:
        print("Virus deleted")
    elif Action4 == LOCATE:
        print("Virus located in Desktop")
    elif Action4 == ALLOW:
        print("System compromised: Backdoor opened")

elif Virus == 5:
    Action5 = float(input(f"{Virus_Name5} (Ransomware) detected! (1.1=Delete, 2.2=Locate, 3.3=Allow): "))
    if Action5 == DELETE:
        print("Ransomware deleted successfully!")
    elif Action5 == LOCATE:
        print("Ransomware located in Documents folder.")
        Action17 = float(input("Enter follow-up action (1.1=Delete, 2.2=Ignore, 3.3=Allow): "))
        if Action17 == DELETE:
            print("Virus deleted, system safe again.")
        elif Action17 == LOCATE:
            print("System locked temporarily!")
        elif Action17 == ALLOW:
            print("Files encrypted! System under attack!")
    elif Action5 == ALLOW:
        print("Ransomware allowed. Files are now encrypted!")

else:
    print("Invalid virus type entered.")
