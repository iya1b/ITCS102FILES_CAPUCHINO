import random
import sys

# =========================
# Global Data Structures
# =========================
assignments = {}
study_tasks = {}
notes = {}
reminders = {}
expenses = {}
ipon = {}
workouts = {}
meals = {}
water_intake = 0
number_guess_history = []
rps_history = []
dice_history = []
quotes = []
timetable = {}
objectives = {}
personal_diary = {}
quick_notes = {}
library = {}
skills = {}
budget = {}
contacts = {}
daily_journal = {}
events = {}
health = {"sleep": [], "mood": []}
mini_games_scores = {}

def main_menu():
    while True:
        print("\n⋆ ˚☁️ ⁀➴ IYA TALA, THE STUDENT LIFE MANAGEMENT SYSTEM  • 🦋")
        print("A – 💻📝   Assignments")
        print("B – 🗓️📌   Study Tasks")
        print("C – 📓🗒    Notes")
        print("D – 📌📝   Reminders")
        print("E – 🧾💸   Expenses")
        print("F – 💰🐖   IPON (Income Tracker)")
        print("G – 💪🏻   Workouts")
        print("H – 🍽️🍰     Meals")
        print("I – 💧🥛    Water Intake")
        print("J – 🎮🔢   Number Guessing Game")
        print("K – 👊✌️✋  Rock Paper Scissors Game")
        print("L – 🎲🎰   Dice Roll Simulator")
        print("M – 🌟💭   Motivational Quotes")
        print("N – 📅⏰   Timetable / Schedule")
        print("O – 📍🎯    Objectives / Goals Tracker")
        print("P – 📔✍🏻   Personal Diary / Journal")
        print("Q – 🗒📝    Quick Notes / Scratchpad")
        print("R – 📚📖   Library / Books")
        print("S – 🛠️✒️     Skills Tracker")
        print("T – 📜      Budget Planner")
        print("U – 🤜🤛   Contacts / Friends")
        print("V – 🌷💭   Daily Journal")
        print("W – 📅🕓   Events / Calendar")
        print("X – 📈🩺   Health Tracker")
        print("Y – 🎮🥇   Fun / Mini Games")
        print("Z – 🔚     Exit Program")
        choice = input("Choose option: ").upper()

        if choice == "A": assignments_menu()
        elif choice == "B": study_tasks_menu()
        elif choice == "C": notes_menu()
        elif choice == "D": reminders_menu()
        elif choice == "E": expenses_menu()
        elif choice == "F": ipon_menu()
        elif choice == "G": workouts_menu()
        elif choice == "H": meals_menu()
        elif choice == "I": water_menu()
        elif choice == "J": number_guess_game()
        elif choice == "K": rps_game()
        elif choice == "L": dice_game()
        elif choice == "M": quotes_menu()
        elif choice == "N": timetable_menu()
        elif choice == "O": objectives_menu()
        elif choice == "P": diary_menu()
        elif choice == "Q": quick_notes_menu()
        elif choice == "R": library_menu()
        elif choice == "S": skills_menu()
        elif choice == "T": budget_menu()
        elif choice == "U": contacts_menu()
        elif choice == "V": daily_journal_menu()
        elif choice == "W": events_menu()
        elif choice == "X": health_menu()
        elif choice == "Y": fun_games_menu()
        elif choice == "Z": exit_program()
        else:
            print("Invalid choice. Try again.")

# ⋆｡‧˚ʚ🍓ɞ˚‧｡⋆
# the program will start here
# ٩(ˊᗜˋ*)و ♡



# ────── ⋆⋅☆⋅⋆ ──────
# A – Assignments
# ────── ⋆⋅☆⋅⋆ ──────

def assignments_menu():
    while True:
        print("\n۶ৎ ASSIGNMENTS MENU ۶ৎ")
        print("1. Add Assignment")
        print("2. View Assignments")
        print("3. Delete Assignment")
        print("4. Back")
        choice = input("Choose option: ")
        if choice == "1":
            aid = input("Assignment ID: ").upper()
            title = input("Title: ")
            due = input("Due Date: ")
            assignments[aid] = [title, due]
            print("Assignment added! ૮ ․ ․ ྀིა")
        elif choice == "2":
            for aid, info in assignments.items():
                print(f"ID: {aid}, Title: {info[0]}, Due: {info[1]}")
        elif choice == "3":
            aid = input("Enter Assignment ID to delete: ").upper()
            if aid in assignments:
                del assignments[aid]
                print("Deleted! ⋆˚✿˖°")
            else:
                print("ID not found.")
        elif choice == "4":
            break
        else:
            print("Sorry, invalid choice.")

# ⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢
#  ﹉﹉﹉﹉﹉୨♡୧﹉﹉﹉﹉﹉
#      B – Study Tasks
#   ┈ ┈ ┈ ┈ ୨♡୧ ┈ ┈ ┈ ┈
# ⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣

def study_tasks_menu():
    while True:
        print("\n❤︎ STUDY TASKS MENU ⋆˚࿔")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Back")
        choice = input("Choose option: ")
        if choice == "1":
            tid = input("Task ID: ").upper()
            desc = input("Description: ")
            study_tasks[tid] = desc
            print("Task added! ദ്ദി(ᵔᗜᵔ)")
        elif choice == "2":
            for tid, desc in study_tasks.items():
                print(f"ID: {tid}, Description: {desc}")
        elif choice == "3":
            tid = input("⋆.˚Please enter the task ID that you want to delete: ").upper()
            if tid in study_tasks:
                del study_tasks[tid]
                print("Deleted! .☘︎ ݁˖")
            else:
                print("Sorry! ID not found.")
        elif choice == "4":
            break
        else:
            print("Sorry, invalid choice.")



#    ─── ⋆⋅☼⋅⋆ ───
#     C – Notes
#    ─── ⋆⋅☼⋅⋆ ───

def notes_menu():
    while True:
        print("\n✮⋆˙ NOTES MENU ♡ˎˊ˗")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Back")
        choice = input("Choose option: ")
        if choice == "1":
            nid = input("Note ID: ").upper()
            content = input("Content: ")
            notes[nid] = content
            print("Note added!<𝟑 .ᐟ")
        elif choice == "2":
            for nid, content in notes.items():
                print(f"ID: {nid}, Note: {content}")
        elif choice == "3":
            nid = input("Note ID to delete: ").upper()
            if nid in notes:
                del notes[nid]
                print("Deleted!࣪ ִֶָ☾.")
            else:
                print("Sorry! ID not found.")
        elif choice == "4":
            break
        else:
            print("Sorry, invalid choice.")



#   ‧₊ ˚  ⊹ ࣭ ⭑ . ₊ ⊹ .₊๋
#     D – Reminders
#   ‧₊ ˚  ⊹ ࣭ ⭑ . ₊ ⊹ .₊๋

def reminders_menu():
    while True:
        print("\n✧˖°. REMINDERS MENU ──★ ˙🍓 ̟ !!")
        print("1. Add Reminder")
        print("2. View Reminders")
        print("3. Delete Reminder")
        print("4. Back")
        choice = input("Choose option: ")
        if choice == "1":
            rid = input("Reminder ID: ").upper()
            desc = input("Reminder: ")
            reminders[rid] = desc
            print("Reminder added! ⪩. .⪨")
        elif choice == "2":
            for rid, desc in reminders.items():
                print(f"ID: {rid}, Reminder: {desc}")
        elif choice == "3":
            rid = input("Reminder ID to delete: ").upper()
            if rid in reminders:
                del reminders[rid]
                print("Deleted! •ᴗ•")
            else:
                print("Sorry! ID not found.")
        elif choice == "4":
            break
        else:
            print("Sorry, invalid choice.")



# ︵‿︵‿୨♡୧‿︵‿︵
#   E – Expenses
# ︵‿︵‿୨♡୧‿︵‿︵

def expenses_menu():
    while True:
        print("\n⟡ ݁₊ . EXPENSES MENU ༘⋆")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Back")
        choice = input("Choose option: ")
        if choice == "1":
            eid = input("Expense ID: ").upper()
            amount = float(input("Amount: "))
            desc = input("Description: ")
            expenses[eid] = [amount, desc]
            print("Expense added! ദ്ദി( T ᗜ T )")
        elif choice == "2":
            for eid, info in expenses.items():
                print(f"ID: {eid}, Amount: {info[0]}, Description: {info[1]}")
        elif choice == "3":
            eid = input("Expense ID to delete: ").upper()
            if eid in expenses:
                del expenses[eid]
                print("Deleted! -`♡´-")
            else:
                print("Sorry! ID not found.")
        elif choice == "4":
            break
        else:
            print("Sorry, invalid choice.")



