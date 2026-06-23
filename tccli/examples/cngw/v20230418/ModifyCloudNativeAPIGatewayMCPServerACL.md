**Example 1: 更新MCP服务黑白名单鉴权规则**



Input: 

```
tccli cngw ModifyCloudNativeAPIGatewayMCPServerACL --cli-unfold-argument  \
    --GatewayId gateway-******** \
    --ServerId ********-****-****-****-************ \
    --ACLType Deny \
    --ACLConsumerIds ********-****-****-****-************ \
    --ACLConsumerGroupIds cg-**************
```

Output: 
```
{
    "Response": {
        "RequestId": "f6d1ce10-18d7-441e-a80e-75c82e8e1758"
    }
}
```

