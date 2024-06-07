import tkinter as tk
import json
from tkinter import messagebox
from widgets import WidgetsFactory
from System import controller, Remote

class IntroWindow(tk.Tk):#-------------------------------------intro----------------------------------------
    def __init__(self, delay=3000):
        super().__init__()
        self.title('MUSIC')
        self.geometry('800x900')
        self.resizable(False, False)
        self.configure(bg='forestgreen')
        self.after(delay, self.show_main_window)
        self.widget = WidgetsFactory()
        self.icon()

    def icon(self):
        self.iccon = self.widget.create_label(self, '🎧', ('Courier', 100))
        self.iccon.pack(expand=True)

    def show_main_window(self):
        self.destroy()
        main_window = LoginWindow()
        main_window.display()

class LoginWindow(tk.Tk):#---------------------------------security-------------------------------------
    def __init__(self):
        super().__init__()
        self.title('MUSIC Login')
        self.geometry('800x900')
        self.resizable(False, False)
        self.configure(bg='forestgreen')
        self.widget = WidgetsFactory()
        self.icon_login()

    def icon_login(self):
        self.icons_frame = self.widget.create_frame(self, width=800, height=100, bg='forestgreen')
        self.icons_frame.pack()

        self.iccon = self.widget.create_label(self.icons_frame, '🎧', ('Courier', 70))
        self.iccon.pack()

        self.icon = self.widget.create_label(self.icons_frame, 'Welcome to music world!', ("Helvetica", 16, "bold"))
        self.icon.pack()

        self.usernem_frame = self.widget.create_frame(self, width=800, height=100, bg='forestgreen')
        self.usernem_frame.pack()

        self.user_name_label = self.widget.create_label(self.usernem_frame, 'userename:', ("Helvetica", 10, "bold"))
        self.user_name_label.pack(side='left')

        self.user_name_entry = self.widget.create_entry(self.usernem_frame, width=20)
        self.user_name_entry.pack(side='left')

        self.passcode_frame = self.widget.create_frame(self, width=800, height=100, bg='forestgreen')
        self.passcode_frame.pack()

        self.passcode_label = self.widget.create_label(self.passcode_frame, '  passcode:', ("Helvetica", 10, "bold"))
        self.passcode_label.pack(side='left')

        self.passcode_entry = self.widget.create_entry(self.passcode_frame, show='*', width=20)
        self.passcode_entry.pack(side='left', pady=10)

        self.login_sign_up_buttons_frame = self.widget.create_frame(self, width=800, height=100, bg='forestgreen')
        self.login_sign_up_buttons_frame.pack()

        self.sign_in_button = self.widget.create_button(self.login_sign_up_buttons_frame, text='Log in', command=self.loginna, width=3, height=1)
        self.sign_in_button.pack(side='left')

        self.passcode_label = self.widget.create_label(self.login_sign_up_buttons_frame, 'or')
        self.passcode_label.pack(side='left', padx=10)

        self.sign_up_button = self.widget.create_button(self.login_sign_up_buttons_frame, text='sign up', command=self.signupna, width=3, height=1)
        self.sign_up_button.pack(side='left', pady=30)

    def display(self):
        self.mainloop()

    def loginna(self):
        username = self.user_name_entry.get()
        password = self.passcode_entry.get()

        if username and password:
            try:
                with open('accounts.json', 'r') as f:
                    accounts = json.load(f)
            except FileNotFoundError:
                print("No accounts found.")
                return

            for account in accounts:
                if account['username'] == username and account['password'] == password:
                    print("Login successful.")
                    self.call_song_list()
                    return

            messagebox("Invalid username or password.")
        else:
            messagebox("Username or password cannot be empty.")

    def signupna(self):
        username = self.user_name_entry.get()
        password = self.passcode_entry.get()

        if username and password:
            try:
                with open('accounts.json', 'r') as f:
                    accounts = json.load(f)
            except FileNotFoundError:
                accounts = []

            for account in accounts:
                if account['username'] == username:
                    print("Username already exists.")
                    return

            accounts.append({'username': username, 'password': password})

            with open('accounts.json', 'w') as f:
                json.dump(accounts, f)

            print("Account created successfully.")
        else:
            print("Username or password cannot be empty.")

    def call_song_list(self):
        self.destroy()
        songlist = MusicList()
        songlist.display()

