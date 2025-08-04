# AutoPoster  
A simple content rewriting bot that takes in raw thoughts and turns them into polished posts for LinkedIn and X — powered by GPT and a bit of brain.

---

# What it Does

AutoPoster is a lightweight content automation tool that:

- Reads **raw logs** (your daily ideas or notes) from a Google Sheet  
- Uses **OpenAI GPT (via API)** to rewrite them into platform-specific posts:
  - A professional-style post for **LinkedIn**
  - A tweet-style version for **X**
- Updates the same sheet with the rewritten content and posting status

---

## How It Was Made

This project was built by me, combining:
- My logic, intuition, and trial-and-error problem-solving
- ChatGPT (my AI co-pilot) to help debug, brainstorm, and clean up
- Python + `gspread` to talk to Google Sheets
- `dotenv` for secret management
- OpenAI API to handle the rewriting

---

## How It Works (Under the Hood)

1. You write your **daily thoughts** or ideas in the “Raw Log” column
2. When you're ready, change the **Status** to `Pending`
3. Run the script:  
   `python rewrite_posts.py`
4. The script:
   - Reads your input
   - Sends it to GPT for rewriting
   - Fills in the "LinkedIn Post" and "X posts" columns
   - Leaves the post for manual review/posting\
   - Changes **Status** from `Pending` to `Ongoing`
5. Then you if youre statisfied by the generated text and is going to post, you can change `Ongoing` to `Posted`

---

## 🛠 Setup

### 1. Clone this repo

git clone https://github.com/YourUsername/AutoPoster-bot.git

cd AutoPoster-bot


### 2. Install Dependencies

pip install -r requirements.txt


### 3. Set up your .env

Create a .env file based on this format on .env.example

**Make sure your service account has edit access to your Google Sheet.**



Contributions Welcome!
This project is open to contributions — feel free to fork, improve, or create issues if you have ideas.