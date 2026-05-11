import random
from day8_hash_sharding import HashShardManager
from day5_shards_intro import Message

def simulate(manager, num_users=1000, num_messages=5000):
    for _ in range(num_messages):
        user_id = random.randint(1, num_users)
        channel_id = random.randint(1, 50)
        msg = Message(user_id, channel_id, "normal traffic")
        manager.send_message(msg)
        
    for _ in range(3000):
        msg = Message(random.randint(1, num_users), 10, "viral spike traffic")
        manager.send_message(msg)

    for shard in manager.shards:
        if shard is not None:
            print(f"Shard {shard.id}: {len(shard.messages)} messages")

def fetch_last_10(manager, channel_id):
    results = []
    shards_checked = 0
    for shard in manager.shards:
        if shard is None:
            print("Warning: A shard is down. Data might be missing!")
            continue
        shards_checked += 1
        chan_msgs = [m for m in shard.messages if m.channel_id == channel_id]
        results.extend(chan_msgs)
    print("Checked", shards_checked, "shards to get this data")
    return results[-10:]

if __name__ == "__main__":
    print("Running stress test on Hash manager:")
    hash_mgr = HashShardManager(3)
    simulate(hash_mgr)

    print("\nSimulating server failure:")
    hash_mgr.shards[1] = None

    print("\nFetching messages for viral channel 10:")
    fetch_last_10(hash_mgr, 10)

    print("\nObservation: The hash manager handled the viral spike perfectly by distributing the 3000 messages evenly. But when I killed Shard 1 and tried to fetch messages I got a missing data warning. Because the messages are spread out randomly losing one shard means losing a random chunk of the conversation.")
