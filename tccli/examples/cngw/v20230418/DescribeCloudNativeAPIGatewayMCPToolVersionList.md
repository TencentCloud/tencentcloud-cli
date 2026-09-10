**Example 1: test**



Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayMCPToolVersionList --cli-unfold-argument  \
    --GatewayId gateway-46a97dc8 \
    --ServerId 18845314-b041-4364-b091-af9ee6086c54 \
    --ToolId 9bc61b25-7eec-4812-b81a-d39457e2980d \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Result": {
            "MCPToolVersions": [
                {
                    "CreateTime": "2026-05-27 11:44:28",
                    "Creator": "100020293116",
                    "IsActive": true,
                    "TotalParam": 0,
                    "Version": "2026052757"
                }
            ],
            "TotalCount": 5
        },
        "RequestId": "dce4c2f7-fb3e-4f5f-b07c-8624006a3613"
    }
}
```

