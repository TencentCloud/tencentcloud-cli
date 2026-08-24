**Example 1: ModifyCkafkaStop**



Input: 

```
tccli csip ModifyDspmCkafkaStop --cli-unfold-argument  \
    --LogDeliveryInfo.0.LogType 0 \
    --LogDeliveryInfo.0.TopicId topic-wwqsa \
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

