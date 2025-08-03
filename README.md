<<<<<<< HEAD
# AutoPoster-bot
AI-powered personal content engine that rewrites daily logs into LinkedIn + X posts.
Built an AI-powered content engine using GPT + Google Sheets + X API. I designed the system and used AI as a coding copilot.
=======
Script 1: rewrite_posts.py
Purpose: Only processes rows with status "Pending"
Action:
Generates LinkedIn + X content
Fills the LinkedIn Post and X posts columns
Changes status to "Ongoing"



Script 2: post_approved.py
Purpose: Only processes rows with status "Approved" or "Skipped"
Action:

Approved:
Posts to LinkedIn and X
Posts all tweets separately (not as a thread)
Ignores any numbering like "1." or "2."
Schedules them for the best tweet times starting from current time
Updates status to "Posted"
Skipped:
Deletes those rows from the sheet
>>>>>>> a33b7ea (Create README.md)
