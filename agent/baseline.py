from env.support_env import SupportEnv
from tasks.easy import TASK as EASY, grade as g1
from tasks.medium import TASK as MEDIUM, grade as g2
from tasks.hard import TASK as HARD, grade as g3


def run_task(task):
    try:
        env = SupportEnv(task)
        obs = env.reset()
        total = 0

        while obs:
            action = {
                "classification": "spam" if "free" in obs.customer_message.lower() else "billing",
                "priority": "high",
                "response": "sorry refund",
                "escalate": True,
                "request_info": False
            }

            obs, reward, done, _ = env.step(action)
            total += reward.score   # FIX: reward.score

            if done:
                break

        return total

    except Exception as e:
        print("Error in task:", e)
        return 0.0


def run_baseline():
    try:
        return {
            "easy": g1(run_task(EASY)),
            "medium": g2(run_task(MEDIUM)),
            "hard": g3(run_task(HARD))
        }
    except Exception as e:
        return {
            "error": str(e)
        }