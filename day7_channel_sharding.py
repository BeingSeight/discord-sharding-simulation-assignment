from day5_shards_intro import ShardManager, Message

class ChannelShardManager(ShardManager):
    def get_shard(self, channel_id):
        return self.shards[channel_id % len(self.shards)]

    def send_message(self, message):
        shard = self.get_shard(message.channel_id)
        shard.store(message)

if __name__ == "__main__":
    channel_manager = ChannelShardManager(3)
    for _ in range(5000):
        channel_manager.send_message(Message(1, 5, "viral event channel"))

    for s in channel_manager.shards:
        print("Shard", s.id, ":", len(s.messages), "messages")
    channel_manager.check_hotspots()
    print("Observation: I changed logic to channel based but the exact same hotspot problem happened. The viral channel 5 forced all 5000 messages onto Shard 2. Channel based is just as bad when there is a sudden spike in one specific room.")
