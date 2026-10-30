class Twitter:

    def __init__(self):
        self.time = 0
        self.timestamps = {} # tweetId: time
        self.tweets = {} # userId: tweets
        self.following = {} # userId: following
        
    def establishUser(self, userId: int):
        if not userId in self.tweets:
            self.tweets[userId] = []
        if not userId in self.following:
            self.following[userId] = {userId,}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.establishUser(userId)
        self.tweets[userId].append(tweetId)
        self.timestamps[tweetId] = self.time
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.establishUser(userId)

        import heapq
        heap = []
        k = 10
        for follower in self.following[userId]:
            for tweet in self.tweets[follower]:
                timestamp = self.timestamps[tweet]
                if k > 0:
                    heapq.heappush(heap, (timestamp, tweet))
                    k -= 1
                elif timestamp > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (timestamp, tweet))
        return [tweetId for _, tweetId in sorted(heap, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.establishUser(followerId)
        self.establishUser(followeeId)
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.establishUser(followerId)
        self.establishUser(followeeId)
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
