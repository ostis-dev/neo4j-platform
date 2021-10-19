import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

path = os.path.normpath(os.path.join(current_dir, "../../db"))
sys.path.append(path)


def run():
    from service.run import main
    main()


run()
