import curses
from curses import wrapper
from __get_index__ import get_index

speech_to_waifu = [
    "   SSSSSSSSSSSSSSS                                                                               hhhhhhh                ",
    " SS:::::::::::::::S                                                                              h:::::h                ",
    "S:::::SSSSSS::::::S                                                                              h:::::h                ",
    "S:::::S     SSSSSSS                                                                              h:::::h                ",
    "S:::::S           ppppp   ppppppppp       eeeeeeeeeeee        eeeeeeeeeeee        cccccccccccccccch::::h hhhhh          ",
    "S:::::S           p::::ppp:::::::::p    ee::::::::::::ee    ee::::::::::::ee    cc:::::::::::::::ch::::hh:::::hhh       ",
    " S::::SSSS        p:::::::::::::::::p  e::::::eeeee:::::ee e::::::eeeee:::::ee c:::::::::::::::::ch::::::::::::::hh     ",
    "  SS::::::SSSSS   pp::::::ppppp::::::pe::::::e     e:::::ee::::::e     e:::::ec:::::::cccccc:::::ch:::::::hhh::::::h    ",
    "    SSS::::::::SS  p:::::p     p:::::pe:::::::eeeee::::::ee:::::::eeeee::::::ec::::::c     ccccccch::::::h   h::::::h   ",
    "       SSSSSS::::S p:::::p     p:::::pe:::::::::::::::::e e:::::::::::::::::e c:::::c             h:::::h     h:::::h   ",
    "            S:::::Sp:::::p     p:::::pe::::::eeeeeeeeeee  e::::::eeeeeeeeeee  c:::::c             h:::::h     h:::::h   ",
    "            S:::::Sp:::::p    p::::::pe:::::::e           e:::::::e           c::::::c     ccccccch:::::h     h:::::h   ",
    "SSSSSSS     S:::::Sp:::::ppppp:::::::pe::::::::e          e::::::::e          c:::::::cccccc:::::ch:::::h     h:::::h   ",
    "S::::::SSSSSS:::::Sp::::::::::::::::p  e::::::::eeeeeeee   e::::::::eeeeeeee   c:::::::::::::::::ch:::::h     h:::::h   ",
    "S:::::::::::::::SS p::::::::::::::pp    ee:::::::::::::e    ee:::::::::::::e    cc:::::::::::::::ch:::::h     h:::::h   ",
    " SSSSSSSSSSSSSSS   p::::::pppppppp        eeeeeeeeeeeeee      eeeeeeeeeeeeee      cccccccccccccccchhhhhhh     hhhhhhh   ",
    "                   p:::::p                                                                                              ",
    "                   p:::::p                                                                                              ",
    "                  p:::::::p                                                                                             ",
    "                  p:::::::p                                                                                             ",
    "                  p:::::::p                                                                                             ",
    "                  ppppppppp                                                                                             ",
    "                                                                                                                        ",
    "                                              tttt                                                                      ",
    "                                           ttt:::t                                                                      ",
    "                                           t:::::t                                                                      ",
    "                                           t:::::t                                                                      ",
    "                                     ttttttt:::::ttttttt       ooooooooooo                                              ",
    "                                     t:::::::::::::::::t     oo:::::::::::oo                                            ",
    "                                     t:::::::::::::::::t    o:::::::::::::::o                                           ",
    "                                     tttttt:::::::tttttt    o:::::ooooo:::::o                                           ",
    "                                           t:::::t          o::::o     o::::o                                           ",
    "                                           t:::::t          o::::o     o::::o                                           ",
    "                                           t:::::t          o::::o     o::::o                                           ",
    "                                           t:::::t    tttttto::::o     o::::o                                           ",
    "                                           t::::::tttt:::::to:::::ooooo:::::o                                           ",
    "                                           tt::::::::::::::to:::::::::::::::o                                           ",
    "                                             tt:::::::::::tt oo:::::::::::oo                                            ",
    "                                               ttttttttttt     ooooooooooo                                              ",
    "         WWWWWWWW                           WWWWWWWW                 iiii     ffffffffffffffff                          ",
    "         W::::::W                           W::::::W                i::::i   f::::::::::::::::f                         ",
    "         W::::::W                           W::::::W                 iiii   f::::::::::::::::::f                        ",
    "         W::::::W                           W::::::W                        f::::::fffffff:::::f                        ",
    "          W:::::W           WWWWW           W:::::Waaaaaaaaaaaaa   iiiiiii  f:::::f       ffffffuuuuuu    uuuuuu        ",
    "           W:::::W         W:::::W         W:::::W a::::::::::::a  i:::::i  f:::::f             u::::u    u::::u        ",
    "            W:::::W       W:::::::W       W:::::W  aaaaaaaaa:::::a  i::::i f:::::::ffffff       u::::u    u::::u        ",
    "             W:::::W     W:::::::::W     W:::::W            a::::a  i::::i f::::::::::::f       u::::u    u::::u        ",
    "              W:::::W   W:::::W:::::W   W:::::W      aaaaaaa:::::a  i::::i f::::::::::::f       u::::u    u::::u        ",
    "               W:::::W W:::::W W:::::W W:::::W     aa::::::::::::a  i::::i f:::::::ffffff       u::::u    u::::u        ",
    "                W:::::W:::::W   W:::::W:::::W     a::::aaaa::::::a  i::::i  f:::::f             u::::u    u::::u        ",
    "                 W:::::::::W     W:::::::::W     a::::a    a:::::a  i::::i  f:::::f             u:::::uuuu:::::u        ",
    "                  W:::::::W       W:::::::W      a::::a    a:::::a i::::::if:::::::f            u:::::::::::::::uu      ",
    "                   W:::::W         W:::::W       a:::::aaaa::::::a i::::::if:::::::f             u:::::::::::::::u      ",
    "                    W:::W           W:::W         a::::::::::aa:::ai::::::if:::::::f              uu::::::::uu:::u      ",
    "                     WWW             WWW           aaaaaaaaaa  aaaaiiiiiiiifffffffff                uuuuuuuu  uuuu      ",
]


