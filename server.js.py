import tornado.ioloop
import tornado.web
import traceback

from marco.handlers import health


def create_server():
    return tornado.web.Application([
        (r"/health", health.HealthHandler),

    ], compress_response=True, autoreload=True)


if __name__ == "__main__":
    try:
        print('Starting server')

        app = create_server()
        app.listen(9000)

        print('Server stated server')

        io_loop = tornado.ioloop.IOLoop.current()
        io_loop.start()
        io_loop.set_blocking_log_threshold(1)

    except Exception as ex:
        print("An error occurred during service: \\n {} \\n {}".format(str(ex),
                                                                              traceback.format_exc()))
