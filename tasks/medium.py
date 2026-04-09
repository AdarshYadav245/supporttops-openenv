TASK = {
    "name": "medium_task",
    "description": "billing issue",
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

def grade(output, expected):
    return 0.7
