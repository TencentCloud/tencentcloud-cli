**Example 1: 解绑路由安全组**



Input: 

```
tccli ckafka DisassociateRoutesSecurityGroup --cli-unfold-argument  \
    --InstanceRoutes.0.InstanceId ckafka-test1234 \
    --InstanceRoutes.0.RouteId 1234 \
    --InstanceRoutes.1.InstanceId ckafka-test1234 \
    --InstanceRoutes.1.RouteId 1235 \
    --InstanceRoutes.2.InstanceId ckafka-test1234 \
    --InstanceRoutes.2.RouteId 1236 \
    --SecurityGroupId sg-xxx1
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "success"
        },
        "RequestId": "test-reqId-1136"
    }
}
```

