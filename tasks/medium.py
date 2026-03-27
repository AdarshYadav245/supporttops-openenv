TASK = {
    "tickets": [
        {
            "id": "2",
            "text": "I was charged twice, please help",
            "ground_truth": {
                "classification": "billing",
                "priority": "high",
                "escalate": False,
                "keyword": "refund"
            }
        }
    ]
}

def grade(score):
    if score > 0.7:
        return 1.0
    elif score > 0.4:
        return 0.5
    return 0.0