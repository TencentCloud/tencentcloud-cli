**Example 1: 删除实例消费组限流**

删除实例消费组限流接口

Input: 

```
tccli ckafka DeleteThrottleRule --cli-unfold-argument  \
    --ThrottleRuleId 1 \
    --InstanceId ckafka-o9gv345o
```

Output: 
```
{
    "Response": {
        "RequestId": "9c7d2d0d-b636-4eba-8c21-31ef7be54820",
        "Result": {
            "Data": {
                "FlowId": 0
            },
            "ReturnCode": "0",
            "ReturnMessage": "apply ok"
        }
    }
}
```

