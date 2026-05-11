import hashlib
from day5_shards_intro import ShardManager, Message

class HashShardManager(ShardManager):
    def get_shard(self, key):
        h = int(hashlib.md5(str(key).encode()).hexdigest(), 16)
        return self.shards[h % len(self.shards)]

    def send_message(self, message):
        unique_key = str(message.user_id) + str(id(message))
        shard = self.get_shard(unique_key)
        shard.store(message)

if __name__ == "__main__":
    print("Observation: I chose to hash a combination of the user id and the unique object id of the message. This makes sure every single message gets a unique hash even if it comes from the same user or same channel. This finally distributes the load evenly across all shards so no server gets overwhelmed.")
