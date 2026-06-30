**Example 1: 查询MCP Tool 列表**



Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayMCPToolList --cli-unfold-argument  \
    --GatewayId gateway-545fe799 \
    --ServerId 865e3a7d-54da-469c-82eb-a63b09d8f47f \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "DataList": [
                {
                    "ContentType": "application/json",
                    "CreateTime": "2026-04-15 09:44:41",
                    "Description": "创建订单",
                    "DisplayName": "创建订单",
                    "InputParams": [
                        {
                            "Description": "id",
                            "Name": "id",
                            "Position": "query",
                            "Required": true,
                            "Type": "string"
                        }
                    ],
                    "Method": "POST",
                    "Name": "create_order",
                    "Path": "/api/orders",
                    "ServiceId": "",
                    "ToolId": "3aab6316-69bb-4610-b10c-479c9320f1b0",
                    "UpdateTime": "2026-04-15 09:46:32"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "d0351c51-ab4a-4d08-b262-20029c1b6b10"
    }
}
```

