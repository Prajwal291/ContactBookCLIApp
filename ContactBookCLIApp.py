#ContactBookCLIApp

contacts=[]

def add_contact():
    name=input("Name: ")
    phone=input("Phone: ")
    email=input("email: ")


    content={"Name":name,
          "Phone": phone,
          "email": email}

    contacts.append(content)




def view_contacts():
    print("\n========Contacts========\n")

    for contact in contacts:
        for key,value in contact.items():
            print(key,":",value,"\n")
        
            
def search_contact():
    name=input("\nEnter name to search: ")
    found=False
    for contact in contacts:
            if(contact["Name"]==name):
                found=True
                for key,value in contact.items():
                    print(key,":",value)
                break
    else:
        if found==False:
            print("\nContact Not found!\n")

def delete_contact():
    name=input("\nEnter name to delete: ")
    found=False
    for contact in contacts:
        if(contact["Name"]==name):
            print("\nContact deleted successfully!\n")
            found=True
            contacts.remove(contact)
            break
    else:
        if found==False:
            print("\nContact Not found!\n")

import json
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)
        print("\nSaved Successfully\n")
      

def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r") as file:
            contacts=json.load(file)
    except FileNotFoundError:
            print("File Not found")


print("\n=============== Contact Book CLI ===============\n")
load_contacts()
choice=0
while choice!=6:
   print("\n================ CONTACT BOOK ===============\n")
   print("\n 1. Add Contact\n 2. View Contacts\n 3. Search Contact\n 4. Delete Contact\n 5. Save Contacts\n 6. Exit\n")
   choice=input("\nEnter your choice: ")
   if choice==1:
       add_contact()
   elif choice==2:
       view_contacts()
   elif choice==3:
       search_contact()
   elif choice==4:
       delete_contact()
   elif choice==5:
       save_contacts()
   elif choice==6:
       break
   else:
       print("\nInvalid Choice!\n")

save_contacts()



