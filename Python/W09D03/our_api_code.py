from sanic import Sanic
from sanic.response import json

app = Sanic("My Hello, world app")

@app.route('/rahul')
async def test(request):
    return json({'hello': 'world'})

@app.route('/mohit')
async def test(request):
    return json({'python': 3})

if __name__ == '__main__':
    app.run()