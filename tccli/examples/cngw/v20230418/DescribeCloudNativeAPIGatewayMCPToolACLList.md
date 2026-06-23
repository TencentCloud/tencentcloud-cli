**Example 1: 查看 MCP Server Tool ACL 列表**



Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayMCPToolACLList --cli-unfold-argument  \
    --GatewayId gateway-******** \
    --ServerId ********-****-****-****-************ \
    --Limit 10 \
    --Offset 0 \
    --Keyword mcp
```

Output: 
```
{
    "Response": {
        "Result": {
            "ACLType": "Deny",
            "DataList": [],
            "TotalCount": 0
        },
        "RequestId": "92ba1ffc-4c82-47fd-9272-e3d75bfa866b"
    }
}
```

