**Example 1: 续费实例**

续费实例

Input: 

```
tccli ckafka RenewCkafkaInstance --cli-unfold-argument  \
    --InstanceId ckafka-xxx \
    --TimeSpan 1
```

Output: 
```
{
    "Response": {
        "Result": {
            "BigDealId": "2023020103xxxx",
            "DealName": "2023020103xxxx"
        },
        "RequestId": "f47ac10b-58cc-4372-a567-0e02b2c3d479"
    }
}
```

