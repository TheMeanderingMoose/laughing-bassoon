# builtin
import asyncio

# internal
from src.api.models import Query, Response

async def send_message(query: Query) -> Response:

    host = '194.195.212.204'
    port = 1234

    reader, writer = await asyncio.open_connection(host, port)
    
    try:
        ititialization_message = "SUk2VzeJBjwy9fcC3p5hWmv"
        print(f"Sending message: {ititialization_message}")
        writer.write(message.encode('utf-8'))
        await writer.drain()

        response = await reader.read(1024)
        print(f"Received response: {response.decode('utf-8')}")

        message = query.msg
        print(f"Sending message: {message}")
        writer.write(message.encode('utf-8'))
        await writer.drain()

        response = await reader.read(1024)
        print(f"Received response: {response.decode('utf-8')}")

        return Response(msg=str(response.decode('utf-8')))

    except ConnectionError as e:
        print(f"Error: {e}")
    finally:
        print("Closing the connection.")
        writer.close()
        await writer.wait_closed()