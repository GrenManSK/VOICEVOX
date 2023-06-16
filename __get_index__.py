import pyaudio


def get_index():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get("deviceCount")

    pocet = 0
    for i in range(0, numdevices):
        if (
            p.get_device_info_by_host_api_device_index(0, i).get("maxInputChannels")
        ) > 0:
            pocet += 1
            print(
                "Input Device id ",
                i,
                " - ",
                p.get_device_info_by_host_api_device_index(0, i).get("name"),
            )

    while True:
        try:
            vstup = int(input("Select your default input device > "))
            if vstup >= pocet:
                print("Out of range")
                continue
            break
        except ValueError:
            continue
