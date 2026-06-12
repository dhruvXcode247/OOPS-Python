class chatbook:
    __user_id=0
    # static variable
    def __init__(self):
        self.id=chatbook.__user_id
        # static variable can only be accessed by using the class name and not by self
        chatbook.__user_id+=1
        # encapsulation
        self.__name="Dhruv"
        # __ before a variable name ensures that the variable is encapsulated and cannot be accessed outside the class
        # to access it outside the class we can create a getter method as "classobjectname._classname__variablename" but inside the class as "self.__variablename"
        # so due to this reason python is not 100% secure like other languages including Java & C++ where we cannot access outside the class
        self.username=''
        self.password=''
        self.loggedin=False
        self.menu()

        @staticmethod
        def get_id():
            return chatbook.__user_id
        
        @staticmethod()
        def set_id(val):
            chatbook.__user_id=val

        def get_name(self):
            return self.__name
        
        def set_name(self,value):
            self.__name=value

    def menu(self):
        user_input=input("""Welcome to Chatbook!! How would you like to proceed?
                         1. Press 1 to Sign Up
                         2. Press 2 to Sign In
                         3. Press 3 to write a post
                         4. Press 4 to message a friend
                         5. Press any other key to exit

                         -> """)
        
        if user_input== "1":
            self.signup()
        elif user_input== "2":
            self.signin()
        elif user_input== "3":
            self.my_post()
        elif user_input== "4":
            self.sendmsg()
        else:
            exit()

    def signup(self):
        email=input("Enter your email:")
        pwd=input("Enter your password:")
        self.username=email
        self.password=pwd
        print("You have successfully signed up!!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print("You have not signed up yet!! Please sign up first by clicking 1 in the main menu")
        else:
            uname=input("Enter your email/username here:")
            pwd=input("Enter your password here:")
            if self.username==uname and self.password==pwd:
                print("You have successfully signed in!!")
                self.Loggedin=True
            else:
                print("Please input correct credentials...")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin==True:
            txt=input("Enter your message here->")
            print(f"The following content has been posted -> {txt}")
        else:
            print("You need to signin first to post something...")
        print("\n")
        self.menu()

    def sendmsg(self):
        if self.loggedin==True:
            txt=input("Enter your message here->")
            frnd=input("Whom to send the message? ->")
            print(f"Your message has been sent to {frnd}")
        else:
            print("You need to signin first to send a message...")
        print("\n")
        self.menu()

user1=chatbook()