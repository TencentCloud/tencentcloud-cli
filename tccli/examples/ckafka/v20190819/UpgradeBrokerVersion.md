**Example 1: broker版本升级**

broker版本升级

Input: 

```
tccli ckafka UpgradeBrokerVersion --cli-unfold-argument  \
    --InstanceId ckafka-test \
    --Type 1 \
    --SourceVersion v2.8.1_r1.1.7 \
    --TargetVersion v2.8.1_r1.1.8 \
    --DelayTimeStamp 
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
        "RequestId": "2412412412asfdsafasdsfd"
    }
}
```

