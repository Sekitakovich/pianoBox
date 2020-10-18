import responder
import pathlib
from loguru import logger

from common import Responder
from piano import Piano


class Main(object):
    def __init__(self):
        Responder.api.add_route(route='/piano/{mode}', endpoint=Piano)

        Responder.api.run(address='0.0.0.0', port=80)


if __name__ == '__main__':
    def main():
        M = Main()
        pass


    main()
