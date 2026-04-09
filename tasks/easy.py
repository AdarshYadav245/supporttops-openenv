TASK = {
    "name": "easy_task",
    "description": "spam classification",
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

def grade(output, expected):
    return 0.6
