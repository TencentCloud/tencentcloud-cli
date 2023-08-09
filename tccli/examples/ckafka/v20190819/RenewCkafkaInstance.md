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
        "RequestId": "xx-xx-xx"
    }
}
```

