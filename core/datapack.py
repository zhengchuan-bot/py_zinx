from io import BytesIO
from core.message import Message
import struct


class DataPack(object):

    def get_head_len(self):
        return 8

    def pack(self, msg):
        # buff = BytesIO()
        # buff.write(msg.get_data_len().to_bytes(4,byteorder="little"))
        # buff.write(msg.get_msg_id().to_bytes(4,byteorder="little"))
        # buff.write(msg.get_data().to_bytes(4,byteorder="little"))
        # print(buff.getvalue())
        data = bytes(msg.get_data(), encoding="utf-8")
        msg = struct.pack("ii%ds" % msg.get_data_len(), msg.get_data_len(), msg.get_msg_id(), data)
        return msg

    def unpack(self, buff_data):
        data_len, msg_id = struct.unpack("ii", buff_data)
        msg = Message(msg_id, data_len)
        return msg


def new_data_pack():
    return DataPack()
