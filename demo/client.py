from socket import *
from core.datapack import DataPack
from core.message import new_message_data_pack
import time, struct

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.connect(("localhost", 8888))

while True:
    dp = DataPack()
    msg = dp.pack(new_message_data_pack(msg_id=1, data="hello mr shu"))
    tcp_socket.send(msg)
    head_data = tcp_socket.recv(dp.get_head_len())
    msg_head = dp.unpack(head_data)
    if msg_head.get_data_len() > 0:
        binary_data = tcp_socket.recv(msg_head.get_data_len())
        data = struct.unpack("%ds" % msg_head.get_data_len(), binary_data)[0].decode("utf-8")
        print(data)
        msg_head.set_data(data)

    time.sleep(1)
tcp_socket.close()