#   -ˋˏ ༻❁༺ ˎˊ-
#    F – IPON
#   -ˋˏ ༻❁༺ ˎˊ-

def ipon_menu():
    while True:
        print("\n⊹₊⟡⋆ IPON MENU ⊹₊⟡⋆")
        print("1. Add Savings")
        print("2. View Savings")
        print("3. Delete Entry")
        print("4. Back")
        choice = input("Choose option: ")
        if choice == "1":
            sid = input("ID: ").upper()
            amount = float(input("Amount: "))
            ipon[sid] = amount
            print("Saved! ೀ")
        elif choice == "2":
            for sid, amount in ipon.items():
                print(f"ID: {sid}, Amount: {amount}")
        elif choice == "3":
            sid = input("ID to delete: ").upper()
            if sid in ipon:
                del ipon[sid]
                print("Deleted! °｡⋆♡")
            else:
                print("Sorry! ID not found.")
        elif choice == "4":
            break
        else:
            print("Sorry, invalid choice.")



# ﹒˚ ₊ ︵﹒⊹ ๑ ︵︵ ๑ ⊹﹒︵
#       G – Workouts
# ﹒˚ ₊ ︵﹒⊹ ๑ ︵︵ ๑ ⊹﹒︵

def workouts_menu():
    while True:
        print("\n ༻ ☽ ⊱ WORKOUTS MENU ⊰ ☾ ༺ ")
        print("1. Add Workout")
        print("2. View Workouts")
        print("3. Delete Workout")
        print("4. Back")
        choice = input("Choose option: ")
        if choice == "1":
            wid = input("Workout ID: ").upper()
            name = input("Workout Name: ")
            duration = input("Duration (minutes): ")
            workouts[wid] = [name, duration]
            print("Workout added! *ೃ༄")
        elif choice == "2":
            for wid, info in workouts.items():
                print(f"ID: {wid}, Name: {info[0]}, Duration: {info[1]} mins")
        elif choice == "3":
            wid = input("Workout ID to delete: ").upper()
            if wid in workouts:
                del workouts[wid]
                print("Deleted! ੈ♡˳")
            else:
                print("Sorry! ID not found.")
        elif choice == "4":
            break
        else:
            print("Sorry, invalid choice.")



#   ─── ⋆⋅ ☾⋅⋆ ───
#     H – Meals
#   ─── ⋆⋅ ☾⋅⋆ ───

def meals_menu():
    while True:
        print("\n✶⋆.˚ MEALS MENU ₊°｡❆")
        print("1. Add Meal")
        print("2. View Meals")
        print("3. Delete Meal")
        print("4. Back")
        choice = input("Choose option: ")
        if choice == "1":
            mid = input("Meal ID: ").upper()
            name = input("Meal Name: ")
            calories = input("Calories: ")
            meals[mid] = [name, calories]
            print("Meal added! ؛༊ ")
        elif choice == "2":
            for mid, info in meals.items():
                print(f"ID: {mid}, Name: {info[0]}, Calories: {info[1]}")
        elif choice == "3":
            mid = input("Meal ID to delete: ").upper()
            if mid in meals:
                del meals[mid]
                print("Deleted! ૮ ˶ᵔ ᵕ ᵔ˶ ა")
            else:
                print("Sorry! ID not found.")
        elif choice == "4":
            break
        else:
            print("Sorry, invalid choice.")



# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
#    I – Water Intake
# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

def water_menu():
    global water_intake
    while True:
        print("\n*ੈ✩‧₊˚ WATER INTAKE MENU *ੈ✩‧₊˚")
        print("1. Add Glass")
        print("2. View Total")
        print("3. Reset")
        print("4. Back")
        choice = input("Choose option: ")
        if choice == "1":
            g = int(input("Glasses: "))
            water_intake += g
            print(f"Added {g} glasses. Total: {water_intake}")
        elif choice == "2":
            print(f"Total glasses: {water_intake}")
        elif choice == "3":
            water_intake = 0
            print("Reset.")
        elif choice == "4":
            break
        else:
            print("Sorry, invalid choice.")



# •───────•°•❀•°•───────•
# J – Number Guessing Game
# •───────•°•❀•°•───────•

