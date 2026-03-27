from fastapi import FastAPI
from env.support_env import SupportEnv
from env.models import Action
from tasks.easy import TASK as EASY, grade as g1
from tasks.medium import TASK as MEDIUM, grade as g2
from tasks.hard import TASK as HARD, grade as g3
from agent.baseline import run_baseline

app = FastAPI()

TASKS = {"easy": EASY, "medium": MEDIUM, "hard": HARD}

env = None
current_score = 0

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/reset")
def reset(task: str = "easy"):
    global env, current_score
    env = SupportEnv(TASKS[task])
    current_score = 0
    return env.reset().dict()

@app.post("/step")
def step(action: Action):
    global current_score

    obs, reward, done, info = env.step(action)
    current_score += reward.score

    return {
        "observation": obs.dict() if obs else None,
        "reward": reward.score,
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    return env.state()

@app.get("/tasks")
def tasks():
    return {
        "tasks": list(TASKS.keys()),
        "action_schema": {
            "classification": "string",
            "priority": "string",
            "response": "string",
            "escalate": "bool",
            "request_info": "bool"
        }
    }

@app.get("/grader")
def grader():
    return {
        "easy": g1(current_score),
        "medium": g2(current_score),
        "hard": g3(current_score)
    }

@app.get("/baseline")
def baseline():
    return run_baseline()