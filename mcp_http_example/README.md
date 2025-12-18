
# MCP HTTP Example

This repository demonstrates how to connect **Claude Desktop (Free version)** to a **remote MCP server over HTTP** using a **local proxy script**, instead of the default STDIO-based MCP connection.

This approach is useful when your MCP server is running on a remote host (for example: `192.168.5.69`).

Claude Desktop (Free) cannot connect directly to remote MCP servers, but this limitation can be worked around by using a local proxy script, as documented here:  
https://gofastmcp.com/integrations/claude-desktop#remote-servers

---

## Architecture

```

Claude Desktop
|
| (STDIO)
v
Local Proxy Script (WSL)
|
| (HTTP)
v
Remote MCP Server (192.168.5.69)

````

---

## Prerequisites

- Claude Desktop (Free version)
- WSL installed and working
- Python 3.x in WSL
- A running MCP server accessible over HTTP

---

## Setup

### Step 1: Create the Proxy Script

1. Create a Python virtual environment in WSL
2. Create a proxy script (for example: `proxy_server.py`)
3. The proxy script should:
   - Communicate with Claude via STDIO
   - Forward requests to the remote MCP server over HTTP

---

### Step 2: Configure Claude Desktop

Edit `claude_desktop_config.json` to configure Claude to launch the proxy script.

Example configuration:

```json
{
  "mcpServers": {
    "remote-mcp": {
      "command": "wsl.exe",
      "args": [
        "/path/to/venv/bin/python",
        "/path/to/proxy_server.py"
      ]
    }
  }
}
````

---

### Step 3: Run the Remote MCP Server

1. Start the MCP server on the remote host (for example: `192.168.5.69`)
2. Ensure the HTTP endpoint is reachable from your WSL environment

---

## Verification

1. Open **Claude Desktop**
2. Go to **Settings → Developer**
3. Confirm that the MCP server is listed and running

If everything is configured correctly, Claude Desktop will communicate with the remote MCP server via the local proxy script.
