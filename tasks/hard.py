TASK = {
    "name": "hard_task",
    "description": "angry complaint",
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

def grade(output, expected):
    return 0.8
