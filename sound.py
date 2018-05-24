import pygame


class Sound:
    
    @staticmethod
    def init(quality='low'):
        # Initialise pygame  and the mixer
        if quality == 'low':
            pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=512)
        elif quality == 'mid':
            pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=1024)
        else:
            pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=2048)
        pygame.mixer.init()
    
    
    def __init__(self, wav_file):
        # load the sound file
        self.wav_file = wav_file
        self.sound = pygame.mixer.Sound(self.wav_file)
        self.sound.set_volume(1)

    def play(self):
        # play the sound file for 10 seconds and then stop it
        self.sound.play()
        print(self.wav_file)

    def shutdown(self):
        self.sound.stop()
        pygame.mixer.quit()
        print('Sound Shutdown')