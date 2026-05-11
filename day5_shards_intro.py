class Shard:
    def __init__(self, shard_id):
        self.id = shard_id
        self.messages = []

    def store(self, message):
        self.messages.append(message)

class Message:
    def __init__(self, user_id, channel_id, content):
        self.user_id = user_id
        self.channel_id = channel_id
        self.content = content

class ShardManager:
    def __init__(self, num_shards):
        self.shards = [Shard(i) for i in range(num_shards)]

    def send_message(self, message):
        pass
    
    def check_hotspots(self):
        total = sum(len(s.messages) for s in self.shards if s is not None)
        if total == 0: return
        for s in self.shards:
            if s is not None and len(s.messages) / total > 0.5:
                print("Warning: Shard", s.id, "has more than 50 percent load!")
