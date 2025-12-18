from fastmcp import FastMCP
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

logger = logging.getLogger("mcp.server")

mcp = FastMCP("Remote Hello World MCP")

@mcp.tool(
    name="add",
    description="Add two integers and return the result."
)
def add(a: int, b: int) -> int:
    logger.info("Adding %s + %s", a, b)
    return a + b


if __name__ == "__main__":
    host = os.getenv("MCP_HTTP_HOST", "0.0.0.0")
    port = int(os.getenv("MCP_HTTP_PORT", "9000"))

    logger.info("Starting MCP HTTP server on %s:%s", host, port)

    mcp.run(
        transport="http",
        host=host,
        port=port,
    )
