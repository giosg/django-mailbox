from django.dispatch.dispatcher import Signal

message_received = Signal()  # providing_args=['message']
# Provides: attachment (MessageAttachment), filename (str), payload (bytes), message (Message)
attachment_received = Signal()
