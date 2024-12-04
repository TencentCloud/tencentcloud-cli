**Example 1: 添加 ACL 策略**



Input: 

```
tccli ckafka CreateAcl --cli-unfold-argument  \
    --InstanceId ckafka-test \
    --ResourceType 2 \
    --ResourceName yourresourcetest1 \
    --Operation 2 \
    --PermissionType 2 \
    --Host 1.1.1.1 \
    --Principal User:user1
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "ok[apply ok]",
            "Data": {
                "FlowId": 0,
                "RouteDTO": {
                    "RouteId": 0
                }
            }
        },
        "RequestId": "b1ce770b-3623-47d3-b31b-538f8941142d"
    }
}
```

