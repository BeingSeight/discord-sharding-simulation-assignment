from day5_shards_intro import ShardManager, Message

class UserShardManager(ShardManager):
    def get_shard(self, user_id):
        return self.shards[user_id % len(self.shards)]

    def send_message(self, message):
        shard = self.get_shard(message.user_id)
        shard.store(message)

if __name__ == "__main__":
    user_manager = UserShardManager(3)
    for _ in range(5000):
        user_manager.send_message(Message(99, 1, "spam from influencer"))

    for s in user_manager.shards:
        print("Shard", s.id, ":", len(s.messages), "messages")
    user_manager.check_hotspots()
    print("Observation: I simulated one influencer sending massive traffic. Because we route by user id all 5000 messages went to Shard 0. The other two shards stayed completely empty. This proves user based routing creates massive load imbalance.")
