TASK = {
    "tickets": [
        {
            "id": "1",
            "text": "Win a free iPhone now!!!",
            "ground_truth": {
                "classification": "spam",
                "priority": "low",
                "escalate": False,
                "keyword": ""
            }
        }
    ]
}

def grade(score):
    return min(1.0, score)