**Example 1: 修改MCP服务认证配置**



Input: 

```
tccli cngw ModifyCloudNativeAPIGatewayMCPServerAuth --cli-unfold-argument  \
    --GatewayId gateway-******** \
    --ServerId 204f2888-7b53-4499-9061-24e623b2bdbd \
    --AuthType ApiKey
```

Output: 
```
{
    "Response": {
        "RequestId": "d892b099-5093-40e5-b2bf-7bcae3d9792b"
    }
}
```

