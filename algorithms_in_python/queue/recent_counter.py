# Problem - https://leetcode.com/problems/number-of-recent-calls/?envType=study-plan-v2&envId=leetcode-75

class RecentCounter:

    def __init__(self):
        self.queue = []
        self.first_message_time = None

    def ping(self, t: int) -> int:
        while len(self.queue) > 0:
            if self.queue[0] < t - 3000:
                self.queue.pop(0)
            else:
                break
        self.queue.append(t)
        return len(self.queue)

counter = RecentCounter()
print([counter.ping(1),counter.ping(100),counter.ping(3001),counter.ping(3002)])