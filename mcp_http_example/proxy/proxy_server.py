import logging
import os
from fastmcp import FastMCP, Client

# Logging

LOG_DIR = os.getenv("MCP_PROXY_LOG_DIR", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "proxy_server.log"),
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

logging.info("Starting MCP STDIO proxy")

# -----------------------------
# Remote MCP server
# -----------------------------
REMOTE_MCP_URL = os.getenv(
    "REMOTE_MCP_URL",
    "http://192.168.5.69:9000/mcp"
)

logging.info("Connecting to remote MCP server: %s", REMOTE_MCP_URL)

client = Client(REMOTE_MCP_URL)

proxy = FastMCP.as_proxy(
    client,
    name="remote_mcp_proxy",
    debug=True,
)

# -----------------------------
# Run proxy (STDIO)
# -----------------------------
if __name__ == "__main__":
    try:
        proxy.run()
    except Exception:
        logging.exception("Proxy crashed")
