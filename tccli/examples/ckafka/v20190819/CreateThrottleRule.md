**Example 1: 创建实例限流规则接口**

创建实例限流规则接口

Input: 

```
tccli ckafka CreateThrottleRule --cli-unfold-argument  \
    --InstanceId ckafka-o9gv345o \
    --GroupNameList test5 \
    --ConsumeThrottle 15 \
    --ThrottleType 2
```

Output: 
```
{
    "Response": {
        "RequestId": "58d37b32-3288-4856-b539-3c7c399b74f9",
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

