
from fastmcp import FastMCP, Client
import logging
import os

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# Configure logging to DEBUG so you can see all messages
logging.basicConfig(
    filename="logs/proxy_server.log",
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logging.info("Starting proxy server...")

# Connect to your remote HTTP MCP server
client = Client("http://192.168.5.69:9000/mcp")

# Create the STDIO proxy
proxy = FastMCP.as_proxy(client, name="hello_world_proxy", debug=True)

if __name__ == "__main__":
    logging.info("Running STDIO proxy...")
    try:
        proxy.run()  # STDIO transport
    except Exception as e:
        logging.exception("Proxy failed:")


# extra code for extra logging

#class LoggingClient(Client):
#    async def send(self, message):
#        logging.debug(f"Sending to server: {message}")
#        return await super().send(message)

#client = LoggingClient("http://192.168.5.69:9000/mcp")
#proxy = FastMCP.as_proxy(client, name="hello_world_proxy", debug=True)