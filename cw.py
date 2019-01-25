def main():
    def quest1():
# * Create a function that has a loop
# * Prompt for numbers until the user enters ```q``` to quit
# * If the user doesn't enter ```q```, ask them to input another number
# * When the user enters ```q``` to quit, print the SUM of all numbers entered
        def omg_this_problem():
            no_more_q=""
            sum=0  #counter
            while (True):
                no_more_q= input("7H15 PR09r4m WIll K33P A 5UM 7r4k 0f UR Num83RZ.\n ""Pr355 q to 35c4p3. ") #Ask for user input
                no_more_q=no_more_q.lower()
                if no_more_q =='q':  #If user enters q, it prints a message and breaks
                    print("0M6 U H4X0R!!!!!!")
                    break
                elif no_more_q == "1337": # Secret message if it enters 1337
                    print("S0 UBER!!!! UR LEET")
                    print(f"The number you entered is: {no_more_q} ") #prints what user entered
                else:
                    print(f"The number you entered is: {no_more_q} ")  #prints what user entered
                sum+=int(no_more_q)
            return sum
        print(omg_this_problem())

    def quest2():
        num1=int(input("Please enter a number. "))
        num2=int(input("Please enter a second number. "))


        def dothemath(firstnum,secondnum):
           #variables for calculatioins
            add=firstnum+secondnum
            sub=firstnum-secondnum
            multi=firstnum*secondnum
            diff=firstnum/secondnum

            x={"Sum":add,"Difference":sub,"Product":multi,"Quotient":diff}  #calculations are values via variablies
            return x
        dummyvar=(dothemath(num1,num2)) #stores as a placeholder variable for the quest2 function to use and calls function


        print(f"You entered: {num1} and {num2}")
        print(f"The Sum is:  {dummyvar['Sum']}")
        print(f"The Difference is: {dummyvar['Difference']}")
        print(f"The Product is: {dummyvar['Product']}")
        print(f"The Quotient is: {dummyvar['Quotient']}")




#quest1()
    quest2()
if __name__ == '__main__':
    main()
