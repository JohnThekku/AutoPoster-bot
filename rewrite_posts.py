import os
from dotenv import load_dotenv
import openai
import gspread
from urllib.parse import urlparse

# Load environment variables
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Setup Google Sheets
gc = gspread.service_account(filename=os.getenv("GOOGLE_CREDS_JSON"))
sheet_url = os.getenv("SHEET_URL")
sheet_id = urlparse(sheet_url).path.split("/")[3]
ws = gc.open_by_key(sheet_id).sheet1

rows = ws.get_all_records()
for idx, row in enumerate(rows, start=2):
    raw_log = row.get("Raw Log", "").strip()
    status = row.get("Status", "").strip().lower()

    if not raw_log or status != "pending":
        continue

    print(f"[DEBUG] Row {idx}: Generating posts for raw_log='{raw_log}'")

    try:
        linkedin_post = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a social media expert."},
                {"role": "user", "content": f"Write a LinkedIn post for this update: {raw_log}"}
            ]
        ).choices[0].message.content.strip()

        x_posts = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Twitter growth hacker."},
                {"role": "user", "content": f"Split the following log into 3–5 high-quality, unnumbered X (Twitter) posts. Each tweet should stand alone, focus on insights, progress, or thoughts. Avoid numbering. Separate each tweet with '/x/' on a new line. {raw_log}"}
            ]
        ).choices[0].message.content.strip()

        # Update Sheet
        ws.update_cell(idx, 3, linkedin_post)
        ws.update_cell(idx, 4, x_posts)
        ws.update_cell(idx, 5, "Ongoing")

        print(f"✅ Row {idx} updated")

    except Exception as e:
        print(f"❌ Error on row {idx}: {e}")


