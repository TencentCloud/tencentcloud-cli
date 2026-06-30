**Example 1: 查询MCP服务认证配置**



Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayMCPServerAuth --cli-unfold-argument  \
    --GatewayId gateway-******** \
    --ServerId 204f2888-7b53-4499-9061-24e623b2bdbd
```

Output: 
```
{
    "Response": {
        "Result": {
            "AuthType": "ApiKey"
        },
        "RequestId": "7ff301e6-8ac5-4c8d-b117-986b71b708c9"
    }
}
```

