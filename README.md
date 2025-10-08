# CB Insights MCP Server

The CBI MCP Server provides an interface for developers to interact with CB Insights ChatCBI LLM through AI Agents.

## Tools

### ChatCBI
Send a message from an agent to ChatCBI and return the response.
- Input parameters:
  - `message`: The content of your message to ChatCBI
  - `chatID`(optional): A unique identifier for the chat session, obtained from a previous response. If included, the conversation is continued. Otherwise, a new conversation is started.
- Returns JSON object containing the following fields:
  - `chatID`: Identifies the conversation. If chatID was provided in the request, this will be the same.
  - `message`: ChatCBI response to the message.
  - `relatedContent`: List of related references.
  - `sources`: List of sources used to generate the response.
  - `suggestions`: List of suggested follow-up questions.
  - `title`: Title of the chat
- For more information see [Using ChatCBI](https://api-docs.cbinsights.com/portal/docs/CBI-API/chatcbi)

## Setup
The CBI MCP Server uses [uv](https://docs.astral.sh/uv/getting-started/installation/) to manage the project. 

Environment variables are set via the .env file:
- `CBI_CLIENT_ID` & `CBI_CLIENT_SECRET` OAuth Client ID and Secret
  - see [CB Insights API Authentication](https://api-docs.cbinsights.com/portal/docs/CBI-API/Authentication) for usage and how to obtain them
- `CBI_MCP_TIMEOUT` (default: 120)
- `CBI_MCP_PORT` (default: 8000)

## Usage

### With Claude Desktop

Update the `claude_desktop_config.json` file using the following command:

```shell
mcp install server.py
```

This will add the following configuration:

```json
{
  "mcpServers": {
    "cbi-mcp-server": {
      "command": "/path/to/.local/bin/uv",
      "args": [
        "--directory",
        "/path/to/cloned/cbi-mcp-server",
        "run",
        "server.py"
      ]
    }
  }
}
```

## Debugging

The [inspector](https://modelcontextprotocol.io/docs/tools/inspector#getting-started) can be used to test/debug your server. 

```shell
mcp dev server.py 
```
[More info on using the inspector](https://modelcontextprotocol.io/docs/tools/inspector#py-pi-package)