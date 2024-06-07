import tkinter as tk
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password):
    hashed_password = hash_password(password)
    with open("user_info.txt", "r") as file:
        for line in file:
            if f"Email: {email}, Password: {hashed_password}" in line:
                return True
    return False

def log_in():
    email = username_entry.get()
    password = password_entry.get()

    if not email or not password:
        login_success_label.config(text="Please enter email and password.")
    elif login(email, password):
        login_success_label.config(text="Login successful!")
        
        playlist_window()
    else:
        login_success_label.config(text="Invalid email or password.")

def sign_in():
    email = username_entry.get()
    password = password_entry.get()

    if not email or not password:
        sign_in_success_label.config(text="Please enter email and password.")
    else:
        hashed_password = hash_password(password)
        with open("user_info.txt", "a") as file:
            file.write(f"Email: {email}, Password: {hashed_password}\n")
        sign_in_success_label.config(text="User information saved.")

        playlist_window()



def toggle_sidebar():
    if sidebar.winfo_viewable():
        sidebar.pack_forget()
    else:
        sidebar.pack(side="left", fill="y")

def on_hover(event):
    event.widget.config(bg="lightgray")

def on_leave(event):
    event.widget.config(bg="gray")

def on_click(event):
    option = event.widget['text']
    print(f"{option} clicked")
    if option == "Artist":
        show_artists_window()
    elif option == "Log Out":
        log_out()
    elif option == "Sign In":
        sign_in()
    elif option == "Settings":
        show_settings_window()

def show_artists_window():
    artists_window = tk.Toplevel(root)
    artists_window.title("Artists")
    artists_window.geometry("300x400")

    specific_artists = {
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

    listbox = tk.Listbox(artists_window, width=40, height=15)
    scrollbar = tk.Scrollbar(artists_window, orient="vertical", command=listbox.yview)
    scrollbar.pack(side="right", fill="y")
    listbox.config(yscrollcommand=scrollbar.set)
    for artist, songs in specific_artists.items():
        listbox.insert("end", artist)
        for song in songs:
            listbox.insert("end", f"   - {song}")

    listbox.pack(fill="both", expand=True)



    def display_artists(artists_to_display=None):
        for widget in artists_frame.winfo_children():
            widget.destroy()
        if artists_to_display:
            for artist, songs in artists_to_display.items():
                tk.Button(artists_frame, text=artist, font=("Helvetica", 10), command=lambda a=artist: display_artist_songs(a, songs)).pack(pady=5)
        else:
            for artist in specific_artists:
                tk.Button(artists_frame, text=artist, font=("Helvetica", 10), command=lambda a=artist: display_artist_songs(a)).pack(pady=5)

    def display_artist_songs(artist_name, songs=None):
        if not songs:
            songs = specific_artists.get(artist_name, [])
        songs_window = tk.Toplevel(root)
        songs_window.title(f"Songs by {artist_name}")
        songs_window.geometry("300x200")
        for song in songs:
            tk.Label(songs_window, text=song, font=("Helvetica", 10)).pack()

    def search_artists():
        query = search_entry.get().strip().lower()
        if query:
            matching_artists = {artist: songs for artist, songs in specific_artists.items() if query in artist.lower()}
            display_artists(matching_artists)
        else:
            display_artists()

    search_frame = tk.Frame(artists_window)
    search_frame.pack(pady=10)
    search_label = tk.Label(search_frame, text="Search Artist:")
    search_label.pack(side="left")
    search_entry = tk.Entry(search_frame)
    search_entry.pack(side="left", padx=5)
    search_button = tk.Button(search_frame, text="Search", command=search_artists)
    search_button.pack(side="left")

    artists_frame = tk.Frame(artists_window)
    artists_frame.pack(pady=10)

    display_artists()

def artist_clicked(artist_name):
    pass


def show_settings_window():
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")
    settings_window.geometry("300x200")

    user_settings = {
        "Account Type": "Premium",
        "Email": "user@example.com",
        "Audio Quality": "High",
        "Download Audio": "Enabled",
        "Privacy Policy": "Agreed"
    }

   
    buttons_frame = tk.Frame(settings_window)
    buttons_frame.pack(pady=10)

    for key in user_settings:
        button = tk.Button(buttons_frame, text=key, width=20,
                           command=lambda setting=key: show_setting_details(settings_window, setting, user_settings[setting]))
        button.pack(side="top", padx=10, pady=5)

def show_setting_details(parent, setting_name, setting_value):
    
    for widget in parent.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()

    tk.Label(parent, text=f"{setting_name}: {setting_value}", font=("Helvetica", 10)).pack(pady=5)


def create_sidebar(root, options):
    sidebar = tk.Frame(root, width=150, bg="gray")

    button_height = 40
    button_padding = 10

    for option in options:
        button = tk.Button(sidebar, text=option, width=15, anchor="w")
        button.pack(fill="x", pady=(button_padding, 0))

        button.bind("<Enter>", on_hover)
        button.bind("<Leave>", on_leave)
        button.bind("<Button-1>", on_click)

    return sidebar

def log_out():
    root.deiconify()
    

def playlist_window():
    playlist_root = tk.Toplevel(root)
    playlist_root.title("Playlist")
    playlist_root.geometry("400x300")
    
    playlist_label = tk.Label(playlist_root, text="Playlist", font=("Helvetica", 16, "bold"))
    playlist_label.pack(pady=25)

   
    options = ["Home", "Favorite Songs", "Artist", "Settings", "Log Out"]


    global sidebar
    sidebar = create_sidebar(playlist_root, options)

    
    toggle_button = tk.Button(playlist_root, text=">>>", command=toggle_sidebar)
    toggle_button.place(x=0, y=0)


root = tk.Tk()
root.title("Music Library App")
root.geometry("800x600")


username_label = tk.Label(root, text="Email:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()


password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()


log_in_button = tk.Button(root, text="Log In", command=log_in)
log_in_button.pack()

or_label = tk.Label(root, text="or", font=("Helvetica", 12))
or_label.pack()

sign_in_button = tk.Button(root, text="Sign In", command=sign_in)
sign_in_button.pack()

login_success_label = tk.Label(root, text="")
login_success_label.pack()


sign_in_success_label = tk.Label(root, text="")
sign_in_success_label.pack()

root.mainloop()