def number_guess_game():
    while True:
        print("\n*ੈ✩‧₊˚ NUMBER GUESSING GAME ˚. ᵎᵎ")
        print("1. Play Game")
        print("2. View History")
        print("3. Back")
        choice = input("Choose option: ")
        if choice == "1":
            num = random.randint(1,10)
            guess = int(input("Guess a number (1-10): "))
            if guess == num:
                print("Wow! you got it right! ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧")
                number_guess_history.append((guess, num, "Win"))
            else:
                print(f"Oooops, sorry! You got it wrong. The number was {num}")
                number_guess_history.append((guess, num, "Lose"))
        elif choice == "2":
            for h in number_guess_history:
                print(f"Guessed: {h[0]}, Actual: {h[1]}, Result: {h[2]}")
        elif choice == "3":
            break
        else:
            print("Sorry, invalid choice.")



#      ─── ⋆⋅ ❤︎ ⋅⋆ ───
# K – Rock Paper Scissors Game
#      ─── ⋆⋅ ❤︎ ⋅⋆ ───

def rps_game():
    while True:
        print("\n✧˖°. ROCK PAPER SCISSORS ༘⋆")
        print("1. Play Game")
        print("2. View History")
        print("3. Back")
        choice = input("Choose option: ")
        if choice == "1":
            options = ["rock","paper","scissors"]
            user = input("Choose rock/paper/scissors: ").lower()
            computer = random.choice(options)
            if user == computer:
                result = "It's a tie ˚.🎀༘⋆"
            elif (user=="rock" and computer=="scissors") or (user=="paper" and computer=="rock") or (user=="scissors" and computer=="paper"):
                result = "Congrats, you win! ˚ ༘ ೀ⋆｡˚"
            else:
                result = "Sorry, you lose (•́ ᴖ •̀)"
            print(f"You: {user}, Computer: {computer}, Result: {result}")
            rps_history.append((user, computer, result))
        elif choice == "2":
            for h in rps_history:
                print(f"You: {h[0]}, Computer: {h[1]}, Result: {h[2]}")
        elif choice == "3":
            break
        else:
            print("Sorry, invalid choice.")



#      ─── ⋆⋅☆⋅⋆ ───
# L – Dice Roll Simulator
#      ─── ⋆⋅☆⋅⋆ ───

def dice_game():
    while True:
        print("\n✮⋆˙ DICE ROLL SIMULATOR ˙⋆✮ ")
        print("1. Roll Dice")
        print("2. View History")
        print("3. Back")
        choice = input("Choose option: ")
        if choice == "1":
            roll = random.randint(1,6)
            print(f"Dice Rolled: {roll}")
            dice_history.append(roll)
        elif choice == "2":
            print("Roll History:", dice_history)
        elif choice == "3":
            break
        else:
            print("Sorry, invalid choice.")



#    ✦•┈๑⋅⋯ ⋯⋅๑┈•✦
# M – Motivational Quotes
#    ✦•┈๑⋅⋯ ⋯⋅๑┈•✦

def quotes_menu():
    while True:
        print("\n.☘︎ ݁˖ MOTIVATIONAL QUOTES MENU .☘︎ ݁˖")
        print("1. Add Quote")
        print("2. View All Quotes")
        print("3. Delete Quote")
        print("4. Get Random Quote")
        print("5. Back")
        choice = input("Choose option: ")
        
        if choice == "1":
            qid = input("Quote ID: ").upper()
            content = input("Enter the quote: ")
            quotes.append((qid, content))
            print("Quote added successfully! ⋆˚✿˖°")
        
        elif choice == "2":
            if len(quotes) == 0:
                print("Sorry, there's no quotes available.")
            else:
                print("\n⋆｡°·☁︎ ALL MOTIVATIONAL QUOTES ☁︎·°｡⋆")
                for qid, content in quotes:
                    print(f"ID: {qid} | \"{content}\"")
        
        elif choice == "3":
            delete_id = input("Quote ID to delete: ").upper()
            found = False
            for i in range(len(quotes)):
                if quotes[i][0] == delete_id:
                    quotes.pop(i)
                    print("Quote deleted successfully! ⋆.ೃ࿔*:･")
                    found = True
                    break
            if not found:
                print("Sorry, Quote ID not found.")
        
        elif choice == "4":
            if len(quotes) == 0:
                print("Sorry, there's no quotes to choose from.")
            else:
                qid, content = random.choice(quotes)
                print("\n✧˖° RANDOM MOTIVATIONAL QUOTE ˚˖𓍢🦢˚")
                print(f"\"{content}\"")
        
        elif choice == "5":
            print("Returning to main menu...")
            break
        
        else:
            print("Sory, invalid option. Please try again.")



