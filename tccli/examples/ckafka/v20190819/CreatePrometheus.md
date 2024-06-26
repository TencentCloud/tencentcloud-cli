**Example 1: 打通普罗米修斯监控**



Input: 

```
tccli ckafka CreatePrometheus --cli-unfold-argument  \
    --InstanceId abc \
    --VpcId abc \
    --SubnetId abc
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "abc",
            "ReturnMessage": "abc",
            "Data": {
                "FlowId": 0,
                "RouteDTO": {
                    "RouteId": 0
                }
            }
        },
        "RequestId": "abc"
    }
}
```

