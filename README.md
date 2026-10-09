# RoadReady — Fuel Trip Calculator

A responsive fuel-cost calculator for road trips. Users enter distance, vehicle MPG, gas price, and optional additional expenses. The Flask back end validates the inputs and returns the estimate; the front end displays fuel required, fuel cost, total cost, cost per mile, and rule-based trip tips.

## Problem and proposed solution
Planning a long drive can be expensive, and drivers may not know how much fuel money to set aside. RoadReady estimates fuel usage and trip cost before departure, helping drivers compare plans and budget more confidently.

## Features
- Responsive form and results dashboard
- Back-end calculation endpoint (`POST /api/calculate`)
- Input validation and user-facing error handling
- Fuel gallons, fuel cost, optional extra expenses, total estimate, and cost per mile
- Rule-based recommendation helper tailored to the entered trip
- No API keys or external AI service required

## Technology stack
- Front end: HTML, CSS, JavaScript
- Back end: Python and Flask
- Deployment: Render with Gunicorn
- Version control: GitHub
- AI development assistance: ChatGPT helped plan, write, and document the prototype

## Calculation
- Gallons needed = distance in miles ÷ vehicle MPG
- Fuel cost = gallons needed × price per gallon
- Estimated trip total = fuel cost + other expenses
- Cost per mile = estimated trip total ÷ distance

## Run locally
1. Install Python 3.10 or newer.
2. In this folder, create/activate a virtual environment if desired.
3. Run `pip install -r requirements.txt`.
4. Run `python app.py`.
5. Open `http://127.0.0.1:5000`.

## Deploy on GitHub and Render
1. Create a GitHub repository named `roadready-fuel-calculator`.
2. Upload `app.py`, `requirements.txt`, `Procfile`, `README.md`, and the `templates/` folder.
3. On Render, create a **New Web Service** and connect this repository.
4. Use build command: `pip install -r requirements.txt`
5. Use start command: `gunicorn app:app`
6. Deploy and open the public `.onrender.com` URL Render provides.
7. Paste the GitHub repository URL and deployed URL into your project submission.

## AI feature note
This version's recommendation helper is a transparent, rule-based decision feature rather than a generative AI model connected to an external service. It adapts suggestions based on distance, MPG, fuel cost, and extra expenses. In a presentation, accurately describe it as a smart/rule-based helper and explain that ChatGPT was used as a development tool. If the instructor requires a live generative AI API integration, add one using a protected server-side API key stored in Render environment variables—never commit secrets to GitHub.

## Example test
Distance 300 miles, MPG 30, gas price $3.50, extra expenses $10:
- Fuel needed: 10 gallons
- Fuel cost: $35.00
- Estimated total: $45.00
- Cost per mile: $0.15

## Project links
- GitHub repository: add your repository URL here.
- Live application: add your Render URL here.
