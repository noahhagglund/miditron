class GameEvents:
    def __init__(self, midi, config):
        self.midi = midi
        self.config = config

        self.turn_count = 0
        self.note_index = 0

        self.scale = [
            57, 59, 60, 62, 64, 65, 67,
            69, 71, 72, 74, 76, 77, 79
        ]

    def accepted_turn(self, direction):
        if direction not in ("left", "right"):
            return

        self.turn_count += 1

        if direction == "right":
            self.note_index += 1
        else:
            self.note_index -= 1

        self.note_index %= len(self.scale)

        melody_channel = self.config["midi"]["channels"]["melody"]
        note = self.scale[self.note_index]

        self.midi.note_on(melody_channel, note, 100)
        self.midi.note_off(melody_channel, note)

        drums = self.config["drums"]
        channels = self.config["midi"]["channels"]

        if self.turn_count % drums["kick_every_turns"] == 0:
            self.midi.note_on(channels["kick"], 36, 110)
            self.midi.note_off(channels["kick"], 36)

        if self.turn_count % drums["snare_every_turns"] == 0:
            self.midi.note_on(channels["snare"], 38, 110)
            self.midi.note_off(channels["snare"], 38)
