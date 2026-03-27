TASK = {
    "tickets": [
        {
            "id": "3",
            "text": "Your service is terrible, fix this NOW",
            "ground_truth": {
                "classification": "complaint",
                "priority": "high",
                "escalate": True,
                "keyword": "sorry"
            }
        }
    ]
}

def grade(score):
    if score > 0.8:
        return 1.0
    elif score > 0.5:
        return 0.5
    return 0.0