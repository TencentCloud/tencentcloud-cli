**Example 1: 成功请求**



Input: 

```
tccli ckafka CreateRoute --cli-unfold-argument  \
    --InstanceId xxx \
    --VipType 1
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "ok",
            "Data": {
                "FlowId": 111,
                "RouteDTO": {
                    "RouteId": 132321
                }
            }
        },
        "RequestId": "36713f94-d07d-4b96-babf-42d139276f23"
    }
}
```

