import asyncio
from asyncio import StreamReader, StreamWriter

async def echo(reader: StreamReader, writer: StreamWriter):
    print('New connection.')
    try:
        while data := await reader.readline():
            writer.write(data.upper())  
            await writer.drain()
        print('Leaving Connection.')
    except asyncio.CancelledError:  
        print('Connection dropped!')

async def main(host='localhost', port=8889):
    server = await asyncio.start_server(echo, host, port)
    async with server:
        await server.serve_forever()

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('Bye!')