#     ⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖
# N – Timetable / Schedule
#     ⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖

def timetable_menu():
    while True:
        print("\n~*🍓 TIMETABLE MENU *~  ིྀ")
        print("1. Add Schedule")
        print("2. View Schedule")
        print("3. Delete Schedule")
        print("4. Back")
        choice = input("Choose option: ")
        if choice == "1":
            tid = input("Schedule ID: ").upper()
            desc = input("Description: ")
            timetable[tid] = desc
            print("Schedule added!.ᐟજ⁀➴")
        elif choice == "2":
            for tid, desc in timetable.items():
                print(f"ID: {tid}, Description: {desc}")
        elif choice == "3":
            tid = input("ID to delete: ").upper()
            if tid in timetable:
                del timetable[tid]
                print("Deleted! 🧸ྀི")
            else:
                print("Sorry! ID not found.")
        elif choice == "4":
            break
        else:
            print("Sorry, invalid choice.")



#        . ݁₊ ⊹ . ݁˖ . ݁༉‧₊˚.
# O – Objectives / Goals Tracker
#        . ݁₊ ⊹ . ݁˖ . ݁༉‧₊˚.

def objectives_menu():
    while True:
        print("\n⁺‧₊˚ ཐི⋆ GOALS MENU ⋆ཋྀ ˚₊‧⁺")
        print("1. Add Goal")
        print("2. View Goals")
        print("3. Delete Goal")
        print("4. Back")
        choice = input("Choose option: ")
        
        if choice == "1":
            oid = input("Goal ID: ").upper()
            desc = input("Goal Description: ")
            objectives[oid] = desc
            print("Goal added! 𓏲 ๋࣭ ࣪ ˖🎐")
        
        elif choice == "2":
            for oid, desc in objectives.items():
                print(f"ID: {oid}, Goal: {desc}")
        
        elif choice == "3":
            oid = input("Goal ID to delete: ").upper()
            if oid in objectives:
                del objectives[oid]
                print("Goal deleted! ⋆｡°✩")
            else:
                print("Sorry, ID not found.")
        
        elif choice == "4":
            break
        
        else:
            print("Sorry, invalid choice.")



#         ─── ⋆⋅☼⋅⋆ ───
# P – Personal Diary / Journal
#         ─── ⋆⋅☼⋅⋆ ───

def diary_menu():
    while True:
        print("\n🎧ྀི⋆.✮ PERSONAL DIARY MENU ✮.⋆ྀི🎧")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Delete Entry")
        print("4. Back")
        choice = input("Choose option: ")
        if choice == "1":
            did = input("Entry ID: ").upper()
            content = input("Content: ")
            personal_diary[did] = content
            print("Entry added! ִ🐇་༘࿐")
        elif choice == "2":
            for did, content in personal_diary.items():
                print(f"ID: {did}, Entry: {content}")
        elif choice == "3":
            did = input("ID to delete: ").upper()
            if did in personal_diary:
                del personal_diary[did]
                print("Deleted! 🎧⊹♡")
            else:
                print("Sorry, ID not found.")
        elif choice == "4":
            break
        else:
            print("Sorry, invalid choice.")



#      ⛧°。 ⋆༺♱༻⋆。 °⛧
# Q – Quick Notes / Scratchpad
#      ⛧°。 ⋆༺♱༻⋆。 °⛧

def quick_notes_menu():
    while True:
        print("\n꒰ঌ₍ᐢ. QUICK NOTES MENU .ᐢ₎໒꒱")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Back")
        choice = input("Choose option: ")
        if choice == "1":
            qnid = input("ID: ").upper()
            content = input("Content: ")
            quick_notes[qnid] = content
            print("Note Added! ˙✧˖°📷 ༘ ⋆｡˚")
        elif choice == "2":
            for qnid, content in quick_notes.items():
                print(f"ID: {qnid}, Note: {content}")
        elif choice == "3":
            qnid = input("ID to delete: ").upper()
            if qnid in quick_notes:
                del quick_notes[qnid]
                print("Deleted! ⭑ .ᐟ ᡣ𐭩")
            else:
                print("Sorry, ID not found.")
        elif choice == "4":
            break
        else:
            print("Sorry, invalid choice.")



