from datetime import datetime

class parseTime:
    @staticmethod
    def parse(time2Bparsed: datetime, format: str):
        """Formats time2Bparsed parameter in the specified format.
        
        :param time2Bparsed: datetime variable.
        :param format: String variable.
        
        .. versionchanged:: 1.3
        """
        return datetime.strptime(time2Bparsed, format) #."%Y-%m-%d %H:%M:%S" strftime("%Y-%m-%d %I:%M:%S %p")
        
        # MessageInstance = MessagesModel(phone_number=phone_number, content=content, sent_at=sentAt)
        # db.session.add(MessageInstance)
        # db.session.commit()
        
        # lastMessageInstance = LastMessageModel.query.filter_by(phone_number=phone_number).first()
        # lastMessageInstance.content = content
        # lastMessageInstance.sent_at = sentAt
        
        # db.session.add_all([MessageInstance,lastMessageInstance])
        # db.session.commit()
        