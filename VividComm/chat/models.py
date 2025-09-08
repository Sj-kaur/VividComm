# chat/models.py
from django.db import models
from django.conf import settings

class ChatRoom(models.Model):
    """
    A chat room between two users.
    """
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='chat_rooms',
        help_text="The users participating in this chat room."
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Display a list of participants for easy identification
        usernames = ", ".join([user.username for user in self.participants.all()])
        return f"Chat Room with: {usernames}"

class Message(models.Model):
    """
    A single message sent within a chat room.
    """
    room = models.ForeignKey(
        ChatRoom,
        on_delete=models.CASCADE,
        related_name='messages',
        help_text="The chat room this message belongs to."
    )
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sent_messages',
        help_text="The user who sent this message."
    )
    content = models.TextField(help_text="The text content of the message.")
    timestamp = models.DateTimeField(auto_now_add=True, help_text="The time the message was sent.")

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"Message by {self.sender.username} in {self.room}"