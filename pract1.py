#Bharati Hospital Information Agent

while True:
    print("\n---------BHARATI HOSPITAL----------")
    print("1)OPD Timings")
    print("2)Book Appointment")
    print("3)Location")
    print("4)Lab Tests")
    print("5)Consulation Fee")
    print("6)Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        print("\n---------OPD TIMINGS---------")
        print("Monday-Saturday, 9:00 AM - 5:00 PM")

    elif choice == "2":
        print("\n-------BOOK APPOINTMENTS----------")
        print("Call +91 9876543221 or Visit the Hospital")

    elif choice == "3":
        print("\n--------LOCATION---------")
        print("Bharati Hospital, Pune-Satara Road, Bharti Vidyapeeth Campus")
        print("Katraj-Dhankawadi Road, Pune")

    elif choice == "4":
        print("\n---------LAB TESTS---------")
        print("Lab services are available 24/7")
        print("1)Haemotolgy")
        print("2)Clinical Pathology")
        print("3)Biochemistry")

        lab = input("Enter your Choice : ")

        if lab == "1":
            print("Haemotology : Complete Blood and Bone marrow tests")

        elif lab == "2":
            print("Clinical Pathology : Urine and stool tests")

        elif lab == "3":
            print("Liver, kidney and lipid profiles")

        else:
            print("Invalid Choice")

    elif choice == "5":
        print("\n-----CONSULTATION FEE-------")
        print("1)Dermatologist")
        print("2)Cardiologist")
        print("3)Orthopaedic")

        doctor = input("Enter your Choice : ")

        if doctor == "1":
            print("Dermatologist : Fee Rs - 400")
            print("Specialist in acne treatment , hair loss , skin etc")

        if doctor == "2":
            print("Cardiologist : Fee Rs - 900")
            print("Specialist in Heart , ECG , blood")

        if doctor == "3":
            print("Orthopedic : Fee Rs - 500")
            print("Specialist in bones, joints etc")

    elif choice == "6":
        print("\nThankyou")
        print("Have a nice day!")
        break

    else:
        print("Invalid Choice")

        