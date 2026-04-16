import requests

API_KEY = "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"


def generate_summary(data):
    try:
        print("STEP 1: Data received")

        alert_hour = data["alert_hour"]
        risk = data["risk_scores"][alert_hour]

        hr = data["vitals_summary"]["HR"][alert_hour]
        temp = data["vitals_summary"]["Temp"][alert_hour]
        resp = data["vitals_summary"]["Resp"][alert_hour]

        print("STEP 2: Data extracted")

        prompt = f"""
Patient has high sepsis risk.

Risk Score: {risk}
Heart Rate: {hr}
Temperature: {temp}
Respiratory Rate: {resp}

Write a short clinical summary.
"""

        print("STEP 3: Prompt created")

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost",   # required
                "X-Title": "sepsis-project"           # required
            },
            json={
                "model": "openai/gpt-3.5-turbo",
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
        )

        print("STEP 4: API called")

        result = response.json()

        print("STEP 5: Response received")

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        print("ERROR OCCURRED:", e)
        return "ERROR"