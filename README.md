# CB Insights MCP Server

The CBI MCP Server provides an interface for developers to interact with CB Insights ChatCBI LLM through AI Agents.

## Tools

### ChatCBI
- Sends a message from an agent to our AI chatbot and returns the response
- Input parameters:
  - `message`: 
  - `chatID`: (optional) The unique id of an existing ChatCBI session. Used for continuity in a conversation. If not provided, a new ChatCBI session will be created
- Returns object containing the following fields:
  - `chatID`: Unique id of current ChatCBI session
  - `message`: ChatCBI message generated in response to the message send in the input.
  - `RelatedContent`: Content that is related to the content returned
  - `Sources`: Supporting sources for the message content returned 
  - `Suggestions` Suggested prompts to further explore the subject matter
- For more information, check the [ChatCBI Docs](https://api-docs.cbinsights.com/portal/docs/api#tag/ChatCBI)

## Setup
The CBI MCP Server uses [uv](https://docs.astral.sh/uv/getting-started/installation/) to manage the project. 

The default port is `8000`, but can be modified by updating the `CBI_MCP_PORT` environment variable in the `.env` file. 

The timeout for requests can also be modified via the `CBI_MCP_TIMEOUT` variable in the `.env` file.

### Authentication

Documentation on how CB Insights APIs are authenticated can be found [here](https://api-docs.cbinsights.com/portal/docs/CBI-API/Authentication)

The server uses the `CBI_CLIENT_ID` and `CBI_CLIENT_SECRET` environment variables set in the `.env` file to authorize requests.

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