# MCP HTTP example 
# if you are running your MCP server on a remote server via HTTP instead of STDIO ( lets say server on 192.168.5.69)
# You can still use Claude Free version to connect to the server via a Proxy script as decribed on :
https://gofastmcp.com/integrations/claude-desktop#remote-servers
# Setup (Claude --> Proxy (via a script)--> remote server (192.168.5.69))
# Step 1:
# Create a virtual environment on WSL with a script. I called it proxy_server.py
# Step2 :
# Configure Claude json file as in claude_desktop_config.json
# Step3:
# run your MCP server on remote host, and now claude should be able to connect to the MCP server
# you can check under Settings > Developer that its running.