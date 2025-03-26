**Example 1: 查看推送通道**



Input: 

```
tccli iotvideo DescribePushChannel --cli-unfold-argument  \
    --ProductId product
```

Output: 
```
{
    "Response": {
        "ForwardKey": "",
        "ForwardAddress": "",
        "CKafkaTopic": "test_ai_result",
        "CKafkaRegion": "gz",
        "RequestId": "id",
        "CKafkaInstance": "ckafka-insfeae",
        "Type": "ckafka"
    }
}
```

