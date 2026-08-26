**Example 1: test**



Input: 

```
tccli monitor ListAIWorkbenchMCPs --cli-unfold-argument  \
    --MCPIds mcp-********
```

Output: 
```
{
    "Response": {
        "MCPs": [
            {
                "AuthSecret": "***",
                "AuthType": "none",
                "Description": "tcop-rum-mcp",
                "Enabled": true,
                "Headers": "***tX\"}",
                "MCPId": "mcp-635dx35o",
                "Name": "tcop-rum-mcp",
                "RetryCount": 3,
                "Timeout": 30,
                "Transport": "streamable_http",
                "Url": "***/sse"
            }
        ],
        "PageResult": {
            "CurrentPageNo": 1,
            "TotalCount": 7,
            "TotalPage": 1
        },
        "RequestId": "5d27dc0e-0158-4f06-b2e4-89c477114b78"
    }
}
```

