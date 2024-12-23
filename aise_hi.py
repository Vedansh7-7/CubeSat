import customtkinter as ctk
import pygame

class AudioApp:
    def __init__(self, frame):
        self.frame = frame
        self.audio_path = "E:/Musics/The Chainsmokers & Coldplay - Something Just Like This (cover by COLOR MUSIC Choir).mp3"  # Ensure correct path

        # Initialize pygame mixer for audio
        pygame.mixer.init()
        
        # Load and play the audio when the application starts
        pygame.mixer.music.load(self.audio_path)
        pygame.mixer.music.play()

        # Create a customtkinter button to stop the audio
        self.play_button = ctk.CTkButton(frame, text="Continue", command=self.stop_audio)
        self.play_button.pack(pady=20)

    def stop_audio(self):
        # Stop the audio playback
        pygame.mixer.music.stop()
        
        # Hide the frame
        self.frame.place_forget()
