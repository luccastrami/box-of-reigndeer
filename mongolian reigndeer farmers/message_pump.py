class MessagePump(object):

    

    def __init__(self):

        self.endpoints = []



    def register(self, obj):

        self.endpoints.append(obj)

    

    def send_message(self, message_type, message):

        for e in self.endpoints:

            e.message(message_type, message)

    

