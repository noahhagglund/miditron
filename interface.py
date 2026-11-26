
import tkinter as tk
from tkinter import ttk


class MiditronInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("MIDITRON")
        self.root.geometry("650x650")
        self.root.configure(bg="#17191f")

        self.setup_style()
        self.build_interface()

    def setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "TLabel",
            background="#17191f",
            foreground="#ffffff",
            font=("Arial", 11)
        )

        style.configure(
            "TButton",
            font=("Arial", 11),
            padding=8
        )

        style.configure(
            "TCombobox",
            padding=5
        )

    def build_interface(self):
        title = tk.Label(
            self.root,
            text="MIDITRON",
            bg="#17191f",
            fg="#65e6ad",
            font=("Arial", 30, "bold")
        )
        title.pack(pady=20)

        subtitle = tk.Label(
            self.root,
            text="RETROCYCLES MIDI CONTROLLER",
            bg="#17191f",
            fg="#888888",
            font=("Arial", 10)
        )
        subtitle.pack(pady=5)

        self.create_section("MELODY")

        melody_frame = tk.Frame(self.root, bg="#252832", padx=20, pady=15)
        melody_frame.pack(fill="x", padx=25, pady=5)

        tk.Label(
            melody_frame,
            text="Scale",
            bg="#252832",
            fg="white"
        ).grid(row=0, column=0, sticky="w")

        self.scale = ttk.Combobox(
            melody_frame,
            values=["A minor", "C major", "D minor", "E minor", "Pentatonic"],
            state="readonly"
        )
        self.scale.set("A minor")
        self.scale.grid(row=0, column=1, padx=20)

        self.create_section("DRUM RULES")

        drum_frame = tk.Frame(self.root, bg="#252832", padx=20, pady=15)
        drum_frame.pack(fill="x", padx=25, pady=5)

        self.kick = self.create_number_control(
            drum_frame, "Kick every turns", 4, 0
        )

        self.snare = self.create_number_control(
            drum_frame, "Snare every turns", 8, 1
        )

        self.create_section("MIDI CHANNELS")

        channel_frame = tk.Frame(self.root, bg="#252832", padx=20, pady=15)
        channel_frame.pack(fill="x", padx=25, pady=5)

        self.channels = {}

        for i, name in enumerate(
            ["Melody", "Kick", "Snare", "Hi-hat", "Bass", "Effects"]
        ):
            tk.Label(
                channel_frame,
                text=name,
                bg="#252832",
                fg="white"
            ).grid(row=i, column=0, sticky="w", pady=3)

            spin = tk.Spinbox(
                channel_frame,
                from_=1,
                to=16,
                width=5
            )
            spin.delete(0, "end")
            spin.insert(0, i + 1)
            spin.grid(row=i, column=1, padx=20, pady=3)

            self.channels[name] = spin

        save_button = tk.Button(
            self.root,
            text="SAVE SETTINGS",
            command=self.save_settings,
            bg="#65e6ad",
            fg="#17191f",
            font=("Arial", 12, "bold"),
            relief="flat",
            padx=20,
            pady=10
        )
        save_button.pack(pady=20)

        self.status = tk.Label(
            self.root,
            text="MIDITRON READY",
            bg="#17191f",
            fg="#65e6ad"
        )
        self.status.pack()

    def create_section(self, name):
        tk.Label(
            self.root,
            text=name,
            bg="#17191f",
            fg="#65e6ad",
            font=("Arial", 12, "bold")
        ).pack(anchor="w", padx=30, pady=(15, 5))

    def create_number_control(self, parent, label, default, row):
        tk.Label(
            parent,
            text=label,
            bg="#252832",
            fg="white"
        ).grid(row=row, column=0, sticky="w", pady=5)

        spin = tk.Spinbox(parent, from_=1, to=64, width=5)
        spin.delete(0, "end")
        spin.insert(0, default)
        spin.grid(row=row, column=1, padx=20)

        return spin

    def save_settings(self):
        self.status.config(text="Settings ready to save")


if __name__ == "__main__":
    root = tk.Tk()
    app = MiditronInterface(root)
    root.mainloop()
