from app.models import CommunicationRecord

# Example function to retrieve all messages from a specific sender
def get_messages_by_sender(sender_name):
    records = CommunicationRecord.query.filter_by(sender=sender_name).all()
    return records