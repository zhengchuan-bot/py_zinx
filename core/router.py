class Router(object):
    # 定义基础路由类
    def pre_handle(self, request):
        # 在处理conn业务之前的钩子方法
        pass

    def handle(self, request):
        # 处理conn业务的方法
        pass

    def post_handle(self, request):
        # 处理conn业务之后的钩子方法
        pass
