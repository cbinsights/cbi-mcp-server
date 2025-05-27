import os
from typing import Optional
from dotenv import load_dotenv
import httpx

from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations

load_dotenv()

CLIENT_ID = os.getenv("CBI_CLIENT_ID")
CLIENT_SECRET = os.getenv("CBI_CLIENT_SECRET")

TIMEOUT = float(os.getenv("CBI_MCP_TIMEOUT", 120))
PORT = int(os.getenv("CBI_MCP_PORT", 8000))

mcp = FastMCP(
    name="cbi-mcp-server",
    port=PORT,
    instructions="ChatCBI is a specialized market intelligence and company research copilot powered by CB Insights data. " \
                 "Use this tool when you need detailed information about companies, business deals, financial transactions, market trends, " \
                 "funding rounds, acquisitions, partnerships, or competitive intelligence. " \
                 "ChatCBI provides access to a comprehensive database of business and market information, allowing for in-depth research and insights.",
)

API_BASE = "https://api.cbinsights.com/v2"


def get_auth_token() -> str:
    url = f"{API_BASE}/authorize"

    payload = {
        "clientId": CLIENT_ID,
        "clientSecret": CLIENT_SECRET
    }

    with httpx.Client() as client:
        try:
            response = client.post(url, json=payload, timeout=30.0)
            response.raise_for_status()
            return response.json()["token"]
        except Exception as e:
            raise Exception(f"Failed to authenticate: {str(e)}")


@mcp.tool(name="ChatCBI",
          description="When using this tool, provide clear, specific queries for the best results. You can continue conversations with ChatCBI by including the chat ID from previous interaction.",
          annotations=ToolAnnotations(title="Chat with CBI", readOnlyHint=True, openWorldHint=True),
          )
def chat_with_cbi(message: str, chat_id: Optional[str] = None) -> {}:
    token = get_auth_token()

    url = f"{API_BASE}/chatcbi"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {"message": message}
    if chat_id:
        payload["chatID"] = chat_id

    with httpx.Client() as client:
        try:
            response = client.post(url, headers=headers, json=payload, timeout=TIMEOUT)
            response.raise_for_status()
            return response.content
        except Exception as e:
            raise Exception(e)

    return {}


if __name__ == "__main__":
    mcp.run()
