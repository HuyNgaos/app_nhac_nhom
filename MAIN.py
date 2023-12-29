from tkinter import *
from tkinter import ttk
import pygame

chosen_song = ''
class window():
    def __init__(self, root):
        self.root = root

class SongSelection(window):
    def __init__(self, root):
        super().__init__(root)
        self.selection = ttk.LabelFrame(self.root, text="Song Selection")
        self.song = StringVar()
        self.songbut1 = ttk.Radiobutton(self.selection, text="Erika", variable=self.song, value="Erika.mp3", command=self.gotem)
        self.songbut2 = ttk.Radiobutton(self.selection, text="Test-Ehe", variable=self.song, value="ehe-te-nandayo-paimon.mp3", command=self.gotem)
        self.songbut3 = ttk.Radiobutton(self.selection, text="Astronomia", variable=self.song, value="Astronomia.mp3", command=self.gotem)
        self.songbut4 = ttk.Radiobutton(self.selection, text="US Anti-Communist", variable=self.song, value="Anti-Communist.mp3", command=self.gotem)
        self.songbut5 = ttk.Radiobutton(self.selection, text="Loli Requiem", variable=self.song, value="loli.mp3", command=self.gotem)
        self.songbut6 = ttk.Radiobutton(self.selection, text="Rasputin", variable=self.song, value="Rasputin.mp3", command=self.gotem)
        self.songbut7 = ttk.Radiobutton(self.selection, text="Baka Mitai", variable=self.song, value="Baka_Mitai.mp3", command=self.gotem)
        self.songbut8 = ttk.Radiobutton(self.selection, text="Cùng nhau bầu cho tổng\nthống Trump", variable=self.song, value="DTrump.mp3", command=self.gotem)
        self.songbut9 = ttk.Radiobutton(self.selection, text="Idol by Hitler", variable=self.song, value="Hitler_Idol.mp3", command=self.gotem)
        self.songbut10 = ttk.Radiobutton(self.selection, text="Hentaiz.net", variable=self.song, value="Circus.mp3", command=self.gotem)
        self.songbut11= ttk.Radiobutton(self.selection, text="Red Sun in the Sky", variable=self.song, value="RedSun.mp3", command=self.gotem)
        self.songbut12 = ttk.Radiobutton(self.selection, text="USSR Anthem", variable=self.song, value="USSR.mp3", command=self.gotem)
        self.songbut13 = ttk.Radiobutton(self.selection, text="Minh-chan", variable=self.song, value="RickRoll.mp3", command=self.gotem)
        self.print = ttk.Button(self.selection, text="Print (debug)", command=self.getprint)
    def show(self):
        self.selection.pack()
        self.songbut1.pack()
        self.songbut12.pack()
        self.songbut4.pack()
        self.songbut11.pack()
        self.songbut6.pack()
        self.songbut7.pack()
        self.songbut8.pack()
        self.songbut3.pack()
        self.songbut5.pack()
        self.songbut9.pack()
        self.songbut10.pack()
        self.songbut13.pack()
        self.songbut2.pack()
        self.print.pack()
    def gotem(self):
        global chosen_song
        chosen_song = self.song.get()
    def getprint(self):
        printvar = self.song.get()
        print(printvar)
class SongPlayer(SongSelection):
    pygame.init()
    pygame.mixer.init()
    def __init__(self, root):
        super().__init__(root)
        self.player = ttk.LabelFrame(self.root, text="Song Player")
        self.playbut = ttk.Button(self.player, text="Play", command=self.play)
        self.note = ttk.Label(self.player, text="Note: You can only play\none song at a time")
    def play(self):
        chosen_song_ = f'data/{chosen_song}'
        soundplay = pygame.mixer.Sound(chosen_song_)
        soundplay.play()
        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(45)
    def show(self):
        self.player.pack()
        self.playbut.pack()
        self.note.pack()


def main():
    root = Tk()
    root.title("Music Player")
    Label(root, text="Nhạc fản động v1.0.0").pack()
    root.geometry("236x413")
    song_selection = SongSelection(root)
    song_selection.show()
    song_player = SongPlayer(root)
    song_player.show()
    root.mainloop()

if __name__ == "__main__":
    main()