**Example 1: 打通普罗米修斯监控**



Input: 

```
tccli ckafka CreatePrometheus --cli-unfold-argument  \
    --InstanceId xx \
    --SubnetId xx \
    --VpcId xx
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

