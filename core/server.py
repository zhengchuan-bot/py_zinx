from socket import *
from core.connection import new_connection
from core.load_conf import conf_json


class Server(object):
    # 定义一个Server服务类
    def __init__(self, name, ip_version, ip, port):
        self.name = name  # 服务器名称
        self.ip_version = ip_version  # tcp4或其他
        self.ip = ip  # 绑定Ip
        self.port = port  # 绑定端口
        self.router = None

    def start(self):
        # 启动服务器方法
        print("server is listen at ip:%s,port:%d,is starting", (self.ip, self.port))
        tcp_socket = socket(AF_INET, SOCK_STREAM)  # 创建一个socket套接字
        tcp_socket.bind((self.ip, self.port))  # 绑定ip和端口
        tcp_socket.listen(1024)  # 最多允许1024个客户端连接
        print("waiting for connect...")
        cid = 0  # 为每个客户端分配一个id
        while True:
            conn, addr = tcp_socket.accept()  # 阻塞等待连接
            print("%s is connect...", addr)
            # 初始化连接
            deal_conn = new_connection(conn, addr, cid, self.router)
            cid += 1
            deal_conn.start(deal_conn)

    def stop(self):
        # 停止服务器
        print("server is stop")

    def serve(self):
        # 开启业务方法
        self.start()

    def add_router(self, router):
        # 给当前服务注册一个路由业务方法
        self.router = router
        print("add router success")


def new_server():
    # 创建一个服务器实例
    s = Server(
        conf_json["name"],
        conf_json["ip_version"],
        conf_json["ip"],
        conf_json["port"]
    )
    return s

# def call_back_to_client(conn,data):
#     # 回写给客户端的方法
#     print("write to client ...")
#     conn.send(data)
