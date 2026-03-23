**Example 1: 删除app的mcp server**

删除app的mcp server

Input: 

```
tccli apis DeleteAgentAppMcpServers --cli-unfold-argument  \
    --InstanceID ins-e6fbc9b9 \
    --ID aga-71702335 \
    --McpServerIDs mcp-6a63b40b
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": "aga-71702335"
        },
        "RequestId": "35433e7a-0634-4b3b-ab95-2ea7de191c38"
    }
}
```

