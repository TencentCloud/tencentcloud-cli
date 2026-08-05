**Example 1: 查询实例消费组限流规则接口示例**

查询实例消费组限流规则接口

Input: 

```
tccli ckafka DescribeThrottleRules --cli-unfold-argument  \
    --InstanceId ckafka-o9gv345o \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "d225d275-a152-4d35-ae9e-529b024a609c",
        "Result": {
            "ThrottleRuleList": [
                {
                    "ClientId": "test3",
                    "ConsumeThrottle": 10,
                    "ThrottleRuleId": 2,
                    "UpdateTime": "2025-09-02 17:49:28",
                    "UserName": ""
                }
            ],
            "TotalCount": 1
        }
    }
}
```

