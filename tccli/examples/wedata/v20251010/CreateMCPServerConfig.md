**Example 1: CreateMCPServerConfig**



Input: 

```
tccli wedata CreateMCPServerConfig --cli-unfold-argument  \
    --WorkspaceId 17697667906247629 \
    --ServerName ta123123vily \
    --ServerType external \
    --ConfigData {"mcpServers":{"tavily":{"url":"https://mcp.tavily.com/mcp/?tavilyApiKey=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"}}} \
    --Description tavilyMCP工具描述
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreatedBy": "700002164619",
            "CreatedOn": "1774964562662",
            "Description": "tavilyMCP工具描述",
            "Key": "9ec226f0177496456266235091a3d",
            "ModifiedBy": "700002164619",
            "ModifiedOn": "1774964562662",
            "RefResource": "",
            "ServerName": "ta123123vily",
            "ServerType": "external",
            "ServerUrl": "https://mcp-test001.wedataapp-test.cloud.tencent.com/api/1.0/mcp/http/external/9ec226f0177496456266235091a3d",
            "Status": "active",
            "TransportType": "streamable-http",
            "WorkspaceId": "17697667906247629"
        },
        "RequestId": "467459cf-5ada-4971-b6a6-aa9fcbf30af4"
    }
}
```

