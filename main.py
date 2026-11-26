
import json
from midi_engine import MidiEngine
from game_events import GameEvents


def main():
    print("========================")
    print("       MIDITRON")
    print("========================")
    print("Starting MIDI engine...")

    with open("config.json", "r") as file:
        config = json.load(file)

    midi = MidiEngine()
    events = GameEvents(midi, config)

    print("MIDI connected!")
    print("Miditron is ready.")
    print("Press Ctrl+C to stop.")

    try:
        while True:
            command = input("Enter L (left), R (right), or Q (quit): ").lower()

            if command == "l":
                events.accepted_turn("left")
                print("LEFT TURN")

            elif command == "r":
                events.accepted_turn("right")
                print("RIGHT TURN")

            elif command == "q":
                break

    except KeyboardInterrupt:
        print("\nStopping Miditron...")

    finally:
        midi.close()
        print("Miditron stopped.")


if __name__ == "__main__":
    main()
