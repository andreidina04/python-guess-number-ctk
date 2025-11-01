import customtkinter as ctk
import random

ctk.set_appearance_mode("dark")

class GuessNumberApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Guess the Number")
        self.geometry("600x500")

        self.numar = 0
        self.incercari = 0
        self.score = 100

        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(expand=True)

        self.score_label = ctk.CTkLabel(self, text=f"Scor: {self.score}", font=("Arial", 18, "bold"))
        self.score_label.pack(pady=10)

        self.frame_dificultate()

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def frame_dificultate(self):
        self.clear_main_frame()

        label = ctk.CTkLabel(self.main_frame, text="Alege dificultatea:", font=("Arial", 27))
        label.pack(pady=15)

        ctk.CTkButton(self.main_frame, text="Easy (10)", width=200, height=50,
                      font=("Arial", 20, "bold"), fg_color="#33ff83", text_color="black",command=lambda: self.start_game(10)).pack(pady=5)

        ctk.CTkButton(self.main_frame, text="Medium (5)", width=200, height=50,
                      font=("Arial", 20, "bold"), fg_color="#33ff83", text_color="black",command=lambda: self.start_game(5)).pack(pady=5)

        ctk.CTkButton(self.main_frame, text="Hard (3)", width=200, height=50,
                      font=("Arial", 20, "bold"), fg_color="#33ff83", text_color="black",command=lambda: self.start_game(3)).pack(pady=5)

    def start_game(self, incercari):
        self.numar = random.randint(0, 101)
        self.incercari = incercari
        self.frame_joc()

    def frame_joc(self):
        self.clear_main_frame()

        ctk.CTkLabel(self.main_frame, text="Ghiceste un numar între 0 și 101", font=("Arial", 18)).pack(pady=10)

        self.entry = ctk.CTkEntry(self.main_frame, width=200, height=50, placeholder_text="Scrie numărul tău aici...")
        self.entry.pack(pady=10)

        self.feedback = ctk.CTkLabel(self.main_frame, font=("Arial", 20), text="")
        self.feedback.pack(pady=5)

        ctk.CTkButton(self.main_frame, text="Verifică", command=self.verifica_numar,font=("Arial", 18, "bold"), text_color="black", fg_color="#33ff83").pack(pady=10)

        ctk.CTkButton(self.main_frame, text="Hint", command=self.show_hint,font=("Arial", 18, "bold"), text_color="black", fg_color="#33ff83").pack(pady=5)

        self.hint_label = ctk.CTkLabel(self.main_frame, font=("Arial", 16), text="")
        self.hint_label.pack(pady=5)

    def verifica_numar(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.feedback.configure(text="Număr invalid!", text_color="red")
            return

        if guess < 0 or guess > 101:
            self.feedback.configure(text="Numărul este în afara intervalului!", text_color="red")
            return

        self.incercari -= 1

        if guess == self.numar:
            self.feedback.configure(text=f"Felicitări! Numărul era {self.numar}", text_color="green")
            self.score += 100
            self.update_score()
            self.after(2000, self.frame_dificultate)
        elif self.incercari == 0:
            self.feedback.configure(text=f"Game Over! Numărul era {self.numar}", text_color="red")
            self.score -= 100
            self.update_score()
            self.after(2000, self.frame_dificultate)
        elif guess < self.numar:
            self.feedback.configure(text=f"Numărul e mai MARE! Încercări rămase: {self.incercari}", text_color="black")
            self.score -= 10
            self.update_score()
        else:
            self.feedback.configure(text=f"Numărul e mai MIC! Încercări rămase: {self.incercari}", text_color="black")
            self.score -= 10
            self.update_score()

    def show_hint(self):
        numar1 = max(0, self.numar - 5)
        numar2 = min(101, self.numar + 5)
        self.hint_label.configure(text=f"Numărul se află între {numar1} și {numar2}.")

    def update_score(self):
        self.score_label.configure(text=f"Scor: {self.score}")

if __name__ == "__main__":
    app = GuessNumberApp()
    app.mainloop()
