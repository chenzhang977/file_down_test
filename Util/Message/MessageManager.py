from .Message import *

async def create_none_message():
        return Message(0, 0, "", 0, "", 0, "", MessageType.TG, -1)

async def create_tg_message(time: int = 0, group_id: int = 0, group_name: str = "", user_id: int = 0, user_name: str = "", msg_id: int = 0, msg: str = "", auto_delete: int = -1):
        return Message(time, group_id, group_name, user_id, user_name, msg_id, msg, MessageType.TG, auto_delete)

async def create_qq_message(time: int = 0, group_id: int = 0, group_name: str = "", user_id: int = 0, user_name: str = "", msg_id: int = 0, msg: str = "", auto_delete: int = -1):
        return Message(time, group_id, group_name, user_id, user_name, msg_id, msg, MessageType.QQ, auto_delete)