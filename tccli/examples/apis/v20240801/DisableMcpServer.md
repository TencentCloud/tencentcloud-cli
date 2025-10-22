**Example 1: 下线mcp server**

下线mcp server

Input: 

```
tccli apis DisableMcpServer --cli-unfold-argument  \
    --InstanceID ins-9c4a1db3 \
    --ID mcp-aa12c447
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": "mcp-aa12c447"
        },
        "RequestId": "1eed7b01-8b36-4b06-97c2-242e461856db"
    }
}
```

