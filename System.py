import pygame
import json
import tkinter as tk

class controller():
    def has(self):
        pass

class MusicGUI:
    def __init__(self, controler=controller()):
        from MusicGUI import IntroWindow
        self.controler = controler
        self.Music_main = IntroWindow()

    def start(self):
        self.Music_main.mainloop()
        
#---------------------------------------Remote---------------------------------------------------
class Remote:
    def __init__(self, list_box, play_button, current_song_label, progress_bar, time_label):
        pygame.mixer.init()
        self.list_box = list_box
        self.play_button = play_button
        self.current_song_label = current_song_label
        self.progress_bar = progress_bar
        self.time_label = time_label
        self.playing = False
        self.paused = False
        self.selected_index = None

        self.play_button.config(command=self.toggle_play)
        self.list_box.bind("<Double-1>", self.play_selected_song)

    def update_play_button(self, playing):
        if playing:
            self.play_button.config(text="❚❚")
        else:
            self.play_button.config(text="▶")

    def play_selected_song(self, event=None):
        selection = self.list_box.curselection()
        if selection:
            index = selection[0]
            self.selected_index = index
            self.play_song()

    def prev_song(self):
        if self.selected_index is not None:
            self.selected_index -= 1
            if self.selected_index < 0:
                self.selected_index = self.list_box.size() - 1
            self.play_song_by_index(self.selected_index)

    def next_song(self):
        if self.selected_index is not None:
            self.selected_index += 1
            if self.selected_index >= self.list_box.size():
                self.selected_index = 0
            self.play_song_by_index(self.selected_index)

    def play_song_by_index(self, index):
        self.list_box.selection_clear(0, tk.END)
        self.list_box.selection_set(index)
        self.list_box.activate(index)
        self.selected_index = index
        self.play_song()

    def play_song(self):
        if self.selected_index is not None:
            selected_song = self.list_box.get(self.selected_index)
            pygame.mixer.music.load(f"{selected_song}.mp3")
            pygame.mixer.music.play()
            self.playing = True
            self.paused = False
            self.update_play_button(self.playing)
            self.current_song_label.config(text=f"{selected_song}")
            self.record_song(selected_song)
            self.update_progress_bar()
            self.update_time_label()

    def toggle_play(self):
        if self.playing:
            pygame.mixer.music.pause()
            self.playing = False
            self.paused = True
        else:
            if self.paused:
                pygame.mixer.music.unpause()
                self.playing = True
            else:
                if self.selected_index is not None:
                    self.play_song()
                else:
                    self.play_selected_song()
        self.update_play_button(self.playing)

    def record_song(self, song):
        try:
            with open("songs_played.json", "r") as file:
                songs_played = json.load(file)
        except FileNotFoundError:
            songs_played = []

        songs_played.append(song)
        with open("songs_played.json", "w") as file:
            json.dump(songs_played, file)

    def update_progress_bar(self):
        song_length = pygame.mixer.Sound(f"{self.list_box.get(self.selected_index)}.mp3").get_length()
        self.progress_bar['maximum'] = song_length
        self.update_progress()

    def update_progress(self):
        if self.playing or self.paused:
            position = pygame.mixer.music.get_pos() / 1000
            self.progress_bar['value'] = position
        self.list_box.after(1000, self.update_progress)

    def update_time_label(self):
        if self.playing or self.paused:
            position = pygame.mixer.music.get_pos() / 1000
            minutes = int(position // 60)
            seconds = int(position % 60)
            self.time_label.config(text=f"{minutes:02}:{seconds:02}")
        self.list_box.after(1000, self.update_time_label)
