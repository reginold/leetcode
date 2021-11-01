class Twitter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = {}
        self.global_tweets = []

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        if self.users.get(userId) is None:
            self.users[userId] = {"tweets": [tweetId], "followers": []}
        else:
            self.users[userId]["tweets"].insert(0, tweetId)
        self.global_tweets.insert(0, tweetId)
        # print(self.users[userId])

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """

        user = self.users.get(userId)
        if user is not None:

            feed = []
            for i in user["tweets"]:
                feed.append(i)
            for i in user["followers"]:
                if self.users.get(i) is not None:
                    for j in self.users[i]["tweets"]:
                        feed.append(j)
            ans = []
            for i in self.global_tweets:
                if i in feed:
                    ans.append(i)
            return ans[:10]
        else:
            return []

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if self.users.get(followerId) is None:
            self.users[followerId] = {"tweets": [], "followers": [followeeId]}
        else:
            self.users[followerId]["followers"].append(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if self.users.get(followerId) is None:
            self.users[followerId] = {"tweets": [], "followers": []}
        else:
            if followeeId in self.users[followerId]["followers"]:
                self.users[followerId]["followers"].remove(followeeId)
            else:
                pass


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
