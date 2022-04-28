**Example 1: 删除路由**



Input: 

```
tccli ckafka DeleteRoute --cli-unfold-argument  \
    --InstanceId xxx \
    --RouteId 1 \
    --CallerAppid 1
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnMessage": "xx",
            "ReturnCode": "xx",
            "Data": {
                "FlowId": 0
            }
        },
        "RequestId": "xx"
    }
}
```

