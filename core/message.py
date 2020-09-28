class Message(object):

    def __init__(self, id, data_len, data=""):
        self.id = id
        self.data_len = data_len
        self.data = data

    def get_data_len(self):
        # 获取消息长度
        return self.data_len

    def get_msg_id(self):
        # 获取消息id
        return self.id

    def get_data(self):
        # 获取消息内容
        return self.data

    def set_msg_id(self, id):
        # 设置消息id
        self.id = id

    def set_data(self, data):
        # 设置消息内容
        self.data = data

    def set_data_len(self, data_len):
        # 设置消息长度
        self.data_len = data_len


def new_message_data_pack(msg_id, data):
    # 创建msg对象
    msg = Message(msg_id, len(data), data)
    return msg
