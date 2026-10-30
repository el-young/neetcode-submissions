from collections import defaultdict
class Twitter:

    def __init__(self):
        self.time = 0
        self.users = defaultdict(lambda: {
            "tweets": list(), # (timestamp, tweetId)
            "following": set(),
        }) 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId]["tweets"].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        import heapq
        heap = []
        followees = self.users[userId]["following"]
        for followee in followees | {userId}:
            for timestamp, tweet in self.users[followee]["tweets"][-10:]:
                if len(heap) < 10:
                    heapq.heappush(heap, (timestamp, tweet))
                elif timestamp > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (timestamp, tweet))
        return [tweetId for _, tweetId in sorted(heap, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId]["following"].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]["following"]:
            self.users[followerId]["following"].remove(followeeId)
