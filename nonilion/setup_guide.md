# Nonilion Import & Setup Guide

This guide walks you through importing **OmniChief** into your Nonilion virtual office.

---

## Method 1: Direct Gemini API Import (Recommended for Live Judging)
1. Sign in to [www.nonilion.com](https://www.nonilion.com) *(ensure `www.` is in the address)*.
2. Enter your office and create or rename a room: **`Strategy War Room`**.
3. In that room, open the **Agents dock** and click **Import** (or visit [www.nonilion.com/import-agent](https://www.nonilion.com/import-agent)).
4. Select **Gemini**.
5. Fill in the agent details:
   - **Name:** `OmniChief`
   - **Role:** `Autonomous Chief of Staff & Operations Strategist`
   - **API Key:** Paste your Gemini API key from [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey).
   - **Instructions:** Copy and paste the entire prompt from `app/prompts.py` (`SYSTEM_INSTRUCTION`).
6. Click **Save / Import**.
7. OmniChief will immediately appear as an interactive character in your Strategy War Room.

---

## Method 2: Custom Webhook / Bot API Route (Using Render Hosting)
1. Deploy this repository to **Render** using your hackathon Render credits.
2. Under Render dashboard, copy your public service URL (e.g. `https://omnichief-nonilion-agent.onrender.com`).
3. In Nonilion, click the **Robot Button** in your room's Agents dock to get a one-time pairing code.
4. Set the webhook URL to: `https://<YOUR_RENDER_URL>/webhook`.
5. Nonilion will now route room messages and @mentions directly to your hosted FastAPI backend.
