**Example 1: 修改MCP工具鉴权配置**



Input: 

```
tccli cngw ModifyCloudNativeAPIGatewayMCPToolACL --cli-unfold-argument  \
    --GatewayId gateway-******** \
    --ServerId 204f2888-7b53-4499-9061-24e623b2bdbd \
    --ToolId f15f49c3-4c99-4930-bd4b-7284f74dda0d \
    --ACLType Allow \
    --ACLConsumerIds ef504000-a818-4e95-97e2-563e236fa26f
```

Output: 
```
{
    "Response": {
        "RequestId": "18e46cf4-3129-4dc5-84f5-f27f88e6bfff"
    }
}
```

