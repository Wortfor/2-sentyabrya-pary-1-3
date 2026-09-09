class MediaPlayer:
    def open(self, file):
        self.filename = file
    
    def play(self):
        print(f"Воспроизведение {self.filename}")
media1 = MediaPlayer()
media2 = MediaPlayer()
media1.open("song.mp3")
media2.open("video.mp4")
media1.play()
media2.play()