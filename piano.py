import responder
from typing import Dict, List
import pathlib
from loguru import logger

from common import Responder


class Piano(object):

    def __init__(self, *, path='MP3s'):
        self.path = pathlib.Path(path)
        self.extension = '.mp3'

    def on_get(self, req: responder.Request, res: responder.Response, *, mode: str = ''):
        if mode == 'list':
            program = self.listup()
            res.content = Responder.api.template('recital.html', program=program)
        elif mode == 'play':
            name = req.params['name'] + self.extension
            res.content = self.stream(name=name)

    def stream(self, *, name: str) -> bytes:
        bin = b''
        dst = self.path / name
        if dst.exists() and dst.is_file():
            logger.debug(dst)
            with open(file=dst, mode='rb') as f:
                bin = f.read()
        else:
            logger.warning(dst)
        return bin

    def listup(self) -> List[str]:
        result: List[str] = []
        for file in self.path.iterdir():
            if file.suffix.lower() == self.extension:
                result.append(file.stem)
        return result


if __name__ == '__main__':
    def main():
        R = Recital()
        ooo = R.listup()
        pass


    main()
