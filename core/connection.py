from core.request import Request

class Connection(object):

    def __init__(self,conn,addr,conn_id,router):
        self.conn = conn # 当前连接的套接字socket
        self.addr = addr # 当前连接的addr
        self.conn_id = conn_id # 当前连接的id
        self.is_closed = False # 当前连接的关闭状态
        # self.handle_api = handle_api # 处理连接的方法
        self.router = router # 该连接的处理方法router

    def start(self):
        # 开启连接读取客户端数据
        self.start_reader()

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
    def deal_router(self,request):
        # 执行注册路由方法
        self.router.pre_handle(request)
        self.router.handle(request)
        self.router.post_handle(request)

    def start_reader(self):
        print("reader is running...")
        print(self.conn,self.conn_id,self.addr)
        while True:
            try:
                data = self.conn.recv(512)
            except Exception as e:
                print(e)
                self.stop()
                break
            print(data)
            req = Request(self.conn,data)
            self.deal_router(req)
            # self.handle_api(self.conn,data)

def new_connection(conn,addr,conn_id,router):
    # 创建连接 并返回连接实例
    c = Connection(
        conn,
        addr,
        conn_id,
        router
    )
    return c
