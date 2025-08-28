**Example 1: 删除路由**



Input: 

```
tccli ckafka DeleteRoute --cli-unfold-argument  \
    --InstanceId ckafka \
    --RouteId 1 \
    --CallerAppid 1
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnMessage": "success",
            "ReturnCode": "0",
            "Data": {
                "FlowId": 0,
                "RouteDTO": {
                    "RouteId": 0
                }
            }
        },
        "RequestId": "3d0d9aeb-82f9-440a-ab9b-a016212c6fb0"
    }
}
```

