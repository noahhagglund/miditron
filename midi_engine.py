import json
import mido


class MidiEngine:
    def __init__(self, config_path="config.json"):
        with open(config_path, "r") as file:
            self.config = json.load(file)

        self.port = mido.open_output(
            self.config["midi"]["output"]
        )

    def note_on(self, channel, note, velocity=100):
        self.port.send(
            mido.Message(
                "note_on",
                channel=channel - 1,
                note=note,
                velocity=velocity
            )
        )

    def note_off(self, channel, note):
        self.port.send(
            mido.Message(
                "note_off",
                channel=channel - 1,
                note=note,
                velocity=0
            )
        )

    def control_change(self, channel, control, value):
        self.port.send(
            mido.Message(
                "control_change",
                channel=channel - 1,
                control=control,
                value=value
            )
        )

    def close(self):
        self.port.close()