#  ✦·┈๑⋅⋯ ⋯⋅๑┈·✦
# R – Library / Books
#  ✦·┈๑⋅⋯ ⋯⋅๑┈·✦


def library_menu():
    while True:
        print("\n✮⋆˙ LIBRARY / BOOKS MENU ˙⋆✮")
        print("1. Add Book")
        print("2. View Books")
        print("3. Delete Book")
        print("4. Back")
        choice = input("Choose option: ")
        if choice == "1":
            bid = input("Book ID: ").upper()
            title = input("Title: ")
            author = input("Author: ")
            library[bid] = [title, author]
            print("Book added! ˚.🎀༘⋆")
        elif choice == "2":
            for bid, info in library.items():
                print(f"ID: {bid}, Title: {info[0]}, Author: {info[1]}")
        elif choice == "3":
            bid = input("ID to delete: ").upper()
            if bid in library:
                del library[bid]
                print("Deleted! .☘︎ ݁˖")
            else:
                print("Sorry! ID not found.")
        elif choice == "4":
            break
        else:
            print("Sorry, invalid choice.")



#  ✦·┈๑⋅⋯ ⋯⋅๑┈·✦
# S – Skills Tracker
#  ✦·┈๑⋅⋯ ⋯⋅๑┈·✦

def skills_menu():
    while True:
        print("\n 𓏲 ๋࣭  ࣪ ˖ SKILLS TRACKER MENU .˖🛸── .✦")
        print("1. Add Skill")
        print("2. View Skills")
        print("3. Delete Skill")
        print("4. Back")
        choice = input("Choose option: ")
        if choice == "1":
            sid = input("Skill ID: ").upper()
            name = input("Skill Name: ")
            level = input("Level (Beginner/Intermediate/Advanced): ")
            skills[sid] = [name, level]
            print("Skill added! ˚ ༘ ೀ⋆｡˚")
        elif choice == "2":
            for sid, info in skills.items():
                print(f"ID: {sid}, Skill: {info[0]}, Level: {info[1]}")
        elif choice == "3":
            sid = input("Skill ID to delete: ").upper()
            if sid in skills:
                del skills[sid]
                print("Deleted! ♬⋆.˚")
            else:
                print("Sorry! ID not found.")
        elif choice == "4":
            break
        else:
            print("Sorry, invalid choice.")




# ▌│█║▌║▌║▌│█║▌║▌║▌│█║▌║▌║
#   T – Budget Planner
# ▌│█║▌║▌║▌│█║▌║▌║▌│█║▌║▌║

def budget_menu():
    while True:
        print("\n˚ ༘ ೀ⋆｡˚ BUDGET PLANNER MENU ୭ ˚. ᵎᵎ")
        print("1. Add Budget")
        print("2. View Budget")
        print("3. Delete Budget")
        print("4. Back")
        choice = input("Choose option: ")
        if choice == "1":
            bid = input("Budget ID: ").upper()
            desc = input("Description: ")
            amount = float(input("Amount: "))
            budget[bid] = [desc, amount]
            print("Budget added! ༘⋆")
        elif choice == "2":
            for bid, info in budget.items():
                print(f"ID: {bid}, Description: {info[0]}, Amount: {info[1]}")
        elif choice == "3":
            bid = input("ID to delete: ").upper()
            if bid in budget:
                del budget[bid]
                print("Deleted! 💗ྀི")
            else:
                print("Sorry! ID not found.")
        elif choice == "4":
            break
        else:
            print("Sorry, invalid choice.")



#       ∘₊✧───✧₊∘
# U – Contacts / Friends
#       ∘₊✧───✧₊∘

def contacts_menu():
    while True:
        print("\n‧₊˚ ☁️ CONTACTS / FRIENDS MENU 🪐༘⋆")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Back")
        choice = input("Choose option: ")
        if choice == "1":
            cid = input("Contact ID: ").upper()
            name = input("Name: ")
            phone = input("Phone Number: ")
            contacts[cid] = [name, phone]
            print("Contact added! ٩(ˊᗜˋ*)و ♡")
        elif choice == "2":
            for cid, info in contacts.items():
                print(f"ID: {cid}, Name: {info[0]}, Phone: {info[1]}")
        elif choice == "3":
            cid = input("Contact ID to delete: ").upper()
            if cid in contacts:
                del contacts[cid]
                print("Deleted! ༘⋆✿")
            else:
                print("Sorry! ID not found.")
        elif choice == "4":
            break
        else:
            print("Sorry, invalid choice.")