push_to_talk_key = "t"

current_row = 0
model_name = "medium.en"

characters = {
    "normal": "10",
    "normal2": "24",
    "whisper": "19",
    "whisper2": "22",
    "whisper3": "37",
    "loli": "43",
    "mommy": "30",
    "male_funny": "42",
    "male_announcement": "51",
}


current = characters["normal"]
name = "normal"

window = {}
history = []
history_jap = []
error = []


def main(stdscr, input_index):
    global current_row
    global window
    global current
    global name
    global history
    global history_jap

    def string(x, y, content, move=0, refresh=True):
        global window
        global history
        global history_jap
        global current_row
        try:
            stdscr.addstr(x, y, content)
        except curses.error:
            error.append([x, y, content, "Please resize the window, and try again"])
        window[x] = content
        current_row += move
        if refresh:
            stdscr.refresh()

    def clear():
        global window
        global current_row
        global current
        global name
        global history
        global history_jap
        global error
        error = []
        stdscr.clear()
        window = {}
        string(
            curses.LINES - 3,
            int(curses.COLS / 3),
            f"Using character: {name} with code: {current}    ",
        )
        string(curses.LINES - 2, int(curses.COLS / 3), "Using VOICEVOX")
        string(
            curses.LINES - 1,
            int(curses.COLS / 3),
            "Check for additional information at https://github.com/VOICEVOX/voicevox_engine",
        )

        # Removes first item from history if history is over 5
        if not error:
            if len(history) > (curses.LINES - 5) / 2 - 1:
                history.pop(0)
            if len(history_jap) > (curses.LINES - 5) / 2 - 1:
                history_jap.pop(0)
            string(0, int(curses.COLS / 3), "English history:")
            string(
                int((curses.LINES - 5) / 2 + 1),
                int(curses.COLS / 3),
                "Japanese translation history:",
            )
            for i in range(curses.LINES - 3):
                string(i, int(curses.COLS / 3) - 1, "|")
            string(
                (curses.LINES - 5) + 1,
                int(curses.COLS / 3) - 1,
                "-" * (int(curses.COLS / 3) * 2 + 1),
            )
            string(
                int((curses.LINES - 5) / 2),
                int(curses.COLS / 3),
                "-" * (int(curses.COLS / 3) * 2),
            )
            for times, text in enumerate(history):
                string(times + 1, int(curses.COLS / 3), text)
            for times, text in enumerate(history_jap):
                string(
                    times + int((curses.LINES - 5) / 2 + 3), int(curses.COLS / 3), text
                )
        else:
            if len(history) > (curses.LINES - 5) / 3:
                history.pop(0)
            if len(history_jap) > (curses.LINES - 5) / 3:
                history_jap.pop(0)
            string(0, int(curses.COLS / 3), "English history:")
            string(
                int((curses.LINES - 5) / 3 + 1),
                int(curses.COLS / 3),
                "Japanese translation history:",
            )
            string(
                int(((curses.LINES - 5) / 3) * 2 + 3),
                int(curses.COLS / 3),
                "Error log:",
            )
            for times, i in enumerate(error):
                string(
                    int(((curses.LINES - 5) / 3) * 2 + 4) + times,
                    int(curses.COLS / 3),
                    f"Error occurred at line {i[0]} column {i[1]}: {i[3]}",
                )
            for i in range(curses.LINES - 3):
                string(i, int(curses.COLS / 3) - 1, "|")
            string(
                (curses.LINES - 5) + 1,
                int(curses.COLS / 3) - 1,
                "-" * (int(curses.COLS / 3) * 2 + 1),
            )
            string(
                int((curses.LINES - 5) / 3 + 1),
                int(curses.COLS / 3),
                "-" * (int(curses.COLS / 3) * 2),
            )
            string(
                int((curses.LINES - 5) / 3 + 1),
                int(curses.COLS / 3),
                "-" * (int(curses.COLS / 3) * 2),
            )
            string(
                int(((curses.LINES - 5) / 3) * 2 + 2),
                int(curses.COLS / 3),
                "-" * (int(curses.COLS / 3) * 2),
            )
            for times, text in enumerate(history):
                string(times + 1, int(curses.COLS / 3), text)
            for times, text in enumerate(history_jap):
                string(
                    times + int((curses.LINES - 5) / 3 + 3), int(curses.COLS / 3), text
                )

    string(current_row, 0, "Importing voicevox...")
    import voicevox

    string(current_row, 0, "Importing voicevox DONE", 1)
    string(current_row, 0, "Importing vboxclient...")
    from voicevox import vboxclient

    string(current_row, 0, "Importing vboxclient DONE", 1)
    string(current_row, 0, "Importing webapi...")
    from voicevox import webapi

    string(current_row, 0, "Importing webapi DONE", 1)
    string(current_row, 0, "Importing pygetwindow...")
    import pygetwindow

    string(current_row, 0, "Importing pygetwindow DONE", 1)
    string(current_row, 0, "Importing pyautogui...")
    import pyautogui as pg

    string(current_row, 0, "Importing pyautogui DONE", 1)
    string(current_row, 0, "Importing mtranslate...")
    from mtranslate import translate

    string(current_row, 0, "Importing mtranslate DONE", 1)
    string(current_row, 0, "Importing os...")
    import os

    string(current_row, 0, "Importing os DONE", 1)
    string(current_row, 0, "Importing subprocess...")
    import subprocess

    string(current_row, 0, "Importing subprocess DONE", 1)
    string(current_row, 0, "Importing signal...")
    import signal

    string(current_row, 0, "Importing signal DONE", 1)
    string(current_row, 0, "Importing whisper...")
    import whisper as wh

    string(current_row, 0, "Importing whisper DONE", 1)
    string(current_row, 0, "Importing threading...")
    from threading import Thread

    string(current_row, 0, "Importing threading DONE", 1)
    string(current_row, 0, "Importing sleep...")
    from time import sleep

    string(current_row, 0, "Importing sleep DONE", 1)
    string(current_row, 0, "Importing keyboard...")
    import keyboard

    string(current_row, 0, "Importing keyboard DONE", 1)
    string(current_row, 0, "Importing pyaudio...")
    import pyaudio

    string(current_row, 0, "Importing pyaudio DONE", 1)
    string(current_row, 0, "Importing wave...")
    import wave

    string(current_row, 0, "Importing wave DONE", 1)
    string(current_row, 0, "Importing pydub...")
    import pydub

    string(current_row, 0, "Importing pydub DONE", 1)
    string(current_row, 0, "Importing sounddevice...")
    import sounddevice as sd

    string(current_row, 0, "Importing sounddevice DONE", 1)
    string(current_row, 0, "Importing soundfile...")
    import soundfile as sf

    string(current_row, 0, "Importing soundfile DONE", 1)
    string(current_row, 0, "Importing mixer...")
    from pygame import mixer

    string(current_row, 0, "Importing mixer DONE", 1)

    string(current_row, 0, f"Loading {model_name}...")
    curses.endwin()
    model = wh.load_model(model_name)
    string(current_row, 0, f"Loading {model_name} DONE", 1)
    string(current_row, 0, "Loading base.en...")
    curses.endwin()
    model_low = wh.load_model("base.en")
    string(current_row, 0, "Loading base.en DONE", 1)

    to_use = model

    string(current_row, 0, "Getting input device index...")
    audio = pyaudio.PyAudio()

    string(current_row + 1, 0, "Searching for VB-Audio Virtual Cable...")

    input_device_index = None
    for i in range(audio.get_device_count()):
        info = audio.get_device_info_by_index(i)
        string(
            current_row + 2, 0, f"Current: {info['name']} at index {info['index']}     "
        )
        sleep(0.1)
        if "VB-Audio Virtual Cable" in info["name"]:
            input_device_index = info["index"]
            string(current_row + 1, 0, "Searching for VB-Audio Virtual Cable DONE")
            break
    else:
        string(current_row + 1, 0, "Searching for VB-Audio Virtual Cable ERROR")

    string(current_row, 0, "Getting input device index DONE", 5)

    string(current_row, 0, "Starting VOICEVOX...")
    name = os.path.abspath("VOICEVOX/run.exe")
    VOICEVOX_instance = subprocess.Popen(name)
    string(current_row, 0, "Starting VOICEVOX DONE", 1)

    for times, line in enumerate(speech_to_waifu):
        sleep(0.01)
        string(times, 0, line + " " * (curses.COLS - len(line)))

    sleep(1)
    clear()
    current_row = 0

    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024

    def speak():
        global window
        global current
        global name
        global current_row
        string(current_row, 0, "Getting text...", 1)

        audio_file = pydub.AudioSegment.from_file("output.wav")
        duration_seconds = len(audio_file) / 1000

        if duration_seconds < 1.75:
            to_use = model_low
            string(current_row, 0, "Using base.en model", -1)
            model_used = "base.en"
        else:
            to_use = model
            string(current_row, 0, f"Using {model_name} model", -1)
            model_used = model_name

        result = to_use.transcribe("output.wav")
        string(current_row, 0, "Getting text DONE", 2)

        string(current_row, 0, result["text"], 1)

        os.remove("output.wav")

        string(current_row, 0, "Translating text...")
        text = result["text"]

        history.append(f"{current}: {model_used}: {text}")

        translation = translate(text, "ja", "en")

        history_jap.append(f"{current}: {model_used}: {translation}")
        string(current_row, 0, "Translating text DONE", 1)
        string(current_row, 0, translation, 1)

        string(current_row, 0, "Generating waifu...")
        vboxapp = vboxclient.voiceclient()

        vboxapp.run(text=translation, speaker=current, filename="translation.wav")
        string(current_row, 0, "Generating waifu DONE", 1)
        # os.remove('translation.txt')
        # os.remove('translation.json')

    def play_audio():
        global window
        global current
        global name
        global current_row
        sleep(0.5)
        row = current_row + 1
        string(
            row,
            0,
            "Playing audio through in device CABLE Input (VB-Audio Virtual Cable)...",
        )
        mixer.init(devicename="CABLE Input (VB-Audio Virtual Cable)")
        mixer.music.load("translation.wav")  # Load the mp3
        channel = mixer.music.play()  # Play it
        while channel.get_busy():
            sleep(0.1)
        string(
            row,
            0,
            "Playing audio through in device CABLE Input (VB-Audio Virtual Cable) DONE",
            2,
        )

    def record_audio():
        global current_row
        global current
        global window

        string(current_row, 0, "Opening stream...")

        p = pyaudio.PyAudio()
        stream = p.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK,
            input_device_index=input_index,
        )

        string(current_row, 0, "Opening stream DONE", 1)

        string(current_row, 0, "Recording audio...")
        frames = []
        while True:
            if check_key(push_to_talk_key):
                data = stream.read(CHUNK)
                frames.append(data)
            else:
                break
        string(current_row, 0, "Recording audio DONE", 1)

        stream.stop_stream()
        stream.close()
        p.terminate()

        string(current_row, 0, "Closing stream...")

        wf = wave.open("output.wav", "wb")
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b"".join(frames))
        wf.close()

        string(current_row, 0, "Closing stream DONE", 1)

        speak()

        Thread(target=play_audio).start()

        string(current_row, 0, "Opening stream in output device...")

        wf = wave.open("translation.wav", "rb")

        p = pyaudio.PyAudio()

        stream = p.open(
            format=p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True,
            input_device_index=input_device_index,
        )
        string(current_row, 0, "Opening stream in output device DONE", 1)

        string(current_row, 0, "Playing sound in output device...")
        chunk_size = 1024
        data = wf.readframes(chunk_size)
        while data:
            stream.write(data)
            data = wf.readframes(chunk_size)

        string(current_row, 0, "Playing sound in output device DONE", 2)

        string(current_row, 0, "Closing stream in output device...")

        stream.stop_stream()
        stream.close()
        p.terminate()
        wf.close()

        string(current_row, 0, "Closing stream in output device DONE", 1)

        sleep(1.25)
        mixer.stop()
        mixer.quit()
        os.remove("translation.wav")

        clear()
        current_row = 0
        window = {}
        string(current_row, 0, "Ready to speak again")

    string(current_row, 0, "Ready to speak")
    stdscr.refresh()

    def check_key(key):
        if isinstance(key, str):
            return bool(keyboard.is_pressed(key))
        if isinstance(key, list):
            approve = True
            for i in key:
                if not keyboard.is_pressed(i):
                    approve = False
            return approve

    def change_char(key, to: str):
        global current
        global name
        if key:
            current = characters[to]
            name = to
            string(
                curses.LINES - 3,
                int(curses.COLS / 3),
                "Using character: "
                + name
                + " with code: "
                + current
                + " " * (curses.COLS - len(current) - len(name) - 29),
            )

    while True:
        try:
            if check_key(push_to_talk_key):
                clear()
                record_audio()
            change_char(check_key([".", "1"]), "normal")
            change_char(check_key([".", "2"]), "normal2")
            change_char(check_key([".", "3"]), "mommy")
            change_char(check_key([".", "4"]), "loli")
            change_char(check_key(["/", "1"]), "male_funny")
            change_char(check_key(["/", "2"]), "male_announcement")
            change_char(check_key([",", "1"]), "whisper")
            change_char(check_key([",", "2"]), "whisper2")
            change_char(check_key([",", "3"]), "whisper3")
        except KeyboardInterrupt:
            quit()


wrapper(main, get_index())
