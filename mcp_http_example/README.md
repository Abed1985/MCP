
---

# MCP HTTP Example (Claude Desktop + Remote MCP)

This repository demonstrates how to connect **Claude Desktop (Free version)** to a
**remote MCP server over HTTP** using a **local STDIO proxy running inside WSL**.

Claude Desktop (Free) does **not** support direct connections to remote MCP servers.
This limitation can be worked around by launching a local proxy script that forwards
STDIO requests from Claude to a remote MCP server over HTTP.

This approach follows the official FastMCP guidance:
https://gofastmcp.com/integrations/claude-desktop#remote-servers

---

## Architecture

```

Claude Desktop (Windows)
|
|  STDIO
v
Local Proxy Script (WSL)
|
|  HTTP
v
Remote MCP Server (e.g. 192.168.5.69)

```