class MusicList(tk.Tk):#----------------------------------Music playlist----------------------------------
    def __init__(self, Controller=controller, remot=Remote):
        super().__init__()
        self.widgests = WidgetsFactory()
        self.remot = remot
        self.controller = Controller
        self.playing = False
        self.selected_index = None
        self.Window_config()
        self.option_frame()
        self.Search_and_list()
        self.Buttons()

    def Window_config(self):
        self.title('🎧Music♬')
        self.geometry('800x900')
        self.resizable(True, True)
        self.configure(bg='forestgreen')

    def option_frame(self):
        self.options_frame = self.widgests.create_frame(self,width=200)
        self.options_frame.pack(side='left', fill='y')

        home = self.widgests.create_button(self.options_frame, text='HOME', command=self.home, width=10, height=1)
        home.pack(pady=5)

        favorites = self.widgests.create_button(self.options_frame, text='FAVORITES', command=print, width=10, height=1)
        favorites.pack(pady=5)

        artist = self.widgests.create_button(self.options_frame, text='ARTISTS', command=self.artist, width=10, height=1)
        artist.pack(pady=5)
        
        settings = self.widgests.create_button(self.options_frame, text='SETTINGS', command=print, width=10, height=1)
        settings.pack(pady=5)
        
        logout = self.widgests.create_button(self.options_frame, text='LOG OUT', command=self.log_out, width=10, height=1)
        logout.pack(pady=5)
        
    def home(self):
        self.destroy()
        home = Options()
        home.display()

    def log_out(self):
        self.destroy()
        call = LoginWindow()
        call.display()

    def artist(self):
        self.destroy()
        call = Artist()
        call.display()

    def Search_and_list(self):
        self.search_list_frame = self.widgests.create_frame(self, bg='forestgreen')
        self.search_list_frame.pack(padx=5)

        self.search_bar = self.widgests.create_entry(self.search_list_frame, width=550)
        self.search_bar.pack(pady=5)
        self.search_bar.bind('<KeyRelease>', self.on_search)

        self.list_box = self.widgests.create_listbox(self.search_list_frame, width=550, height=33, selectmode=tk.SINGLE, bg='limegreen')
        self.list_box.pack()
        self.list_box.bind('<<ListboxSelect>>', self.play_selected_song)

        self.time_label = self.widgests.create_label(self.search_list_frame, text="00:00", font=("Helvetica", 12, "bold"), bg='forestgreen', fg='black')
        self.time_label.pack(side='left')

        self.progress_bar = self.widgests.create_progressbar(self.search_list_frame, orient='horizontal', length=550, mode='determinate')
        self.progress_bar.pack(side='left')

        self.items = [
            "KANABOON Silhoutte",
            "My little monkey",
            "Arthur Miguel ft. Trisha Macapagal - Ang Wakas (Official Lyric Video)",
            "AURORA Runaway Lyrics"
        ]
        self.items.sort()
        self.update_listbox(self.items)

    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[len(arr) // 2][0]
            left = [item for item in arr if item[0] < pivot]
            middle = [item for item in arr if item[0] == pivot]
            right = [item for item in arr if item[0] > pivot]
            return self.quick_sort(left) + middle + self.quick_sort(right)

    def levenshtein_distance(self, s1, s2):
        if len(s1) < len(s2):
            return self.levenshtein_distance(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]

    def update_listbox(self, data):
        self.list_box.delete(0, tk.END)
        for item in data:
            self.list_box.insert(tk.END, item)

    def on_search(self, event):
        typed = self.search_bar.get().lower()
        if typed == '':
            data = self.items
            self.list_box.configure(fg="black")
        else:
            distances = [(self.levenshtein_distance(typed, item.lower()), item) for item in self.items]
            data = self.quick_sort(distances)
            closest_matches = [item for _, item in data[:]]
            data = closest_matches
            self.list_box.configure(fg="black")

        self.update_listbox(data)

    def Buttons(self):
        self.buttons_frame = self.widgests.create_frame(self, width=550, bg='chartreuse')
        self.buttons_frame.pack(side='left', padx=10)

        prev_button = self.widgests.create_button(self.buttons_frame, text='၊◀', command=self.prev_song, width=2, height=2)
        prev_button.pack(side='left', pady=5)

        self.play_button = self.widgests.create_button(self.buttons_frame, text="▶︎", command=self.toggle_play, width=2, height=2)
        self.play_button.pack(side='left', pady=5)

        next_button = self.widgests.create_button(self.buttons_frame, text="▶︎၊", command=self.next_song, width=2, height=2)
        next_button.pack(side='left', pady=5)

        self.current_song_label = self.widgests.create_label(self.buttons_frame, text="", font=("Helvetica", 8, "bold"), bg='chartreuse', fg='black')
        self.current_song_label.pack(side='left', padx=5, pady=5)

        quit_button = self.widgests.create_button(self, text='EXIT', command=self.quit, width=2, height=2)
        quit_button.pack(side='right', padx=10)

        self.remote = Remote(self.list_box, self.play_button, self.current_song_label, self.progress_bar, self.time_label) 

    def prev_song(self):
        self.remote.prev_song()

    def play_selected_song(self, event):
        self.remote.play_selected_song(event)

    def toggle_play(self):
        self.remote.toggle_play()

    def next_song(self):
        self.remote.next_song()

    def quit(self):
        self.destroy()

    def display(self):
        self.mainloop()

class Options(tk.Tk):#------------------------------------Opsions----------------------------------------
    def __init__(self):
        super().__init__()
        self.widgets = WidgetsFactory()
        self.window_config()
        self.option_frame()
        self.display()

    def window_config(self):
        self.title('Options')
        self.geometry('800x900')
        self.resizable(True, True)
        self.configure(bg='green')

    def option_frame(self):
        self.options_frame = self.widgets.create_frame(self,width=200)
        self.options_frame.pack(side='left', fill='y')

        home = self.widgets.create_button(self.options_frame, text='PLAYLIST', command=self.home, width=10, height=1)
        home.pack(pady=5)

        favorites = self.widgets.create_button(self.options_frame, text='FAVORITES', command=print, width=10, height=1)
        favorites.pack(pady=5)

        artist = self.widgets.create_button(self.options_frame, text='ARTISTS', command=print, width=10, height=1)
        artist.pack(pady=5)
        
        settings = self.widgets.create_button(self.options_frame, text='SETTINGS', command=print, width=10, height=1)
        settings.pack(pady=5)
        
        logout = self.widgets.create_button(self.options_frame, text='LOG OUT', command=self.log_out, width=10, height=1)
        logout.pack(pady=5)

    def home(self):
        self.withdraw()
        home = MusicList()
        home.display()

    def log_out(self):
        self.destroy()
        call = LoginWindow()
        call.display()

    def print(self):
        self.print('clicked')

    def display(self):
        self.mainloop()

class Artist(tk.Tk):
    def __init__(self):
        super().__init__()
        self.widgets = WidgetsFactory()
        self.window_config()
        self.optionss_frame()
        self.fr_fr()
        self.display()

    def window_config(self):
        self.title('Options')
        self.geometry('800x900')
        self.resizable(True, True)
        self.configure(bg='green')

    def optionss_frame(self):
        self.options_frame = self.widgets.create_frame(self, width=200)
        self.options_frame.pack(side='left', fill='y')

        home = self.widgets.create_button(self.options_frame, text='PLAYLIST', command=self.home, width=10, height=1)
        home.pack(pady=5)

        favorites = self.widgets.create_button(self.options_frame, text='FAVORITES', command=self.print, width=10, height=1)
        favorites.pack(pady=5)

        artist = self.widgets.create_button(self.options_frame, text='ARTISTS', command=self.print, width=10, height=1)
        artist.pack(pady=5)

        settings = self.widgets.create_button(self.options_frame, text='SETTINGS', command=self.print, width=10, height=1)
        settings.pack(pady=5)

        logout = self.widgets.create_button(self.options_frame, text='LOG OUT', command=self.log_out, width=10, height=1)
        logout.pack(pady=5)

    def display_artists(self):
        self.search_bar = self.widgets.create_entry(self, width=550)
        self.search_bar.pack(pady=5)
        self.search_bar.bind('<KeyRelease>', self.on_search)

        self.listbox = self.widgets.create_listbox(self, width=550, height=33, selectmode=tk.SINGLE, bg='limegreen')
        self.listbox.pack(pady=20)

        self.update_listbox(self.artists.keys())

    def fr_fr(self):
        self.artists = {
            "Justin Bieber": ["Baby", "Sorry", "Love Yourself", "What Do You Mean?", "Boyfriend", "Intentions", "Yummy", "Despacito (Remix) [with Luis Fonsi & Daddy Yankee]", "As Long As You Love Me", "Never Say Never [feat. Jaden Smith]"],
            "Adele": ["Hello", "Someone Like You", "Rolling in the Deep", "Set Fire to the Rain", "Skyfall", "When We Were Young", "Make You Feel My Love", "Chasing Pavements", "Water Under the Bridge", "Rumour Has It"],
            "Ed Sheeran": ["Shape of You", "Thinking Out Loud", "Perfect", "Castle on the Hill", "Photograph", "Galway Girl", "The A Team", "I Don't Care (with Justin Bieber)", "Sing", "Happier"],
            "Taylor Swift": ["Love Story", "Shake It Off", "Blank Space", "You Belong with Me", "Look What You Made Me Do", "I Knew You Were Trouble", "We Are Never Ever Getting Back Together", "ME! (feat. Brendon Urie)", "Style", "Delicate"],
            "Beyoncé": ["Single Ladies (Put a Ring on It)", "Halo", "Crazy in Love", "Irreplaceable", "Formation", "Drunk in Love (feat. Jay-Z)", "If I Were a Boy", "Run the World (Girls)", "Sorry", "Love on Top"],
            "Michael Jackson": ["Thriller", "Billie Jean", "Beat It", "Smooth Criminal", "Man in the Mirror"],
            "Queen": ["Bohemian Rhapsody", "We Will Rock You", "Another One Bites the Dust", "Somebody to Love", "Don't Stop Me Now"],
            "Elton John": ["Rocket Man", "Your Song", "Tiny Dancer", "Crocodile Rock", "Goodbye Yellow Brick Road"],
            "Madonna": ["Like a Prayer", "Vogue", "Material Girl", "Like a Virgin", "Hung Up"],
            "Bob Dylan": ["Like a Rolling Stone", "Blowin' in the Wind", "Knockin' on Heaven's Door", "The Times They Are a-Changin'", "Tangled Up in Blue"],
            "The Beatles": ["Hey Jude", "Let It Be", "Yesterday", "Come Together", "Here Comes the Sun"],
            "Elvis Presley": ["Jailhouse Rock", "Can't Help Falling in Love", "Suspicious Minds", "Love Me Tender", "Hound Dog"],
            "Celine Dion": ["My Heart Will Go On", "Because You Loved Me", "The Power of Love", "It's All Coming Back to Me Now", "A New Day Has Come"],
            "Frank Sinatra": ["My Way", "Fly Me to the Moon", "Strangers in the Night", "New York, New York", "Come Fly with Me"],
            "Whitney Houston": ["I Will Always Love You", "I Wanna Dance with Somebody", "Greatest Love of All", "How Will I Know", "Saving All My Love for You"]
        }
        self.display_artists()

    def update_listbox(self, data):
        self.listbox.delete(0, tk.END)
        for item in data:
            self.listbox.insert(tk.END, item)

    def on_search(self, event):
        typed = self.search_bar.get().lower()
        if typed == '':
            data = self.artists
            self.listbox.configure(fg="black")
        else:
            distances = [(self.levenshtein_distance(typed, item.lower()), item) for item in self.artists]
            data = self.quick_sort(distances)
            closest_matches = [item for _, item in data[:[]]]
            data = closest_matches
            self.listbox.configure(fg="black")

        self.update_listbox(data)

    def home(self):
        self.withdraw()
        home = MusicList()
        home.display()

    def log_out(self):
        self.destroy()
        call = LoginWindow()
        call.display()

    def print(self):
        print('clicked')

    def display(self):
        self.mainloop()
