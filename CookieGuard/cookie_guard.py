import WalabotAPI
import time
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from hand_state_machine import HandStateMachine, Sound

energy_threshold = 0.8
delay_frames = 30
buzzer_wav = r'buzzer.wav'
sound_quality = 'low'
debug = True

Sound.init(sound_quality)


def run():
    print("Connected to Walabot")
    WalabotAPI.SetProfile(WalabotAPI.PROF_TRACKER)

    # Set scan arena
    WalabotAPI.SetArenaR(15, 40, 10)
    WalabotAPI.SetArenaPhi(-60, 60, 10)
    WalabotAPI.SetArenaTheta(-30, 30, 10)
    print("Arena set")

    # Set image filter
    WalabotAPI.SetDynamicImageFilter(WalabotAPI.FILTER_TYPE_MTI)
    WalabotAPI.SetThreshold(35)

    # Start scan
    WalabotAPI.Start()

    with HandStateMachine(buzzer_wav, delay_frames) as hand_sm:
        t = time.time()
        while True:
            WalabotAPI.Trigger()
            energy = WalabotAPI.GetImageEnergy() * 1000

            hand_sm.state_in() if energy > energy_threshold else hand_sm.state_out()

            if debug:
                print('Energy: {:<10}Frame Rate: {}'.format(energy, 1/(time.time()-t)))
                t = time.time()


if __name__ == '__main__':
    print("Initialize API")
    WalabotAPI.Init()

    while True:
        WalabotAPI.Initialize()
        # Check if a Walabot is connected
        try:
            WalabotAPI.ConnectAny()
            run()
        except WalabotAPI.WalabotError as err:
            print('Failed to connect to Walabot. error code: {}'.format(str(err.code)))
        except Exception as err:
            print(err)
        finally:
            print("Cleaning API")
            WalabotAPI.Clean()
            time.sleep(2)
