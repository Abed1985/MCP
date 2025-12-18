from fastmcp import FastMCP
import logging, os

os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename="logs/hello_world_http.log", level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP("Hello World")

@mcp.tool(
        name="add", 
        description="Add two integers and return the result."
        )
def add(a: int, b: int) -> int:
    logger.info(f"Adding {a} and {b}")
    return a + b


if __name__ == "__main__":
    # If running from MCP inspector (mcp dev), use stdio
    if os.environ.get("MCP_INSPECTOR") == "1":
        print("[MCP] Running in INSPECTOR (STDIO) mode...")
        mcp.run()

    else:
        print("[MCP] Running HTTP server at http://192.168.5.69:9000 ...")
        mcp.run(
            transport="http",
            host="192.168.5.69",
            port=9000,
        )
