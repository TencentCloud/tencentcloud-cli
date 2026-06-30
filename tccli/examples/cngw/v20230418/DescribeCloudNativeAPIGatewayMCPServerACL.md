**Example 1: 查看MCP服务黑白名单鉴权规则**



Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayMCPServerACL --cli-unfold-argument  \
    --GatewayId gateway-******** \
    --ServerId ********-****-****-****-************
```

Output: 
```
{
    "Response": {
        "Result": {
            "ACLConsumerGroups": [
                {
                    "Id": "cg-**************",
                    "Name": "默认消费者组"
                }
            ],
            "ACLConsumers": [
                {
                    "Id": "********-****-****-****-************",
                    "Name": "****"
                }
            ],
            "ACLType": "Deny",
            "AuthType": "None"
        },
        "RequestId": "e392e2bd-d7dd-469e-b04f-f33d774e27e0"
    }
}
```

