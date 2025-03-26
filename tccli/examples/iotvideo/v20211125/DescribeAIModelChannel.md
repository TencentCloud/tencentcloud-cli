**Example 1: 查看AI推理结果推送配置**



Input: 

```
tccli iotvideo DescribeAIModelChannel --cli-unfold-argument  \
    --ProductId product \
    --ModelId body_detect
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

