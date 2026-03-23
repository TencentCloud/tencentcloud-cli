**Example 1: 创建app的mcp server关联**

创建app的mcp server关联

Input: 

```
tccli apis CreateAgentAppMcpServers --cli-unfold-argument  \
    --ID aga-71702335 \
    --InstanceID ins-e6fbc9b9 \
    --McpServers.0.ID mcp-6a63b40b \
    --McpServers.0.NeedAuth False
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": "6a63b40b"
        },
        "RequestId": "c613fd7b-5f4b-41b9-80f0-8c18ab8cccdf"
    }
}
```

