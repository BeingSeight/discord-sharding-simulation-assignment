import time

class Message:
    def __init__(self, user_id, channel_id, content):
        self.user_id = user_id
        self.channel_id = channel_id
        self.content = content

class ChatServer:
    def __init__(self):
        self.messages = []
    
    def send_message(self, message):
        self.messages.append(message)

    def stats(self):
        print("Total messages:", len(self.messages))

if __name__ == "__main__":
    server = ChatServer()
    start = time.time()
    for i in range(10000):
        server.send_message(Message(i, 1, "hello"))
    print("Time for 10000 msgs:", time.time() - start)
    server.stats()
    print("Observation: The system works fine for a few users but as I simulated 10000 messages the list just keeps growing. There is no separation and the memory grows endlessly. If this runs for a real game event the server will run out of RAM and just shut down.")
