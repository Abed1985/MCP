# MCP STDIO → HTTP Proxy (WSL)

This proxy allows **Claude Desktop (Free)** to connect to a **remote MCP server**
over HTTP by running a local STDIO proxy inside **WSL**.
Normally this script is launched automatically by Claude Desktop.

Claude Desktop cannot connect directly to remote MCP servers.
This proxy bridges that gap.

---

## Architecture

Claude Desktop (Windows)
│
│ STDIO
▼
Proxy Script (WSL)
│
│ HTTP
▼
Remote MCP Server (e.g. 192.168.5.69)

---

## Setup (WSL)

```bash
cd proxy

uv venv
source .venv/bin/activate
uv pip install -e .
