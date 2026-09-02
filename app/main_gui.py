import customtkinter as ctk
import requests
import threading

ctk.set_appearance_mode("System")

class PrivateTriageClient(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Private-Triage Client")
        self.geometry("900x600")

        self.api_url = "http://127.0.0.1:8000/api/v1/triage"

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=200)
        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)

        self.btn_sample = ctk.CTkButton(self.sidebar, text="Process Test Email", command=self.send_sample_email)
        self.btn_sample.pack(padx=10, pady=20)

        # Content Area
        self.scroll = ctk.CTkScrollableFrame(self, label_text="Inbox Summaries")
        self.scroll.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    def send_sample_email(self):
        payload = {
            "sender": "prof@mits.ac.in",
            "subject": "Hello Prince this is Internshala",
            "body": "Internshala B.Tech students, explore this Work from Home opportunity Internshala Student Partner Program Are you looking for work opportunities in your free time? This program connects students with relevant opportunities. Program highlights: Learning Opportunity - Masterclasses by industry professionals Skill Development - Gain professional experience Professional Development - Develop skills like Leadership, Communication & Marketing What's more? Add program experience to your resume to boost it. Eligibility - B.Tech students from Madhav Institute can apply. Click here for more information. Applications are currently open"
        }
        
        # Async HTTP request to prevent GUI freeze
        threading.Thread(target=self._call_api, args=(payload,), daemon=True).start()

    def _call_api(self, payload: dict):
        try:
            res = requests.post(self.api_url, json=payload, timeout=30)
            if res.status_code == 200:
                data = res.json()
                self.after(0, self.render_card, payload, data)
        except Exception as e:
            print(f"API Error: {e}")

    def render_card(self, email_data: dict, result: dict):
        card = ctk.CTkFrame(self.scroll)
        card.pack(fill="x", expand=True, pady=5, padx=5)

        title = ctk.CTkLabel(card, text=f"[{result['category']}] From: {email_data['sender']}", font=ctk.CTkFont(weight="bold"))
        title.pack(anchor="w", padx=10, pady=5)

        subj = ctk.CTkLabel(card, text=f"Subject: {email_data['subject']}")
        subj.pack(anchor="w", padx=10)

        summary = ctk.CTkLabel(card, text=f"📌 Summary: {result['summary']}\n⚡ Action: {result['action_item']}")
        summary.pack(anchor="w", padx=10, pady=5)

if __name__ == "__main__":
    app = PrivateTriageClient()
    app.mainloop()