class Request(object):

    def __init__(self, conn, msg):
        self.conn = conn  # 已经和客户端建立好的连接
        self.msg = msg  # 客户端的请求数据

    def get_connection(self):
        # 获取请求连接信息
        return self.conn

    def get_data(self):
        # 获取请求消息的数据
        return self.msg.get_data()

    def get_msg_id(self):
        # 获取请的消息
        return self.msg.get_msg_id()
