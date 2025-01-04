import customtkinter as ctk
import pygame

class AudioApp:
    def __init__(self, frame):
        self.frame = frame
        self.audio_path = "september.mp3"  # Ensure correct path

        # Initialize pygame mixer for audio
        pygame.mixer.init()
        
        # Load and play the audio when the application starts
        pygame.mixer.music.load(self.audio_path)
        pygame.mixer.music.play()

        # Create a customtkinter button to stop the audio
        self.play_button = ctk.CTkButton(frame, text="Continue", command=self.stop_audio)
        self.play_button.pack(pady=20)

    def stop_audio(self):
        # Fade out the audio playback over 2000 milliseconds (2 seconds)
        self.frame.place_forget()
        
        pygame.mixer.music.fadeout(2000)
        
        # Hide the frame after the audio fades out
        # self.frame.after(2000, self.frame.place_forget)  # 2000 ms corresponds to the fadeout duration
        
