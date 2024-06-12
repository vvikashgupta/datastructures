class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        pindex = 0
        tindex = 0
        count = 0
        while pindex < len(players) and tindex < len(trainers):
            if players[pindex] <= trainers[tindex]:
                count += 1
                pindex += 1
                tindex += 1
            elif players[pindex] > trainers[tindex]:
                tindex += 1
        return count
