class Request(object):

    def __init__(self,conn,data):
        self.conn = conn # 已经和客户端建立好的连接
        self.data = data # 客户端的请求数据

    def get_connection(self):
        # 获取请求连接信息
        pass

    def get_data(self):
        # 获取请求消息的数据
        pass
