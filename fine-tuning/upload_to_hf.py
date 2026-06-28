import os
import pandas as pd
from datasets import Dataset, DatasetDict

# 1. Configuration
PICKLE_FILE = "Triage_dataset_Next_3.pkl"  # Change to unified_triaged_dataset.pkl if you merged it
HF_DATASET_NAME = "dokodeen/my-triaged-messages_Next_3"  # 👈 Replace with your HF username and desired repo name

print("🔄 Loading your processed dataset...")
try:
    # Load your pickle dataframe
    df = pd.read_pickle(PICKLE_FILE)
    
    # Ensure all data formatting columns are clean strings
    df['message'] = df['message'].astype(str)
    df['intent_output'] = df['intent_output'].astype(str)
    df['category'] = df['category'].astype(str)

    # 2. Convert Pandas DataFrame to Hugging Face Dataset format
    print("📦 Converting to Hugging Face Dataset format...")
    hf_dataset = Dataset.from_pandas(df)

    # (Optional) Split into train/validation sets automatically (e.g., 90% train, 10% test)
    dataset_dict = hf_dataset.train_test_split(test_size=0.1, seed=42)

    # 3. Push to Hugging Face Hub
    print(f"🚀 Uploading dataset to Hugging Face Hub as: {HF_DATASET_NAME}...")
    
    # This will automatically read your logged-in git credentials or token
    dataset_dict.push_to_hub(HF_DATASET_NAME, private=True) # Set to False if you want it public
    
    print("\n✅ Success! Your dataset is safely uploaded and hosted on Hugging Face.")
    print("Finally time to sleep peacefully now. 🛌💤")

except FileNotFoundError:
    print(f"❌ Error: Could not find '{PICKLE_FILE}'. Double-check the filename path.")
except Exception as e:
    print(f"❌ An error occurred during the upload process: {e}")