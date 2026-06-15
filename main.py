import json

try:
    with open("notes.json", "r") as file:
        notes= json.load(file)
except FileNotFoundError:
        print("file NOT found")
        notes={}
def menu():
    try :
        choice=int(input("ENTER THE CHOICE: \n 1) ADD NOTE \n 2) VIEW NOTES \n 3) DELETE NOTES \n 4) EXIT  \n"))
    except ValueError:
        print("Invalid value entered")
        menu()
    else:
        return choice

def add_note():
    note_id=str(len(notes)+1)  #use str because during json parsing , the key are turned into string and here they are int , this creates mixed type of datat types. AVOID IT!!    
    try :
        note_enter=str(input("ENTER THE NOTE PLEASE : \n"))
    except ValueError:
        print("INVALID STRING ! TRY AGAIN")
        add_note()
    else:
        notes[note_id]=note_enter
        with open("notes.json",'w') as file:
            json.dump(notes,file) 
        main()  
          
def view_note():
    for key , value in notes.items():
        print(f"{key}: {value}")
    main()
def delete_note():
    try:
        index=int(input("Enter note's index to be deleted : "))
    except ValueError:
        print("Enter an integer please \n")
        delete_note()
    else:
        del notes[f"{index}"]
    main()
        
        
        
def main():
    choice = menu()
    match choice:
        case 1:
            add_note()
        case 2:
            view_note()
        case 3:
            delete_note()
        case 4:
            pass
        case _:
            print("Nothing corresponds to this option")
    
main()