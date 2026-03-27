from env.models import Observation, Action, Reward

class SupportEnv:
    def __init__(self, task):
        self.task = task
        self.index = 0
        self.total_reward = 0
        self.satisfaction = 0  # bonus for creativity

    def reset(self):
        self.index = 0
        self.total_reward = 0
        self.satisfaction = 0
        return self._get_obs()

    def state(self):
        return {"current_index": self.index}

    def step(self, action: Action):
        action = action.dict()

        ticket = self.task["tickets"][self.index]
        gt = ticket["ground_truth"]

        score = 0.0

        if action["classification"] == gt["classification"]:
            score += 0.3
        if action["priority"] == gt["priority"]:
            score += 0.2
        if action["escalate"] == gt["escalate"]:
            score += 0.2
        if gt["keyword"] in action["response"].lower():
            score += 0.3

        # 🔥 creativity bonus
        if "sorry" in action["response"].lower():
            self.satisfaction += 0.1

        score += self.satisfaction

        self.total_reward += score
        self.index += 1

        done = self.index >= len(self.task["tickets"])
        obs = self._get_obs() if not done else None

        return obs, Reward(score=score), done, {}

    def _get_obs(self):
        t = self.task["tickets"][self.index]
        return Observation(
            ticket_id=t["id"],
            customer_message=t["text"],
            history=[],
            step=self.index
        )