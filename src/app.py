import os, json, time
import asyncio
from aiohttp import web
# from apistar import App, Route
from utils import logger



routes = web.RouteTableDef()


@routes.get('/')
async def hello(request):
    return web.Response(text="Hello, world")


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.add_routes(routes)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logger.info('server started at http://127.0.0.1:9000...')
    return srv


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()

