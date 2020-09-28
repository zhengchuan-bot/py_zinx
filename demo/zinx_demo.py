from core.server import new_server
from core.router import Router

class ping_router(Router):

    # def pre_handle(self,request):
    #     print("pre_handle....")
    #     request.conn.send("pre_handle hello".encode("utf-8"))

    def handle(self, request):
        print("handle ....")
        # print(request.get_connection().)
        request.get_connection().send_msg(msg_id=1, data="hello Mr shu")

    # def post_handle(self,request):
    #     print("post_handle....")
    #     request.conn.send("post_handle hello".encode("utf-8"))
    #     pass


s = new_server()
s.add_router(ping_router())
s.serve()
