# Private-Triage: Local AI-Powered Desktop Notification Agent

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Model](https://img.shields.io/badge/Model-Gemma--4--E4B-orange)](https://huggingface.co/google/gemma-4-e4b-it)
[![OS-Ready](https://img.shields.io/badge/Platform-Windows_11-blue)](https://microsoft.com/windows)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

A privacy-first, system-level agent that intercepts incoming desktop notifications (Email, Slack, Teams) and uses a local **Gemma 4 E4B** model to categorize them by intent, provide reasoning, and suggest instant actions—all without sending data to the cloud.

## 🚀 Key Features

*   **Real-Time Notification Hook:** Intercepts incoming OS-level notifications using system APIs (WinRT/Desktop-Notifier).
*   **Explainable AI (XAI):** Provides a short "Rationalize" block for every alert, explaining why a specific priority was assigned.
*   **Zero-Cloud Privacy:** Processes sensitive communication snippets entirely in local memory; 100% functional in Airplane Mode.
*   **Context-Aware Action:** Automatically drafts email replies or calendar invites based on the intent detected in the notification snippet.
*   **High-Speed Inference:** Leverages Gemma 4's **Multi-Token Prediction (MTP)** drafters for near-instant classification on consumer laptop GPUs.

## 🏗️ Architecture

The system operates as a seamless background service:

1.  **Stage 1 (System Listener):** A Python background process monitors the Windows/macOS Notification Center.
2.  **Stage 2 (Inference):** Extracted snippets are fed to a quantized **Gemma 4 E4B** model. It performs a "Rationale-First" analysis to determine intent (Urgent, Scheduling, Info, or Social).
3.  **Stage 3 (Triage GUI):** High-priority alerts are mirrored in a custom **CustomTkinter** dashboard with "One-Click" action buttons.

## 📂 Project Structure

```text
├── core/                # Notification listener & System Hooks (PyWinRT)
├── fine-tuning/         # Dataset scripts (AESLC/BC3) & LoRA configs
├── inference/           # Local engine setup (Ollama/llama.cpp integration)
├── app/                 # Triage Dashboard GUI (CustomTkinter)
├── screenshots/         # UI/UX demonstrations
├── LICENSE              # Apache 2.0 License (Code & Weights)
├── NOTICE               # Attribution for Google Gemma 4
└── README.md            # Project Documentation
```

## 📊 Dataset & TrainingModel: Google Gemma 4 E4B (Instruction Tuned). 

Training Method: Fine-tuned via QLoRA on 15,000 synthesized notification-intent pairs.

Inference Optimization: Uses 4-bit Quantization (Q4_K_M) to maintain a ~3.5GB memory footprint, ideal for background laptop use.

Metric: Optimized for Recall, ensuring that "Urgent" business logic is never missed.

## 💻 Hardware RequirementsOS: 

Windows 11 or macOS.

RAM: 8GB Minimum (16GB Recommended). otherwise it would be difficult to fine-ttrain the model on the device

GPU: Any DirectX 12 or Metal compatible GPU for accelerated inference.

## ⚖️ License

This project is licensed under the Apache License 2.0. As of April 2026, the Gemma 4 family is fully open-source under Apache 2.0, allowing for complete developer sovereignty.


### Author: Prince Parashar
### Affiliation: Madhav Institute of Technology and Science (MITS), Gwalior

## Start Date of the Project = 21-06-2006