#    ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆
#  V – Daily Journal
#    ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆

def daily_journal_menu():
    while True:
        print("\n🩰˚˖𓍢 DAILY JOURNAL MENU ✧˚.🎀")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Delete Entry")
        print("4. Back")
        choice = input("Choose option: ")
        if choice == "1":
            vid = input("Entry ID: ").upper()
            content = input("Content: ")
            daily_journal[vid] = content
            print("Entry added! 🎧ྀི")
        elif choice == "2":
            for vid, content in daily_journal.items():
                print(f"ID: {vid}, Entry: {content}")
        elif choice == "3":
            vid = input("ID to delete: ").upper()
            if vid in daily_journal:
                del daily_journal[vid]
                print("Deleted! ⋆˚🐾˖°")
            else:
                print("Sorry! ID not found.")
        elif choice == "4":
            break
        else:
            print("Sorry, invalid choice.")




#  ⋅˚₊‧ ୨🍙🍣🍱🥢୧ ‧₊˚ ⋅
# W – Events / Calendar
#  ⋅˚₊‧ ୨🍙🍣🍱🥢୧ ‧₊˚ ⋅

def events_menu():
    while True:
        print("\nᲘ︵𐑼 EVENTS / CALENDAR MENU Ი︵𐑼")
        print("1. Add Event")
        print("2. View Events")
        print("3. Delete Event")
        print("4. Back")
        choice = input("Choose option: ")
        if choice == "1":
            eid = input("Event ID: ").upper()
            desc = input("Description: ")
            date = input("Date: ")
            events[eid] = [desc, date]
            print("Event added! ⋆˚✿🍒")
        elif choice == "2":
            for eid, info in events.items():
                print(f"ID: {eid}, Event: {info[0]}, Date: {info[1]}")
        elif choice == "3":
            eid = input("Event ID to delete: ").upper()
            if eid in events:
                del events[eid]
                print("Deleted! ᶻ 𝗓 𐰁 .ᐟ")
            else:
                print("Sorry! ID not found.")
        elif choice == "4":
            break
        else:
            print("Sorry, invalid choice.")



# •───────•°•❀•°•───────•
#   X – Health Tracker
# •───────•°•❀•°•───────•

def health_menu():
    while True:
        print("\nꕥ HEALTH TRACKER MENU ༊*·˚")
        print("1. Add Sleep Hours")
        print("2. Add Mood")
        print("3. View Health Data")
        print("4. Back")
        choice = input("Choose option: ")
        if choice == "1":
            hours = float(input("Sleep hours: "))
            health["sleep"].append(hours)
            print("Added! ✨")
        elif choice == "2":
            mood = input("Mood: ")
            health["mood"].append(mood)
            print("Added! ✨")
        elif choice == "3":
            print("Sleep Records:", health["sleep"])
            print("Mood Records:", health["mood"])
        elif choice == "4":
            break
        else:
            print("Sorry, invalid choice.")



#   ─── ⋆⋅ ❤︎ ⋅⋆ ───
# Y – Fun / Mini Games
#   ─── ⋆⋅ ❤︎ ⋅⋆ ───

def fun_games_menu():
    while True:
        print("\n｡･ﾟﾟ･ MINI GAMES MENU ･ﾟﾟ･｡")
        print("1. Number Guessing Game")
        print("2. Rock Paper Scissors")
        print("3. Dice Roll")
        print("4. Back")
        choice = input("Choose option: ")
        if choice == "1":
            number_guess_game()
        elif choice == "2":
            rps_game()
        elif choice == "3":
            dice_game()
        elif choice == "4":
            break
        else:
            print("Sorry, invalid choice.")



#   ༻ ☽ ⊱⋆⊰ ☾ ༺ 
# Z – Exit Program
#   ༻ ☽ ⊱⋆⊰ ☾ ༺ 

def exit_program():
    print("Exiting program. Bye!")
    sys.exit()

main_menu()