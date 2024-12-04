**Example 1: 打通普罗米修斯监控**



Input: 

```
tccli ckafka CreatePrometheus --cli-unfold-argument  \
    --InstanceId ckafka-test \
    --VpcId vpc-test \
    --SubnetId subnet-test
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "success",
            "Data": {
                "FlowId": 0,
                "RouteDTO": {
                    "RouteId": 0
                }
            }
        },
        "RequestId": "84770b4b-df34-4ccf-8e22-41d3b1d0fe0d"
    }
}
```

