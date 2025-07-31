import uuid
import mongoengine as me
from datetime import datetime

class Website(me.Document):
    id = me.StringField(primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = me.StringField(required=True)
    title = me.StringField(required=True)
    content = me.DictField()
    created_at = me.DateTimeField(default=datetime.utcnow)

    meta = {'collection': 'websites'}
