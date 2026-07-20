**Example 1: 修改MCP服务认证配置**



Input: 

```
tccli cngw ModifyCloudNativeAPIGatewayMCPServerAuth --cli-unfold-argument  \
    --GatewayId gateway-aeb0be15 \
    --ServerId 412b0a7c-f2f6-42f7-8a65-ec5e708b637f \
    --AuthType ApiKey
```

Output: 
```
{
    "Response": {
        "RequestId": "9345ec58-3656-4882-9282-29ede7fc8c5c"
    }
}
```

