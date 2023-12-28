from collections import defaultdict

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radient_q = []
        dire_q = []
        for i,senator in enumerate(senate):
            if senator == 'R':
                radient_q.append(i)
            else:
                dire_q.append(i)
        index = len(senate)
        while len(radient_q) > 0 and len(dire_q) > 0:
            r = radient_q.pop(0)
            d = dire_q.pop(0)
            if r > d:
                dire_q.append(index)
                index += 1
            else:
                radient_q.append(index)
                index += 1
        if len(radient_q) > 0:
            return 'Radiant'
        else:
            return 'Dire'

print(Solution().predictPartyVictory('RDD'))
print(Solution().predictPartyVictory('RRDDDDDDDRRDRRDDRRRR'))
#print(Solution().predictPartyVictory('DDRRR'))



# def predictPartyVictory(self, senate: str) -> str:
#     current_vote_count = {'D': 0, 'R': 0}
#     next_vote_count = {'D': 0, 'R': 0}
#     party_name = {'R': 'Radiant', 'D': 'Dire'}
#     banned_count = {'R': 0, 'D': 0}
#     queue = []
#     for senator in senate:
#         current_vote_count[senator] += 1
#         queue.append(senator)
#     # End of round marker
#     queue.append('X')
#     while len(queue) > 0:
#         current_party = queue.pop(0)
#         if current_party == 'X':
#             current_vote_count, next_vote_count = dict(next_vote_count), {'D': 0, 'R': 0}
#             banned_count = {'R': 0, 'D': 0}
#             queue.append('X')
#             continue
#         if banned_count[current_party] > 0:
#             banned_count[current_party] -= 1
#             continue
#         other_party = 'D' if current_party == 'R' else 'R'
#         if current_vote_count[current_party] > current_vote_count[other_party]:
#             return party_name[current_party]
#         else:
#             if current_vote_count[other_party] > 0:
#                 current_vote_count[other_party] -= 1
#                 banned_count[other_party] += 1
#             else:
#                 return party_name[current_party]
#         current_vote_count[current_party] -= 1
#         next_vote_count[current_party] += 1
#         queue.append(current_party)