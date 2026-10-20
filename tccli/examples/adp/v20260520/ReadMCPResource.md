**Example 1: 获取MCP-APP资源**



Input: 

```
tccli adp ReadMCPResource --cli-unfold-argument  \
    --PluginId 418eee0b-4aa7-4aef-939b-3c48d404e846 \
    --ThreadId b18c602d-054d-4f1a-ad9b-f785ba4d69c5 \
    --Uri ui://overtime-list/overtime-list.html
```

Output: 
```
{
    "Response": {
        "Contents": [
            {
                "Blob": null,
                "Meta": "",
                "MimeType": "text/html;profile=mcp-app",
                "Text": "<!DOCTYPE ",
                "Uri": "ui://overtime-list/overtime-list.html"
            }
        ],
        "ResourceMeta": "<>",
        "RequestId": "4be49907-1928-419f-9b26-5c4199ea7967"
    }
}
```

