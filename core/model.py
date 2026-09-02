import json
import time
from llama_cpp import Llama
from core.schemas import EmailTriageResponse

class GemmaTriageEngine:
    def __init__(self, model_path: str):
        # Load local model into VRAM
        self.llm = Llama(
            model_path=model_path,
            n_gpu_layers=-1,  # Offload all layers to GPU
            n_ctx=2048,
            verbose=False
        )

    def analyze_email(self, sender: str, subject: str, body: str) -> EmailTriageResponse:
        prompt = f"""<start_of_turn>user
Analyze and summarize the following email.

From: {sender}
Subject: {subject}
Body: "{body}"

Respond STRICTLY with a valid JSON object using these exact keys:
- "category": ("Action Required" | "Informational" | "Newsletter/Promotional" | "Low Priority")
- "summary": (A concise 1-2 sentence summary of the email content)
- "action_item": (Specific task required or "None")
- "quick_reply": (A short proposed 1-sentence draft reply)
<end_of_turn>
<start_of_turn>model
"""

        start_time = time.time()
        output = self.llm(
            prompt,
            max_tokens=180,
            temperature=0.1,
            stop=["<end_of_turn>"]
        )
        latency = round(time.time() - start_time, 2)

        raw_text = output['choices'][0]['text'].strip()
        print(raw_text)
        try:
            parsed = json.loads(raw_text)
        except json.JSONDecodeError:
            parsed = {
                "category": "Informational",
                "summary": "Failed to parse structured response.",
                "action_item": "Review email manually.",
                "quick_reply": "Thank you for the update."
            }

        return EmailTriageResponse(
            category=parsed.get("category", "Informational"),
            summary=parsed.get("summary", ""),
            action_item=parsed.get("action_item", "None"),
            quick_reply=parsed.get("quick_reply", ""),
            latency_seconds=latency
        )