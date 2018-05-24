from sound import Sound


class HandStateMachine:
    IN = 0
    OUT = 1

    def __init__(self, wav_file, delay_frames):
        self.state = self.OUT
        self.wav_file = wav_file
        self.sound = Sound(wav_file)
        self.delay_frames = delay_frames
        self.frame_cnt = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.sound.shutdown()

    def state_in(self):
        if self.state == self.OUT and self.frame_cnt is 0:
            self.sound.play()
            self.frame_cnt = self.delay_frames
            pass

        self.state = self.IN
        self.frame_cnt = max(self.frame_cnt - 1, 0)

    def state_out(self):
        self.state = self.OUT
        self.frame_cnt = max(self.frame_cnt - 1, 0)