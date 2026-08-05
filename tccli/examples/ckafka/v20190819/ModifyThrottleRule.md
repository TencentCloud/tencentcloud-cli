**Example 1: 修改实例限流规则接口**

修改实例限流规则接口

Input: 

```
tccli ckafka ModifyThrottleRule --cli-unfold-argument  \
    --ThrottleRuleId 2 \
    --InstanceId ckafka-o9gv345o \
    --ConsumeThrottle 13
```

Output: 
```
{
    "Response": {
        "RequestId": "8beb3efd-9451-44ee-b975-6b61d266f5af",
        "Result": {
            "Data": null,
            "ReturnCode": "0",
            "ReturnMessage": "success"
        }
    }
}
```

