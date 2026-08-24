**Example 1: ModifyCkafkaStart**



Input: 

```
tccli csip ModifyDspmCkafkaStart --cli-unfold-argument  \
    --LogDeliveryInfo.0.LogType 0 \
    --LogDeliveryInfo.0.TopicId topc-2ws \
    --LogDeliveryInfo.0.TopicName send-mail
```

Output: 
```
{
    "Response": {
        "RequestId": "d0f51893-e15f-44ac-be6d-900450a6b8c2"
    }
}
```

