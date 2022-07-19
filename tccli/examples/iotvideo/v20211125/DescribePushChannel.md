**Example 1: 查看推送通道**



Input: 

```
tccli iotvideo DescribePushChannel --cli-unfold-argument  \
    --ProductId test
```

Output: 
```
{
    "Response": {
        "ForwardKey": "",
        "ForwardAddress": "",
        "CKafkaTopic": "test_ai_result",
        "CKafkaRegion": "gz",
        "RequestId": "xx",
        "CKafkaInstance": "ckafka-insfeae",
        "Type": "ckafka"
    }
}
```

