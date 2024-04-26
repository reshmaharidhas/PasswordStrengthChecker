import tkinter as tk
import PicturesBase64

# class 'PasswordStrengthChecker'
class PasswordStrengthChecker:
    def __init__(self):
        self.root = tk.Tk()
        # setting the title of the GUI
        self.root.title("Password Strength Checker")
        # Setting the dimension of GUI
        self.root.geometry("600x700")
        self.root.resizable(0, 0)
        # setting the background color of root container
        self.root.config(bg="#E1F7F5")
        # frame 'window' created inside 'root' container with background color set as #E1F7F5
        self.window = tk.Frame(self.root, bg="#E1F7F5")
        self.window.pack(pady=20)
        # pictures converted to PhotoImage variables
        self.bulbPicture = tk.PhotoImage(data=PicturesBase64.bulbPicture)
        self.errorPicture = tk.PhotoImage(data=PicturesBase64.errorPicture)
        self.iconPicture = tk.PhotoImage(data=PicturesBase64.iconPicture)
        # Label
        self.passwordLabel = tk.Label(self.window, text="Password", font=("Arial", 12, "bold"), bg="#E1F7F5")
        self.passwordLabel.pack(pady=1)
        # Entry for user to type or paste their password to check for strength.
        self.passwordEntry = tk.Entry(self.window, font=("Helvetica",15), show="*", width=40)
        self.passwordEntry.pack(pady=10)
        # setting border color and border width of Entry which appears on clicking the Entry
        self.passwordEntry.config(highlightcolor="black", highlightthickness=2)
        # Enabling copy in Entry
        self.passwordEntry.event_generate("<<Copy>>")
        # Enabling paste in Entry
        self.passwordEntry.event_generate("<<Paste>>")
        # variable of integer type to monitor ON and OFF conditions of checkbutton 'hidePassword'
        self.choiceNum = tk.IntVar()
        self.hidePassword = tk.Checkbutton(self.window,text="Show password", onvalue=1,offvalue=0,bg="#E1F7F5",variable=self.choiceNum,command=self.showOrHideEntry,activebackground="#E1F7F5")
        self.hidePassword.pack(pady=2)
        # Button to check the strength of user's password in the Entry 'passwordEntry'.
        self.submitButton = tk.Button(self.window,text="Check your password strength",command=self.checkPasswordStrength, font=("Helvetica",15),bg="blue",fg="white",activebackground="black",activeforeground="white",padx=9)
        self.submitButton.pack(pady=8)
        self.passwordStrength = tk.Label(self.window, font=("Arial", 15), bg="#E1F7F5")
        self.passwordStrength.pack(pady=7)
        # Frame inside 'window' container
        self.frame1 = tk.Frame(self.window, bg="#E1F7F5")
        self.frame1.pack()
        # Setting the icon near to title in GUI
        self.root.iconphoto(True, self.iconPicture)
        self.window.mainloop()

    # Function to check the strength of user entered password in Entry 'passwordEntry'/
    def checkPasswordStrength(self):
        # Getting the string entered by user in Entry 'passwordEntry'.
        userPassword = self.passwordEntry.get()
        # List of strings to display as strength of password in the order of weak to very strong password.
        strength = ["Weak password","Moderate password","Strong password","Very strong password"]
        # symbols in list
        symbolsList = ["!","'",",",".","\"","+","-","/","\\","(",")","*","=","_","&","^","%","$","#","@","|","[","]","{","}","<",">","~","`"]
        # List of commonly used weak passwords worldwide
        commonWeakPasswords = ["password","qwerty","qwertyui","123","123456","xyz","abc","abcdef","admin","1111","000","password123",
                           "password1","123321","monkey","football","hello","iloveyou","dragon","letmein","baseball","flower",
                           "superman","princess","passw0rd","master","root","welcome","starwars","sunshine","777","555","google",
                           "qwert","qwer","qwe","computer","laptop","soccer","222","333","444","666","888","999","apple",
                           "internet","angel","lion","pokemon","ccc","www","zzz","gotham","batman","spiderman","ball","happy",
                           "princes","prince","family","beatles","school","meme","cool","music","dance","man","secret","college",
                           "cat","dog","sweet","disney","house","home","thankyou","software","date"]
        status = 3
        issuesInPassword = []
        ideasToUser = []
        if len(userPassword)<8:
            issuesInPassword.append("Password length very small")
            status = 0
        elif userPassword.isspace():
            issuesInPassword.append("Only white spaces is present")
            status = 0
        # Initialized boolean variables to check for letters, numbers, symbols to False
        hasUpperCase = hasLowerCase = hasDigit = hasSymbol = hasWhiteSpace = False
        countWhiteSpace = sameCharacterRepetition=0
        # Iterate through every character in the string 'userPassword'.
        for ptr in range(len(userPassword)):
            if ptr>0 and userPassword[ptr]==userPassword[ptr-1]:
                sameCharacterRepetition += 1
            character = userPassword[ptr]
            if character==" ":
                hasWhiteSpace = True
                countWhiteSpace += 1
            elif character.isdecimal():
                hasDigit = True
            elif character.isalpha()==True:
                if character.islower():
                    hasLowerCase = True
                elif character.isupper():
                    hasUpperCase = True
            elif character in symbolsList:
                hasSymbol = True
        if sameCharacterRepetition>0:
            issuesInPassword.append("Characters repeating continuously")
        if countWhiteSpace>1:
            issuesInPassword.append("Too many white spaces")
        if hasDigit==False:
            issuesInPassword.append("No numbers present")
        if hasLowerCase==False and hasUpperCase==False:
            issuesInPassword.append("No alphabets present")
        elif hasLowerCase==False and hasUpperCase==True:
            issuesInPassword.append("No letters in lowercase")
        elif hasUpperCase==False and hasLowerCase==True:
            issuesInPassword.append("No letters in uppercase")
        if hasSymbol==False:
            issuesInPassword.append("No symbols")
        # If password has digits,upper and lowercase letters, symbols, rank password based on its length.
        # Also rank based on characters repeating continuously.
        if hasLowerCase==True and hasUpperCase==True and hasDigit==True and hasSymbol==True:
            if len(userPassword)>=8 and len(userPassword)<=10:
                ideasToUser.append("Make password longer")
                status = 1
            elif len(userPassword)>=11 and len(userPassword)<=14:
                ideasToUser.append("Make the password a little longer")
                status = 2
            elif len(userPassword)>=15: # password is length greater than or equal to 15 is considered as VERY STRONG password.
                status = 3
                if len(userPassword)>30:
                    ideasToUser.append("Password very long. Use password manager to store your password!")
            if sameCharacterRepetition>0 or countWhiteSpace>1:
                status = 1
        else:  # User password has digit or letter or symbol missing
            status = 0
        # Check for repeated pattern in user's password.
        # If there are more than 1 pattern repeating, the user password is assumed to be weak.
        # If there is only 1 pattern repeating, if the length of user password is less than 9, it is assumed as weak.
        # Otherwise, if there is only 1 pattern repeating, and the length of user password is more than 8,
        # it is not assumed as weak.
        hasRepeatedPattern = self.checkForPatternRepeating()
        if hasRepeatedPattern==True:
            issuesInPassword.append("Repeating patterns in password")
            status = 0
        # check for commonly used word worldwide as in password.
        # If the user password has any string from the array 'commonWeakPasswords', assume it as WEAK password
        userPasswordInLower = userPassword.lower()
        for commonWord in commonWeakPasswords:
            if userPasswordInLower.find(commonWord) >= 0:
                status = 0
                issuesInPassword.append("Commonly used words found")
                break
        # Displaying strength of password based on its strength number 'status' in different colors.
        if status==0:
            self.passwordStrength.config(text=strength[status],fg="red")
        elif status==1:
            self.passwordStrength.config(text=strength[status],fg="brown")
        elif status==2:
            self.passwordStrength.config(text=strength[status],fg="purple")
        elif status==3:
            self.passwordStrength.config(text=strength[status],fg="green")
        # Before displaying the issues in the user password, delete all previously created widgets within the frame 'frame1'
        for widgets in self.frame1.winfo_children():
            widgets.destroy()
        # Displaying issues in the user's password
        for currentIndex in range(len(issuesInPassword)):
            self.issue = tk.Label(self.frame1,text=issuesInPassword[currentIndex],font=("Arial",13),anchor=tk.NW,image=self.errorPicture,compound=tk.LEFT,bg="#E1F7F5")
            self.issue.pack()
        # Displaying any recommendations to user if available
        for currentIndex in range(len(ideasToUser)):
            self.ideas = tk.Label(self.frame1,text=ideasToUser[currentIndex],image=self.bulbPicture,compound=tk.LEFT,font=("Arial",12),bg="#E1F7F5")
            self.ideas.pack()

    # Function to check if any pattern of string is repeating user's password entered

    def checkForPatternRepeating(self):
        # Get the password entered by user in the Entry
        userPassword = self.passwordEntry.get()
        patternMap = {}
        # variable to store count of repeating patterns of length 3 in the user password
        countOfRepeatedPattern = 0
        for ptr in range(len(userPassword)):
            if (ptr+2)<len(userPassword):
                pattern = userPassword[ptr:ptr+3]
                if pattern not in patternMap:
                    patternMap.update({pattern:1})
                else:
                    # Increment the value of the key in dictionary 'patternMap' as key is reappearing
                    patternMap.update({pattern:patternMap.get(pattern)+1})
        # Get the list of values in the dictionary 'patternMap' and loop through it.
        for patternCount in patternMap.values():
            # If the patternCount is more than 1, increment the value of variable 'countOfRepeatedPattern'.
            if patternCount>1:
                countOfRepeatedPattern += 1
        # If there is only 1 pattern repeating in the user's password, if the length of password is less than 8,
        # consider it as weak password. If the length is greater than 10, return FALSE denoting it is not weak password.
        if countOfRepeatedPattern == 1:
            if len(userPassword) <= 10:
                return True # Weak password
            else:
                return False # Not weak password
        # If the count of patterns repeating is more than 1, then assume the user's password as weak password.
        elif countOfRepeatedPattern > 1:
            return True
        # countOfRepeated is zero. Hence, returning False
        return False
    # Function to change the text to secret code based on whether the checkbutton is clicked
    def showOrHideEntry(self):
        if self.choiceNum.get()==1:
            self.passwordEntry.config(show="")
        else:
            self.passwordEntry.config(show="*")
# Object created for the class 'PasswordStrengthChecker'
PasswordStrengthChecker()