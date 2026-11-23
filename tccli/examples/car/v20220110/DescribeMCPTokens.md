**Example 1: 查询 MCP Token 列表**

用于获取 MCP Token 信息

Input: 

```
tccli car DescribeMCPTokens --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Tokens": [
            {
                "CreatedTime": "2026-10-14T05:25:21Z",
                "ExpiresTime": "2026-10-15T14:45:21Z",
                "Scopes": [
                    "*"
                ],
                "Status": "ACTIVE",
                "TokenId": "tok_b29*******7aebe2",
                "TokenName": "victo****ken2",
                "UserId": ""
            }
        ],
        "TotalCount": 2,
        "RequestId": "d6a04877-3267-4f35-94d0-f6809e5b961d"
    }
}
```

