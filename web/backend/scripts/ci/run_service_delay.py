import time
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.normpath(os.path.join(current_dir, "../../")))
sys.path.append(os.path.normpath(os.path.join(current_dir, "../../../../db")))


def run():
    from service.run import main
    import tornado.ioloop

    def stop_service():
        tornado.ioloop.IOLoop.instance().stop()

    tornado.ioloop.IOLoop.instance().call_later(10, stop_service)

    main()


run()
