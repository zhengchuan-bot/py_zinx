from core.request import Request
from core.datapack import DataPack
from core.message import new_message_data_pack
import struct


class Connection(object):

    def __init__(self, conn, addr, conn_id, router):
        self.conn = conn  # 当前连接的套接字socket
        self.addr = addr  # 当前连接的addr
        self.conn_id = conn_id  # 当前连接的id
        self.is_closed = False  # 当前连接的关闭状态
        # self.handle_api = handle_api # 处理连接的方法
        self.router = router  # 该连接的处理方法router

    def start(self, deal_conn):
        # 开启连接读取客户端数据
        self.start_reader(deal_conn)

    def stop(self):
        # 关闭连接
        self.conn.close()

    def get_tcp_connection(self):
        # 从连接中获取socket
        return self.conn

    def get_conn_id(self):
        # 获取当前连接id
        return self.conn_id

    def get_remote_addr(self):
        # 获取远程客户端地址信息
        return self.addr

    def deal_router(self, request):
        # 执行注册路由方法
        self.router.pre_handle(request)
        self.router.handle(request)
        self.router.post_handle(request)

    def start_reader(self, deal_conn):
        print("reader is running...")
        print(self.conn, self.conn_id, self.addr)
        from core.datapack import DataPack

        while True:
            try:
                dp = DataPack()
                header_data = self.conn.recv(dp.get_head_len())
                msg = dp.unpack(header_data)
                if msg.get_data_len() > 0:
                    binary_data = self.conn.recv(msg.get_data_len())
                    data = struct.unpack("%ds" % msg.get_data_len(), binary_data)[0].decode("utf-8")
                    msg.set_data(data)
                    print(data)
                    req = Request(deal_conn, msg)
                    self.deal_router(req)
            except Exception as e:
                print(e)
                self.stop()
                break
            # self.handle_api(self.conn,data)

    def send_msg(self, msg_id, data):
        # 发送消息
        if self.is_closed:
            raise ("connection is closed")
        dp = DataPack()
        msg = dp.pack(new_message_data_pack(msg_id, data))
        # 回写给客户端
        self.conn.send(msg)


def new_connection(conn, addr, conn_id, router):
    # 创建连接 并返回连接实例
    c = Connection(
        conn,
        addr,
        conn_id,
        router
    )
    return c
