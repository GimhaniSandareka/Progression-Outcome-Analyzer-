#I declare that my work contains no examples of misconduct,such as plagarism,or collusion
#Any code taken from other sources is referenced within my code solution.


#Date- 3/12/2023

#initializing the variables
user_input=" "
total_credit=0
progress_count=0
trailer_count=0
retriever_count=0
exclude_count=0
total_count=0

#create an empty file named "marks sheet"
import os
file=open("marks sheet.txt",'w')
file.close()
#creating a list to store progression outcomes
progression_outcome=[]
#creating a function to determine pass_credit,defer_credit,fail_credit
def progression():
    global pass_credit,defer_credit,fail_credit
    global progress_count,trailer_count,retriever_count,exclude_count
    global progression_outcome
    if pass_credit==120:
        progression_outcome="Progress"
        progress_count+=1
    elif pass_credit==100:
        progression_outcome="Progress (module trailer)"
        trailer_count+=1
    elif pass_credit<100 and fail_credit<80:
        print("Do not progress- ",end='')
        progression_outcome="Module retriever"
        retriever_count+=1
    elif fail_credit>=80:
        progression_outcome="Exclude"
        exclude_count+=1
    print(progression_outcome)
 
#To store the pass_credit,defer_credit,fail_credit for each progression_outcome in a nested list 
    data_list[progressions.index(progression_outcome)].append([pass_credit,defer_credit,fail_credit])
    
    data=f"{progression_outcome} : {pass_credit}, {defer_credit}, {fail_credit}"
    Text_file(data)
#Creating a function to print the data stored in data_list    
def List():   
    for i in range(len(data_list)):
            for element in data_list[i]:
                print(f"{progressions[i]}-", end =" ")
                print(*element, sep=",")
            
#Function to write the contents of "data"
def Text_file(data):
    with open("marks sheet.txt",'a') as file:
        file.write(data + "\n")
 
credit_list=[0,20,40,60,80,100,120]
#Function to check if user's prompts for pass_credit,defer_credit,fail_credit are valid
def get_credit(prompt):
    
    while True:
        try:
            try:
                credit=int(input(prompt))
                if credit not in credit_list:
                    print("Out of range")
                    continue
                else:
                    return credit
            except ValueError:
                print("Integer required")
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            continue
        
#To store pass_credit,defer_credit,fail_credit of each progreesion_outcome
data_list=[[],[],[],[]]

progressions=["Progress","Progress (module trailer)","Module retriever","Exclude"]
#Ask user to input their pass_credit,defer_credit,fail_credit
while True:
    try:
        user=int(input("Enter '1' if you are a student\nEnter '2' if you are a staff\n"))
        if user==1:             #Checking if user is a student
            while True:
                pass_credit=get_credit("Enter your total PASS credits: ")
                
                defer_credit=get_credit("Enter your total DEFER credits: ")
                
                fail_credit=get_credit("Enter your total FAIL credits: ")
               
                total= (pass_credit+defer_credit+fail_credit)
                
                if total!=120: #check if total is not equal to 120
                    print("Total incorrect")
                    continue
                progression()
                break
            break
                    
        elif user==2:        #Checking if user is a staff member
            
            while True:
                pass_credit=get_credit("Enter your total PASS credits: ")
                
                defer_credit=get_credit("Enter your total DEFER credits: ")
                
                fail_credit=get_credit("Enter your total FAIL credits: ")
               
                total= (pass_credit+defer_credit+fail_credit)
                
                if total!=120: #check if total is not equal to 120
                    print("Total incorrect")
                else:

                    progression()
                    while True:
                        print("Would you like to enter another set of data?")
                        user_choice=input("Enter 'y' for yes or 'q' to quit and view results: ").lower()
                        if user_choice not in ["y", "q"]:#check if user want to enter another set of data .
                            continue
                        else:#check if user want to quit .
                            break
                    if user_choice == "q":
                        break
            print("\n-----------------------------------------------")           
            List() #calling list function
            total_count=progress_count+trailer_count+retriever_count+exclude_count


            progress_px=(progress_count/total_count)*150     #setting the height of progress bar
            trailer_px=(trailer_count/total_count)*150       #setting the height of trailer bar
            retriever_px=(retriever_count/total_count)*150   #setting the height of retriever bar
            exclude_px=(exclude_count/total_count)*150       #setting the height of exclude bar

            import graphics
            from graphics import*


            win=GraphWin("Histogram",600,600)  
            win.setBackground("white")

            heading=Text(Point(200,30),"Histogram Results")  #Display the heading
            heading.setStyle("bold")
            heading.setSize(25)
            heading.draw(win)


            progress_rect=Rectangle(Point(70,500),Point(170,500-progress_px))         #Setting the points of progress bar
            progress_rect.setFill("blue")                                              #Setting a colour to progress bar  
            progress_rect.draw(win)
            progress_rect_count=Text(Point(120,500-progress_px-20),progress_count)     #To display number of progress_count at the top of the progress bar
            progress_rect_count.draw(win)
            progress_rect_name=Text(Point(120,520),"Progress")                          #Display the bar name at the bottom of the bar below x-axis
            progress_rect_name.draw(win)

            trailer_rect=Rectangle(Point(200,500),Point(290,500-trailer_px))
            trailer_rect.setFill("pink")
            trailer_rect.draw(win)
            trailer_rect_count=Text(Point(240,500-trailer_px-20),trailer_count)
            trailer_rect_count.draw(win)
            trailer_rect_name=Text(Point(240,520),"Trailer")
            trailer_rect_name.draw(win)

            retriever_rect=Rectangle(Point(330,500),Point(420,500-retriever_px))
            retriever_rect.setFill("green")
            retriever_rect.draw(win)
            retriever_rect_count=Text(Point(380,500-retriever_px-20),retriever_count)
            retriever_rect_count.draw(win)
            retriever_rect_name=Text(Point(380,520),"Retriever")
            retriever_rect_name.draw(win)

            exclude_rect=Rectangle(Point(460,500),Point(550,500-exclude_px))
            exclude_rect.setFill("yellow")
            exclude_rect.draw(win)
            exclude_rect_count=Text(Point(510,500-exclude_px-20),exclude_count)
            exclude_rect_count.draw(win)
            exclude_rect_name=Text(Point(510,520),"Exclude")
            exclude_rect_name.draw(win)

            xline=Line(Point(50,500),Point(560,500))     #X-axis
            xline.setWidth(3)
            xline.draw(win)

            end_sen=Text(Point(190,550),f"{total_count} outcomes in total")   #Display the total outcomes
            end_sen.setStyle("bold")
            end_sen.setSize(15)
            end_sen.draw(win)

            print("\n--------------------------------------------")
            if os.path.exists("marks sheet.txt"):            #checks if the file "mark sheet.txt" exists
                with open("marks sheet.txt",'r') as file:    # if exists, opens the file in read mode
                    line=file.read()
                    print(line+"\n")
                    
            else:
                print("File doesn't exist")# If FileNotFoundError ,program displays "File doesn't exists"
                break
            break
        
        else:
            print("Please enter '1' or '2'")
            continue
    except KeyboardInterrupt:           #KeyboardInterrupt Error
        print("Keyboard  interrupt")
        continue
    except ValueError:             #Display to enter a integer if user didn't enter integer value
        print("Integer required")
        continue
        

    
